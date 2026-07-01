"""Build 2-stereocenter Fischer-projection SVGs for the stereochemistry cards,
plus a verification montage rendered to PNG via qlmanage (run separately)."""

CX = 75
SPACING = 46
BB_TOP = 26


def fischer_chain(centers, highlight_idx=None, top="CHO", bottom="CH₂OH", w=150):
    n = len(centers)
    bb_bot = BB_TOP + SPACING * (n + 1)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{bb_bot + 28}" '
             f'viewBox="0 0 {w} {bb_bot + 28}">']
    # backbone
    parts.append(f'<line x1="{CX}" y1="{BB_TOP}" x2="{CX}" y2="{bb_bot}" stroke="black" stroke-width="2"/>')
    # top / bottom groups
    parts.append(f'<text x="{CX}" y="{BB_TOP - 8}" font-family="Arial" font-size="13" text-anchor="middle">{top}</text>')
    parts.append(f'<text x="{CX}" y="{bb_bot + 18}" font-family="Arial" font-size="13" text-anchor="middle">{bottom}</text>')
    for k, (left, right) in enumerate(centers):
        cy = BB_TOP + SPACING * (k + 1)
        hl = (highlight_idx == k)
        if hl:
            parts.append(f'<circle cx="{CX}" cy="{cy}" r="34" fill="#fff3f3" stroke="#c00" '
                         f'stroke-width="1.5" stroke-dasharray="4,3"/>')
        parts.append(f'<line x1="{CX-42}" y1="{cy}" x2="{CX+42}" y2="{cy}" stroke="black" stroke-width="2"/>')
        col = ' fill="#c00"' if hl else ''
        parts.append(f'<text x="{CX-46}" y="{cy+5}" font-family="Arial" font-size="13" text-anchor="end"{col}>{left}</text>')
        parts.append(f'<text x="{CX+46}" y="{cy+5}" font-family="Arial" font-size="13" text-anchor="start"{col}>{right}</text>')
    parts.append('</svg>')
    return "".join(parts)


# distinct projections (C2 top stereocenter, C3 lower)
SVGS = {
    "stereo-rr":     fischer_chain([("H", "OH"), ("H", "OH")]),                 # OH right, right
    "stereo-ll":     fischer_chain([("OH", "H"), ("OH", "H")]),                 # OH left, left (mirror of rr)
    "stereo-lr":     fischer_chain([("OH", "H"), ("H", "OH")]),                 # differ at C2 only
    "stereo-rr-hl":  fischer_chain([("H", "OH"), ("H", "OH")], highlight_idx=0),
    "stereo-lr-hl":  fischer_chain([("OH", "H"), ("H", "OH")], highlight_idx=0),
}

for name, svg in SVGS.items():
    with open(f"{name}.svg", "w") as f:
        f.write(svg)

# verification montage: lay the 5 out in a row with captions
captions = {
    "stereo-rr": "A (OH R,R)", "stereo-ll": "B mirror (L,L)", "stereo-lr": "C (L,R) diff@C2",
    "stereo-rr-hl": "A highlight C2", "stereo-lr-hl": "C highlight C2",
}
cell_w = 165
items = list(SVGS.items())
montage = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{cell_w*len(items)}" height="240" '
           f'viewBox="0 0 {cell_w*len(items)} 240">',
           '<rect width="100%" height="100%" fill="white"/>']
for i, (name, svg) in enumerate(items):
    inner = svg.split('>', 1)[1].rsplit('</svg>', 1)[0]
    montage.append(f'<g transform="translate({i*cell_w+8},10)">{inner}</g>')
    montage.append(f'<text x="{i*cell_w+cell_w//2}" y="225" font-family="Arial" font-size="12" '
                   f'text-anchor="middle">{captions[name]}</text>')
montage.append('</svg>')
with open("verify_stereo.svg", "w") as f:
    f.write("".join(montage))
print("wrote", len(SVGS), "svgs + verify_stereo.svg")
