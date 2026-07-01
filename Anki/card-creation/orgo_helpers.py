"""
Organic skeletal-structure diagram helpers for MCAT Anki cards.

Renders skeletal (line-angle) structures from SMILES with RDKit, stores them as
Anki media via AnkiConnect storeMediaFile, and returns an <img> snippet to embed
in a card field.

Run under uv so RDKit gets a compatible Python (system Python is 3.14, no wheels):

    uv run --python 3.13 --with rdkit --with requests push_orgo_cards.py
"""

import base64
import re
import requests

ANKI_URL = "http://localhost:8765"


def anki(action, **params):
    r = requests.post(ANKI_URL, json={"action": action, "version": 6, "params": params})
    data = r.json()
    if data.get("error"):
        raise RuntimeError(f"AnkiConnect '{action}' error: {data['error']}")
    return data["result"]


def assert_connected():
    assert anki("version") == 6, "Anki not running or AnkiConnect missing"


def slugify(name):
    """benzene -> benzene ; 2-Methylbutane -> 2-methylbutane"""
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def render_svg(smiles, w=320, h=240, dummy_labels=None, highlight_atoms=None):
    """SMILES -> skeletal-structure SVG string (transparent background).

    dummy_labels: list of strings to label `*` dummy atoms in order (e.g. ["R", "R'"])
                  for generic functional-group structures.
    highlight_atoms: list of atom indices to highlight (e.g. the anomeric carbon).
    """
    from rdkit import Chem
    from rdkit.Chem.Draw import rdMolDraw2D

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles!r}")
    if dummy_labels:
        i = 0
        for atom in mol.GetAtoms():
            if atom.GetAtomicNum() == 0:
                atom.SetProp("atomLabel", dummy_labels[i] if i < len(dummy_labels) else "R")
                i += 1
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    opts = d.drawOptions()
    opts.clearBackground = False   # transparent -> sits on the white card
    opts.bondLineWidth = 2
    opts.padding = 0.1
    if highlight_atoms:
        rdMolDraw2D.PrepareAndDrawMolecule(d, mol, highlightAtoms=list(highlight_atoms))
    else:
        rdMolDraw2D.PrepareAndDrawMolecule(d, mol)
    d.FinishDrawing()
    return d.GetDrawingText()


def store_media(filename, svg_text):
    """Store an SVG string as an Anki media file (idempotent: overwrites)."""
    b64 = base64.b64encode(svg_text.encode("utf-8")).decode("ascii")
    return anki("storeMediaFile", filename=filename, data=b64)


def render_and_store(name, smiles, w=320, h=240, max_width=300,
                     dummy_labels=None, highlight_atoms=None, inline=False):
    """
    Render `smiles`, store as orgo-<slug>.svg, and return an <img> snippet ready to
    drop into a card field (front or back). White-bg cards only — no night-mode wrapper.

    inline=True returns an inline-block image (for laying out reaction schemes
    side-by-side); default is a centered block image.
    """
    filename = f"orgo-{slugify(name)}.svg"
    svg = render_svg(smiles, w=w, h=h, dummy_labels=dummy_labels,
                     highlight_atoms=highlight_atoms)
    store_media(filename, svg)
    if inline:
        return (f"<img src=\"{filename}\" "
                f"style=\"max-width:{max_width}px; vertical-align:middle;\">")
    return (f"<img src=\"{filename}\" "
            f"style=\"max-width:{max_width}px; margin:8px auto; display:block;\">")


def validate(front, back):
    for char, cname in [('\t', 'tab'), ('\r', 'CR'), ('\n', 'newline'),
                        ('\v', 'vtab'), ('\f', 'ff')]:
        assert char not in front, f"FRONT contains {cname}!"
        assert char not in back, f"BACK contains {cname}!"


def push_cards(cards, deck_name):
    """Upsert by Front field: add new notes, updateNote any duplicates.

    Uses canAddNotes to split new vs. duplicate first, since addNotes raises
    (or returns an error array) when the whole batch is duplicates.
    """
    notes = [
        {
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {"Front": c["front"], "Back": c["back"]},
            "tags": c["tags"],
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        for c in cards
    ]
    can_add = anki("canAddNotes", notes=notes)  # list[bool]; False = duplicate/invalid

    added = updated = 0
    errors = []

    to_add = [n for n, ok in zip(notes, can_add) if ok]
    if to_add:
        ids = anki("addNotes", notes=to_add)
        added = sum(1 for i in ids if i is not None)

    for card, ok in zip(cards, can_add):
        if not ok:  # already exists -> update fields + tags
            if _find_and_update(card, deck_name):
                updated += 1
            else:
                errors.append(card["front"][:60])

    return added, updated, errors


def _find_and_update(card, deck_name):
    title = re.search(r"<b>(.*?)</b>", card["front"])
    keyword = title.group(1).split("&")[0].strip() if title else card["front"][:20]
    note_ids = anki("findNotes", query=f'deck:"{deck_name}" "front:*{keyword}*"')
    if not note_ids:
        return False
    anki("updateNote", note={
        "id": note_ids[0],
        "fields": {"Front": card["front"], "Back": card["back"]},
        "tags": card["tags"],
    })
    return True
