"""
One-time fix: replace all specific-example skeletal diagrams with generic
R-group structures across all 24 functional-group cards (12 learn + 12 recognize).

Run:
    uv run --python 3.13 --with rdkit --with requests fix_all_functional_group_images.py
"""

import re
import sys
sys.path.insert(0, "/Users/abigailbliss/Documents/mcat/03-consolidate/Anki")
from orgo_helpers import assert_connected, anki, render_and_store, validate

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::definition", "orgo::functional-groups"]
CARD_DIV = ("<div style='font-family: Arial, sans-serif; font-size: 18px; "
            "text-align: center; padding: 20px;'>")

# Generic SMILES with R-group wildcards for each functional group.
# dummy_labels replaces * atoms in order of appearance.
GENERIC = {
    "Alkane":          dict(img_name="alkane-generic",         smiles="[*]C[*]",         dummy_labels=["R", "R'"]),
    "Alkene":          dict(img_name="alkene-generic",         smiles="[*]C=C[*]",       dummy_labels=["R", "R'"]),
    "Alkyne":          dict(img_name="alkyne-generic",         smiles="[*]C#C[*]",       dummy_labels=["R", "R'"]),
    "Aromatic":        dict(img_name="aromatic-generic",       smiles="c1ccccc1",         dummy_labels=None),
    "Alcohol":         dict(img_name="alcohol-generic",        smiles="[*][OH]",          dummy_labels=["R"]),
    "Ether":           dict(img_name="ether-generic",          smiles="[*]O[*]",          dummy_labels=["R", "R'"]),
    "Aldehyde":        dict(img_name="aldehyde-generic",       smiles="[*]C(=O)[*]",     dummy_labels=["R", "H"]),
    "Ketone":          dict(img_name="ketone-generic",         smiles="[*]C(=O)[*]",     dummy_labels=["R", "R'"]),
    "Carboxylic acid": dict(img_name="carboxylic-acid-generic",smiles="[*]C(=O)[OH]",   dummy_labels=["R"]),
    "Ester":           dict(img_name="ester-generic",          smiles="[*]C(=O)O[*]",   dummy_labels=["R", "R'"]),
    "Amine":           dict(img_name="amine-generic",          smiles="[*][NH2]",         dummy_labels=["R"]),
    "Amide":           dict(img_name="amide-generic",          smiles="[*]C(=O)[NH2]",  dummy_labels=["R"]),
}

# Original facts from push_orgo_functional_groups.py (preserved verbatim)
GROUPS = [
    dict(name="Alkane",          ex="propane",        formula="C<sub>3</sub>H<sub>8</sub>",
         char="only C&ndash;C and C&ndash;H single bonds",
         suffix="<i>-ane</i>", note="Saturated hydrocarbon &mdash; single bonds only"),
    dict(name="Alkene",          ex="propene",        formula="C<sub>3</sub>H<sub>6</sub>",
         char="a carbon&ndash;carbon double bond (C=C)",
         suffix="<i>-ene</i>", note="Unsaturated &mdash; the C=C is the reactive site"),
    dict(name="Alkyne",          ex="propyne",        formula="C<sub>3</sub>H<sub>4</sub>",
         char="a carbon&ndash;carbon triple bond (C&equiv;C)",
         suffix="<i>-yne</i>", note="Unsaturated &mdash; linear around the triple bond"),
    dict(name="Aromatic",        ex="benzene",        formula="C<sub>6</sub>H<sub>6</sub>",
         char="a benzene ring &mdash; a 6-membered ring with delocalized &pi; electrons",
         suffix="<i>phenyl-</i> / <i>-benzene</i>",
         note="Extra-stable ring; often drawn with a circle inside"),
    dict(name="Alcohol",         ex="ethanol",        formula="CH<sub>3</sub>CH<sub>2</sub>OH",
         char="a hydroxyl group (&ndash;OH) bonded to a carbon",
         suffix="<i>-ol</i>", note="The &ndash;OH makes it polar and able to H-bond"),
    dict(name="Ether",           ex="diethyl ether",  formula="CH<sub>3</sub>CH<sub>2</sub>OCH<sub>2</sub>CH<sub>3</sub>",
         char="an oxygen bonded to two carbons (R&ndash;O&ndash;R)",
         suffix="<i>alkoxy-</i> / &ldquo;ether&rdquo;",
         note="Oxygen bridging two carbon groups"),
    dict(name="Aldehyde",        ex="acetaldehyde",   formula="CH<sub>3</sub>CHO",
         char="a terminal carbonyl (&ndash;CHO) &mdash; a C=O at the END of the chain",
         suffix="<i>-al</i>", note="Carbonyl carbon also carries an H"),
    dict(name="Ketone",          ex="acetone",        formula="CH<sub>3</sub>COCH<sub>3</sub>",
         char="an internal carbonyl (C=O) with a carbon on EACH side",
         suffix="<i>-one</i>", note="Carbonyl flanked by two carbons (never terminal)"),
    dict(name="Carboxylic acid", ex="acetic acid",    formula="CH<sub>3</sub>COOH",
         char="a carboxyl group (&ndash;COOH) &mdash; a C=O and an &ndash;OH on the SAME carbon",
         suffix="<i>-oic acid</i>", note="Acidic &mdash; donates the &ndash;OH proton"),
    dict(name="Ester",           ex="ethyl acetate",  formula="CH<sub>3</sub>COOCH<sub>2</sub>CH<sub>3</sub>",
         char="a carbonyl bonded to an oxygen&ndash;carbon (&ndash;C(=O)O&ndash;R)",
         suffix="<i>-oate</i>", note="A carboxylic acid with its H replaced by a carbon group"),
    dict(name="Amine",           ex="ethylamine",     formula="CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>",
         char="an amino group (&ndash;NH<sub>2</sub>) &mdash; nitrogen bonded to carbon",
         suffix="<i>-amine</i>", note="Basic &mdash; the N lone pair accepts a proton"),
    dict(name="Amide",           ex="acetamide",      formula="CH<sub>3</sub>CONH<sub>2</sub>",
         char="a carbonyl bonded to nitrogen (&ndash;C(=O)N)",
         suffix="<i>-amide</i>", note="Carbonyl + nitrogen &mdash; the linkage in peptide bonds"),
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
    learn_back  = CARD_DIV + "<b>" + g["name"] + "</b><br><br>" + img + "<br>" + facts + note + "</div>"
    rec_front   = (CARD_DIV + "<b>Identify the Functional Group</b><br><br>" + img +
                   "<br>What functional group is shown?</div>")
    rec_back    = CARD_DIV + "<b>" + g["name"] + "</b><br><br>" + facts + note + "</div>"
    return {"learn": (learn_front, learn_back), "recognize": (rec_front, rec_back)}


def main():
    assert_connected()

    # Render all generic images up front
    print("Rendering generic images...")
    imgs = {}
    for name, spec in GENERIC.items():
        imgs[name] = render_and_store(
            spec["img_name"], spec["smiles"],
            dummy_labels=spec["dummy_labels"]
        )
        print(f"  {name}: {spec['img_name']}.svg")

    # Fetch all existing functional-group notes
    ids = anki("findNotes", query=f'deck:"{DECK}" tag:orgo::functional-groups')
    notes_info = anki("notesInfo", notes=ids)
    print(f"\nFound {len(notes_info)} existing notes.")

    # Index by (direction, group_name)
    existing = {}
    for n in notes_info:
        back_val = n["fields"]["Back"]["value"]
        front_val = n["fields"]["Front"]["value"]
        # Group name is always in <b>...</b> in the back
        m = re.search(r"<b>(.*?)</b>", back_val)
        if not m:
            continue
        group_name = m.group(1)
        # Direction: recognize cards have the image in the front
        direction = "recognize" if "orgo-" in front_val else "learn"
        existing[(direction, group_name)] = n["noteId"]

    print(f"Indexed {len(existing)} notes by (direction, group).\n")

    updated = 0
    errors = []
    for g in GROUPS:
        name = g["name"]
        cards = build_cards(g, imgs[name])
        for direction, (front, back) in cards.items():
            validate(front, back)
            key = (direction, name)
            if key not in existing:
                errors.append(f"NOT FOUND: {direction} / {name}")
                continue
            anki("updateNote", note={
                "id": existing[key],
                "fields": {"Front": front, "Back": back},
                "tags": TAGS,
            })
            updated += 1
            print(f"  Updated {direction:9s} | {name}")

    print(f"\nDone: {updated} updated.")
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  {e}")


if __name__ == "__main__":
    main()
