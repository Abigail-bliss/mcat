"""
Geometric (cis/trans, E/Z) isomers card for the MCAT Organic Chemistry deck.

Run:
    uv run --python 3.13 --with rdkit --with requests push_geometric_isomers_card.py
"""

from orgo_helpers import (
    assert_connected, anki, render_and_store, validate, push_cards,
)

DECK = "MCAT Organic Chemistry"
TOPIC = "Geometric Isomers"


def card_front(topic, question):
    return (
        r"<div style='font-family: Arial, sans-serif; font-size: 18px; "
        r"text-align: center; padding: 20px;'><b>" + topic + r"</b><br><br>" +
        question + r"</div>"
    )


def card_back(topic, body):
    return (
        r"<div style='font-family: Arial, sans-serif; font-size: 18px; "
        r"text-align: center; padding: 20px;'><b>" + topic + r"</b><br><br>" +
        body + r"</div>"
    )


def figure(img, caption):
    return (
        r"<div style='display:inline-block; vertical-align:top; margin:6px 10px; "
        r"width:180px;'>" + img +
        r"<div style='font-size:13px; color:#555;'>" + caption + r"</div></div>"
    )


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    cis = render_and_store("cis-2-butene", r"C/C=C\C", w=180, h=150, max_width=160)
    trans = render_and_store("trans-2-butene", r"C/C=C/C", w=180, h=150, max_width=160)
    print("Rendered + stored cis- and trans-2-butene.")

    blue = r"<span style='color: #4a90d9;'>"

    cards = [
        {
            "front": card_front(
                TOPIC,
                r"What are " + blue + r"geometric isomers</span>, and how do you "
                r"name them?",
            ),
            "back": card_back(
                TOPIC,
                r"Geometric (cis/trans) isomers arise when a <b>rigid &pi; bond</b> "
                r"(C=C) blocks rotation between two atoms.<br><br>"
                r"<b>1,2-disubstituted alkenes:</b> substituents on the "
                r"<b>same side = cis</b>, on <b>opposite sides = trans</b>. The "
                r"<b>trans</b> isomer is more stable (less steric repulsion)."
                + figure(cis, r"<b>cis</b>-2-butene") + figure(trans, r"<b>trans</b>-2-butene") +
                r"<br><b>Tri-/tetrasubstituted alkenes &rarr; use E/Z:</b>"
                r"<table style='margin: 10px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px;'><b>1.</b></td>"
                r"<td>Cut the alkene in half vertically</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>2.</b></td>"
                r"<td>Assign high/low priority on each side by the "
                r"<b>Cahn&ndash;Ingold&ndash;Prelog</b> rules (same as R/S)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>3.</b></td>"
                r"<td>High-priority groups on the <b>same</b> side &rarr; <b>(Z)</b></td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>4.</b></td>"
                r"<td>High-priority groups on <b>opposite</b> sides &rarr; <b>(E)</b></td></tr>"
                r"</table>"
                r"<span style='font-size:13px; color:#888;'>Mnemonic: <b>Z = &ldquo;zame "
                r"zide&rdquo;</b> (Z is like &ldquo;zis&rdquo; &rarr; cis).</span>",
            ),
            "tags": ["orgo::concept", "orgo::stereochemistry"],
        },
    ]

    print("Validating...")
    for c in cards:
        validate(c["front"], c["back"])
    print("Validation passed.")

    added, updated, errors = push_cards(cards, DECK)
    print(f"\nDone: {added} added, {updated} updated, {len(errors)} errors.")
    for e in errors:
        print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
