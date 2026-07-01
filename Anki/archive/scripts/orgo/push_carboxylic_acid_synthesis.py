"""Push a single summary card: three reaction pathways that form a carboxylic acid.
Skeletal diagrams rendered generically with an R group via RDKit dummy labels.

    uv run --python 3.13 --with rdkit --with requests push_carboxylic_acid_synthesis.py
"""

from orgo_helpers import assert_connected, render_and_store, validate, push_cards

DECK = "MCAT Organic Chemistry"

assert_connected()

# Generic skeletal diagrams (R = dummy atom labeled "R"), small for table cells.
aldehyde = render_and_store("cooh-from-aldehyde", "*C=O",
                            dummy_labels=["R"], w=200, h=150, max_width=120, inline=True)
alcohol  = render_and_store("cooh-from-1alcohol", "*CO",
                            dummy_labels=["R"], w=200, h=150, max_width=120, inline=True)
halide   = render_and_store("cooh-from-alkylhalide", "*Br",
                            dummy_labels=["R"], w=200, h=150, max_width=120, inline=True)
acid     = render_and_store("cooh-product", "*C(=O)O",
                            dummy_labels=["R"], w=200, h=150, max_width=120, inline=True)

front = (
    r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>"
    r"<b>Forming a Carboxylic Acid</b><br><br>"
    r"What are the <span style='color: #4a90d9;'>three reaction pathways</span> that produce a "
    r"<span style='color: #4a90d9;'>carboxylic acid</span>?</div>"
)

cell = "padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: middle;"
hcell = "padding: 8px 12px; border-bottom: 2px solid #ccc;"

back = (
    r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
    r"<b>Forming a Carboxylic Acid</b><br><br>"
    r'<table style="margin: auto; text-align: center; font-size: 14px; border-collapse: collapse;"><tbody>'
    rf'<tr><td style="{hcell}"><b>Starting Material</b></td>'
    rf'<td style="{hcell}"><b>Reagents / Conditions</b></td>'
    rf'<td style="{hcell}"><b>Product</b></td></tr>'
    # Row 1 - aldehyde
    rf'<tr><td style="{cell}"><b>Aldehyde</b><br>(R&ndash;CHO)<br>{aldehyde}</td>'
    rf'<td style="{cell}">Jones&rsquo; Reagent<br><b>OR</b><br>Tollens&rsquo; Reagent</td>'
    rf'<td style="{cell}"><b>Carboxylic Acid</b><br>{acid}</td></tr>'
    # Row 2 - 1 alcohol
    rf'<tr><td style="{cell}"><b>1&deg; Alcohol</b><br>(R&ndash;CH<sub>2</sub>OH)<br>{alcohol}</td>'
    rf'<td style="{cell}">Jones&rsquo; Reagent</td>'
    rf'<td style="{cell}"><b>Carboxylic Acid</b><br>{acid}</td></tr>'
    # Row 3 - alkyl halide (Grignard carboxylation)
    rf'<tr><td style="{cell}"><b>Alkyl Halide</b><br>(R&ndash;Br)<br>{halide}</td>'
    rf'<td style="{cell}">1. Mg, ether &rarr;<br>2. CO<sub>2</sub> &rarr;<br>3. H<sub>3</sub>O<sup>+</sup></td>'
    rf'<td style="{cell}"><b>Carboxylic Acid</b><br>{acid}</td></tr>'
    r"</tbody></table><br>"
    r'<span style="font-size: 13px; color: #888;">Grignard route (R&ndash;Br) <b>adds one carbon</b> &mdash; '
    r"the new COOH carbon comes from CO<sub>2</sub>; the oxidations preserve the carbon count.</span></div>"
)

validate(front, back)

card = {"front": front, "back": back, "tags": ["orgo::reaction", "orgo::carboxylic-acids"]}
added, updated, errors = push_cards([card], DECK)
print(f"added={added} updated={updated} errors={errors}")
