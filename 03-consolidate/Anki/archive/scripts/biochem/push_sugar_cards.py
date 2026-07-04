"""Push 4 monosaccharide Fischer-projection cards (fructose, glucose, galactose, mannose).

    uv run --python 3.13 --with requests push_sugar_cards.py
"""
from orgo_helpers import assert_connected, store_media, validate, push_cards

DECK = "MCAT Organic Chemistry"
TAGS = ["orgo::concept", "orgo::carbohydrates"]
assert_connected()

def media(name, caption=None, mw=120):
    with open(f"{name}.svg") as f:
        store_media(f"orgo-{name}.svg", f.read())
    img = f'<img src="orgo-{name}.svg" style="max-width:{mw}px; margin:6px auto; display:block;">'
    if caption:
        img += f'<div style="font-size:12px; color:#c00; margin-bottom:6px;">{caption}</div>'
    return img

WRAP = r'<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;">'
FOOT = lambda t: rf'<span style="font-size: 13px; color: #888;">{t}</span>'

cards = []

# ---- D-Fructose ----
cards.append({
    "front": WRAP + r"<b>D-Fructose</b><br><br>Draw and identify <span style='color:#4a90d9;'>D-fructose</span>.</div>",
    "back": WRAP + r"<b>D-Fructose</b><br><br>"
        r"A <b>ketohexose</b> &mdash; a 6-carbon sugar with a <b>ketone at C2</b> (not an aldehyde). In cyclic form it makes a 5-membered <b>furanose</b> ring.<br>"
        + media("sugar-fructose")
        + FOOT(r"The <b>only</b> common monosaccharide that is a <b>ketose</b> (glucose, galactose, mannose are aldoses). Forms a 5-membered <b>furanose</b> ring while the aldoses form 6-membered <b>pyranose</b> rings. D designation: <b>C5 OH on the right</b>.")
        + r"</div>",
    "tags": TAGS})

# ---- D-Glucose ----
cards.append({
    "front": WRAP + r"<b>D-Glucose</b><br><br>Draw and identify <span style='color:#4a90d9;'>D-glucose</span>.</div>",
    "back": WRAP + r"<b>D-Glucose</b><br><br>"
        r"An <b>aldohexose</b> &mdash; a 6-carbon sugar with an <b>aldehyde at C1</b>. The body&rsquo;s <b>primary fuel</b>; forms a 6-membered <b>pyranose</b> ring.<br>"
        + media("sugar-glucose")
        + FOOT(r"Memory aid: OH on the <b>RIGHT</b> at C2, C4, C5 &mdash; only <b>C3</b> breaks the pattern (OH left). C5 OH on the right confirms <b>D</b>.")
        + r"</div>",
    "tags": TAGS})

# ---- D-Galactose ----
cards.append({
    "front": WRAP + r"<b>D-Galactose</b><br><br>Draw and identify <span style='color:#4a90d9;'>D-galactose</span> &mdash; how does it differ from D-glucose?</div>",
    "back": WRAP + r"<b>D-Galactose</b><br><br>"
        r"An <b>aldohexose</b> that differs from D-glucose <b>only at C4</b> &mdash; the C4 OH is on the <b>LEFT</b> (vs right in glucose). This makes it the <b>C4 epimer</b> of glucose. Forms a 6-membered <b>pyranose</b> ring.<br>"
        + media("sugar-galactose", caption="C4 &mdash; epimer vs glucose")
        + FOOT(r"Found in dairy (part of lactose). The flipped <b>C4 OH</b> is the only difference from glucose &mdash; galactose is the <b>C4 epimer</b>.")
        + r"</div>",
    "tags": TAGS})

# ---- D-Mannose ----
cards.append({
    "front": WRAP + r"<b>D-Mannose</b><br><br>Draw and identify <span style='color:#4a90d9;'>D-mannose</span> &mdash; how does it differ from D-glucose?</div>",
    "back": WRAP + r"<b>D-Mannose</b><br><br>"
        r"An <b>aldohexose</b> that differs from D-glucose <b>only at C2</b> &mdash; the C2 OH is on the <b>LEFT</b> (vs right in glucose). This makes it the <b>C2 epimer</b> of glucose. Forms a 6-membered <b>pyranose</b> ring.<br>"
        + media("sugar-mannose", caption="C2 &mdash; epimer vs glucose")
        + FOOT(r"The <b>C2 epimer</b> of glucose &mdash; only C2 is flipped. Found on cell-surface glycoproteins; important in immune recognition.")
        + r"</div>",
    "tags": TAGS})

for cd in cards:
    validate(cd["front"], cd["back"])

added, updated, errors = push_cards(cards, DECK)
print(f"added={added} updated={updated} errors={errors}")
