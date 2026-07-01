"""Push one card on the Gabriel synthesis (1-deg amine from alkyl halide).

    uv run --python 3.13 --with rdkit --with requests push_gabriel_synthesis.py
"""

from orgo_helpers import assert_connected, render_and_store, validate, push_cards

DECK = "MCAT Organic Chemistry"
assert_connected()

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'

phthalimide = render_and_store("gabriel-phthalimide", "O=C1c2ccccc2C(=O)N1",
                               w=220, h=170, max_width=130, inline=True)
amine = render_and_store("gabriel-primary-amine", "*N", dummy_labels=["R"],
                         w=200, h=150, max_width=110, inline=True)

arrow = (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 6px;">'
         r'<div style="font-size:12px; color:#4a90d9; white-space:nowrap;">R&ndash;X, then<br>hydrolysis</div>'
         r'<div style="font-size:26px; line-height:1;">&rarr;</div></div>')

front = (WRAP + r"<b>Gabriel Synthesis</b><br><br>"
    r"What does the <span style='color:#4a90d9;'>Gabriel synthesis</span> make, and what is the "
    r"<span style='color:#4a90d9;'>starting material</span>?</div>")

back = (WRAP + r"<b>Gabriel Synthesis</b><br><br>"
    r"Converts a <b>1&deg; alkyl halide</b> into a <b>1&deg; amine</b>.<br><br>"
    r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:6px 0;">'
    + phthalimide + arrow + amine + r"</div>"
    r'<table style="margin:8px auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Start</b></td>'
    r'<td style="padding:4px 10px;">Potassium phthalimide (a <b>masked amine nucleophile</b>) + 1&deg; alkyl halide</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Result</b></td>'
    r'<td style="padding:4px 10px;">A clean <b>primary amine</b>, released by hydrolysis / hydrazine</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Why</b></td>'
    r'<td style="padding:4px 10px;">Makes <b>only 1&deg; amines</b> &mdash; avoids the <b>over-alkylation</b> seen when ammonia reacts directly with R&ndash;X</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>How</b></td>'
    r'<td style="padding:4px 10px;">The phthalimide <b>N&ndash;H is acidic</b> &rarr; deprotonate, and the nitrogen anion does <b>S<sub>N</sub>2</b> on R&ndash;X</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Scope</b></td>'
    r'<td style="padding:4px 10px;">S<sub>N</sub>2 &rarr; needs <b>1&deg;</b> (or unhindered 2&deg;) halides; fails on <b>3&deg;</b> (elimination) and <b>aryl/vinyl</b> halides</td></tr>'
    r"</tbody></table><br>"
    r'<span style="font-size: 13px; color: #888;">Think of phthalimide as <b>&ldquo;protected ammonia&rdquo;</b> &mdash; it delivers exactly one alkyl group, so you get a pure primary amine.</span>'
    r"</div>")

validate(front, back)
card = {"front": front, "back": back, "tags": ["orgo::reaction", "orgo::amines"]}
added, updated, errors = push_cards([card], DECK)
print(f"added={added} updated={updated} errors={errors}")
