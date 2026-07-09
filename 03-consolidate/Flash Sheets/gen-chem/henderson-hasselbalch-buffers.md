# [CLUE] Henderson–Hasselbalch & Polyprotic Acids (buffers, acid:base ratios, pKa matching)
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 CPF Q5 — missed HH direction; CPF Q9 — missed polyprotic phosphate matching.)

- **Henderson–Hasselbalch equation**
  - **pH = pKₐ + log([A⁻]/[HA])**
  - [A⁻] = conjugate base · [HA] = weak acid
  - Note: the log is base/acid (NOT acid/base). Write this direction every time.

- **Using HH: find acid:base ratio from pH and pKₐ**
  - rearrange: **log([A⁻]/[HA]) = pH − pKₐ**
  - if pH > pKₐ → log > 0 → [A⁻] > [HA] → more base than acid
  - if pH < pKₐ → log < 0 → [HA] > [A⁻] → more acid than base
  - **1 pH unit above pKₐ → 10× more base** (log = 1 → ratio = 10)
  - **1 pH unit below pKₐ → 10× more acid** (log = −1 → ratio = 1/10)
  - at pH = pKₐ → 1:1 ratio (equal amounts of acid and conjugate base)
  - Note: Q5 trap — the stem asked for [acid]/[base], not [base]/[acid]. Always identify which species is in the numerator before computing. pH 7.1 with pKₐ 6.1 → 1 unit above pKₐ → 10× more base → [acid]:[base] = 1:10.

- **Buffer effectiveness**
  - a buffer works best when pH is **within ±1 unit of pKₐ**
  - maximum buffering capacity **at pH = pKₐ** (1:1 ratio, resists pH change in both directions)
  - Note: this is the center of the flat plateau on a titration curve.

- **Polyprotic acids and titration curves**
  - a polyprotic acid (e.g., H₃PO₄) has **one buffering region per proton**
  - each flat plateau on the titration curve is centered at that proton's pKₐ
  - **match the compartment's pH to the nearest plateau → pick the active dissociation**
  - H₃PO₄ has three protons → three plateaus → three pKₐ's (~2, ~7, ~12)
    - plateau 1 (pH ≈ 2): H₃PO₄ ⇌ H₂PO₄⁻ + H⁺ → Kₐ = [H₂PO₄⁻][H⁺]/[H₃PO₄]
    - plateau 2 (pH ≈ 7): H₂PO₄⁻ ⇌ HPO₄²⁻ + H⁺ → Kₐ = [HPO₄²⁻][H⁺]/[H₂PO₄⁻] ← **cytosol**
    - plateau 3 (pH ≈ 12): HPO₄²⁻ ⇌ PO₄³⁻ + H⁺ → Kₐ = [PO₄³⁻][H⁺]/[HPO₄²⁻]
  - Note: Q9 trap — cytosol is ~pH 7 → second plateau → second dissociation. Trap answer D was the first dissociation (pH ≈ 2), way too acidic for cytosol.
  - Note: Kₐ expressions are always **products over reactants**. Inverting gives Kₐ⁻¹ (wrong).

- **Bicarbonate buffer (blood, the MCAT's favorite buffer)**
  - CO₂ + H₂O ⇌ HCO₃⁻ + H⁺ · pKₐ = 6.1
  - blood pH ≈ 7.4, so HCO₃⁻ >> H₂CO₃ (more base by ~20×)
  - acidosis (↑H⁺) → shifts left → CO₂ exhaled to compensate
  - alkalosis (↓H⁺) → shifts right → retains CO₂ / kidneys excrete HCO₃⁻
