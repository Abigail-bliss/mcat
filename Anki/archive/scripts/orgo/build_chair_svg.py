"""Build a labeled cyclohexane chair SVG (axial/equatorial) and render a PNG to verify."""
import math

# Ring carbons in ring order (para apexes at index 0 and 3).
P = [
    (210, 85),   # 0  top apex   (axial up)
    (290, 110),  # 1
    (230, 160),  # 2
    (150, 185),  # 3  bottom apex (axial down)
    (70, 160),   # 4
    (130, 110),  # 5
]
cx = sum(p[0] for p in P) / 6
cy = sum(p[1] for p in P) / 6

AX_LEN = 30
EQ_LEN = 30
axial_up = [True, False, True, False, True, False]  # alternating

def unit(dx, dy):
    m = math.hypot(dx, dy)
    return (dx / m, dy / m)

lines = []
labels = []

# ring bonds
for i in range(6):
    x1, y1 = P[i]
    x2, y2 = P[(i + 1) % 6]
    lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" stroke-width="2.5"/>')

# axial bonds (vertical) + labels
for i, (x, y) in enumerate(P):
    ey = y - AX_LEN if axial_up[i] else y + AX_LEN
    lines.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{ey}" stroke="#c00" stroke-width="2"/>')
    ly = ey - 6 if axial_up[i] else ey + 14
    labels.append(f'<text x="{x}" y="{ly}" font-family="Arial" font-size="12" fill="#c00" text-anchor="middle">ax</text>')

# equatorial bonds (parallel to bond i+1 -> i+2, pointing outward) + labels
for i, (x, y) in enumerate(P):
    bx = P[(i + 2) % 6][0] - P[(i + 1) % 6][0]
    by = P[(i + 2) % 6][1] - P[(i + 1) % 6][1]
    ux, uy = unit(bx, by)
    # outward sign
    if ux * (x - cx) + uy * (y - cy) < 0:
        ux, uy = -ux, -uy
    ex, ey = x + ux * EQ_LEN, y + uy * EQ_LEN
    lines.append(f'<line x1="{x}" y1="{y}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#06c" stroke-width="2"/>')
    lx = ex + (10 if ux > 0 else -10)
    ly = ey + (5 if uy >= 0 else -2)
    anchor = "start" if ux > 0 else "end"
    labels.append(f'<text x="{lx:.1f}" y="{ly:.1f}" font-family="Arial" font-size="12" fill="#06c" text-anchor="{anchor}">eq</text>')

svg = (
    '<svg xmlns="http://www.w3.org/2000/svg" width="370" height="260" viewBox="0 0 370 260">'
    + "".join(lines) + "".join(labels) + "</svg>"
)

with open("chair.svg", "w") as f:
    f.write(svg)

from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
drawing = svg2rlg("chair.svg")
renderPM.drawToFile(drawing, "chair_preview.png", fmt="PNG", bg=0xFFFFFF)
print("written chair.svg and chair_preview.png")
