"""Push one card: ribose vs deoxyribose. Structures stored by build_ribose_svgs.py.

    uv run --python 3.13 --with requests push_ribose_card.py
"""
from orgo_helpers import assert_connected, validate, push_cards

DECK = "MCAT Organic Chemistry"
assert_connected()

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'

def cell(key, label):
    return (r'<div style="display:inline-block; vertical-align:top; text-align:center; margin:4px 10px;">'
            rf'<img src="orgo-{key}.svg" style="max-width:150px; vertical-align:middle;">'
            rf'<div style="font-size:13px; color:#555;">{label}</div></div>')

front = (WRAP + r"<b>Ribose vs Deoxyribose</b><br><br>"
    r"What are <span style='color:#4a90d9;'>ribose</span> and <span style='color:#4a90d9;'>deoxyribose</span>, "
    r"and how do they differ?</div>")

back = (WRAP + r"<b>Ribose vs Deoxyribose</b><br><br>"
    r"Both are <b>5-carbon sugars</b> (pentose monosaccharides).<br>"
    r'<div style="margin:8px 0;">'
    + cell("ribose-furanose", "<b>ribose</b> &mdash; 2&prime;-OH")
    + cell("deoxyribose-furanose", "<b>deoxyribose</b> &mdash; 2&prime;-H")
    + r"</div>"
    r'<table style="margin:auto; text-align:left; font-size:14px; border-collapse:collapse;"><tbody>'
    r'<tr style="border-bottom:2px solid #ccc;"><td style="padding:5px 12px;"></td>'
    r'<td style="padding:5px 12px;"><b>Ribose</b></td><td style="padding:5px 12px;"><b>Deoxyribose</b></td></tr>'
    r'<tr><td style="padding:5px 12px;"><b>What</b></td><td style="padding:5px 12px;">a monosaccharide</td>'
    r'<td style="padding:5px 12px;">a relative of ribose (2-deoxyribose)</td></tr>'
    r'<tr><td style="padding:5px 12px;"><b>Found in</b></td><td style="padding:5px 12px;"><b>RNA</b></td>'
    r'<td style="padding:5px 12px;"><b>DNA</b></td></tr>'
    r'<tr><td style="padding:5px 12px;"><b>C2 position</b></td><td style="padding:5px 12px;">&ndash;<b>OH</b> (2&prime;-OH)</td>'
    r'<td style="padding:5px 12px;">&ndash;<b>H</b> (no 2&prime;-OH)</td></tr>'
    r"</tbody></table><br>"
    r'<span style="font-size: 13px; color: #888;">The <b>only</b> difference is at <b>C2</b>: <b>&ldquo;deoxy&rdquo; = ribose minus one oxygen</b> '
    r"(H instead of OH at C2). RNA &rarr; ribose; DNA &rarr; deoxyribose.</span>"
    r"</div>")

validate(front, back)
card = {"front": front, "back": back, "tags": ["orgo::concept", "orgo::carbohydrates"]}
added, updated, errors = push_cards([card], DECK)
print(f"added={added} updated={updated} errors={errors}")
