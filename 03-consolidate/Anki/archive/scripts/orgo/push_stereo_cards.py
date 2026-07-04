"""Push 3 comprehensive stereochemistry cards (enantiomers, diastereomers, epimers)
with verified hand-built Fischer-projection SVGs.

    uv run --python 3.13 --with requests push_stereo_cards.py
"""
from orgo_helpers import assert_connected, store_media, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::concept", "orgo::stereochemistry"]
assert_connected()

def media(name, mw=115):
    with open(f"{name}.svg") as f:
        store_media(f"orgo-{name}.svg", f.read())
    return f'<img src="orgo-{name}.svg" style="max-width:{mw}px; vertical-align:middle;">'

rr     = media("stereo-rr")
ll     = media("stereo-ll")
lr     = media("stereo-lr")
rr_hl  = media("stereo-rr-hl")
lr_hl  = media("stereo-lr-hl")

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

def pair(a, b, sym, lblA, lblB):
    def cell(img, lbl):
        return (r'<div style="display:inline-block; vertical-align:middle; text-align:center; margin:0 4px;">'
                rf'{img}<div style="font-size:12px; color:#555;">{lbl}</div></div>')
    return (r'<div style="display:flex; align-items:center; justify-content:center; flex-wrap:wrap; margin:8px 0;">'
            + cell(a, lblA)
            + rf'<span style="font-size:22px; padding:0 4px; vertical-align:middle;">{sym}</span>'
            + cell(b, lblB) + r"</div>")

cards = []

# ============ CARD 1: ENANTIOMERS ============
front1 = (WRAP + r"<b>Enantiomers</b><br><br>"
    r"What are <span style='color:#4a90d9;'>enantiomers</span> &mdash; definition, properties, and requirements?</div>")
back1 = (WRAP + r"<b>Enantiomers</b><br><br>"
    r"<b>Non-superimposable mirror images.</b> They differ in configuration at <b>every</b> chiral center.<br>"
    + pair(rr, ll, "&harr;", "one enantiomer", "mirror image")
    + r'<div style="font-size:12px; color:#888; margin-bottom:6px;">mirror image &mdash; both stereocenters inverted</div>'
    r'<table style="margin:auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Requirement</b></td><td style="padding:4px 10px;">Molecule must be <b>chiral</b> (no internal plane of symmetry)</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Same</b></td><td style="padding:4px 10px;"><b>Identical</b> physical properties (mp, bp, density, solubility) and identical reactions with <b>achiral</b> reagents</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Different</b></td><td style="padding:4px 10px;">(1) rotate plane-polarized light <b>equally but oppositely</b> (+ / &minus;); (2) interact differently with <b>other chiral</b> things (enzymes, receptors)</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>1:1 mix</b></td><td style="padding:4px 10px;"><b>Racemic mixture</b> &mdash; optically inactive (rotations cancel)</td></tr>'
    r"</tbody></table><br>"
    + FOOT(r"Differ at <b>ALL</b> stereocenters = enantiomers. Differ at <b>SOME</b> = diastereomers.")
    + r"</div>")
cards.append({"front": front1, "back": back1, "tags": TAGS})

# ============ CARD 2: DIASTEREOMERS ============
front2 = (WRAP + r"<b>Diastereomers</b><br><br>"
    r"What are <span style='color:#4a90d9;'>diastereomers</span>, and how do they differ from enantiomers?</div>")
back2 = (WRAP + r"<b>Diastereomers</b><br><br>"
    r"Stereoisomers that are <b>NOT mirror images</b> &mdash; they differ at <b>some but not all</b> stereocenters (requires &ge; 2).<br>"
    + pair(rr, lr, "vs", "differ at C2 only", "(not a mirror image)")
    + r'<table style="margin:auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Properties</b></td><td style="padding:4px 10px;"><b>Different</b> physical properties (mp, bp, solubility, optical rotation all differ)</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Separation</b></td><td style="padding:4px 10px;">Separable by <b>ordinary means</b> (distillation, crystallization, chromatography)</td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Includes</b></td><td style="padding:4px 10px;"><b>cis/trans</b> (geometric) isomers, <b>epimers</b>, and <b>anomers</b></td></tr>'
    r"</tbody></table><br>"
    + FOOT(r"Mirror images = enantiomers; non-mirror-image stereoisomers = diastereomers.")
    + r"</div>")
cards.append({"front": front2, "back": back2, "tags": TAGS})

# ============ CARD 3: EPIMERS ============
front3 = (WRAP + r"<b>Epimers</b><br><br>"
    r"What are <span style='color:#4a90d9;'>epimers</span> (and anomers)?</div>")
back3 = (WRAP + r"<b>Epimers</b><br><br>"
    r"Diastereomers that differ at <b>exactly one</b> stereocenter &mdash; a <b>subset of diastereomers</b>.<br>"
    + pair(rr_hl, lr_hl, "vs", "differ at C2 only", "(one center)")
    + r'<table style="margin:auto; text-align:left; font-size:14px;"><tbody>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Examples</b></td><td style="padding:4px 10px;">D-glucose &amp; D-galactose = <b>C4 epimers</b>; D-glucose &amp; D-mannose = <b>C2 epimers</b></td></tr>'
    r'<tr><td style="padding:4px 10px; vertical-align:top;"><b>Anomers</b></td><td style="padding:4px 10px;">Special epimers that differ at the new <b>anomeric carbon</b> formed on ring closure (&alpha; vs &beta;)</td></tr>'
    r"</tbody></table><br>"
    + FOOT(r"All epimers are diastereomers; not all diastereomers are epimers (epimers differ at <b>exactly one</b> center).")
    + r"</div>")
cards.append({"front": front3, "back": back3, "tags": TAGS})

for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
