"""
Proof-of-concept for the MCAT Organic Chemistry deck: skeletal structures rendered
from SMILES via RDKit, stored as Anki media, embedded on cards.

Run:
    uv run --python 3.13 --with rdkit --with requests push_orgo_cards.py
"""

from orgo_helpers import (
    assert_connected, anki, render_and_store, validate, push_cards,
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
    print(f"Deck '{DECK}' ready.")

    # Render skeletal structures (returns ready-to-embed <img> snippets)
    benzene_img = render_and_store("benzene", "c1ccccc1")
    ethanol_img = render_and_store("ethanol", "CCO")
    print("Rendered + stored: orgo-benzene.svg, orgo-ethanol.svg")

    cards = [
        {
            "front": card_front(
                "Aromatic Compounds",
                r"Name this molecule and give its molecular formula.<br>" + benzene_img,
            ),
            "back": card_back(
                "Aromatic Compounds",
                r"<b>Benzene</b> &mdash; C<sub>6</sub>H<sub>6</sub><br><br>"
                r"<span style='font-size: 14px; color: #555;'>Planar 6-membered aromatic "
                r"ring; delocalized &pi; system (resonance, bond order 1.5).</span>",
            ),
            "tags": ["orgo::concept", "orgo::aromatics"],
        },
        {
            "front": card_front(
                "Alcohols",
                r"Draw the skeletal structure of <span style='color: #4a90d9;'>ethanol</span> "
                r"(C<sub>2</sub>H<sub>5</sub>OH).",
            ),
            "back": card_back(
                "Alcohols",
                ethanol_img +
                r"<br><span style='font-size: 14px; color: #555;'>Two carbons with a terminal "
                r"hydroxyl (&ndash;OH) functional group.</span>",
            ),
            "tags": ["orgo::nomenclature", "orgo::alcohols"],
        },
    ]

    print("Validating...")
    for c in cards:
        validate(c["front"], c["back"])
    print("Validation passed.")

    added, updated, errors = push_cards(cards, DECK)
    print(f"\nDone: {added} added, {updated} updated, {len(errors)} errors.")
    if errors:
        for e in errors:
            print(f"  ERROR: {e}")


if __name__ == "__main__":
    main()
