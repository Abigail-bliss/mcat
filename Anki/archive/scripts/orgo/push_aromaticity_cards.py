"""
Aromaticity cards for the MCAT Organic Chemistry deck.

Four concept cards:
  1. The 4 criteria for aromaticity
  2. Carbon-only examples (aromatic vs. anti-/non-aromatic) + skeletal diagrams
  3. How heteroatoms (N, O, S) contribute pi electrons
  4. Heteroatom aromatic examples + skeletal diagrams

Run:
    uv run --python 3.13 --with rdkit --with requests push_aromaticity_cards.py
"""

from orgo_helpers import (
    assert_connected, anki, render_and_store, validate, push_cards,
)

DECK = "MCAT Organic Chemistry"
TOPIC = "Aromaticity"


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
    """A small skeletal structure with a caption underneath, inline-block so several
    sit side-by-side and wrap as needed."""
    return (
        r"<div style='display:inline-block; vertical-align:top; margin:6px 10px; "
        r"width:170px;'>" + img +
        r"<div style='font-size:13px; color:#555;'>" + caption + r"</div></div>"
    )


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    # --- skeletal structures (small, for side-by-side figures) ---
    benzene = render_and_store("benzene", "c1ccccc1", w=170, h=150, max_width=150)
    cyclobutadiene = render_and_store("cyclobutadiene", "C1=CC=C1", w=170, h=150, max_width=150)
    cot = render_and_store("cyclooctatetraene", "C1=CC=CC=CC=C1", w=170, h=150, max_width=150)
    pyrrole = render_and_store("pyrrole", "c1cc[nH]c1", w=170, h=150, max_width=150)
    pyridine = render_and_store("pyridine", "c1ccncc1", w=170, h=150, max_width=150)
    furan = render_and_store("furan", "c1ccoc1", w=170, h=150, max_width=150)
    thiophene = render_and_store("thiophene", "c1ccsc1", w=170, h=150, max_width=150)
    print("Rendered + stored 7 structures.")

    blue = r"<span style='color: #4a90d9;'>"

    cards = [
        # ---- Card 1: the 4 criteria ----
        {
            "front": card_front(
                TOPIC,
                r"What four criteria must a molecule meet to be " + blue +
                r"aromatic</span>?",
            ),
            "back": card_back(
                TOPIC,
                r"Aromatic compounds meet a strict set of criteria and are "
                r"<b>especially stable</b>. All four are required:"
                r"<table style='margin: 12px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px;'><b>1.</b></td>"
                r"<td>Obeys <b>H&uuml;ckel's Rule</b>: # &pi; electrons = <b>4n + 2</b> "
                r"(2, 6, 10, &hellip;)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>2.</b></td>"
                r"<td>Has a concentric ring of <b>aligned p-orbitals</b> "
                r"(i.e. resonance / conjugation)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>3.</b></td>"
                r"<td><b>Planar</b> (big rings are not planar)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>4.</b></td>"
                r"<td><b>Cyclic</b></td></tr></table>"
                r"<span style='font-size:13px; color:#888;'>Miss any one criterion "
                r"&rarr; not aromatic.</span>",
            ),
            "tags": ["orgo::concept", "orgo::aromatics"],
        },
        # ---- Card 2: carbon-only examples ----
        {
            "front": card_front(
                TOPIC,
                r"Among these carbon-only rings, which are " + blue +
                r"aromatic</span> and which are not?<br><br>" +
                figure(benzene, r"benzene") +
                figure(cyclobutadiene, r"cyclobutadiene") +
                figure(cot, r"cyclooctatetraene"),
            ),
            "back": card_back(
                TOPIC,
                figure(benzene, r"<b>Benzene &#10003;</b><br>6 &pi; e&minus; (4n+2, n=1)"
                                r"<br>planar, cyclic, conjugated") +
                figure(cyclobutadiene, r"<b>Cyclobutadiene &#10007;</b><br>4 &pi; e&minus; (4n)"
                                       r"<br><i>antiaromatic</i>") +
                figure(cot, r"<b>Cyclooctatetraene &#10007;</b><br>8 &pi; e&minus; (4n) "
                            r"and too big to stay planar &mdash; puckers into a tub") +
                r"<br><span style='font-size:13px; color:#888;'>Alternating double bonds "
                r"alone are <b>not</b> enough &mdash; all four criteria must hold.</span>",
            ),
            "tags": ["orgo::concept", "orgo::aromatics"],
        },
        # ---- Card 3: heteroatom contributions ----
        {
            "front": card_front(
                TOPIC,
                r"How do the heteroatoms " + blue + r"N, O, and S</span> contribute "
                r"&pi; electrons to an aromatic ring?",
            ),
            "back": card_back(
                TOPIC,
                r"Cyclic molecules with heteroatoms can be aromatic too. Look out for:"
                r"<table style='margin: 12px auto; text-align: left; font-size: 15px;'>"
                r"<tr><td style='padding:4px 10px;'><b>Nitrogen</b></td>"
                r"<td><b>pyrrole-type</b> (lone pair in the p-orbital, part of the &pi; "
                r"system) &rarr; donates <b>2</b> &pi; e&minus;<br>"
                r"<b>pyridine-type</b> (N in a C=N double bond, lone pair in-plane) "
                r"&rarr; donates <b>0</b> &pi; e&minus;</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>Oxygen</b></td>"
                r"<td>sp&sup2; &rarr; donates <b>2</b> &pi; e&minus; "
                r"(one lone pair into the &pi; system, one stays in-plane)</td></tr>"
                r"<tr><td style='padding:4px 10px;'><b>Sulfur</b></td>"
                r"<td>sp&sup2; &rarr; donates <b>2</b> &pi; e&minus;</td></tr></table>"
                r"<span style='font-size:13px; color:#888;'>Count every &pi; electron, "
                r"then check 4n+2.</span>",
            ),
            "tags": ["orgo::concept", "orgo::aromatics"],
        },
        # ---- Card 4: heteroatom examples ----
        {
            "front": card_front(
                TOPIC,
                r"Why is each of these heteroatom rings " + blue +
                r"aromatic</span>?<br><br>" +
                figure(pyrrole, r"pyrrole") +
                figure(pyridine, r"pyridine") +
                figure(furan, r"furan") +
                figure(thiophene, r"thiophene"),
            ),
            "back": card_back(
                TOPIC,
                figure(pyrrole, r"<b>Pyrrole</b><br>N donates 2 + two C=C (4) = "
                                r"<b>6 &pi; e&minus;</b>") +
                figure(pyridine, r"<b>Pyridine</b><br>N donates 0; three double bonds = "
                                 r"<b>6 &pi; e&minus;</b>") +
                figure(furan, r"<b>Furan</b><br>O donates 2 + 4 = <b>6 &pi; e&minus;</b>") +
                figure(thiophene, r"<b>Thiophene</b><br>S donates 2 + 4 = "
                                  r"<b>6 &pi; e&minus;</b>") +
                r"<br><span style='font-size:13px; color:#888;'>All four reach "
                r"<b>6 &pi; electrons</b> (4n+2, n=1) &rarr; aromatic.</span>",
            ),
            "tags": ["orgo::concept", "orgo::aromatics"],
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
