"""Push the Chair Conformations card, embedding the verified hand-built chair SVG.

    uv run --python 3.13 --with requests push_chair_card.py
"""
from orgo_helpers import assert_connected, store_media, validate, push_cards

DECK = "MCAT Organic Chemistry"
assert_connected()

with open("chair.svg") as f:
    chair_svg = f.read()
store_media("orgo-chair-conformation.svg", chair_svg)
chair_img = '<img src="orgo-chair-conformation.svg" style="max-width:320px; margin:8px auto; display:block;">'

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'

front = (WRAP + r"<b>Chair Conformations</b><br><br>"
    r"What are the key rules for <span style='color:#4a90d9;'>chair conformations</span> of cyclohexane?</div>")

back = (WRAP + r"<b>Chair Conformations</b><br><br>"
    + chair_img +
    r'<div style="font-size:12px; color:#888; margin-bottom:8px;">'
    r'<span style="color:#c00;"><b>ax</b> = axial</span> &nbsp;&middot;&nbsp; <span style="color:#06c;"><b>eq</b> = equatorial</span></div>'
    r'<table style="margin:auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:5px 10px; vertical-align:top;"><b>Why chairs exist</b></td>'
    r'<td style="padding:5px 10px;">Ring carbons are <b>sp&sup3;</b> (tetrahedral, 109.5&deg;). A flat hexagon would force 120&deg; angles &rarr; strain. Benzene is flat because its carbons are <b>sp&sup2;</b>.</td></tr>'
    r'<tr><td style="padding:5px 10px; vertical-align:top;"><b>Axial vs equatorial</b></td>'
    r'<td style="padding:5px 10px;">Each carbon has one <b>axial</b> (straight up/down, &perp; to ring, alternating) and one <b>equatorial</b> (outward, ~in plane). Larger substituents prefer <b>equatorial</b> to avoid <b>1,3-diaxial strain</b>.</td></tr>'
    r'<tr><td style="padding:5px 10px; vertical-align:top;"><b>Cis vs trans</b></td>'
    r'<td style="padding:5px 10px;">Groups point up (wedge) or down (dash). <b>Cis</b> = same side, <b>trans</b> = opposite. On <b>neighboring</b> carbons, cis groups occupy <b>one axial + one equatorial</b> (never both equatorial).</td></tr>'
    r"</tbody></table><br>"
    r'<span style="font-size: 13px; color: #888;">MCAT tip: when the ring <b>flips</b>, all axial groups become equatorial and vice versa &mdash; the preferred conformation has the <b>largest group equatorial</b>.</span>'
    r"</div>")

validate(front, back)
card = {"front": front, "back": back, "tags": ["orgo::concept", "orgo::conformations"]}
added, updated, errors = push_cards([card], DECK)
print(f"added={added} updated={updated} errors={errors}")
