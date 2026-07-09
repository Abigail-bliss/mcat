# [CLUE] Molecular Genetics / Central Dogma (DNA structure → packaging → strands → splicing → translation)
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 — several Bio misses, migrated/merged from Anki + Q58. Splice-site "missense" trap; strand direction; histone location.)

## DNA molecular structure (backbone, base orientation, RNA differences)

- **Nucleotide = the monomer**
  - **nitrogenous base + sugar (deoxyribose) + phosphate group**

- **Backbone = sugar–phosphate chain**
  - **phosphodiester bonds** link the **3′ carbon** of one sugar to the **5′ carbon** of the next
  - **backbone faces OUTWARD** (hydrophilic, solvent-facing)
  - **bases face INWARD** (pair in the core, H-bond across the helix)
  - Note: the phosphodiester linkage (3′ carbon → next 5′ carbon) is what gives a strand its directionality
  - **"read" vs "synthesized" — the distinction that trips people up:**
    - **template strand is READ 3′→5′** → therefore the **new strand is SYNTHESIZED 5′→3′** (polymerase can only add to a free 3′-OH)
    - Note: same event, two strands — reading the template 3′→5′ *is* building the new strand 5′→3′ (they're antiparallel)
    - Note: MCAT trap — if given a template 3′→5′, its product is the complement written 5′→3′

- **RNA differences**
  - uses **ribose** (has a **2′-OH**) instead of deoxyribose
  - Note: the 2′-OH makes RNA less stable / more reactive than DNA

## DNA packaging — histones / chromatin

- **What they bind & where**
  - **positively charged proteins** that bind and stabilize **DNA** (NOT RNA)
  - located in the **nucleus**
  - Note: positive histones grip the negative DNA phosphate backbone — opposite charges attract

- **What they do**
  - act like **spools** that DNA wraps around (nucleosome packaging)
  - **control gene accessibility** via chemical marks (**methyl / acetyl** groups)
    - modifying how tightly DNA wraps turns genes **"on" (accessible)** or **"off" (hidden)**
  - Note: this is epigenetic regulation — the DNA sequence doesn't change, only its accessibility

- **Trap**
  - histones are in the nucleus → **NOT** in axons, dendrites, or synaptic terminals (those lack a nucleus)

## Sense vs. antisense strands (coding/template + antisense oligos)

- **Coding (sense) strand**
  - **same sequence as the mRNA** (with T → U)
  - Note: "sense" = it reads like the message

- **Template (antisense) strand**
  - the strand **RNA polymerase actually reads**, **3′→5′**, to build the mRNA 5′→3′
  - Note: complementary to the mRNA

- **Antisense oligonucleotide (drug logic)**
  - a short strand **complementary to the mRNA** → **binds the mRNA** → **blocks translation or triggers degradation**
  - Note: mnemonic — **sense strand ≈ mRNA**; an **antisense oligo targets mRNA** the way the template strand is antisense to it

## RNA splicing (introns, exons, the GU–AG rule, splice-site mutations)

- **Core idea:** a eukaryotic gene is **exons interrupted by introns**. After transcription, the **spliceosome cuts out introns and joins exons** to make mature mRNA.
  - **Ex**ons = **ex**pressed (kept in the final mRNA → translated)
  - **In**trons = **in**tervening / thrown out (removed before translation)
  - Note: happens in the nucleus, part of pre-mRNA processing (along with 5' cap + poly-A tail).

- **How the spliceosome finds the cut sites — the GU–AG rule**
  - Introns almost always **start with GU** (5' splice site / "donor") and **end with AG** (3' splice site / "acceptor")
  - The **guanine right at the exon/intron boundary** is part of the recognition signal the spliceosome reads
  - Note: mnemonic — introns are **"GU..AG"**; they open with GU, close with AG.

- **The spliceosome machinery** (enough for MCAT)
  - made of **snRNPs** ("snurps") = small nuclear RNAs + proteins
  - it recognizes the splice sites, loops the intron into a **lariat**, cuts it out, seals the exons together

- **Why this matters: splice-site mutations ≠ coding mutations** (the Q58 trap)
  - A base at a **splice site** is read as a *cut signal*, NOT as part of a codon
  - Mutate the boundary G → spliceosome can't recognize the site → **intron is retained** in the mRNA
  - Retained intron throws off the **reading frame** for everything downstream → usually a broken protein, but the *primary/direct* effect is **failed splicing**, not a single amino-acid swap
  - Note: **tell in the stem** = "boundary" language ("terminal guanine of a 5' exon"). Boundary/splice-site wording → think **intron retention**, not **missense**.
  - Note: contrast — a **missense** mutation is one base *inside a codon* → one amino acid changes. A **splice-site** mutation is a base *at the exon/intron seam* → whole intron stays.

- **Bonus payoff: alternative splicing**
  - the same pre-mRNA can be spliced different ways (keep/drop different exons) → **one gene → many proteins**
  - Note: a big reason humans have ~20k genes but far more proteins.

## Translation — the wobble hypothesis (why ~45 tRNAs cover 64 codons)

- **The rule**
  - the **3rd codon position** (the **wobble position**) can form **non-Watson–Crick base pairs** with the tRNA anticodon
  - → **one tRNA can read multiple codons** for the **same amino acid**
  - Note: **1st and 2nd positions are strict**; only the 3rd wobbles

- **Consequence**
  - **~45 tRNAs cover all 64 codons** (fewer tRNAs than codons)

- **Wobble pairings**
  - **G pairs with U**
  - **inosine (I)** pairs with **U, C, or A** (the most flexible)
  - Note: ties to the degeneracy of the code — synonymous codons usually differ only at position 3
