# [CLUE] Hydrostatic Pressure (P = P_atm + ρgh, why a *difference* is just ρgh, and how the units make a Pascal)
> Cover everything below and lecture it from memory.
> (From Altius FLE 1 CPF Q10 — blood pressure feet vs. head. Missed: multiplication/units slip, answered 2000 Pa instead of 18000. Physics.)

- **Core idea:** pressure in a static fluid **increases with depth**. At any depth `h` below the surface:
  - **P = P_atm + ρgh**
    - `P_atm` = pressure pushing down on the top of the fluid (atmosphere).
    - `ρ` (rho) = fluid **density** (kg/m³).
    - `g` = gravity (9.8 m/s², or **10** for fast estimating).
    - `h` = **vertical depth** below the surface (m) — straight down, not along a tube.
  - Note: the `ρgh` term is the weight of the fluid column above you, spread over area. Deeper column → more weight → more pressure.

- **The key move: a pressure *difference* is JUST ρgh** (this is the whole trick of the question)
  - Between two points in the same fluid, the `P_atm` is the **same at both**, so it **cancels**:
    - ΔP = (P_atm + ρgh_bottom) − (P_atm + ρgh_top) = **ρg·Δh**
  - So when a question asks "how much does pressure **differ** between two heights," ignore atmosphere entirely — **just compute ρg·Δh** using the height *difference*.
  - Note: the trap is overthinking it. Don't hunt for P_atm or absolute pressures. Write **ΔP = ρgh**, plug the three numbers, estimate.

- **Worked example (the miss):** feet vs. head of a 1.70 m person, blood ρ = 1060 kg/m³
  - ΔP = ρgh = 1060 × 9.8 × 1.70 = **17,660 Pa ≈ 18,000 Pa**
  - Estimate version: 1000 × 10 × 1.7 = 17,000 Pa → still points at 18,000. 
  - Note: her wrong answer (2,000 Pa) came from a plug/multiply slip. Fix = **write P = ρgh, list the 3 given numbers, multiply/estimate — don't eyeball.**

- **What a Pascal actually is** (so the units aren't magic)
  - **Pressure = force / area**, so **1 Pa = 1 N/m²** (one newton spread over one square meter).
  - Note: a Pascal is small — atmospheric pressure ≈ 101,000 Pa (~101 kPa). So a ~18,000 Pa head-to-foot difference is real but sub-atmospheric.

- **How ρ·g·h gives you Pascals** (unit-cancellation, do this to sanity-check any answer)
  - ρ·g·h = (kg/m³) × (m/s²) × (m)
    - kg/m³ × m/s² × m = **kg·m⁻¹·s⁻²**
    - and kg·m⁻¹·s⁻² = (kg·m/s²)/m² = **N/m² = Pa** ✓ (since force N = kg·m/s²)
  - Note: if your units don't collapse to N/m², you plugged something wrong (e.g. used cm for h, or g/cm³ for ρ). Units are the free error-check.

- **Gotchas**
  - `h` is **vertical** depth only — a slanted or coiled tube uses the height difference, not the tube length.
  - Cross-sectional **area and shape don't matter** (hydrostatic paradox) — a thin straw and a wide lake at the same depth have the same pressure.
  - Keep SI: ρ in kg/m³, h in m. Mixing units is the #1 way to land on a wrong multiple.
  - Note: neighbor concepts — buoyancy (F_b = ρgV) and Pascal's law both build on this same ρg·h idea (future sheets).
