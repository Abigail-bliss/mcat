"""
Chirality cards for the MCAT Organic Chemistry deck.

Two concept cards:
  1. Chiral vs. achiral molecules
  2. How to find a chiral center (+ stereocenter vs. chiral center distinction)

Run:
    uv run --python 3.13 --with rdkit --with requests push_chirality_cards.py
"""

from orgo_helpers import (
    assert_connected, anki, render_and_store, validate, push_cards,
)

DECK = "MCAT Organic Chemistry"
TOPIC = "Chirality"


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

    # 2-bromobutane: CC(Br)CC -> C0, C1(center), Br2, C3, C4. Highlight the chiral C (index 1).
    bromobutane = render_and_store(
        "2-bromobutane", "CC(Br)CC", w=220, h=180, max_width=200, highlight_atoms=[1]
    )
    print("Rendered + stored 2-bromobutane (chiral C highlighted).")

    blue = r"<span style='color: #4a90d9;'>"

    cards = [
        # ---- Card 1: chiral vs. achiral ----
        {
            "front": card_front(
                TOPIC,
                r"What is the difference between a " + blue + r"chiral</span> and an " +
                blue + r"achiral</span> molecule?",
            ),
            "back": card_back(
                TOPIC,
                r"<table style='margin: 10px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px;'><b>Chiral</b></td>"
                r"<td><b>Non-superimposable</b> on its mirror image "
                r"(like your left vs. right hand); has <b>no</b> internal plane of "
                r"symmetry</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>Achiral</b></td>"
                r"<td><b>Superimposable</b> on its mirror image; <b>has</b> an internal "
                r"plane of symmetry</td></tr></table>"
                r"<span style='font-size:13px; color:#888;'>Test: build the mirror image &mdash; "
                r"if you can rotate it to overlap the original it's achiral; if not, "
                r"it's chiral.</span>",
            ),
            "tags": ["orgo::concept", "orgo::stereochemistry"],
        },
        # ---- Card 2: finding chiral centers ----
        {
            "front": card_front(
                TOPIC,
                r"How do you find a " + blue + r"chiral center</span>?",
            ),
            "back": card_back(
                TOPIC,
                r"Look for an <b>sp&sup3; (tetrahedral) carbon bonded to 4 different "
                r"groups</b>."
                r"<table style='margin: 10px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px;'><b>1.</b></td>"
                r"<td>Scan each carbon in turn</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>2.</b></td>"
                r"<td>Check that all 4 attached groups differ &mdash; even subtle "
                r"differences count (&ndash;CH<sub>3</sub> vs. &ndash;CH<sub>2</sub>CH<sub>3</sub>)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>3.</b></td>"
                r"<td>Carbons inside rings count too</td></tr></table>"
                + bromobutane +
                r"<span style='font-size:14px; color:#555;'><b>2-bromobutane</b> &mdash; the "
                r"highlighted C holds H, Br, &ndash;CH<sub>3</sub>, and "
                r"&ndash;CH<sub>2</sub>CH<sub>3</sub> (all 4 different) &rarr; chiral "
                r"center.</span><br><br>"
                r"<span style='font-size:13px; color:#888;'><b>Stereocenter vs. chiral "
                r"center:</b> all chiral centers are stereocenters, but stereocenters also "
                r"include double-bond carbons that give E/Z isomers.</span>",
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
