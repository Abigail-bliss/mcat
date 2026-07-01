"""
Screenshot-image helpers for the MCAT Biochemistry deck.

Workflow: the user routes macOS screenshots into ./biochem_images/ (filenames keep
their auto-generated "Screenshot YYYY-MM-DD at H.MM.SS PM.png" timestamps). For a
card that needs an image we grab the NEWEST file (by mtime), store it as Anki media
under a clean key, and embed an <img>. The user never renames anything.

No RDKit here, so plain system Python works:

    python3 push_biochem_cards.py

Card formatting, tags, and the upsert flow mirror orgo_helpers.py.
"""

import base64
import os
import re
import requests

ANKI_URL = "http://localhost:8765"
# biochem_images/ lives one level up in the Anki/ root (it's the macOS screenshot
# auto-save destination — kept in place when scripts were grouped under card-creation/).
IMAGE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "biochem_images"
)


def anki(action, **params):
    r = requests.post(ANKI_URL, json={"action": action, "version": 6, "params": params})
    data = r.json()
    if data.get("error"):
        raise RuntimeError(f"AnkiConnect '{action}' error: {data['error']}")
    return data["result"]


def assert_connected():
    assert anki("version") == 6, "Anki not running or AnkiConnect missing"


def slugify(name):
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def recent_images(n=3):
    """Return the n most-recently-modified files in biochem_images/ (newest first).

    Returns full paths. Use this to preview which screenshot(s) are candidates before
    committing one to a card.
    """
    if not os.path.isdir(IMAGE_DIR):
        return []
    entries = [
        os.path.join(IMAGE_DIR, f)
        for f in os.listdir(IMAGE_DIR)
        if not f.startswith(".") and os.path.isfile(os.path.join(IMAGE_DIR, f))
    ]
    entries.sort(key=os.path.getmtime, reverse=True)
    return entries[:n]


def newest_image():
    """Path to the single most-recent screenshot, or None if the folder is empty."""
    imgs = recent_images(1)
    return imgs[0] if imgs else None


def store_screenshot(name, source_path=None, max_width=420):
    """
    Store a screenshot as Anki media under a clean key (biochem-<slug>.<ext>) and
    return a centered <img> snippet ready to drop into a card field.

    source_path defaults to the newest file in biochem_images/. The original messy
    filename stays in the folder untouched; only the Anki copy is renamed.
    White-bg cards only.
    """
    if source_path is None:
        source_path = newest_image()
    if not source_path or not os.path.isfile(source_path):
        raise FileNotFoundError(f"No screenshot found at {source_path!r}")

    ext = os.path.splitext(source_path)[1].lower() or ".png"
    filename = f"biochem-{slugify(name)}{ext}"
    with open(source_path, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode("ascii")
    anki("storeMediaFile", filename=filename, data=b64)
    return (f"<img src=\"{filename}\" "
            f"style=\"max-width:{max_width}px; margin:8px auto; display:block;\">")


def render_svg(smiles, w=320, h=240):
    """SMILES -> skeletal-structure SVG string (transparent bg). Lazy RDKit import
    so plain-Python (screenshot-only) runs don't need RDKit. Run under uv for these."""
    from rdkit import Chem
    from rdkit.Chem.Draw import rdMolDraw2D

    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles!r}")
    d = rdMolDraw2D.MolDraw2DSVG(w, h)
    opts = d.drawOptions()
    opts.clearBackground = False
    opts.bondLineWidth = 2
    opts.padding = 0.1
    rdMolDraw2D.PrepareAndDrawMolecule(d, mol)
    d.FinishDrawing()
    return d.GetDrawingText()


def render_and_store(name, smiles, w=320, h=240, max_width=300):
    """Render `smiles`, store as biochem-<slug>.svg, return a centered <img> snippet."""
    filename = f"biochem-{slugify(name)}.svg"
    svg = render_svg(smiles, w=w, h=h)
    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    anki("storeMediaFile", filename=filename, data=b64)
    return (f"<img src=\"{filename}\" "
            f"style=\"max-width:{max_width}px; margin:8px auto; display:block;\">")


def validate(front, back):
    for char, cname in [('\t', 'tab'), ('\r', 'CR'), ('\n', 'newline'),
                        ('\v', 'vtab'), ('\f', 'ff')]:
        assert char not in front, f"FRONT contains {cname}!"
        assert char not in back, f"BACK contains {cname}!"


def push_cards(cards, deck_name):
    """Upsert by Front field: add new notes, updateNote any duplicates."""
    notes = [
        {
            "deckName": deck_name,
            "modelName": c.get("model", "Basic"),
            "fields": {"Front": c["front"], "Back": c["back"]},
            "tags": c["tags"],
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        for c in cards
    ]
    can_add = anki("canAddNotes", notes=notes)

    added = updated = 0
    errors = []

    to_add = [n for n, ok in zip(notes, can_add) if ok]
    if to_add:
        ids = anki("addNotes", notes=to_add)
        added = sum(1 for i in ids if i is not None)

    for card, ok in zip(cards, can_add):
        if not ok:
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
