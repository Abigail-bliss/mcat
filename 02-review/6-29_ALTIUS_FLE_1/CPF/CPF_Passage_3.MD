# Chemical and Physical Foundations of Biological Systems (CP) Section

## Passage 3 (Questions 13–16)

The size, weight, and charge life of the batteries used in implanted medical devices are limiting factors in device implementation. Researchers investigated the use of solar cells implanted below the skin as an alternative power source.

One experimental solar cell is a system of ZnO nanowires coated with dye molecules, as shown in Figure 1. The nanowires are finger-like structures with a diameter of approximately 100 nm. The dye molecules act roughly as would the leaves of a tree, absorbing light. Excited electrons pass from the dye molecules into the nanowires. The electrical circuit is completed as electrons pass from the nanowires to a F:SnO₂ electrode (bottom of Figure 1), through a wire to the load, from the load to a Pt:F:SnO₂ electrode, and through a liquid electrolyte back to the nanowires. The two electrodes are separated by 20 µm and have a typical area of 0.5 cm².

**Figure 1** — Schematic of the nanowire-based solar cell. From top to bottom: **Pt/F:SnO₂/glass** electrode (top), liquid electrolyte, ZnO nanowires with absorbed dye monolayer, **F:SnO₂/glass** electrode (bottom). Light enters from the bottom; a Load is wired between the two electrodes. Electrons flow nanowires → bottom (F:SnO₂) electrode → wire → Load → top (Pt/F:SnO₂) electrode → electrolyte → back to nanowires.

Researchers measured the current density (current per electrode area) as a function of operating voltage. The results are shown in Figure 2. By convention, normal operating current is considered to be negative. In order to function as a solar cell, a voltage must be chosen that results in a negative current.

**Figure 2** — Current density (mA/cm²) vs. voltage (V), for "100 mW/cm² visible light" and "dark." Under light, current density is negative (≈ −1.5 mA/cm²) at 0 V, crosses zero near ≈ 0.7 V, and rises steeply positive beyond ≈ 0.8 V. The dark curve stays near zero until it rises sharply past ≈ 0.8 V.

The efficiency of the device at various wavelengths was determined using two measures: the Incident Photon-to-electron Conversion Efficiency (IPCE) and the Light Harvesting Efficiency (LHE).

**Figure 3** — Solar cell efficiency (LHE and IPCE, %) vs. wavelength (nm). Both curves peak near **≈ 530 nm** (LHE peak ≈ 9%, IPCE somewhat lower) and fall off toward 400 nm and 700 nm.

*Adapted from Jason B. Baxter and Eray S. Aydil, Nanowire-based dye-sensitized solar cells, Applied Physics Letters 86, 053114 (2005). © 2005, AIP Publishing LLC.*

---

## Questions

### Question 13 ✗ (missed)

When illuminated, the solar cell is analogous to a battery. In this context, which portion of the solar cell acts as the positive terminal?

- *Subtopic 542 — Current I = ΔQ/Δt, sign conventions, units · Topic 159 — Circuit Elements · SIR 2: Scientific Reasoning and Problem Solving · Discipline 6: Physics*

- **A. Pt/F:SnO₂ electrode ✓ (correct)**
- B. F:SnO₂ electrode — **✗ (her answer)**
- C. Both electrodes
- D. Nanowires

**Solution:** Electrons leave the bottom electrode and flow upward through the load. Because electrons carry negative charge, conventional **current** (opposite to electron flow) flows *downward* through the load. Current is "pushed out of" the positive terminal of a battery, so the **top** electrode, Pt:F:SnO₂, is the positive terminal (Choice A). D is tempting because electrons do leave the nanowires like an electrode, but the passage explicitly defines the two electrodes — the nanowires are not one of them. **Her trap (B):** the F:SnO₂ (bottom) electrode is where electrons *enter* the load — that's the negative terminal, not the positive. *Draw the electron-flow loop, then flip the arrow to get conventional current.*

### Question 14 ✗ (missed)

If the solar cell is illuminated by monochromatic light in the visible spectrum, which color would produce the most electrical energy per photon?

- *Subtopic 585 — Classification of electromagnetic spectrum, photon energy E = hf · Topic 164 — Light, Electromagnetic Radiation · SIR 2: Scientific Reasoning and Problem Solving · Discipline 6: Physics*

- A. Red — **✗ (her answer)**
- **B. Green ✓ (correct)**
- C. Violet
- D. Ultraviolet

**Solution:** The question asks which color is most *efficient* — read from the efficiency plot (Figure 3), whose peak is ≈ 530 nm. D (ultraviolet) is outside the visible spectrum required by the stem. The visible range is ≈ 390–700 nm (390 = violet, 700 = red); the ≈ 530 nm peak sits in the middle → **green (Choice B).** **Her trap (A, Red):** this question is about the *efficiency curve*, not photon energy — don't answer it with "E = hf ⇒ shortest wavelength." Red (≈ 700 nm) is at the low-efficiency edge of Figure 3. *Note this is the mirror image of Q16 — here the graph governs, there the E = hf physics governs. Read what the stem actually asks: "most electrical energy produced by the cell" (efficiency) vs. "most energy per photon" (E = hf).*

### Question 15 ✗ (missed)

The two parallel plate electrodes give the solar cell an inherent capacitance. If the distance between the plates in Figure 1 were increased from 20 µm to 40 µm, the capacitance would:

- *Subtopic 550 — Capacitance: capacitors in parallel · Topic 159 — Circuit Elements · SIR 2: Scientific Reasoning and Problem Solving · Discipline 6: Physics*

- A. increase by a factor of 2.
- B. increase by a factor of 4.
- **C. decrease by a factor of 2. ✓ (correct)**
- D. decrease by a factor of 4. — **✗ (her answer)**

**Solution:** Parallel-plate capacitance C = ε₀A/d. Capacitance is inversely proportional to plate separation d. Doubling d (20 → 40 µm) halves C → **decrease by a factor of 2 (Choice C).** **Her trap (D):** factor-of-4 would apply if the relationship were inverse-square (like Coulomb's law or gravitation), but C ∝ 1/d is inverse-*linear*. *Write the formula and check the exponent on the variable that changed before choosing 2× vs. 4×.*

### Question 16 ✗ (missed)

Figure 3 compares solar cell efficiency for light of various wavelengths. For four wavelengths, 400 nm, 525 nm, 700 nm, and 820 nm, which wavelength contains photons with the most energy?

- *Subtopic 1109 — Resistance: General · Topic 159 — Circuit Elements · SIR 2: Scientific Reasoning and Problem Solving · Discipline 6: Physics*

- **A. 400 nm ✓ (correct)**
- B. 525 nm — **✗ (her answer)**
- C. 700 nm
- D. 820 nm

**Solution:** Photon energy E = hf, and via v = fλ frequency and wavelength are inversely related (all light travels at c). So shorter wavelength ⇒ higher frequency ⇒ higher energy per photon. The shortest wavelength given is **400 nm (Choice A).** B, C, D are all longer (lower-energy) wavelengths. **Her trap (B, 525 nm):** that's the *efficiency* peak from Figure 3 — but this stem asks for energy *per photon*, which is pure E = hf, independent of the cell's efficiency curve. *Contrast directly with Q14: same figure in play, opposite governing idea. "Per photon" = E = hf (shortest λ). "Most electrical energy from the cell" = efficiency graph (peak λ).*

---

## Terms & Notes

_Add `{...}` marks in the passage/questions above, then ask to "define the marks." First-pass definitions land here; concept-level gaps get promoted to a Flash Sheet at end-of-review._

## Flashcards to Make

_Running list for this passage — cards get generated at the end of review (don't make them yet)._

- [ ] _(candidate) **Conventional current vs. electron flow** — current flows opposite to electrons; it exits the + terminal. Map electron loop, then reverse. (From Q13.)_
- [ ] _(candidate) **Parallel-plate capacitance** — C = ε₀A/d, so C ∝ 1/d (inverse-linear, not inverse-square): double d ⇒ half C. (From Q15.)_
- [ ] _(candidate) **"Per photon energy" vs. "cell efficiency"** — E = hf ⇒ shortest λ = most energetic photon (Q16); efficiency = read the peak off the graph (Q14). Same figure, opposite question — read the stem._
