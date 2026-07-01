"""Push 5 cards on carboxylic acid derivatives, with RDKit skeletal diagrams.

    uv run --python 3.13 --with rdkit --with requests push_carboxylic_acid_derivatives.py
"""

from orgo_helpers import assert_connected, render_and_store, validate, push_cards

DECK = "MCAT Organic Chemistry"
SUB = "orgo::carboxylic-acid-derivatives"
assert_connected()

def R(name, smiles, labels, w=200, h=150, mw=110):
    return render_and_store(name, smiles, dummy_labels=labels, w=w, h=h, max_width=mw, inline=True)

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

# ---- shared derivative structures ----
acid_chloride = R("cad-acid-chloride", "*C(=O)Cl", ["R"])
anhydride     = R("cad-anhydride", "*C(=O)OC(=O)*", ["R", "R'"])
ester         = R("cad-ester", "*C(=O)O*", ["R", "R'"])
amide         = R("cad-amide", "*C(=O)N", ["R"])

cards = []

# ============ CARD 1: Nomenclature ============
hc = "padding: 6px 12px; border-bottom: 2px solid #ccc;"
c = "padding: 8px 12px; border-bottom: 1px solid #eee; vertical-align: middle;"
front1 = (WRAP + r"<b>Carboxylic Acid Derivatives: Nomenclature</b><br><br>"
    r"What are the <span style='color: #4a90d9;'>four carboxylic acid derivatives</span> and their "
    r"<span style='color: #4a90d9;'>naming suffixes</span>?</div>")
back1 = (WRAP + r"<b>Carboxylic Acid Derivatives: Nomenclature</b><br><br>"
    r'<table style="margin: auto; text-align: center; font-size: 14px; border-collapse: collapse;"><tbody>'
    rf'<tr><td style="{hc}"><b>Derivative</b></td><td style="{hc}"><b>Structure</b></td><td style="{hc}"><b>Suffix</b></td></tr>'
    rf'<tr><td style="{c}"><b>Acid Chloride</b></td><td style="{c}">{acid_chloride}</td><td style="{c}">-oyl chloride</td></tr>'
    rf'<tr><td style="{c}"><b>Acid Anhydride</b></td><td style="{c}">{anhydride}</td><td style="{c}">-anhydride</td></tr>'
    rf'<tr><td style="{c}"><b>Ester</b></td><td style="{c}">{ester}</td><td style="{c}">-ate</td></tr>'
    rf'<tr><td style="{c}"><b>Amide</b></td><td style="{c}">{amide}</td><td style="{c}">-amide</td></tr>'
    r"</tbody></table><br>"
    + FOOT(r"Amides have both H-bond <b>donors and acceptors</b>. All other carboxylic acid derivatives only experience <b>dipole-dipole</b> interactions.")
    + r"</div>")
cards.append({"front": front1, "back": back1, "tags": ["orgo::nomenclature", SUB]})

# ============ CARD 2: Amide Resonance ============
am1 = R("cad-amide-res1", "*C(=O)N", ["R"], mw=120)
am2 = R("cad-amide-res2", "*[C+]([O-])N", ["R"], mw=120)
am3 = R("cad-amide-res3", "*C([O-])=[NH2+]", ["R"], mw=120)
arrow = r'<span style="font-size:22px; padding:0 4px; vertical-align:middle;">&harr;</span>'
front2 = (WRAP + r"<b>Resonance Structure of Amides</b><br><br>"
    r"What is the <span style='color: #4a90d9;'>hybridization of the nitrogen</span> in an amide, and why?</div>")
back2 = (WRAP + r"<b>Resonance Structure of Amides</b><br><br>"
    r"The amide nitrogen is <b>sp&sup2;</b> (not sp&sup3;).<br><br>"
    r"<b>Resonance</b> delocalizes the nitrogen lone pair into the carbonyl, giving the "
    r"<b>C&ndash;N bond partial double-bond character</b> &mdash; so N must be sp&sup2;. This also makes amides "
    r"<b>especially stable</b>.<br>"
    rf'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:10px 0;">{am1}{arrow}{am2}{arrow}{am3}</div>'
    + FOOT(r"MCAT trap &mdash; the amide nitrogen <i>looks</i> sp&sup3; but is <b>sp&sup2;</b> due to resonance.")
    + r"</div>")
cards.append({"front": front2, "back": back2, "tags": ["orgo::concept", SUB]})

# ============ CARD 3: Lactones & Lactams ============
lactone = R("cad-lactone", "O=C1CCCO1", None, mw=140)
lactam  = R("cad-lactam", "O=C1CCCN1", None, mw=140)
front3 = (WRAP + r"<b>Cyclic Acid Derivatives: Lactones &amp; Lactams</b><br><br>"
    r"What are <span style='color: #4a90d9;'>cyclic esters</span> and <span style='color: #4a90d9;'>cyclic amides</span> called?</div>")
back3 = (WRAP + r"<b>Cyclic Acid Derivatives: Lactones &amp; Lactams</b><br><br>"
    r'<div style="display:inline-block; vertical-align:top; margin:6px 16px;">'
    rf'{lactone}<div style="font-size:14px; color:#555;"><b>Lactone</b><br>(cyclic ester)</div></div>'
    r'<div style="display:inline-block; vertical-align:top; margin:6px 16px;">'
    rf'{lactam}<div style="font-size:14px; color:#555;"><b>Lactam</b><br>(cyclic amide)</div></div>'
    r"</div>")
cards.append({"front": front3, "back": back3, "tags": ["orgo::nomenclature", SUB]})

# ============ CARD 4: General Reactivity ============
rxn_arrow = r'<span style="font-size:22px; padding:0 2px; vertical-align:middle;">&rarr;</span>'
def col(img, label):
    return (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 2px;">'
            rf'{img}<div style="font-size:13px; color:#555;"><b>{label}</b></div></div>')
front4 = (WRAP + r"<b>Reactivity of Carboxylic Acid Derivatives</b><br><br>"
    r"What <span style='color: #4a90d9;'>determines the reactivity</span> of carboxylic acid derivatives, and what is the <span style='color: #4a90d9;'>order</span>?</div>")
fac = "padding: 4px 10px;"
back4 = (WRAP + r"<b>Reactivity of Carboxylic Acid Derivatives</b><br><br>"
    r"All are <b>electrophilic at the carbonyl carbon</b>. Reactivity is set by <b>leaving-group ability</b>.<br>"
    r'<div style="font-size:13px; color:#888; margin-top:8px;">most reactive &rarr; least reactive</div>'
    r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; margin:6px 0;">'
    + col(acid_chloride, "Acid halide") + rxn_arrow + col(anhydride, "Anhydride") + rxn_arrow
    + col(ester, "Ester") + rxn_arrow + col(amide, "Amide") + r"</div><br>"
    r'<table style="margin: auto; text-align: left; font-size: 14px;"><tbody>'
    rf'<tr><td style="{fac}"><b>Steric</b></td><td style="{fac}">smaller leaving groups depart faster</td></tr>'
    rf'<tr><td style="{fac}"><b>Electronic</b></td><td style="{fac}">larger bond dipoles increase reactivity</td></tr>'
    rf'<tr><td style="{fac}"><b>Ring strain</b></td><td style="{fac}">lactones &amp; lactams react faster than linear analogues</td></tr>'
    r"</tbody></table></div>")
cards.append({"front": front4, "back": back4, "tags": ["orgo::concept", SUB]})

# ============ CARD 5: General Mechanism ============
m_start = R("cad-mech-start", "*C(=O)*", ["R", "LG"], mw=120)
m_tet   = R("cad-mech-tetrahedral", "*C([O-])(*)*", ["R", "LG", "Nu"], mw=120)
m_prod  = R("cad-mech-product", "*C(=O)*", ["R", "Nu"], mw=120)
front5 = (WRAP + r"<b>General Mechanism at the Carbonyl</b><br><br>"
    r"What are the <span style='color: #4a90d9;'>three steps</span> of <span style='color: #4a90d9;'>nucleophilic acyl substitution</span> at a carbonyl?</div>")
ms = "padding: 4px 10px;"
back5 = (WRAP + r"<b>General Mechanism at the Carbonyl</b><br><br>"
    r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; margin:6px 0;">'
    + col(m_start, "carbonyl + LG") + rxn_arrow + col(m_tet, "tetrahedral<br>intermediate")
    + rxn_arrow + col(m_prod, "product") + r"</div><br>"
    r'<table style="margin: auto; text-align: left; font-size: 14px;"><tbody>'
    rf'<tr><td style="{ms}">1.</td><td style="{ms}"><b>Nucleophile attacks</b> the electrophilic carbonyl carbon</td></tr>'
    rf'<tr><td style="{ms}">2.</td><td style="{ms}">A <b>tetrahedral intermediate</b> forms (O&minus; and LG still attached)</td></tr>'
    rf'<tr><td style="{ms}">3.</td><td style="{ms}">The <b>leaving group departs</b>, reforming the carbonyl</td></tr>'
    r"</tbody></table><br>"
    + FOOT(r"The carbonyl carbon is electrophilic due to the <b>C=O bond dipole</b> &mdash; LG = X, OC(O)R, OR, or NR<sub>2</sub>.")
    + r"</div>")
cards.append({"front": front5, "back": back5, "tags": ["orgo::concept", SUB]})

# ---- validate & push ----
for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
