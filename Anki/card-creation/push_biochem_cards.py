"""
MCAT Biochemistry deck push. Screenshots come from biochem_images/ (newest by mtime),
stored as Anki media via biochem_helpers. Runs on plain system Python:

    python3 push_biochem_cards.py
"""

import os

from biochem_helpers import (
    assert_connected, anki, store_screenshot, render_and_store, validate,
    push_cards, IMAGE_DIR,
)

REVERSED = "Basic (and reversed card)"

DECK = "MCAT Biochemistry"


def pin(substring):
    """Resolve a screenshot by a unique timestamp substring (avoids the U+202F
    narrow-no-break-space macOS puts before AM/PM). Searches biochem_images/ and its
    subfolders (e.g. used/) so processed sources still resolve after being filed away."""
    for root, _dirs, files in os.walk(IMAGE_DIR):
        for f in files:
            if substring in f:
                return os.path.join(root, f)
    raise FileNotFoundError(f"No screenshot matching {substring!r}")


def card_front(topic, question):
    return (
        r"<div style='font-family: Arial, sans-serif; font-size: 18px; "
        r"text-align: center; padding: 20px;'><b>" + topic + r"</b><br><br>" +
        question + r"</div>"
    )


def card_back(topic, body):
    return (
        r"<div style='font-family: Arial, sans-serif; font-size: 18px; "
        r"text-align: center; padding: 20px;'><b>" + topic + r"</b><br><br>" +
        body + r"</div>"
    )


def main():
    assert_connected()
    print("AnkiConnect connected.")

    anki("createDeck", deck=DECK)
    print(f"Deck '{DECK}' ready.")

    # Pinned to its source file so re-runs don't grab a newer unrelated screenshot.
    fa_img = store_screenshot("fatty-acids", pin("7.06.56"))
    print("Stored screenshot as biochem-fatty-acids.png")

    front = card_front(
        "Fatty Acids",
        r"Describe fatty acids in full: their <span style='color: #4a90d9;'>two "
        r"structural parts</span> (and the polarity of each), what their tails are "
        r"like, and the difference between <span style='color: #4a90d9;'>saturated "
        r"and unsaturated</span>.",
    )

    back = card_back(
        "Fatty Acids",
        # one-line framing
        r"<span style='font-size: 15px; color: #555;'>Lipids that store energy and "
        r"build complex lipids (phospholipids, glycolipids, sphingolipids).</span>"
        r"<br><br>"
        # two structural parts
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Carboxyl head</b></td>"
        r"<td>polar &mdash; <b>hydrophilic</b></td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Hydrocarbon tail</b></td>"
        r"<td>nonpolar &mdash; <b>hydrophobic</b></td></tr>"
        r"</table>"
        r"<span style='font-size: 14px; color: #555;'>Tails: usually an "
        r"<b>even</b> number of carbons; in humans up to <b>24</b> long.</span>"
        r"<br><br>"
        # saturated vs unsaturated
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Saturated</b></td>"
        r"<td>all single C&ndash;C bonds &rarr; straight, packs tightly</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Unsaturated</b></td>"
        r"<td>one or more C=C double bonds &rarr; kink/bend</td></tr>"
        r"</table>"
        r"<span style='font-size: 14px; color: #555;'>Double bonds create "
        r"<b>kinks</b> that stop unsaturated fatty acids from clustering &rarr; "
        r"lower melting point, <b>liquid</b> at room temp. Saturated pack tightly "
        r"&rarr; higher melting point, <b>solid</b> at room temp.</span>"
        r"<br><br>" + fa_img,
    )

    validate(front, back)

    # --- Triacylglycerols (Fats) ---
    adipocyte_img = store_screenshot("adipocyte", pin("7.41.16"))
    triglyceride_img = store_screenshot("triglyceride-formation", pin("7.41.23"))
    print("Stored screenshots as biochem-adipocyte.png, biochem-triglyceride-formation.png")

    tg_front = card_front(
        "Triacylglycerols (Fats)",
        r"What is the <span style='color: #4a90d9;'>function</span> and "
        r"<span style='color: #4a90d9;'>components</span> of a triacylglycerol? "
        r"Describe the <span style='color: #4a90d9;'>bond</span> joining glycerol to "
        r"the fatty acids, and the cells that store them.",
    )

    tg_back = card_back(
        "Triacylglycerols (Fats)",
        r"<span style='font-size: 15px; color: #555;'>Also called triglycerides, "
        r"fats, or oils. Store <b>energy</b> and provide <b>thermal insulation</b>.</span>"
        r"<br><br>"
        r"Stored in <b>adipocytes</b> (fat cells) &rarr; <b>adipose tissue</b>."
        r"<br>" + adipocyte_img +
        r"<br>"
        r"Components: <b>glycerol + 3 fatty acids</b>.<br>"
        r"Joined by <b>ester bonds</b> via <b>dehydration synthesis</b> "
        r"(condensation) between glycerol's &ndash;OH and each fatty acid's "
        r"&ndash;COOH &mdash; forming 3 ester bonds releases <b>3 H<sub>2</sub>O</b>."
        r"<br>" + triglyceride_img,
    )

    validate(tg_front, tg_back)

    # --- Glycolipids & Sphingolipids ---
    glycolipid_img = store_screenshot("glycolipid", pin("11.12.55"))
    sphingolipid_img = store_screenshot("sphingolipid", pin("11.13.47"))
    print("Stored screenshots as biochem-glycolipid.png, biochem-sphingolipid.png")

    gs_front = card_front(
        "Glycolipids &amp; Sphingolipids",
        r"How does each differ from a <span style='color: #4a90d9;'>phosphoglyceride</span>, "
        r"and where is each found?",
    )

    gs_back = card_back(
        "Glycolipids &amp; Sphingolipids",
        r"<b>Glycolipid</b> &mdash; like a phosphoglyceride but with one or more "
        r"<b>carbohydrates</b> attached to the glycerol backbone <i>instead of</i> a "
        r"phosphate group. Amphipathic; abundant in membranes of "
        r"<b>myelinated nerve cells</b>."
        r"<br>" + glycolipid_img +
        r"<br>"
        r"<b>Sphingolipid</b> &mdash; like a phosphoglyceride (long fatty acid tail + "
        r"polar head) but built on an amino-alcohol backbone, <b>sphingosine</b>, "
        r"<i>instead of</i> glycerol. Amphipathic; component of the <b>cell membrane</b>."
        r"<br>" + sphingolipid_img,
    )

    validate(gs_front, gs_back)

    # --- Steroid / Cholesterol / Waxes / Terpenes (RDKit structures, two-way) ---
    testosterone_img = render_and_store("testosterone", "CC12CCC3C(CCC4=CC(=O)CCC34C)C1CCC2O")
    cholesterol_img = render_and_store(
        "cholesterol", "CC(C)CCCC(C)C1CCC2C1(CCC3C2CC=C4C3(CCC(C4)O)C)C")
    wax_img = render_and_store("wax", "CCCCCCCCCCCCCCCC(=O)OCCCCCCCCCCCCCCCC")
    isoprene_img = render_and_store("isoprene", "CC(=C)C=C")
    print("Rendered structures: steroid, cholesterol, wax, terpene")

    steroid_front = card_front("Steroid", testosterone_img)
    steroid_back = card_back(
        "Steroid",
        r"<b>Steroid</b> (shown: testosterone)<br>"
        r"<span style='font-size: 15px;'>"
        r"&bull; Four fused carbon rings (3 six- + 1 five-membered)<br>"
        r"&bull; Include some hormones, vitamin D, and cholesterol<br>"
        r"&bull; Examples: <b>estrogen</b> and <b>testosterone</b> (steroid hormones)<br>"
        r"&bull; <b>Cholesterol is the building block of steroids</b></span>",
    )

    chol_front = card_front("Cholesterol", cholesterol_img)
    chol_back = card_back(
        "Cholesterol",
        r"<b>Cholesterol</b> &mdash; a steroid; building block of steroids.<br>"
        r"<span style='font-size: 15px;'>"
        r"&bull; Important component of <b>animal cell membranes</b><br>"
        r"&bull; Prevents extremes in membrane fluidity:</span>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>High temp</b></td>"
        r"<td>squishes phospholipids together / restrains them &rarr; "
        r"<b>stabilizes</b> (less fluid)</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Low temp</b></td>"
        r"<td>prevents clustering &rarr; <b>maintains fluidity</b></td></tr>"
        r"</table>",
    )

    wax_front = card_front("Wax", wax_img)
    wax_back = card_back(
        "Wax",
        r"<b>Wax</b><br>"
        r"<span style='font-size: 15px;'>"
        r"&bull; <b>Ester linkage</b> between a long-chain alcohol and a "
        r"long-chain fatty acid<br>"
        r"&bull; Water-repellent texture; variety of functions<br>"
        r"&bull; Example: ear wax</span>",
    )

    terpene_front = card_front("Terpene", isoprene_img)
    terpene_back = card_back(
        "Terpene",
        r"<b>Terpene</b> (building block shown: isoprene)<br>"
        r"<span style='font-size: 15px;'>"
        r"&bull; Built from repeating <b>isoprene (C5) units</b><br>"
        r"&bull; <b>Vitamin A is a terpene</b> &mdash; a fat-soluble vitamin</span>",
    )

    for f, b in [(steroid_front, steroid_back), (chol_front, chol_back),
                 (wax_front, wax_back), (terpene_front, terpene_back)]:
        validate(f, b)

    # --- Lipoproteins (screenshot 2.07.31) ---
    lipoprotein_img = store_screenshot("lipoprotein", pin("2.07.31"))
    lipo_front = card_front(
        "Lipoproteins",
        r"What are lipoproteins, what is their <span style='color: #4a90d9;'>structure"
        r"</span>, and how are they <span style='color: #4a90d9;'>classified</span>?",
    )
    lipo_back = card_back(
        "Lipoproteins",
        r"Lipids are insoluble in aqueous solution, so they are transported in blood "
        r"via <b>lipoproteins</b>.<br>"
        r"<span style='font-size: 15px;'>"
        r"&bull; <b>Lipid core</b> surrounded by <b>phospholipids + apoproteins</b><br>"
        r"&bull; Hydrophobic core carries the lipids; hydrophilic shell lets them "
        r"travel in the bloodstream<br>"
        r"&bull; Classified by <b>density</b>: higher lipid:protein ratio &rarr; "
        r"<b>lower</b> density</span><br>"
        r"<span style='font-size: 14px; color: #555;'>Classes (low&rarr;high density): "
        r"Chylomicrons, VLDL, LDL, HDL</span>"
        r"<br>" + lipoprotein_img,
    )

    # --- Monosaccharides (screenshot 2.08.39) ---
    mono_img = store_screenshot("monosaccharides", pin("2.08.39"))
    mono_front = card_front(
        "Monosaccharides",
        r"Describe monosaccharides: <span style='color: #4a90d9;'>composition</span>, "
        r"<span style='color: #4a90d9;'>functional groups</span>, "
        r"<span style='color: #4a90d9;'>isomers</span>, and function.",
    )
    mono_back = card_back(
        "Monosaccharides",
        r"Simple sugars, <b>3&ndash;7 carbons</b>, as a chain or ring.<br>"
        r"<span style='font-size: 15px;'>Functional groups: <b>hydroxyl (&ndash;OH)</b> "
        r"+ <b>carbonyl (C=O)</b> &mdash; aldehyde at chain <b>end</b> (aldose), "
        r"ketone in the <b>middle</b> (ketose). Example: glucose "
        r"C<sub>6</sub>H<sub>12</sub>O<sub>6</sub>.</span>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Structural isomers</b></td>"
        r"<td>groups on different carbons &mdash; glucose vs <b>fructose</b></td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Stereoisomers</b></td>"
        r"<td>same carbon, different arrangement &mdash; glucose vs <b>galactose</b></td></tr>"
        r"</table>"
        r"<span style='font-size: 14px; color: #555;'>Glucose &asymp; 80% of absorbed "
        r"carbs &rarr; oxidized for ATP, or polymerized to glycogen for storage.</span>"
        r"<br>" + mono_img,
    )

    # --- Disaccharides (screenshot 2.09.17) ---
    di_img = store_screenshot("disaccharides", pin("2.09.17"))
    di_front = card_front(
        "Disaccharides",
        r"How are disaccharides formed, and what are the three common ones "
        r"(and their monomers)?",
    )
    di_back = card_back(
        "Disaccharides",
        r"Two monosaccharides joined by a <b>dehydration / condensation</b> reaction, "
        r"forming a <b>glycosidic linkage</b>.<br>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Maltose</b></td>"
        r"<td>glucose + glucose</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Sucrose</b> (table sugar)</td>"
        r"<td>glucose + fructose</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Lactose</b> (milk)</td>"
        r"<td>glucose + galactose</td></tr>"
        r"</table>"
        r"<br>" + di_img,
    )

    # --- Polysaccharides (screenshots 2.09.46 + 2.10.33) ---
    poly_img1 = store_screenshot("polysaccharides-amylose-amylopectin", pin("2.09.46"))
    poly_img2 = store_screenshot("polysaccharides-comparison", pin("2.10.33"))
    poly_front = card_front(
        "Polysaccharides",
        r"What are the storage vs. structural polysaccharides, their examples, and "
        r"<span style='color: #4a90d9;'>glycosidic linkages</span>?",
    )
    poly_back = card_back(
        "Polysaccharides",
        r"<span style='font-size: 15px;'>Oligosaccharides = 3&ndash;10 units; "
        r"polysaccharides = &gt;10.</span><br>"
        r"<b>Storage (&alpha;-linkages):</b>"
        r"<span style='font-size: 15px;'><br>"
        r"&bull; <b>Starch</b> &mdash; glucose, plant storage (helical), <b>&alpha;-1,4</b>"
        r"<br>&nbsp;&nbsp;&ndash; <b>Amylose</b>: linear; <b>Amylopectin</b>: branched "
        r"(&alpha;-1,6) every 24&ndash;30 C<br>"
        r"&bull; <b>Glycogen</b> &mdash; glucose, animal storage; <b>&alpha;-1,4 + "
        r"&alpha;-1,6</b>, highly branched (like amylopectin)</span><br>"
        r"<b>Structural (&beta;-linkages):</b>"
        r"<span style='font-size: 15px;'><br>"
        r"&bull; <b>Cellulose</b> &mdash; glucose, plant cell walls, <b>&beta;-1,4</b>; "
        r"most abundant polysaccharide; needs <b>cellulase</b> to break down<br>"
        r"&bull; Chitin</span>"
        r"<br>" + poly_img1 + poly_img2,
    )

    # --- ATP (RDKit structure) ---
    atp_img = render_and_store(
        "atp", "Nc1ncnc2c1ncn2C1OC(COP(=O)(O)OP(=O)(O)OP(=O)(O)O)C(O)C1O",
        w=420, h=300, max_width=360)
    atp_front = card_front(
        "ATP (Adenosine Triphosphate)",
        r"What are the <span style='color: #4a90d9;'>three components</span> of ATP "
        r"and its role in the cell?",
    )
    atp_back = card_back(
        "ATP (Adenosine Triphosphate)",
        r"<b>Adenine + ribose + 3 phosphate groups.</b><br>"
        r"<span style='font-size: 15px;'>The cell's <b>energy currency</b>. Energy is "
        r"stored in the <b>phosphoanhydride bonds</b> between phosphates and released "
        r"by hydrolysis: ATP &rarr; ADP + P<sub>i</sub>.</span>"
        r"<br>" + atp_img,
    )

    # --- Nitrogenous bases (textbook screenshots, two-way recognition) ---
    base_shots = {
        "Adenine": "2.51.12",
        "Guanine": "2.51.19",
        "Cytosine": "2.51.25",
        "Uracil": "2.51.30",
        "Thymine": "2.51.36",
    }
    base_facts = {
        "Adenine": ("Purine", "DNA &amp; RNA", "pairs with T (DNA) / U (RNA)"),
        "Guanine": ("Purine", "DNA &amp; RNA", "pairs with C"),
        "Cytosine": ("Pyrimidine", "DNA &amp; RNA", "pairs with G"),
        "Thymine": ("Pyrimidine", "<b>DNA only</b>", "pairs with A"),
        "Uracil": ("Pyrimidine", "<b>RNA only</b>", "pairs with A"),
    }
    base_cards = []
    for name, ts in base_shots.items():
        img = store_screenshot(name.lower(), pin(ts), max_width=240)
        ring, where, pair = base_facts[name]
        bfront = card_front("Nitrogenous Base", img)
        bback = card_back(
            name,
            r"<b>" + name + r"</b><br>"
            r"<span style='font-size: 15px;'>"
            r"&bull; " + ring + r" (" +
            (r"double ring" if ring == "Purine" else r"single ring") + r")<br>"
            r"&bull; Found in " + where + r"<br>"
            r"&bull; " + pair + r"</span>",
        )
        base_cards.append((bfront, bback, name))

    # --- Purines vs Pyrimidines (screenshot 2.11.41) ---
    pp_img = store_screenshot("purines-pyrimidines", pin("2.11.41"))
    pp_front = card_front(
        "Purines vs. Pyrimidines",
        r"What are the <span style='color: #4a90d9;'>purines</span> and the "
        r"<span style='color: #4a90d9;'>pyrimidines</span>, and how do their rings differ?",
    )
    pp_back = card_back(
        "Purines vs. Pyrimidines",
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Purines</b></td>"
        r"<td><b>double ring</b> (fused 6+5) &mdash; <b>Adenine, Guanine</b></td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Pyrimidines</b></td>"
        r"<td><b>single ring</b> (6-membered) &mdash; <b>Cytosine, Thymine, Uracil</b></td></tr>"
        r"</table>"
        r"<span style='font-size: 13px; color: #888;'>Mnemonic: <b>PUR</b>e <b>A</b>s "
        r"<b>G</b>old (purines = A, G); <b>CUT</b> the <b>py</b> (pyrimidines = C, U, T).</span>"
        r"<br>" + pp_img,
    )

    # --- DNA vs RNA nucleotides ---
    dnarna_front = card_front(
        "DNA vs. RNA Nucleotides",
        r"How do the nucleotides in DNA differ from those in RNA?",
    )
    dnarna_back = card_back(
        "DNA vs. RNA Nucleotides",
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'></td><td><b>DNA</b></td><td><b>RNA</b></td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Sugar</b></td>"
        r"<td>deoxyribose (no 2&prime;-OH)</td><td>ribose (2&prime;-OH)</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Pyrimidine base</b></td>"
        r"<td><b>thymine</b></td><td><b>uracil</b></td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Strands</b></td>"
        r"<td>double-stranded</td><td>single-stranded</td></tr>"
        r"</table>"
        r"<span style='font-size: 13px; color: #888;'>Shared bases: adenine, guanine, "
        r"cytosine.</span>",
    )

    # --- Phospholipids / Phosphoglycerides (screenshot 7.46.02) ---
    phospho_img = store_screenshot("phosphoglyceride", pin("7.46.02"))
    phospho_front = card_front(
        "Phospholipids (Phosphoglycerides)",
        r"What are they made of, what does <span style='color: #4a90d9;'>amphipathic"
        r"</span> mean, and how/why do they form a <span style='color: #4a90d9;'>"
        r"bilayer</span> in water?",
    )
    phospho_back = card_back(
        "Phospholipids (Phosphoglycerides)",
        r"A <b>phospholipid</b> is a lipid with a <b>phosphate group</b>. The MCAT's "
        r"key type is <b>phosphoglycerides</b>:<br>"
        r"<span style='font-size: 15px;'>glycerol backbone + a polar <b>phosphate head"
        r"</b> (hydrophilic) + <b>2 nonpolar fatty acid tails</b> (hydrophobic).</span>"
        r"<br>" + phospho_img +
        r"<span style='font-size: 15px;'>&rarr; <b>Amphipathic</b> (both a hydrophilic "
        r"and a hydrophobic end) &rarr; major component of <b>biological membranes</b>."
        r"<br><br>In water, hydrophilic heads face <b>out</b> toward water and "
        r"hydrophobic tails hide <b>inward</b> &rarr; a <b>phospholipid bilayer</b> "
        r"(heads on both outer surfaces, tails sandwiched between).</span>",
    )
    validate(phospho_front, phospho_back)

    # --- Nucleotide Structure (screenshot 2.11.01) ---
    nucleotide_img = store_screenshot("nucleotide-structure", pin("2.11.01"))
    nuc_front = card_front(
        "Nucleotide Structure",
        r"What are the <span style='color: #4a90d9;'>three components</span> of a "
        r"nucleotide, how does a <span style='color: #4a90d9;'>nucleoside</span> "
        r"differ, and what other roles do nucleotides play?",
    )
    nuc_back = card_back(
        "Nucleotide Structure",
        r"Nucleotides are the <b>monomers of nucleic acids</b> (DNA &amp; RNA).<br>"
        r"<span style='font-size: 15px;'>Three parts: <b>phosphate + sugar + "
        r"nitrogenous base</b>.</span>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>Nucleoside</b></td>"
        r"<td>sugar + base</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>Nucleotide</b></td>"
        r"<td>nucleoside + one or more phosphates</td></tr>"
        r"</table>"
        r"<span style='font-size: 14px; color: #555;'>Other roles: <b>ATP</b> (energy), "
        r"<b>cAMP</b> (secondary messenger), <b>NADH / FADH<sub>2</sub></b> "
        r"(coenzymes).</span>"
        r"<br>" + nucleotide_img,
    )

    # --- Nucleic Acid Structure (screenshot 2.12.21) ---
    nacid_img = store_screenshot("nucleic-acid-structure", pin("2.12.21"))
    nacid_front = card_front(
        "Nucleic Acid Structure",
        r"How are nucleotides joined into a chain, and what defines the "
        r"<span style='color: #4a90d9;'>5&prime; and 3&prime; ends</span>?",
    )
    nacid_back = card_back(
        "Nucleic Acid Structure",
        r"Nucleotides join by a <b>dehydration / condensation</b> reaction forming a "
        r"<b>phosphodiester bond</b> &mdash; between the phosphate of one nucleotide "
        r"and the <b>hydroxyl on the sugar</b> of the next.<br>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>5&prime; end</b></td>"
        r"<td>free <b>phosphate</b> (on the 5&prime; carbon)</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>3&prime; end</b></td>"
        r"<td>free <b>hydroxyl</b> (on the 3&prime; carbon)</td></tr>"
        r"</table>"
        r"<br>" + nacid_img,
    )

    # --- DNA Double Helix (screenshot 2.12.57) ---
    helix_img = store_screenshot("dna-double-helix", pin("2.12.57"))
    helix_front = card_front(
        "The DNA Double Helix",
        r"Describe the <span style='color: #4a90d9;'>arrangement</span>, "
        r"<span style='color: #4a90d9;'>bonding</span>, and "
        r"<span style='color: #4a90d9;'>pairing rules</span> of the two strands.",
    )
    helix_back = card_back(
        "The DNA Double Helix",
        r"<span style='font-size: 15px;'>"
        r"&bull; Sugar-phosphate backbone on the <b>outside</b>, nitrogenous bases "
        r"pointing <b>inward</b><br>"
        r"&bull; Bases <b>hydrogen-bond</b> to hold the strands together<br>"
        r"&bull; <b>Complementary</b>: A&ndash;T and C&ndash;G (A&ndash;U in RNA)<br>"
        r"&bull; <b>Antiparallel</b>: one strand 5&prime;&rarr;3&prime;, the other "
        r"3&prime;&rarr;5&prime;</span>"
        r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
        r"<tr><td style='padding: 4px 10px;'><b>A&ndash;T</b></td>"
        r"<td><b>2</b> hydrogen bonds</td></tr>"
        r"<tr><td style='padding: 4px 10px;'><b>C&ndash;G</b></td>"
        r"<td><b>3</b> hydrogen bonds</td></tr>"
        r"</table>"
        r"<br>" + helix_img,
    )

    for f, b in [(lipo_front, lipo_back), (mono_front, mono_back),
                 (di_front, di_back), (poly_front, poly_back),
                 (atp_front, atp_back), (pp_front, pp_back),
                 (dnarna_front, dnarna_back),
                 (nuc_front, nuc_back), (nacid_front, nacid_back),
                 (helix_front, helix_back)]:
        validate(f, b)
    for bfront, bback, _ in base_cards:
        validate(bfront, bback)

    cards = [
        {
            "front": front,
            "back": back,
            "tags": ["biochem::definition", "biochem::lipids::fatty-acids"],
        },
        {
            "front": tg_front,
            "back": tg_back,
            "tags": ["biochem::definition", "biochem::lipids::triacylglycerols"],
        },
        {
            "front": gs_front,
            "back": gs_back,
            "tags": ["biochem::definition", "biochem::lipids::glycolipids-sphingolipids"],
        },
        {
            "front": steroid_front, "back": steroid_back, "model": REVERSED,
            "tags": ["biochem::definition", "biochem::lipids::steroids"],
        },
        {
            "front": chol_front, "back": chol_back, "model": REVERSED,
            "tags": ["biochem::definition", "biochem::lipids::steroids"],
        },
        {
            "front": wax_front, "back": wax_back, "model": REVERSED,
            "tags": ["biochem::definition", "biochem::lipids::waxes"],
        },
        {
            "front": terpene_front, "back": terpene_back, "model": REVERSED,
            "tags": ["biochem::definition", "biochem::lipids::terpenes"],
        },
        {
            "front": phospho_front, "back": phospho_back,
            "tags": ["biochem::definition", "biochem::lipids::phospholipids"],
        },
        {
            "front": lipo_front, "back": lipo_back,
            "tags": ["biochem::definition", "biochem::lipids::lipoproteins"],
        },
        {
            "front": mono_front, "back": mono_back,
            "tags": ["biochem::definition", "biochem::carbohydrates::monosaccharides"],
        },
        {
            "front": di_front, "back": di_back,
            "tags": ["biochem::definition", "biochem::carbohydrates::disaccharides"],
        },
        {
            "front": poly_front, "back": poly_back,
            "tags": ["biochem::definition", "biochem::carbohydrates::polysaccharides"],
        },
        {
            "front": atp_front, "back": atp_back,
            "tags": ["biochem::definition", "biochem::nucleotides::atp"],
        },
        {
            "front": pp_front, "back": pp_back,
            "tags": ["biochem::concept", "biochem::nucleic-acids::bases"],
        },
        {
            "front": dnarna_front, "back": dnarna_back,
            "tags": ["biochem::concept", "biochem::nucleic-acids::dna-rna"],
        },
        {
            "front": nuc_front, "back": nuc_back,
            "tags": ["biochem::definition", "biochem::nucleic-acids::nucleotides"],
        },
        {
            "front": nacid_front, "back": nacid_back,
            "tags": ["biochem::definition", "biochem::nucleic-acids::structure"],
        },
        {
            "front": helix_front, "back": helix_back,
            "tags": ["biochem::concept", "biochem::nucleic-acids::dna-helix"],
        },
    ]

    added, updated, errors = push_cards(cards, DECK)
    print(f"Added: {added}, Updated: {updated}, Errors: {errors}")

    # Base structure cards need special handling: they all share the same visible
    # front text ("Nitrogenous Base"), and Anki strips HTML/media before computing
    # the duplicate key -> all 5 collapse to ONE key and clobber each other through
    # the normal upsert. So push them separately: delete existing reversed base notes,
    # then add fresh with allowDuplicate=True (idempotent via delete-first).
    existing = anki("findNotes",
                    query='deck:"MCAT Biochemistry" tag:biochem::nucleic-acids::bases')
    stale = [n["noteId"] for n in anki("notesInfo", notes=existing)
             if n["modelName"] == REVERSED]
    if stale:
        anki("deleteNotes", notes=stale)
    base_notes = [
        {
            "deckName": DECK, "modelName": REVERSED,
            "fields": {"Front": bf, "Back": bb},
            "tags": ["biochem::definition", "biochem::nucleic-acids::bases"],
            "options": {"allowDuplicate": True},
        }
        for bf, bb, _ in base_cards
    ]
    bids = anki("addNotes", notes=base_notes)
    print(f"Base notes re-added: {sum(1 for i in bids if i)} "
          f"({', '.join(n for _, _, n in base_cards)})")


if __name__ == "__main__":
    main()
