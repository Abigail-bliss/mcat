"""Build Fischer-projection SVGs for D-fructose, D-glucose, D-galactose, D-mannose,
plus a verification montage rendered via qlmanage."""

CX = 75
SPACING = 44
BB_TOP = 24


def fischer_sugar(centers, top, bottom, highlight_idx=None, w=150):
    """centers: list of (left,right) tuples or the literal 'C=O' for a carbonyl carbon."""
    n = len(centers)
    bb_bot = BB_TOP + SPACING * (n + 1)
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{bb_bot + 28}" '
         f'viewBox="0 0 {w} {bb_bot + 28}">']
    p.append(f'<line x1="{CX}" y1="{BB_TOP}" x2="{CX}" y2="{bb_bot}" stroke="black" stroke-width="2"/>')
    p.append(f'<text x="{CX}" y="{BB_TOP - 8}" font-family="Arial" font-size="13" text-anchor="middle">{top}</text>')
    p.append(f'<text x="{CX}" y="{bb_bot + 18}" font-family="Arial" font-size="13" text-anchor="middle">{bottom}</text>')
    for k, c in enumerate(centers):
        cy = BB_TOP + SPACING * (k + 1)
        hl = (highlight_idx == k)
        if hl:
            p.append(f'<circle cx="{CX}" cy="{cy}" r="32" fill="#fff3f3" stroke="#c00" '
                     f'stroke-width="1.5" stroke-dasharray="4,3"/>')
        if c == "C=O":
            p.append(f'<line x1="{CX}" y1="{cy-2}" x2="{CX+26}" y2="{cy-2}" stroke="black" stroke-width="2"/>')
            p.append(f'<line x1="{CX}" y1="{cy+2}" x2="{CX+26}" y2="{cy+2}" stroke="black" stroke-width="2"/>')
            p.append(f'<text x="{CX+34}" y="{cy+5}" font-family="Arial" font-size="13" text-anchor="start">O</text>')
        else:
            left, right = c
            p.append(f'<line x1="{CX-42}" y1="{cy}" x2="{CX+42}" y2="{cy}" stroke="black" stroke-width="2"/>')
            col = ' fill="#c00"' if hl else ''
            p.append(f'<text x="{CX-46}" y="{cy+5}" font-family="Arial" font-size="13" text-anchor="end"{col}>{left}</text>')
            p.append(f'<text x="{CX+46}" y="{cy+5}" font-family="Arial" font-size="13" text-anchor="start"{col}>{right}</text>')
    p.append('</svg>')
    return "".join(p)


SVGS = {
    # C2, C3, C4, C5
    "sugar-glucose":   fischer_sugar([("H","OH"),("OH","H"),("H","OH"),("H","OH")], "CHO", "CH₂OH"),
    "sugar-galactose": fischer_sugar([("H","OH"),("OH","H"),("OH","H"),("H","OH")], "CHO", "CH₂OH", highlight_idx=2),
    "sugar-mannose":   fischer_sugar([("OH","H"),("OH","H"),("H","OH"),("H","OH")], "CHO", "CH₂OH", highlight_idx=0),
    # fructose: C2=O, C3, C4, C5
    "sugar-fructose":  fischer_sugar(["C=O",("OH","H"),("H","OH"),("H","OH")], "CH₂OH", "CH₂OH"),
}

for name, svg in SVGS.items():
    with open(f"{name}.svg", "w") as f:
        f.write(svg)

# montage
captions = {"sugar-glucose": "D-glucose", "sugar-galactose": "D-galactose (C4)",
            "sugar-mannose": "D-mannose (C2)", "sugar-fructose": "D-fructose (keto)"}
cell_w = 175
items = list(SVGS.items())
m = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{cell_w*len(items)}" height="300" '
     f'viewBox="0 0 {cell_w*len(items)} 300"><rect width="100%" height="100%" fill="white"/>']
for i, (name, svg) in enumerate(items):
    inner = svg.split('>', 1)[1].rsplit('</svg>', 1)[0]
    m.append(f'<g transform="translate({i*cell_w+12},10)">{inner}</g>')
    m.append(f'<text x="{i*cell_w+cell_w//2}" y="290" font-family="Arial" font-size="13" '
             f'text-anchor="middle">{captions[name]}</text>')
m.append('</svg>')
with open("verify_sugar.svg", "w") as f:
    f.write("".join(m))
print("wrote", len(SVGS), "sugar svgs + verify_sugar.svg")
