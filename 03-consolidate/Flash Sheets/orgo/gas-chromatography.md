# [CLUE] Gas Chromatography (GC/GLC — retention time, temperature, stationary phase polarity)
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 CPF Q17, Q18, Q20 — Orgo/lab-techniques weakness, 3 misses.)

- **How GC works**
  - sample is injected, vaporized, swept through a column by an **inert carrier gas** (mobile phase)
  - column interior is coated with a **liquid stationary phase**
  - compounds constantly partition between gas phase and liquid phase
  - **more volatile** = stays in gas phase → exits column faster
  - **less volatile** = lingers in liquid phase → exits column later
  - detector records concentration over time → chromatogram peaks

- **Retention time (tᵣ) — the fundamental rule**
  - **longer retention time = higher boiling point** (less volatile, sticks to stationary phase longer)
  - use this to read any GC table: highest tᵣ = highest boiling point
  - Note: Q17 trap — scan ALL options' tᵣ values first, then pick the max. Trap answer had a shorter tᵣ than the correct one.

- **Effect of temperature on the run**
  - **lower temperature** → everything is slowed down in the column
    - **longer retention time** for all peaks
    - **better (increased) resolution** between peaks — the baseline between peaks stretches out
  - **higher temperature** → faster run, shorter retention, peaks crowd together (worse resolution)
  - Note: Q18 trap: "longer retention" sounds like it would smear peaks together, but the opposite is true — slow = more separation time = better resolution. Think of it as giving each compound more time to separate from its neighbor.

- **Effect of stationary phase polarity**
  - with a **polar stationary phase** (and inert gas mobile phase):
    - **polar analytes interact more strongly** with the stationary phase → longer retention
    - **nonpolar analytes** interact weakly → elute faster
  - Note: "like dissolves like" — polar stationary phase holds polar analytes.
  - Note: Q20 trap: "decreased polarity = longer retention" was wrong. More polar compound = more attracted to polar stationary phase = stays longer.

- **Cis vs. trans isomers and boiling point (Q17 geometry subtlety)**
  - **trans isomers** pack more linearly → closer intermolecular contact → stronger forces → **higher boiling point** → longer tᵣ
  - **cis isomers** are bent/compact → can't stack as tightly → lower boiling point → shorter tᵣ
  - Note: even without knowing the geometry, read tᵣ off the table and you're done.
  - Real-world analogy: trans fats are solid at room temp (pack well), cis fats are liquid (can't pack).

- **GC vs. column chromatography (key distinctions)**
  - GC = **gas** mobile phase, **liquid** stationary phase; separates by **volatility/boiling point**
  - column chromatography (HPLC etc.) = liquid mobile phase; separates by polarity/affinity
