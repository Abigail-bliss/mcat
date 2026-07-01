"""
MCAT Organic Chemistry — Core 12 functional groups, both directions (24 cards).

Per group:
  - LEARN card  (name -> structure): front = group name; back = skeletal image + facts
  - RECOGNIZE card (structure -> name): front = image (generic title, no giveaway); back = name + facts

Robust upsert: re-runs UPDATE in place. Anki reformats stored HTML (single->double quotes,
adds <tbody>) and strips <img> when computing duplicate keys, so we key off the stable
(direction, image-filename) signature rather than exact Front text.

Run:
    uv run --python 3.13 --with rdkit --with requests push_orgo_functional_groups.py
"""

import re
from orgo_helpers import assert_connected, anki, render_and_store, validate

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::definition", "orgo::functional-groups"]

CARD_DIV = ("<div style='font-family: Arial, sans-serif; font-size: 18px; "
            "text-align: center; padding: 20px;'>")

GROUPS = [
    dict(name="Alkane", ex="propane", formula="C<sub>3</sub>H<sub>8</sub>", smiles="CCC",
         char="only C&ndash;C and C&ndash;H single bonds", suffix="<i>-ane</i>",
         note="Saturated hydrocarbon &mdash; single bonds only"),
    dict(name="Alkene", ex="propene", formula="C<sub>3</sub>H<sub>6</sub>", smiles="CC=C",
         char="a carbon&ndash;carbon double bond (C=C)", suffix="<i>-ene</i>",
         note="Unsaturated &mdash; the C=C is the reactive site"),
    dict(name="Alkyne", ex="propyne", formula="C<sub>3</sub>H<sub>4</sub>", smiles="CC#C",
         char="a carbon&ndash;carbon triple bond (C&equiv;C)", suffix="<i>-yne</i>",
         note="Unsaturated &mdash; linear around the triple bond"),
    dict(name="Aromatic", ex="benzene", formula="C<sub>6</sub>H<sub>6</sub>", smiles="c1ccccc1",
         char="a benzene ring &mdash; a 6-membered ring with delocalized &pi; electrons",
         suffix="<i>phenyl-</i> / <i>-benzene</i>",
         note="Extra-stable ring; often drawn with a circle inside"),
    dict(name="Alcohol", ex="ethanol", formula="CH<sub>3</sub>CH<sub>2</sub>OH", smiles="CCO",
         char="a hydroxyl group (&ndash;OH) bonded to a carbon", suffix="<i>-ol</i>",
         note="The &ndash;OH makes it polar and able to H-bond"),
    dict(name="Ether", ex="diethyl ether", formula="CH<sub>3</sub>CH<sub>2</sub>OCH<sub>2</sub>CH<sub>3</sub>",
         smiles="CCOCC", char="an oxygen bonded to two carbons (R&ndash;O&ndash;R)",
         suffix="<i>alkoxy-</i> / &ldquo;ether&rdquo;",
         note="Oxygen bridging two carbon groups"),
    dict(name="Aldehyde", ex="acetaldehyde", formula="CH<sub>3</sub>CHO", smiles="CC=O",
         char="a terminal carbonyl (&ndash;CHO) &mdash; a C=O at the END of the chain",
         suffix="<i>-al</i>", note="Carbonyl carbon also carries an H"),
    dict(name="Ketone", ex="acetone", formula="CH<sub>3</sub>COCH<sub>3</sub>", smiles="CC(=O)C",
         char="an internal carbonyl (C=O) with a carbon on EACH side", suffix="<i>-one</i>",
         note="Carbonyl flanked by two carbons (never terminal)"),
    dict(name="Carboxylic acid", ex="acetic acid", formula="CH<sub>3</sub>COOH", smiles="CC(=O)O",
         char="a carboxyl group (&ndash;COOH) &mdash; a C=O and an &ndash;OH on the SAME carbon",
         suffix="<i>-oic acid</i>", note="Acidic &mdash; donates the &ndash;OH proton"),
    dict(name="Ester", ex="ethyl acetate", formula="CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>",
         smiles="CCOC(=O)C", char="a carbonyl bonded to an oxygen&ndash;carbon (&ndash;C(=O)O&ndash;R)",
         suffix="<i>-oate</i>", note="A carboxylic acid with its H replaced by a carbon group"),
    dict(name="Amine", ex="ethylamine", formula="CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>", smiles="CCN",
         char="an amino group (&ndash;NH<sub>2</sub>) &mdash; nitrogen bonded to carbon", suffix="<i>-amine</i>",
         note="Basic &mdash; the N lone pair accepts a proton"),
    dict(name="Amide", ex="acetamide", formula="CH<sub>3</sub>CONH<sub>2</sub>", smiles="CC(=O)N",
         char="a carbonyl bonded to nitrogen (&ndash;C(=O)N)", suffix="<i>-amide</i>",
         note="Carbonyl + nitrogen &mdash; the linkage in peptide bonds"),
]


def facts_block(g):
    return (
        "<table style='margin: auto; text-align: left; font-size: 15px;'>"
        "<tr><td style='padding: 4px 10px;'><b>Group</b></td><td>" + g["char"] + "</td></tr>"
        "<tr><td style='padding: 4px 10px;'><b>Naming</b></td><td>" + g["suffix"] + "</td></tr>"
        "<tr><td style='padding: 4px 10px;'><b>Example</b></td><td>" + g["ex"] +
        " (" + g["formula"] + ")</td></tr></table>"
    )


def footnote(text):
    return "<br><span style='font-size: 13px; color: #888;'>" + text + "</span>"


def build_cards(g, img):
    facts = facts_block(g)
    note = footnote(g["note"])

    learn_front = (CARD_DIV + "<b>" + g["name"] + "</b><br><br>What is its "
                   "<span style='color: #4a90d9;'>structure</span>?</div>")
    learn_back = (CARD_DIV + "<b>" + g["name"] + "</b><br><br>" + img + "<br>" + facts + note + "</div>")

    rec_front = (CARD_DIV + "<b>Identify the Functional Group</b><br><br>" + img +
                 "<br>What functional group is shown?</div>")
    rec_back = (CARD_DIV + "<b>" + g["name"] + "</b><br><br>" + facts + note + "</div>")

    return [
        {"front": learn_front, "back": learn_back, "tags": TAGS},
        {"front": rec_front, "back": rec_back, "tags": TAGS},
    ]


def signature(front, back):
    """Stable identity: (direction, image filename). Survives Anki's HTML reformatting."""
    m = re.search(r"orgo-[a-z0-9\-]+\.svg", front)
    if m:
        return ("recognize", m.group(0))
    m = re.search(r"orgo-[a-z0-9\-]+\.svg", back)
    if m:
        return ("learn", m.group(0))
    return None


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    # --- delete the 2 disposable PoC cards ---
    poc = anki("findNotes", query=f'deck:"{DECK}" "front:*Name this molecule*"')
    poc += anki("findNotes", query=f'deck:"{DECK}" "front:*Draw the skeletal structure*"')
    if poc:
        anki("deleteNotes", notes=poc)
    print(f"Deleted {len(poc)} PoC card(s).")

    # --- render images + build cards ---
    cards = []
    for g in GROUPS:
        img = render_and_store(g["ex"], g["smiles"])
        cards.extend(build_cards(g, img))
    print(f"Rendered {len(GROUPS)} images, built {len(cards)} cards.")

    for c in cards:
        validate(c["front"], c["back"])
    print("Validation passed.")

    # --- upsert by (direction, filename) signature ---
    existing = {}
    ids = anki("findNotes", query=f'deck:"{DECK}"')
    if ids:
        for n in anki("notesInfo", notes=ids):
            sig = signature(n["fields"]["Front"]["value"], n["fields"]["Back"]["value"])
            if sig:
                existing[sig] = n["noteId"]

    added = updated = 0
    for c in cards:
        sig = signature(c["front"], c["back"])
        if sig in existing:
            anki("updateNote", note={"id": existing[sig],
                                     "fields": {"Front": c["front"], "Back": c["back"]},
                                     "tags": c["tags"]})
            updated += 1
        else:
            anki("addNote", note={
                "deckName": DECK, "modelName": "Basic",
                "fields": {"Front": c["front"], "Back": c["back"]},
                "tags": c["tags"],
                # recognize-card fronts strip to identical text (image removed), so Anki
                # would flag them as mutual duplicates; allow it — our signature upsert
                # is what actually guarantees no real duplicates across runs.
                "options": {"allowDuplicate": True},
            })
            added += 1

    print(f"\nDone: {added} added, {updated} updated. Total cards: {len(cards)}.")


if __name__ == "__main__":
    main()
