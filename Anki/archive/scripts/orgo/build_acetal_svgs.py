"""Render RDKit structures for the aldehyde/acetal and ketone/ketal cards,
store as Anki media, and build a verification montage (nested SVGs) for qlmanage."""
import re
from orgo_helpers import render_svg, store_media

# (key, smiles, dummy_labels, highlight_atoms)
STRUCTS = [
    ("ak2-aldehyde",     "*C=O",          ["R"],            None),
    ("ak2-hemiacetal",   "*C(O)O*",       ["R", "R'"],      None),
    ("ak2-acetal",       "*C(O*)O*",      ["R", "R'", "R'"], None),
    ("ak2-ring-hemiacetal", "OC1CCCCO1",  None,             [1]),
    ("ak2-ring-acetal",  "COC1CCCCO1",    None,             [2]),
    ("ak2-ketone",       "*C(=O)*",       ["R", "R"],       None),
    ("ak2-hemiketal",    "*C(O)(O*)*",    ["R", "R'", "R"], None),
    ("ak2-ketal",        "*C(O*)(O*)*",   ["R", "R'", "R'", "R"], None),
    ("ak2-ring-hemiketal", "CC1(O)CCCO1", None,             [1]),
    ("ak2-ring-ketal",   "COC1(C)CCCO1",  None,             [2]),
]

svgs = {}
for key, smi, labels, hl in STRUCTS:
    svg = render_svg(smi, w=240, h=190, dummy_labels=labels, highlight_atoms=hl)
    svgs[key] = svg
    store_media(f"orgo-{key}.svg", svg)  # also store to Anki media now (idempotent)

# montage: 5 columns x 2 rows, nested svgs
captions = {
    "ak2-aldehyde": "aldehyde R-CHO", "ak2-hemiacetal": "hemiacetal (OH+OR)",
    "ak2-acetal": "acetal (OR+OR)", "ak2-ring-hemiacetal": "ring hemiacetal",
    "ak2-ring-acetal": "ring acetal",
    "ak2-ketone": "ketone R-CO-R", "ak2-hemiketal": "hemiketal (OH+OR)",
    "ak2-ketal": "ketal (OR+OR)", "ak2-ring-hemiketal": "ring hemiketal",
    "ak2-ring-ketal": "ring ketal",
}
order = [s[0] for s in STRUCTS]
CW, CH = 215, 200
cols = 5
outer = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW*cols}" height="{CH*2}" '
         f'viewBox="0 0 {CW*cols} {CH*2}"><rect width="100%" height="100%" fill="white"/>']
for i, key in enumerate(order):
    col, row = i % cols, i // cols
    x, y = col * CW + 5, row * CH + 5
    # strip XML declaration, then rewrite the opening <svg ...> tag with x/y/size
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", svgs[key])
    s = re.sub(r"<svg[^>]*>",
               f'<svg x="{x}" y="{y}" width="200" height="158" viewBox="0 0 240 190">',
               s, count=1)
    outer.append(s)
    outer.append(f'<text x="{x+100}" y="{y+182}" font-family="Arial" font-size="13" '
                 f'text-anchor="middle">{captions[key]}</text>')
outer.append('</svg>')
with open("verify_acetal.svg", "w") as f:
    f.write("".join(outer))
print("stored", len(STRUCTS), "media + verify_acetal.svg")
