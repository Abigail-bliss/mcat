"""
Cahn-Ingold-Prelog priority rules + R/S assignment cards for the
MCAT Organic Chemistry deck.

Run:
    uv run --python 3.13 --with rdkit --with requests push_cip_rs_cards.py
"""

from orgo_helpers import (
    assert_connected, anki, validate, push_cards,
)

DECK = "MCAT Organic Chemistry"


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


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    blue = r"<span style='color: #4a90d9;'>"

    cards = [
        # ---- Card 1: CIP priority rules ----
        {
            "front": card_front(
                "Cahn-Ingold-Prelog Rules",
                r"How do you rank the priority of the substituents on a " + blue +
                r"stereocenter</span>?",
            ),
            "back": card_back(
                "Cahn-Ingold-Prelog Rules",
                r"They rank the four substituents so you can assign <b>R/S</b>."
                r"<table style='margin: 10px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>1.</b></td>"
                r"<td>Confirm it's a <b>chiral carbon</b> &mdash; you cannot have R/S at a "
                r"non-chiral atom</td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>2.</b></td>"
                r"<td>Compare the atoms <b>directly bonded</b> to the center &mdash; "
                r"<b>higher atomic number = higher priority</b></td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>3.</b></td>"
                r"<td><b>Ties:</b> move outward atom-by-atom, comparing the set of atoms at "
                r"each step, until you reach the first point of difference</td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>4.</b></td>"
                r"<td><b>Multiple bonds</b> duplicate atoms: <b>C=X</b> &rarr; C bonded to "
                r"<b>two</b> X&rsquo;s; <b>C&equiv;X</b> &rarr; C bonded to <b>three</b> "
                r"X&rsquo;s</td></tr></table>"
                r"<span style='font-size:13px; color:#888;'>Same priority rules are used to "
                r"assign E/Z on alkenes.</span>",
            ),
            "tags": ["orgo::concept", "orgo::stereochemistry"],
        },
        # ---- Card 2: assigning R/S ----
        {
            "front": card_front(
                "R / S Nomenclature",
                r"How do you assign " + blue + r"R or S</span> to a stereocenter?",
            ),
            "back": card_back(
                "R / S Nomenclature",
                r"<table style='margin: 10px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>1.</b></td>"
                r"<td>Find the chiral center (stereocenter)</td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>2.</b></td>"
                r"<td>Rank the four substituents by <b>CIP</b> priority</td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>3.</b></td>"
                r"<td><b>#4 (lowest) in back:</b> trace 1&rarr;2&rarr;3 &mdash; "
                r"clockwise = <b>R</b>, counterclockwise = <b>S</b></td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>4.</b></td>"
                r"<td><b>#4 in front:</b> trace 1&rarr;2&rarr;3 &mdash; clockwise = "
                r"<b>S</b>, counterclockwise = <b>R</b> (reversed)</td></tr>"
                r"<tr><td style='padding:4px 10px; vertical-align:top;'><b>5.</b></td>"
                r"<td><b>#4 in the plane:</b> redraw so it points back, then apply step 3</td></tr>"
                r"</table>"
                r"<span style='font-size:13px; color:#888;'>Tip: if #4 is in front, assign "
                r"as if it were in back, then <b>flip</b> the answer.</span>",
            ),
            "tags": ["orgo::nomenclature", "orgo::stereochemistry"],
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
