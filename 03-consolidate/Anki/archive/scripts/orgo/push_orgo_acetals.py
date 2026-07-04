"""
MCAT Organic Chemistry — Acetal / Ketal formation, recognition, and biology (3 cards).

Run:
    uv run --python 3.13 --with rdkit --with requests push_orgo_acetals.py
"""

import re
from orgo_helpers import assert_connected, anki, render_and_store, validate

DECK = "MCAT Organic Chemistry"

CARD_DIV = ("<div style='font-family: Arial, sans-serif; font-size: 18px; "
            "text-align: center; padding: 20px;'>")


def glucose_highlight(smiles):
    """Return (ring_oxygen_idxs + anomeric_carbon_idx) for highlighting the hemiacetal."""
    from rdkit import Chem
    mol = Chem.MolFromSmiles(smiles)
    ring = mol.GetRingInfo().AtomRings()[0]
    ring_oxys = [a for a in ring if mol.GetAtomWithIdx(a).GetSymbol() == "O"]
    anomeric = None
    for a in ring:
        at = mol.GetAtomWithIdx(a)
        if at.GetSymbol() != "C":
            continue
        nbrs = at.GetNeighbors()
        in_ring_O = any(n.GetIdx() in ring_oxys for n in nbrs)
        exo_OH = any(n.GetSymbol() == "O" and n.GetIdx() not in ring for n in nbrs)
        if in_ring_O and exo_OH:
            anomeric = a
    return ring_oxys + ([anomeric] if anomeric is not None else [])


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    # --- render diagrams ---
    # generic reaction-scheme pieces (small, inline)
    ald = render_and_store("ak-aldehyde", "*C=O", w=220, h=170,
                           dummy_labels=["R"], max_width=95, inline=True)
    acetal_sm = render_and_store("ak-acetal", "*C(O*)O*", w=240, h=190,
                                 dummy_labels=["R", "R'", "R'"], max_width=130, inline=True)
    ket = render_and_store("ak-ketone", "*C(=O)*", w=220, h=170,
                           dummy_labels=["R", "R'"], max_width=110, inline=True)
    ketal_sm = render_and_store("ak-ketal", "*C(*)(O*)O*", w=250, h=200,
                                dummy_labels=["R", "R'", "R''", "R''"], max_width=140, inline=True)

    # bigger centered acetal for the recognition card
    acetal_big = render_and_store("ak-acetal", "*C(O*)O*", w=240, h=190,
                                  dummy_labels=["R", "R'", "R'"], max_width=220)

    # glucose cyclic hemiacetal, anomeric C + ring O highlighted
    glu_smiles = "OC[C@H]1O[C@@H](O)[C@H](O)[C@@H](O)[C@@H]1O"
    glu = render_and_store("glucose-hemiacetal", glu_smiles, w=300, h=260,
                           highlight_atoms=glucose_highlight(glu_smiles), max_width=230)
    print("Diagrams rendered + stored.")

    arrow = "<span style='font-size:22px;'>&rarr;</span>"

    def scheme(left, right):
        return ("<div style='margin:8px 0; font-size:16px;'>" + left +
                " &nbsp;+&nbsp; 2&nbsp;R&prime;OH &nbsp;" + arrow + "&nbsp; " +
                right + " &nbsp;+&nbsp; H<sub>2</sub>O</div>")

    cards = [
        # 1 — Formation
        {
            "front": CARD_DIV + "<b>Acetal &amp; Ketal Formation</b><br><br>"
            "How do <span style='color: #4a90d9;'>acetals and ketals</span> form? "
            "Give the reaction and the conditions.</div>",
            "back": CARD_DIV + "<b>Acetal &amp; Ketal Formation</b><br><br>"
            "<span style='font-size:14px; color:#555;'>Acetal (from an <b>aldehyde</b>):</span>"
            + scheme(ald, acetal_sm) +
            "<span style='font-size:14px; color:#555;'>Ketal (from a <b>ketone</b>):</span>"
            + scheme(ket, ketal_sm) +
            "<br><b>Acid-catalyzed</b> and <b>reversible</b>."
            "<br><span style='font-size:13px; color:#888;'>Product = a central carbon bonded "
            "to two &ndash;OR groups. Each carbonyl reacts with <b>two</b> alcohol (R&prime;OH) "
            "groups, releasing water.</span></div>",
            "tags": ["orgo::reaction", "orgo::acetals-ketals"],
        },
        # 2 — Recognition + properties
        {
            "front": CARD_DIV + "<b>Recognizing Acetals &amp; Ketals</b><br><br>"
            "How do you <span style='color: #4a90d9;'>recognize</span> an acetal/ketal, and "
            "what are its key stability properties?</div>",
            "back": CARD_DIV + "<b>Recognizing Acetals &amp; Ketals</b><br><br>"
            + acetal_big +
            "A carbon bonded to <b>two &ndash;OR groups</b>.<br>"
            "<table style='margin:auto; text-align:left; font-size:15px;'>"
            "<tr><td style='padding:4px 10px;'><b>Acetal</b></td><td>from an <b>aldehyde</b> "
            "&mdash; central C also keeps an H</td></tr>"
            "<tr><td style='padding:4px 10px;'><b>Ketal</b></td><td>from a <b>ketone</b> "
            "&mdash; central C has two R groups</td></tr>"
            "<tr><td style='padding:4px 10px;'><b>Base</b></td><td><b>Stable</b> under basic "
            "conditions</td></tr>"
            "<tr><td style='padding:4px 10px;'><b>Acid</b></td><td><b>Hydrolyzes</b> back to the "
            "original carbonyl (acidic aqueous)</td></tr></table>"
            "<br><span style='font-size:13px; color:#888;'>A protecting group for carbonyls: "
            "stable in base, removed in aqueous acid.</span></div>",
            "tags": ["orgo::concept", "orgo::acetals-ketals"],
        },
        # 3 — Biological relevance
        {
            "front": CARD_DIV + "<b>Acetals &amp; Ketals &mdash; Biological Relevance</b><br><br>"
            "Why do <span style='color: #4a90d9;'>acetals/ketals</span> matter biologically?</div>",
            "back": CARD_DIV + "<b>Acetals &amp; Ketals &mdash; Biological Relevance</b><br><br>"
            + glu +
            "<span style='font-size:14px; color:#555;'>&beta;-D-glucose (cyclic hemiacetal) "
            "&mdash; red = anomeric carbon + ring O</span><br>"
            "<table style='margin:auto; text-align:left; font-size:15px;'>"
            "<tr><td style='padding:4px 10px;'><b>Sugar rings</b></td><td>form cyclic "
            "<b>hemiacetals/acetals</b> &mdash; how glucose exists in its ring form</td></tr>"
            "<tr><td style='padding:4px 10px;'><b>Glycosidic bonds</b></td><td>the linkages "
            "between sugars are <b>acetal</b> bonds</td></tr></table>"
            "<br><span style='font-size:13px; color:#888;'>Shows up constantly in carbohydrate "
            "passages. Hemiacetal = one OR + one OH on the carbon; acetal = two OR groups.</span></div>",
            "tags": ["orgo::concept", "orgo::acetals-ketals"],
        },
    ]

    for c in cards:
        validate(c["front"], c["back"])
    print("Validation passed.")

    # upsert by front <b>title</b> (each of these 3 titles is unique)
    existing = {}
    ids = anki("findNotes", query=f'deck:"{DECK}"')
    if ids:
        for n in anki("notesInfo", notes=ids):
            m = re.search(r"<b>(.*?)</b>", n["fields"]["Front"]["value"])
            if m:
                existing.setdefault(m.group(1), n["noteId"])

    added = updated = 0
    for c in cards:
        title = re.search(r"<b>(.*?)</b>", c["front"]).group(1)
        if title in existing:
            anki("updateNote", note={"id": existing[title],
                                     "fields": {"Front": c["front"], "Back": c["back"]},
                                     "tags": c["tags"]})
            updated += 1
        else:
            anki("addNote", note={"deckName": DECK, "modelName": "Basic",
                                  "fields": {"Front": c["front"], "Back": c["back"]},
                                  "tags": c["tags"], "options": {"allowDuplicate": False}})
            added += 1

    print(f"\nDone: {added} added, {updated} updated.")


if __name__ == "__main__":
    main()
