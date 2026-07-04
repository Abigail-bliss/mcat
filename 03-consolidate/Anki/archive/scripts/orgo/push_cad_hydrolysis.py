"""Push 3 cards: hydrolysis of acid halides/anhydrides, esters/amides, and transesterification.

    uv run --python 3.13 --with rdkit --with requests push_cad_hydrolysis.py
"""

from orgo_helpers import assert_connected, render_and_store, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::reaction", "orgo::carboxylic-acid-derivatives"]
assert_connected()

def R(name, smiles, labels, mw=115):
    return render_and_store(name, smiles, dummy_labels=labels, w=200, h=150, max_width=mw, inline=True)

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

acyl_lg = R("cad-acyl-lg", "*C(=O)*", ["R", "LG"])
acid    = R("cad-carboxylic-acid", "*C(=O)O", ["R"])
ester   = R("cad-ester", "*C(=O)O*", ["R", "R'"])

def arrow(label):
    return (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 6px;">'
            rf'<div style="font-size:12px; color:#4a90d9; white-space:nowrap;">{label}</div>'
            r'<div style="font-size:26px; line-height:1;">&rarr;</div></div>')

def plus():
    return r'<span style="font-size:20px; padding:0 4px; vertical-align:middle;">+</span>'

def heat(color):
    return rf'<span style="font-size:15px; color:{color}; vertical-align:middle;"><b>heat</b></span>'

def txt(t):
    return rf'<span style="font-size:15px; vertical-align:middle;">{t}</span>'

def scheme(*parts):
    return (r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:10px 0;">'
            + "".join(parts) + r"</div>")

cards = []

# 1 — Hydrolysis of acid halides & anhydrides (exothermic)
cards.append({
    "front": WRAP + r"<b>Hydrolysis of Acid Halides &amp; Anhydrides</b><br><br>"
        r"What happens when <span style='color:#4a90d9;'>acid halides or anhydrides</span> are hydrolyzed?</div>",
    "back": WRAP + r"<b>Hydrolysis of Acid Halides &amp; Anhydrides</b><br><br>"
        r"They react with <b>water</b> to form <b>carboxylic acids</b>. Because they are highly reactive, the reaction is "
        r"<b>exothermic</b> &mdash; it releases heat.<br>"
        r'<span style="font-size:13px; color:#888;">(LG = X or OC(=O)R)</span>'
        + scheme(acyl_lg, arrow(r"H<sub>2</sub>O"), acid, plus(), heat("#c00"))
        + FOOT(r"The more reactive the derivative, the more energy released &mdash; acid halides and anhydrides hydrolyze <b>spontaneously</b>.")
        + r"</div>",
    "tags": TAGS})

# 2 — Hydrolysis of esters & amides (endothermic)
cards.append({
    "front": WRAP + r"<b>Hydrolysis of Esters &amp; Amides</b><br><br>"
        r"What happens when <span style='color:#4a90d9;'>esters or amides</span> are hydrolyzed?</div>",
    "back": WRAP + r"<b>Hydrolysis of Esters &amp; Amides</b><br><br>"
        r"They react with <b>water</b> to form <b>carboxylic acids</b>. Because they are less reactive, the reaction "
        r"<b>requires heat input</b> &mdash; it is <b>endothermic</b>.<br>"
        r'<span style="font-size:13px; color:#888;">(LG = OR or NR<sub>2</sub>)</span>'
        + scheme(acyl_lg, plus(), heat("#c00"), arrow(r"H<sub>2</sub>O"), acid)
        + FOOT(r"Contrast with acid halides and anhydrides &mdash; those hydrolyze spontaneously and release heat. Esters and amides <b>need heat</b> to react.")
        + r"</div>",
    "tags": TAGS})

# 3 — Transesterification
cards.append({
    "front": WRAP + r"<b>Transesterification</b><br><br>"
        r"What is <span style='color:#4a90d9;'>transesterification</span> and how does it work?</div>",
    "back": WRAP + r"<b>Transesterification</b><br><br>"
        r"Converts <b>one ester into another</b> using an <b>alcohol (ROH)</b> nucleophile under acid catalysis.<br>"
        r'<table style="margin:6px auto; text-align:left; font-size:14px;"><tbody>'
        r'<tr><td style="padding:3px 10px;">1.</td><td style="padding:3px 10px;"><b>Acid catalyzed</b></td></tr>'
        r'<tr><td style="padding:3px 10px;">2.</td><td style="padding:3px 10px;"><b>Reversible</b> (weak alcohol nucleophile)</td></tr>'
        r'<tr><td style="padding:3px 10px;">3.</td><td style="padding:3px 10px;">Mechanistically <b>identical to Fischer esterification</b>, but the nucleophile is an alcohol instead of water</td></tr>'
        r"</tbody></table>"
        + scheme(ester, arrow(r"ROH, H<sup>+</sup>"), ester, plus(), txt("ROH"))
        + FOOT(r"To push toward product, add the reactant alcohol in <b>excess</b> &mdash; Le Ch&acirc;telier&rsquo;s principle drives the equilibrium forward.")
        + r"</div>",
    "tags": TAGS})

for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
