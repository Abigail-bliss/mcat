"""Push 2 amino-acid cards with hand-built Fischer-projection SVGs.

Fischer projections use a fixed cross convention (horizontal = toward viewer,
vertical = away), which RDKit does not draw -- so these SVGs are built by hand.

    uv run --python 3.13 --with rdkit --with requests push_amino_acid_cards.py
"""

from orgo_helpers import assert_connected, store_media, slugify, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::concept", "orgo::amino-acids"]
assert_connected()

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'


def fischer(name, top, bottom, left, right, mw=120):
    """Build a Fischer-cross SVG, store as media, return an inline <img> snippet."""
    w, h = 185, 185
    cx, cy = 92, 92
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
        f'<line x1="{cx}" y1="42" x2="{cx}" y2="142" stroke="black" stroke-width="2"/>'
        f'<line x1="50" y1="{cy}" x2="134" y2="{cy}" stroke="black" stroke-width="2"/>'
        f'<text x="{cx}" y="34" font-family="Arial" font-size="15" text-anchor="middle">{top}</text>'
        f'<text x="{cx}" y="164" font-family="Arial" font-size="15" text-anchor="middle">{bottom}</text>'
        f'<text x="45" y="{cy+5}" font-family="Arial" font-size="15" text-anchor="end">{left}</text>'
        f'<text x="139" y="{cy+5}" font-family="Arial" font-size="15" text-anchor="start">{right}</text>'
        f'</svg>'
    )
    fname = f"aa-fischer-{slugify(name)}.svg"
    store_media(fname, svg)
    return f'<img src="{fname}" style="max-width:{mw}px; vertical-align:middle;">'


def labeled(img, label):
    return (r'<div style="display:inline-block; vertical-align:top; text-align:center; margin:4px 8px;">'
            rf'{img}<div style="font-size:13px; color:#555;">{label}</div></div>')


cards = []

# ============ CARD 1: Stereochemistry ============
L = fischer("l-amino-acid", "COOH", "R", "H&#8322;N", "H")
D = fischer("d-amino-acid", "COOH", "R", "H", "NH&#8322;")

front1 = (WRAP + r"<b>Stereochemistry of Amino Acids</b><br><br>"
    r"What are the key <span style='color:#4a90d9;'>stereochemistry rules</span> for amino acids?</div>")
back1 = (WRAP + r"<b>Stereochemistry of Amino Acids</b><br><br>"
    r"The alpha-carbon bears four groups: <b>NH<sub>2</sub>, COOH, H, and R</b>.<br>"
    r'<table style="margin:8px auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:3px 8px; vertical-align:top;">1.</td><td style="padding:3px 8px;">The alpha-carbon is <b>chiral for all amino acids except glycine</b> (R = H &rarr; two identical groups)</td></tr>'
    r'<tr><td style="padding:3px 8px; vertical-align:top;">2.</td><td style="padding:3px 8px;">All chiral amino acids in the body are <b>S</b> &mdash; <b>except cysteine</b>, which is R</td></tr>'
    r'<tr><td style="padding:3px 8px; vertical-align:top;">3.</td><td style="padding:3px 8px;">Classified <b>D or L</b> by Fischer-projection orientation</td></tr>'
    r'<tr><td style="padding:3px 8px; vertical-align:top;">4.</td><td style="padding:3px 8px;">Amino acids in the body are <b>L-amino acids</b></td></tr>'
    r'<tr><td style="padding:3px 8px; vertical-align:top;">5.</td><td style="padding:3px 8px;"><b>D/L do NOT correlate with R/S</b></td></tr>'
    r"</tbody></table>"
    r'<div style="margin:8px 0;">' + labeled(L, "<b>L</b>-amino acid") + labeled(D, "<b>D</b>-amino acid") + r"</div>"
    + FOOT(r"Fischer convention: <b>horizontal lines come forward</b> (toward you), <b>vertical lines go back</b> (away). Heavily tested on the MCAT.")
    + r"</div>")
cards.append({"front": front1, "back": back1, "tags": TAGS})

# ============ CARD 2: Charge States ============
acidic  = fischer("aa-acidic", "COOH", "R", "&#8314;H&#8323;N", "H")
neutral = fischer("aa-neutral", "COO&#8315;", "R", "&#8314;H&#8323;N", "H")
basic   = fischer("aa-basic", "COO&#8315;", "R", "H&#8322;N", "H")
rxn_arrow = r'<span style="font-size:24px; padding:0 2px; vertical-align:middle;">&rarr;</span>'

hc = "padding: 6px 12px; border-bottom: 2px solid #ccc;"
c = "padding: 6px 12px; border-bottom: 1px solid #eee;"
front2 = (WRAP + r"<b>Amino Acid Charge States</b><br><br>"
    r"What are the <span style='color:#4a90d9;'>three charge states</span> of an amino acid, and what "
    r"<span style='color:#4a90d9;'>pH conditions</span> produce each?</div>")
back2 = (WRAP + r"<b>Amino Acid Charge States</b><br><br>"
    r'<table style="margin:auto; text-align:left; font-size:13px; border-collapse:collapse;"><tbody>'
    rf'<tr><td style="{hc}"><b>pH</b></td><td style="{hc}"><b>COOH</b></td><td style="{hc}"><b>NH<sub>2</sub></b></td><td style="{hc}"><b>Net</b></td></tr>'
    rf'<tr><td style="{c}"><b>Low</b> (acidic)</td><td style="{c}">COOH</td><td style="{c}">NH<sub>3</sub><sup>+</sup></td><td style="{c}"><b>+</b> positive</td></tr>'
    rf'<tr><td style="{c}"><b>Physiological</b></td><td style="{c}">COO<sup>&minus;</sup></td><td style="{c}">NH<sub>3</sub><sup>+</sup></td><td style="{c}"><b>0</b> zwitterion</td></tr>'
    rf'<tr><td style="{c}"><b>High</b> (basic)</td><td style="{c}">COO<sup>&minus;</sup></td><td style="{c}">NH<sub>2</sub></td><td style="{c}"><b>&minus;</b> negative</td></tr>'
    r"</tbody></table><br>"
    r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:2px; margin:6px 0;">'
    + labeled(acidic, "acidic pH") + rxn_arrow + labeled(neutral, "neutral pH<br>(zwitterion)") + rxn_arrow + labeled(basic, "basic pH")
    + r"</div>"
    r'<div style="font-size:12px; color:#888;">increasing pH &rarr;</div><br>'
    + FOOT(r"At physiological pH amino acids exist as <b>zwitterions</b> &mdash; both a + and &minus; charge at once, but <b>net neutral</b>.")
    + r"</div>")
cards.append({"front": front2, "back": back2, "tags": TAGS})

for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
