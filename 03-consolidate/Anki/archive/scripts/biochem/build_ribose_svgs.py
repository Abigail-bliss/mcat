"""Render ribose vs deoxyribose furanose rings (C2 highlighted), store as media,
and build a verification montage for qlmanage."""
import re
from orgo_helpers import render_svg, store_media

STRUCTS = [
    # furanose rings; highlight the C2' position (and its OH for ribose)
    ("ribose-furanose",     "OCC1OC(O)C(O)C1O", [6, 7]),
    ("deoxyribose-furanose", "OCC1OC(O)CC1O",   [6]),
]

svgs = {}
for key, smi, hl in STRUCTS:
    svg = render_svg(smi, w=240, h=200, highlight_atoms=hl)
    svgs[key] = svg
    store_media(f"orgo-{key}.svg", svg)

captions = {"ribose-furanose": "ribose (2'-OH, red)",
            "deoxyribose-furanose": "deoxyribose (2'-H, red)"}
CW, CH = 250, 230
outer = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{CW*2}" height="{CH}" '
         f'viewBox="0 0 {CW*2} {CH}"><rect width="100%" height="100%" fill="white"/>']
for i, (key, _, _) in enumerate(STRUCTS):
    x, y = i * CW + 10, 10
    s = re.sub(r"<\?xml[^>]*\?>\s*", "", svgs[key])
    s = re.sub(r"<svg[^>]*>", f'<svg x="{x}" y="{y}" width="230" height="192" viewBox="0 0 240 200">', s, count=1)
    outer.append(s)
    outer.append(f'<text x="{x+115}" y="{y+212}" font-family="Arial" font-size="14" '
                 f'text-anchor="middle">{captions[key]}</text>')
outer.append('</svg>')
with open("verify_ribose.svg", "w") as f:
    f.write("".join(outer))
print("stored 2 media + verify_ribose.svg")
