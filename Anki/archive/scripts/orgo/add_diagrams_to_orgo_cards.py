
"""
Add skeletal diagrams to 15 orgo cards + re-render ester with compact OR' label.

Run:
    uv run --python 3.13 --with rdkit --with requests add_diagrams_to_orgo_cards.py
"""

import re, sys
sys.path.insert(0, "/Users/abigailbliss/Documents/MCAT/Anki")
from orgo_helpers import assert_connected, anki, render_and_store, validate


# ── Layout helpers ───────────────────────────────────────────────────────────

def rxn(parts, arrow="→"):
    """Inline reaction scheme: list of img snippets or text strings, arrows between."""
    html_parts = []
    for p in parts:
        if p.startswith("<"):           # raw HTML — pass through
            html_parts.append(p)
        else:                           # text label — wrap in span
            html_parts.append(f"<span style='font-size:15px; padding:0 5px;'>{p}</span>")
    sep = f"<span style='font-size:20px; padding:0 5px;'>{arrow}</span>"
    return (
        "<div style='display:flex; align-items:center; justify-content:center; "
        "flex-wrap:wrap; gap:2px; margin:6px 0;'>" + sep.join(html_parts) + "</div>"
    )


def side_by_side(label1, img1, label2, img2):
    """Two labeled structures side by side (for kinetic vs thermodynamic, etc.)."""
    def box(lbl, im):
        return (
            f"<div style='text-align:center; margin:4px 14px;'>"
            f"<span style='font-size:13px; color:#555;'><b>{lbl}</b></span><br>{im}</div>"
        )
    return (
        "<div style='display:flex; justify-content:center; align-items:flex-start; "
        "flex-wrap:wrap; margin:6px 0;'>" + box(label1, img1) + box(label2, img2) + "</div>"
    )


def insert(back_html, diagram_html):
    """Inject diagram right after <b>Title</b><br><br> in a card back."""
    new = re.sub(
        r'(<b>[^<]+</b><br><br>)',
        lambda m: m.group(1) + diagram_html + "<br>",
        back_html, count=1
    )
    assert new != back_html, "Insertion pattern <b>...</b><br><br> not found!"
    return new


# ── Render helpers ───────────────────────────────────────────────────────────

def img(name, smiles, labels=None, w=200, h=150, mw=185):
    """Standalone centered image."""
    return render_and_store(name, smiles, w=w, h=h, max_width=mw, dummy_labels=labels)


def ii(name, smiles, labels=None, w=170, h=125, mw=155):
    """Inline image for reaction schemes."""
    return render_and_store(name, smiles, w=w, h=h, max_width=mw, dummy_labels=labels, inline=True)


# ── Main ─────────────────────────────────────────────────────────────────────

assert_connected()

TARGET_IDS = [
    1781215049708, 1781215049711, 1781215049713,
    1781215275208, 1781215275210, 1781215275211, 1781215275213, 1781215275214,
    1781215275215, 1781216205236,
    1781216920119, 1781216920167,
    1781220735378, 1781221866461, 1781221866483,
]
notes = {n["noteId"]: n for n in anki("notesInfo", notes=TARGET_IDS)}


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


# ── 0. Ester: compact OR' label (just re-render the SVG; both cards auto-update) ──
render_and_store("ester-generic", "[*]C(=O)[*]", dummy_labels=["R", "OR'"])
print("Ester SVG updated.")

# ── Fix aldehyde generic: use [*]C=O (RC=O), NOT [H]C(=O)[*] ──────────────
# Explicit H creates a visible bond line (propeller layout) — looks wrong in skeletal.
# [*]C=O with label "R" gives R-C=O (terminal carbonyl = aldehyde; H is implicit).
render_and_store("aldehyde-generic", "[*]C=O", dummy_labels=["R"])
print("Aldehyde SVG fixed.\n")

# ── Keto-Enol ────────────────────────────────────────────────────────────────
keto_i = ii("keto-form",  r"[*]CC(=O)[*]",   labels=["R", "R'"])
enol_i = ii("enol-form",  r"[*]C=C(O)[*]",   labels=["R", "R'"])
keto_enol = rxn([keto_i, enol_i], arrow="⇌")

print("Keto-enol:")
update(1781215049708, keto_enol)         # structural difference
update(1781215049711, keto_enol)         # interconversion (same diagram)
update(1781215049713, img("phenol", "c1ccccc1O"))  # enol exception: phenol

# ── Cyanohydrin ──────────────────────────────────────────────────────────────
cyano_i  = ii("cyanohydrin-inline",   r"[*]C([OH])C#N", labels=["R"])
cyano_sa = img("cyanohydrin-generic", r"[*]C([OH])C#N", labels=["R"])
ald_i    = ii("cyanohydrin-aldehyde", "[*]C=O",          labels=["R"])

print("Cyanohydrin:")
update(1781215275208, cyano_sa)                                                   # what is it
update(1781215275210, rxn([ald_i, "+ HCN", cyano_i]))                            # formation reaction
update(1781215275211, rxn([cyano_i, ii("cyanohydrin-amine-prod",    r"[*]C([OH])C[NH2]",       labels=["R"])]))
update(1781215275213, rxn([cyano_i, ii("cyanohydrin-acid-prod",     r"[*]C([OH])C(=O)[OH]",    labels=["R"])]))

# Strecker: aminonitrile → amino acid
print("Strecker:")
update(1781215275214, rxn([
    ii("alpha-aminonitrile",   r"[*]C([NH2])C#N",       labels=["R"]),
    ii("strecker-amino-acid",  r"[*]C([NH2])C(=O)[OH]", labels=["R"]),
]))

# ── Enolates ─────────────────────────────────────────────────────────────────
print("Enolates:")
update(1781215275215, rxn([                              # resonance: C⁻ ↔ O⁻
    ii("enolate-carbanion", r"[CH2-]C(=O)[*]", labels=["R"]),
    ii("enolate-oxyanion",  r"C=C([O-])[*]",   labels=["R"]),
], arrow="↔"))

# Kinetic vs thermodynamic from methyl ethyl ketone (2-butanone)
print("Kinetic vs thermodynamic:")
update(1781216205236, side_by_side(
    "Kinetic",        ii("kinetic-enolate",       r"[CH2]=C([O-])CC"),
    "Thermodynamic",  ii("thermodynamic-enolate", r"CC([O-])=CC"),
))

# ── Aldol ────────────────────────────────────────────────────────────────────
print("Aldol:")
acetald_i = ii("aldol-acetaldehyde", "CC=O")
update(1781216920119, rxn([                              # what is it
    f"<span style='font-size:15px;'>2&times;</span>{acetald_i}",
    ii("aldol-product", "CC(O)CC=O"),
]))
update(1781216920167, rxn([                              # aldol vs condensation product
    ii("aldol-beta-hydroxy",  "CC(O)CC=O"),
    ii("aldol-condensation",  "CC=CC=O"),
], arrow="&minus;H<sub>2</sub>O"))

# ── Grignard ─────────────────────────────────────────────────────────────────
print("Grignard:")
ald_grignard_i = ii("grignard-aldehyde", "[*]C=O",              labels=["R'"])
co2_i          = ii("co2-molecule",      "O=C=O")
rcooh_i        = ii("grignard-cooh",     r"[*]C(=O)[OH]",       labels=["R"])
product_i      = ii("grignard-product",  r"[*]C([OH])[*]",      labels=["R", "R'"])

update(1781220735378, rxn([
    f"<span style='font-size:15px;'>RMgX&nbsp;+</span>{ald_grignard_i}",
    product_i,
]))
update(1781221866461, rxn([
    f"<span style='font-size:15px;'>RMgX&nbsp;+</span>{co2_i}",
    rcooh_i,
]))

# ── Decarboxylation ───────────────────────────────────────────────────────────
print("Decarboxylation:")
beta_keto_i  = ii("beta-keto-acid",  r"[*]C(=O)CC(=O)[OH]", labels=["R"])
ketone_i     = ii("decarb-product",  r"[*]C(=O)C",           labels=["R"])
co2_decarb_i = ii("co2-decarb",     "O=C=O")
products_html = (
    f"<div style='display:flex; align-items:center; gap:3px;'>"
    f"{ketone_i}<span style='font-size:15px;'>+</span>{co2_decarb_i}</div>"
)
update(1781221866483, rxn([beta_keto_i, products_html]))

print("\nAll done! 15 cards updated + ester SVG.")
