# [CLUE] Enzyme Kinetics & Inhibition
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 Q28 + WizePrep slides — biochem weakness, missed.)

- **Michaelis–Menten**
  - equation: **V = Vmax·[S] / (KM + [S])**
  - **Vmax** = max rate, reached when enzyme is saturated with substrate
  - **KM** = the [S] at which V = ½·Vmax
    - Note: KM is an **affinity proxy** — *low* KM = *high* affinity (saturates at low [S])
  - curve = hyperbola: rises steeply, then plateaus at Vmax

- **Lineweaver–Burke** (double-reciprocal — straightens the hyperbola into a line)
  - equation: **1/V = (KM/Vmax)·(1/[S]) + 1/Vmax**
  - **y-intercept = 1/Vmax**
  - **x-intercept = −1/KM**
  - **slope = KM/Vmax**
  - Note: read a L-B plot by what moves — y-int up = Vmax down; x-int position tells KM

- **Inhibitor types** — memorize what happens to **KM** and **Vmax**
  - **Competitive** — binds the active site; competes with substrate
    - KM ↑ (looks like lower affinity) · Vmax **same**
    - overcome-able by ↑[S]
    - Note: a **structural analogue** of the substrate = competitive (default pattern to reach for)
  - **Noncompetitive** — binds an allosteric site on E or E–S equally
    - KM **same** · Vmax ↓
    - NOT overcome-able by ↑[S]
  - **Uncompetitive** — binds **only the E–S complex**
    - KM ↓ · Vmax ↓ (both drop)
    - Note: locks substrate in, so apparent affinity rises (KM down)
  - **Mixed** — binds E and E–S with different affinities
    - KM ↑ or ↓ · Vmax ↓

- **Quick recall table**
  - Competitive: KM↑, Vmax—
  - Noncompetitive: KM—, Vmax↓
  - Uncompetitive: KM↓, Vmax↓
  - Mixed: KM↕, Vmax↓

- **Lineweaver–Burke signatures per inhibitor type** (from CPF Q43 miss)
  - **Competitive** — same y-intercept (Vmax same), x-intercept shifts RIGHT (KM↑), slope↑
  - **Noncompetitive** — same x-intercept (KM same), y-intercept shifts UP (Vmax↓), slope↑
  - **Uncompetitive** — **parallel lines** (slope same), both y-intercept UP and x-intercept shifts (both KM and Vmax drop proportionally)
  - **Mixed** — lines intersect left of the y-axis (both intercepts change, slope changes)
  - Note: to ID inhibitor from an L-B plot: find what DOESN'T move. Same y-int = competitive. Same x-int = noncompetitive. Parallel = uncompetitive.
  - Note: Vmax↓ always shows as y-intercept moving UP on an L-B plot (y-axis = 1/V, so higher = smaller Vmax).

- **Cooperativity** (multi-subunit enzymes — binding of one substrate changes affinity for the next)
  - **Positive** — 1st binding **↑** affinity for the next → **sigmoidal** V vs. [S] curve
    - Note: classic example = **hemoglobin** (O₂ binding makes the next O₂ bind easier)
  - **Negative** — 1st binding **↓** affinity for the next
  - **None (standard Michaelis–Menten)** — **hyperbolic** curve
  - **Hill coefficient (n)**: **n > 1 = positive** · **n < 1 = negative** · **n = 1 = standard MM**
  - Note: a **sigmoidal V vs. [S] curve = cooperativity** on the MCAT (contrast the MM hyperbola)
