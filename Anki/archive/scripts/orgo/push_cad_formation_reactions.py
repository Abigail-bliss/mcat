"""Push 9 carboxylic-acid-derivative formation-reaction cards (reaction schemes).

    uv run --python 3.13 --with rdkit --with requests push_cad_formation_reactions.py
"""

from orgo_helpers import assert_connected, render_and_store, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::reaction", "orgo::carboxylic-acid-derivatives"]
assert_connected()

def R(name, smiles, labels, mw=110):
    return render_and_store(name, smiles, dummy_labels=labels, w=200, h=150, max_width=mw, inline=True)

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

# ---- structures ----
acid    = R("cad-carboxylic-acid", "*C(=O)O", ["R"])
halide  = R("cad-acid-chloride", "*C(=O)Cl", ["R"])
anhyd   = R("cad-anhydride", "*C(=O)OC(=O)*", ["R", "R"])
ester   = R("cad-ester", "*C(=O)O*", ["R", "R'"])
esterMe = R("cad-ester-ome", "*C(=O)OC", ["R"])
amide   = R("cad-amide-nr2", "*C(=O)N(*)*", ["R", "R", "R"])

def arrow(label):
    return (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 6px;">'
            rf'<div style="font-size:12px; color:#4a90d9; white-space:nowrap;">{label}</div>'
            r'<div style="font-size:26px; line-height:1;">&rarr;</div></div>')

def plus():
    return r'<span style="font-size:20px; padding:0 4px; vertical-align:middle;">+</span>'

def txt(t):
    return rf'<span style="font-size:15px; vertical-align:middle;">{t}</span>'

def scheme(*parts):
    return (r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:10px 0;">'
            + "".join(parts) + r"</div>")

def card(title, front_q, body, scheme_html, foot):
    front = WRAP + rf"<b>{title}</b><br><br>{front_q}</div>"
    back = WRAP + rf"<b>{title}</b><br><br>{body}{scheme_html}" + (FOOT(foot) if foot else "") + r"</div>"
    return {"front": front, "back": back, "tags": TAGS}

cards = []

# 1 — Acid halides from carboxylic acids
cards.append(card(
    "Formation of Acid Halides",
    r"How are <span style='color:#4a90d9;'>acid halides</span> formed from carboxylic acids?",
    r"Carboxylic acids react with <b>chlorinating reagents</b> to form acid halides &mdash; the <b>most reactive</b> carboxylic acid derivative.",
    scheme(acid, arrow(r"POCl<sub>3</sub>, PCl<sub>3</sub>,<br>PCl<sub>5</sub>, or SOCl<sub>2</sub>"), halide),
    r"Acid halides are the <b>most reactive</b> carboxylic acid derivative &mdash; Cl is an excellent leaving group."))

# 2 — Acid anhydrides from carboxylic acids
cards.append(card(
    "Acid Anhydrides from Carboxylic Acids",
    r"How are <span style='color:#4a90d9;'>acid anhydrides</span> formed from carboxylic acids?",
    r"Two carboxylic acids undergo a <b>dehydration (condensation)</b> with heat, losing one H<sub>2</sub>O.",
    scheme(acid, plus(), acid, arrow(r"heat, &minus;H<sub>2</sub>O"), anhyd),
    r"Second most reactive derivative. The condensation loses <b>exactly one H<sub>2</sub>O</b>."))

# 3 — Acid anhydrides from acid halides
cards.append(card(
    "Acid Anhydrides from Acid Halides",
    r"How are <span style='color:#4a90d9;'>acid anhydrides</span> formed from acid halides?",
    r"An acid halide reacts with a <b>carboxylate</b> (deprotonated carboxylic acid) nucleophile.",
    scheme(halide, arrow(r"Na<sup>+</sup> <sup>&minus;</sup>OC(=O)R"), anhyd, plus(), txt("NaCl")),
    r"A <b>nucleophilic acyl substitution</b> &mdash; the carboxylate attacks the carbonyl carbon and Cl<sup>&minus;</sup> departs."))

# 4 — Fischer esterification
cards.append(card(
    "Fischer Esterification",
    r"How are <span style='color:#4a90d9;'>esters</span> formed from carboxylic acids (Fischer esterification)?",
    r"Carboxylic acids react with an <b>alcohol</b> under <b>acid catalysis</b> to form an ester + water.<br>"
    r'<table style="margin:6px auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:3px 10px;">1.</td><td style="padding:3px 10px;"><b>Acid catalyzed</b></td></tr>'
    r'<tr><td style="padding:3px 10px;">2.</td><td style="padding:3px 10px;"><b>Dehydration</b> &mdash; loses one H<sub>2</sub>O</td></tr>'
    r'<tr><td style="padding:3px 10px;">3.</td><td style="padding:3px 10px;"><b>Reversible</b> (the alcohol nucleophile is weak)</td></tr>'
    r"</tbody></table>",
    scheme(acid, arrow(r"H<sup>+</sup>, ROH, &minus;H<sub>2</sub>O"), esterMe),
    r"Because it is reversible, <b>excess alcohol</b> or <b>removing water</b> drives equilibrium toward ester (Le Ch&acirc;telier&rsquo;s principle)."))

# 5 — Esters from acid halides
cards.append(card(
    "Esters from Acid Halides",
    r"How are <span style='color:#4a90d9;'>esters</span> formed from acid halides?",
    r"An acid halide reacts with an <b>alcohol (ROH)</b> &mdash; the alcohol oxygen attacks the carbonyl carbon and Cl<sup>&minus;</sup> departs (nucleophilic acyl substitution).",
    scheme(halide, arrow(r"ROH"), ester, plus(), txt("HCl")),
    r"Acid halides are the most reactive derivative, so this needs <b>no acid catalysis</b> (unlike Fischer esterification)."))

# 6 — Esters from acid anhydrides
cards.append(card(
    "Esters from Acid Anhydrides",
    r"How are <span style='color:#4a90d9;'>esters</span> formed from acid anhydrides?",
    r"An acid anhydride reacts with an <b>alcohol (ROH)</b> to form an ester + a carboxylic acid byproduct.",
    scheme(anhyd, arrow(r"ROH"), ester, plus(), acid),
    r"One half of the anhydride becomes the ester; the other half leaves as a <b>carboxylic acid</b>. Esters are the third most reactive derivative."))

# 7 — Amides from acid halides
cards.append(card(
    "Amides from Acid Halides",
    r"How are <span style='color:#4a90d9;'>amides</span> formed from acid halides?",
    r"An acid halide reacts with an <b>amine (R<sub>2</sub>NH)</b> to form an amide + HCl.",
    scheme(halide, arrow(r"R<sub>2</sub>NH"), amide, plus(), txt("HCl")),
    r"Amides are the <b>least reactive</b> derivative &mdash; but acid halides form them easily since Cl<sup>&minus;</sup> is an excellent leaving group."))

# 8 — Amides from acid anhydrides
cards.append(card(
    "Amides from Acid Anhydrides",
    r"How are <span style='color:#4a90d9;'>amides</span> formed from acid anhydrides?",
    r"An acid anhydride reacts with an <b>amine (R<sub>2</sub>NH)</b> to form an amide + a carboxylic acid byproduct.",
    scheme(anhyd, arrow(r"R<sub>2</sub>NH"), amide, plus(), acid),
    r"One half of the anhydride becomes the amide; the other half leaves as a <b>carboxylic acid</b>."))

# 9 — Amides from esters
cards.append(card(
    "Amides from Esters",
    r"How are <span style='color:#4a90d9;'>amides</span> formed from esters?",
    r"An ester reacts with an <b>amine (R<sub>2</sub>NH)</b> under heat to form an amide + an alcohol (ROH).",
    scheme(ester, arrow(r"R<sub>2</sub>NH, heat"), amide, plus(), txt("ROH")),
    r"Heat is required because esters are relatively unreactive &mdash; OR is a <b>poor leaving group</b> vs. Cl<sup>&minus;</sup> or the carboxylate in anhydrides."))

# ---- validate & push ----
for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
