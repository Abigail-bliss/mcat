"""Push 2 cards: aldehyde->hemiacetal->acetal and ketone->hemiketal->ketal,
with formation schemes, recognition tables, and ring-form recognition.
Structures already stored as orgo-ak2-*.svg by build_acetal_svgs.py.

    uv run --python 3.13 --with requests push_acetal_cards.py
"""
from orgo_helpers import assert_connected, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::concept", "orgo::acetals-ketals"]
assert_connected()

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

def img(key, mw=115):
    return f'<img src="orgo-{key}.svg" style="max-width:{mw}px; vertical-align:middle;">'

def arrow(label):
    return (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 4px;">'
            rf'<div style="font-size:11px; color:#4a90d9; white-space:nowrap;">{label}</div>'
            r'<div style="font-size:24px; line-height:1;">&rarr;</div></div>')

def scheme(*parts):
    return (r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:10px 0;">'
            + "".join(parts) + r"</div>")

def ringcell(key, label):
    return (r'<div style="display:inline-block; vertical-align:top; text-align:center; margin:4px 10px;">'
            rf'{img(key, 130)}<div style="font-size:12px; color:#555;">{label}</div></div>')

cards = []

# ===== CARD A: Aldehyde -> Hemiacetal -> Acetal =====
front_a = (WRAP + r"<b>Aldehyde &rarr; Hemiacetal &rarr; Acetal</b><br><br>"
    r"How do you form a <span style='color:#4a90d9;'>hemiacetal</span> and an "
    r"<span style='color:#4a90d9;'>acetal</span> from an aldehyde, and how do you recognize each "
    r"(including in <span style='color:#4a90d9;'>rings</span>)?</div>")
back_a = (WRAP + r"<b>Aldehyde &rarr; Hemiacetal &rarr; Acetal</b><br><br>"
    + scheme(img("ak2-aldehyde", 80),
             arrow(r"1 R&prime;OH,<br>H<sup>+</sup>"), img("ak2-hemiacetal"),
             arrow(r"2nd R&prime;OH,<br>H<sup>+</sup>, &minus;H<sub>2</sub>O"), img("ak2-acetal"))
    + r'<span style="font-size:13px; color:#888;">Acid-catalyzed and reversible. Each step adds one alcohol.</span>'
    r'<table style="margin:10px auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px;"><b>Hemiacetal</b></td><td style="padding:4px 10px;">one <b>&ndash;OH</b> + one <b>&ndash;OR</b> on the same carbon (+ one H)</td></tr>'
    r'<tr><td style="padding:4px 10px;"><b>Acetal</b></td><td style="padding:4px 10px;"><b>two &ndash;OR</b> groups on the same carbon (+ one H)</td></tr>'
    r"</tbody></table>"
    r'<b style="color:#4a90d9;">Recognizing them in rings</b><br>'
    r'<div style="font-size:13px; color:#555; margin:4px 0;">Look at the <b>anomeric carbon</b> (red) &mdash; the ring carbon bonded to the <b>ring O</b>:</div>'
    r'<div style="margin:6px 0;">'
    + ringcell("ak2-ring-hemiacetal", "ring O + <b>OH</b><br>= cyclic <b>hemiacetal</b>")
    + ringcell("ak2-ring-acetal", "ring O + <b>OR</b><br>= cyclic <b>acetal</b>")
    + r"</div>"
    + FOOT(r"In a sugar: the free ring form is a <b>hemiacetal</b>; once it links to another group through O (glycosidic bond) it becomes an <b>acetal</b>.")
    + r"</div>")
cards.append({"front": front_a, "back": back_a, "tags": TAGS})

# ===== CARD B: Ketone -> Hemiketal -> Ketal =====
front_b = (WRAP + r"<b>Ketone &rarr; Hemiketal &rarr; Ketal</b><br><br>"
    r"How do you form a <span style='color:#4a90d9;'>hemiketal</span> and a "
    r"<span style='color:#4a90d9;'>ketal</span> from a ketone, and how do you recognize each "
    r"(including in <span style='color:#4a90d9;'>rings</span>)?</div>")
back_b = (WRAP + r"<b>Ketone &rarr; Hemiketal &rarr; Ketal</b><br><br>"
    + scheme(img("ak2-ketone", 90),
             arrow(r"1 R&prime;OH,<br>H<sup>+</sup>"), img("ak2-hemiketal"),
             arrow(r"2nd R&prime;OH,<br>H<sup>+</sup>, &minus;H<sub>2</sub>O"), img("ak2-ketal"))
    + r'<span style="font-size:13px; color:#888;">Same mechanism as acetal formation &mdash; acid-catalyzed and reversible.</span>'
    r'<table style="margin:10px auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px;"><b>Hemiketal</b></td><td style="padding:4px 10px;">one <b>&ndash;OH</b> + one <b>&ndash;OR</b> on the same carbon (+ <b>two C/R</b> groups, <b>no H</b>)</td></tr>'
    r'<tr><td style="padding:4px 10px;"><b>Ketal</b></td><td style="padding:4px 10px;"><b>two &ndash;OR</b> groups on the same carbon (+ <b>two C/R</b> groups, <b>no H</b>)</td></tr>'
    r"</tbody></table>"
    r'<b style="color:#4a90d9;">Recognizing them in rings</b><br>'
    r'<div style="font-size:13px; color:#555; margin:4px 0;">Same as acetals, but the anomeric carbon (red) also bears a <b>carbon</b> substituent (no H) &mdash; e.g. fructose:</div>'
    r'<div style="margin:6px 0;">'
    + ringcell("ak2-ring-hemiketal", "ring O + <b>OH</b> + C<br>= cyclic <b>hemiketal</b>")
    + ringcell("ak2-ring-ketal", "ring O + <b>OR</b> + C<br>= cyclic <b>ketal</b>")
    + r"</div>"
    + FOOT(r"Ketoses (e.g. <b>fructose</b>) cyclize to <b>hemiketals</b>; the key difference from acetals is the extra carbon on the anomeric center (no H).")
    + r"</div>")
cards.append({"front": front_b, "back": back_b, "tags": TAGS})

for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
