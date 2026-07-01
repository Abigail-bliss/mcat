"""Fix Grignard+CO2 and Decarboxylation cards (nested <sub> in title broke regex)."""
import re, sys
sys.path.insert(0, "/Users/abigailbliss/Documents/MCAT/Anki")
from orgo_helpers import assert_connected, anki, render_and_store, validate


def rxn(parts, arrow="→"):
    html_parts = []
    for p in parts:
        if p.startswith("<"):
            html_parts.append(p)
        else:
            html_parts.append(f"<span style='font-size:15px; padding:0 5px;'>{p}</span>")
    sep = f"<span style='font-size:20px; padding:0 5px;'>{arrow}</span>"
    return (
        "<div style='display:flex; align-items:center; justify-content:center; "
        "flex-wrap:wrap; gap:2px; margin:6px 0;'>" + sep.join(html_parts) + "</div>"
    )


def insert(back_html, diagram_html):
    # Use .*? (lazy) to allow nested tags like <sub> inside the <b> title
    new = re.sub(
        r'(<b>.*?</b><br><br>)',
        lambda m: m.group(1) + diagram_html + "<br>",
        back_html, count=1, flags=re.DOTALL
    )
    assert new != back_html, "Pattern not found!"
    return new


def ii(name, smiles, labels=None, w=170, h=125, mw=155):
    return render_and_store(name, smiles, w=w, h=h, max_width=mw, dummy_labels=labels, inline=True)


assert_connected()
notes = {n["noteId"]: n for n in anki("notesInfo", notes=[1781221866461, 1781221866483])}


def update(nid, diagram_html):
    n = notes[nid]
    new_back = insert(n["fields"]["Back"]["value"], diagram_html)
    validate(n["fields"]["Front"]["value"], new_back)
    anki("updateNote", note={
        "id": nid,
        "fields": {"Front": n["fields"]["Front"]["value"], "Back": new_back},
        "tags": n["tags"],
    })
    print(f"  ✓ {nid}")


# Grignard + CO₂ → carboxylic acid
co2_i   = ii("co2-molecule",  "O=C=O")
rcooh_i = ii("grignard-cooh", "[*]C(=O)[OH]", labels=["R"])
update(1781221866461, rxn([
    f"<span style='font-size:15px;'>RMgX&nbsp;+</span>{co2_i}",
    rcooh_i,
]))

# Decarboxylation: β-keto acid → ketone + CO₂
beta_keto_i  = ii("beta-keto-acid", "[*]C(=O)CC(=O)[OH]", labels=["R"])
ketone_i     = ii("decarb-product", "[*]C(=O)C",           labels=["R"])
co2_decarb_i = ii("co2-decarb",    "O=C=O")
products_html = (
    f"<div style='display:flex; align-items:center; gap:3px;'>"
    f"{ketone_i}<span style='font-size:15px;'>+</span>{co2_decarb_i}</div>"
)
update(1781221866483, rxn([beta_keto_i, products_html]))

print("Done.")
