"""
MCAT Organic Chemistry — Imine / Enamine formation and recognition (2 cards).

Run:
    uv run --python 3.13 --with rdkit --with requests push_orgo_imines_enamines.py
"""

import re
from orgo_helpers import assert_connected, anki, render_and_store, validate

DECK = "MCAT Organic Chemistry"

CARD_DIV = ("<div style='font-family: Arial, sans-serif; font-size: 18px; "
            "text-align: center; padding: 20px;'>")


def main():
    assert_connected()
    print("AnkiConnect connected.")
    anki("createDeck", deck=DECK)

    arrow = "<span style='font-size:22px;'>&rarr;</span>"

    # --- render diagrams ---
    ald = render_and_store("ie-aldehyde", r"*C=O", w=200, h=160,
                           dummy_labels=["R"], max_width=85, inline=True)

    # generic imine R-CH=N-R' — inline for scheme, also used in recognition table
    imine_cell = render_and_store("ie-imine", r"*C=N*", w=230, h=180,
                                  dummy_labels=["R", "R'"], max_width=160, inline=True)

    # enamine CH2=CH-N(CH3)2 — shows the C=C-N pattern
    enamine_cell = render_and_store("ie-enamine", r"C=CN(C)C", w=240, h=185,
                                    max_width=160, inline=True)

    # smaller inline versions for reaction scheme
    imine_sm = render_and_store("ie-imine", r"*C=N*", w=230, h=180,
                                dummy_labels=["R", "R'"], max_width=110, inline=True)
    enamine_sm = render_and_store("ie-enamine", r"C=CN(C)C", w=240, h=185,
                                  max_width=115, inline=True)

    print("Diagrams rendered + stored.")

    def scheme(left, amine_text, right):
        return ("<div style='margin:8px 0; font-size:16px;'>" + left +
                " &nbsp;+&nbsp; " + amine_text + " &nbsp;" + arrow + "&nbsp; " +
                right + " &nbsp;+&nbsp; H<sub>2</sub>O</div>")

    cards = [
        # 1 — Formation
        {
            "front": (CARD_DIV + "<b>Imine &amp; Enamine Formation</b><br><br>"
                     "How do <span style='color: #4a90d9;'>imines and enamines</span> form? "
                     "What type of amine gives each product?</div>"),
            "back": (CARD_DIV + "<b>Imine &amp; Enamine Formation</b><br><br>"
                    "<span style='font-size:14px; color:#555;'>Imine (from a <b>primary amine</b>, "
                    "R&prime;&ndash;NH<sub>2</sub>):</span>"
                    + scheme(ald, "R&prime;&ndash;NH<sub>2</sub>", imine_sm) +
                    "<span style='font-size:14px; color:#555;'>Enamine (from a <b>secondary amine</b>, "
                    "R&prime;<sub>2</sub>NH):</span>"
                    + scheme(ald, "R&prime;<sub>2</sub>NH", enamine_sm) +
                    "<br><b>Acid-catalyzed</b> and <b>reversible</b>. "
                    "Enamine requires an &alpha;&ndash;hydrogen on the carbonyl."
                    "<br><span style='font-size:13px; color:#888;'>Primary amine (one R on N) "
                    "&rarr; <b>imine</b> (C=N). Secondary amine (two R&rsquo;s on N) "
                    "&rarr; <b>enamine</b> (C=C&ndash;N). "
                    "In both cases the carbonyl O leaves as water.</span></div>"),
            "tags": ["orgo::reaction", "orgo::imines-enamines"],
        },
        # 2 — Recognition + Properties
        {
            "front": (CARD_DIV + "<b>Recognizing Imines &amp; Enamines</b><br><br>"
                     "How do you <span style='color: #4a90d9;'>identify</span> an imine vs. an enamine "
                     "on a structure? What are their key stability properties?</div>"),
            "back": (CARD_DIV + "<b>Recognizing Imines &amp; Enamines</b><br><br>"
                    "<table style='margin:auto; text-align:center; font-size:15px;'>"
                    "<tr>"
                    "<td style='padding:6px 20px; vertical-align:bottom;'>" + imine_cell + "</td>"
                    "<td style='padding:6px 20px; vertical-align:bottom;'>" + enamine_cell + "</td>"
                    "</tr><tr>"
                    "<td style='padding:4px 20px;'><b>Imine</b><br>C=N&ndash;R</td>"
                    "<td style='padding:4px 20px;'><b>Enamine</b><br>C=C&ndash;N</td>"
                    "</tr><tr>"
                    "<td style='padding:2px 20px; font-size:14px; color:#555;'>from a <b>primary</b> amine</td>"
                    "<td style='padding:2px 20px; font-size:14px; color:#555;'>from a <b>secondary</b> amine</td>"
                    "</tr></table>"
                    "<br><b>Both:</b> acid-catalyzed &amp; reversible &mdash; "
                    "hydrolyze in acidic aqueous &rarr; original carbonyl."
                    "<br><span style='font-size:13px; color:#888;'>Key tell: imine has the "
                    "<b>C=N</b> bond; enamine has <b>C=C adjacent to N</b>.</span></div>"),
            "tags": ["orgo::concept", "orgo::imines-enamines"],
        },
    ]

    for c in cards:
        validate(c["front"], c["back"])
    print("Validation passed.")

    # upsert by front <b>title</b>
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
                                  "tags": c["tags"],
                                  "options": {"allowDuplicate": False}})
            added += 1

    print(f"\nDone: {added} added, {updated} updated.")


if __name__ == "__main__":
    main()
