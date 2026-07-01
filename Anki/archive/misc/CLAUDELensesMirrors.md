# CLAUDE.md — Mirror & Lens Ray Diagram Explorer

## Project goal

Build a single self-contained HTML file (`lens-mirror-explorer.html`) that lets the user explore ray diagrams for thin mirrors and lenses interactively. Sidebar with controls, main canvas with the diagram, metric cards showing computed values, insight text at the bottom.

**Style/layout reference:** `wave-explorer.html` (DM Sans / DM Mono, light surface, sidebar 290px, blue/green/orange accents).

**Scope:** MCAT-level optics. Thin mirrors and lenses only. No aberrations, no compound systems, no off-axis objects.

---

## User controls (sidebar)

- **Optic type** (toggle): Mirror | Lens
- **Shape** (toggle): Concave | Convex
- **Focal length |f|** (slider): 5 to 50 cm, step 1
- **Object distance dₒ** (slider): 5 to 100 cm, step 1
- **Object height h** (slider): 1 to 10 cm, step 0.5 (controls visual magnification clarity)

The slider shows the **magnitude** of f. The sign is determined by the shape toggle:

```
mirror + concave  → f > 0
mirror + convex   → f < 0
lens   + convex   → f > 0   (convex lens converges)
lens   + concave  → f < 0   (concave lens diverges)
```

⚠️ The lens convention flips: a **convex lens is converging** (+f); a **concave lens is diverging** (−f). Label the toggle as "Convex (converging)" / "Concave (diverging)" when in lens mode to prevent confusion.

---

## Computed displays (metric cards, top bar)

- **dᵢ** — image distance, signed, with annotation ("in front of mirror" / "behind mirror" / "opposite side of lens" / "same side as object")
- **m** — magnification, signed
- **Type** — real / virtual
- **Orientation** — upright / inverted
- **Size** — magnified / diminished / same size
- **R** — radius of curvature, computed: `R = 2·|f|` for mirrors, `R = 2·f·(n−1)` for lenses with `n = 1.5` fixed

---

## Core math — ONE equation, four cases

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

### Sign convention (used everywhere)

| Quantity | Sign | Meaning |
|---|---|---|
| f > 0 | concave mirror / convex (converging) lens |
| f < 0 | convex mirror / concave (diverging) lens |
| dₒ > 0 | real object, in front of optic (always, for this project) |
| dᵢ > 0 | real image, in front of mirror / far side of lens |
| dᵢ < 0 | virtual image, behind mirror / same side of lens as object |
| m = −dᵢ/dₒ | m > 0 upright, m < 0 inverted, \|m\| > 1 magnified |

### One math engine, no branches

The same equation works for all four cases. The only branch in the entire math layer is the sign of `f`. Do NOT special-case concave vs convex or mirror vs lens in the math — only in the **rendering** (where the post-interaction rays live: x ≤ 0 for mirrors, x ≥ 0 for lenses).

---

## Coordinate system

- Origin at the vertex of the mirror/lens
- +x to the right, +y up (physics convention)
- Object always on the LEFT at x = −dₒ, tip at (−dₒ, h)
- F (primary focal point) at (−|f|, 0) for converging cases; for diverging cases f<0 and F at (+|f|, 0) is the virtual focal point
- C (mirrors only) at (−2|f|, 0)
- Render in physics coords everywhere. ONE function flips y at draw time:

```js
function toCanvas(x, y) {
  return [originPx + x * scale, midY - y * scale];
}
```

Never mix coords. If you find yourself flipping y outside `toCanvas`, stop and fix it.

---

## The three principal rays — closed-form equations

Object tip at (−dₒ, h). These formulas were derived and validated by hand; trust them.

### Ray 1 — Parallel ray
- **Pre:** horizontal from (−dₒ, h) to (0, h)
- **Post (mirror):** `y = h + (h/f) · x` for x ≤ 0
- **Post (lens):**   `y = h − (h/f) · x` for x ≥ 0

### Ray 2 — Central ray (through vertex / lens center)
- **Pre:** straight line from (−dₒ, h) to (0, 0)
- **Post (mirror):** `y = (h/dₒ) · x` for x ≤ 0 (reflects symmetrically about axis)
- **Post (lens):**   continues straight, `y = −(h/dₒ) · x` for x ≥ 0

### Ray 3 — Focal ray
- **Pre (mirror, concave, dₒ > f):** from (−dₒ, h) through F at (−f, 0), hits mirror at height `h_hit = −h·f / (dₒ − f)`
- **Post:** horizontal at y = h_hit, going back leftward (mirror) or forward rightward (lens)
- **Edge case:** when `dₒ ≈ f`, the line is nearly vertical and breaks. Detect and skip Ray 3 in that case (or use Ray 1 reversed as an alternative).
- **For convex mirrors / diverging lenses:** Ray 3 is geometrically awkward. Acceptable to draw only Rays 1 and 2 for those cases.

### Virtual extensions (dashed)
When dᵢ < 0 (virtual image), the rays diverge after interaction and never meet on the working side. Extend each post-interaction ray **backward** as a dashed line until they meet at the virtual image location (on the opposite side of the optic from where rays normally converge).

---

## Phased build plan — DO NOT SKIP PHASES

Each phase must produce something that works end-to-end before the next phase starts. The whole point of phasing is to never have a half-broken state.

### Phase 1 — Math engine only (no UI, no rendering)

Build:
```js
computeImage({type, shape, fMag, do_, h}) → {
  f,            // signed
  di,           // signed
  m,            // signed
  hi,           // signed
  isReal,       // boolean
  isInverted,   // boolean
  isMagnified,  // boolean
  atInfinity,   // boolean — true when |do - |f|| < 0.5
  R             // radius of curvature
}
```

**Test cases — must ALL pass before Phase 2:**

| type | shape | f (signed) | dₒ | expected dᵢ | expected m |
|---|---|---|---|---|---|
| mirror | concave | +10 | 30 | +15    | −0.50 |
| mirror | concave | +10 | 20 | +20    | −1.00 |
| mirror | concave | +10 | 15 | +30    | −2.00 |
| mirror | concave | +10 | 10 | ∞ (atInfinity) | — |
| mirror | concave | +10 | 5  | −10    | +2.00 |
| mirror | convex  | −10 | 20 | −6.67  | +0.33 |
| lens   | convex  | +10 | 30 | +15    | −0.50 |
| lens   | concave | −10 | 20 | −6.67  | +0.33 |

Run these as console assertions on page load. If any fail, halt with a visible error. Do not proceed to Phase 2 until all pass.

### Phase 2 — Static skeleton render
Render only: principal axis (horizontal line), optic shape, F marker(s), C marker (mirrors only), object arrow. No rays. Verify scale and centering across full slider ranges (try extremes: f=5,dₒ=100 and f=50,dₒ=5).

### Phase 3 — Add Ray 1 only
Implement Ray 1 (parallel) pre + post. Visually verify the post-segment passes through F for concave/converging cases, and that its backward extension passes through F for convex/diverging cases.

### Phase 4 — Add Ray 2 (central)
Both rays must now intersect at (−dᵢ, hᵢ) using the values from `computeImage`. For virtual cases (dᵢ < 0), they meet at the virtual image location on the opposite side — draw dashed backward extensions.

**Sanity assertion:** compute the actual intersection point of Ray 1 and Ray 2 analytically and assert it equals (−dᵢ, hᵢ) within 0.01. If it doesn't, math is wrong somewhere.

### Phase 5 — Add Ray 3 (focal)
All three rays must converge at the same point. Add a debug assertion. Handle the dₒ ≈ f edge case by skipping Ray 3 cleanly.

### Phase 6 — Image arrow + virtual extensions
Real images: solid red arrow at (−dᵢ, hᵢ). Virtual images: dashed red arrow at virtual image location, plus dashed backward extensions on each ray.

### Phase 7 — UI: controls + metric cards + insight text
Sidebar with the two toggles and three sliders. Metric cards in the top bar showing computed values. Adaptive insight text at the bottom (e.g., "Object beyond C — image is real, inverted, and diminished, located between F and C").

### Phase 8 — Edge cases
- `|dₒ − |f|| < 0.5` → overlay "Image at infinity — reflected/refracted rays parallel"
- `|dᵢ|` exceeds canvas range → clamp visual, show "image far off-screen →" indicator
- Smooth transitions when sliders cross critical thresholds (at f, at 2f for mirrors)

---

## Failure modes to avoid (lessons from past attempts)

1. **Don't special-case in the math layer.** Concave vs convex is just `sign(f)`. Mirror vs lens is which side of x=0 the post-rays live on. That's it.
2. **Rays are STRAIGHT LINE SEGMENTS.** Two endpoints, one line. No Béziers, no curves. If your code has curve drawing for rays, delete it.
3. **Don't build UI before math passes.** If Phase 1 assertions fail, fix the math. Do not move on.
4. **One y-flip only.** `toCanvas()` is the only place y is flipped. If you flip y elsewhere you will spend two hours debugging it.
5. **Debug panel always on.** A small corner panel showing computed `f, dᵢ, m, hᵢ` lets you immediately tell whether a visual bug is in the math or the rendering.
6. **Don't try to render everything at once.** Phases 3, 4, 5 each add ONE ray. Verify each ray independently before adding the next.

---

## File output

Single self-contained `lens-mirror-explorer.html`. All CSS and JS inline. Only external dependencies: Google Fonts (DM Sans, DM Mono).

## Visual style (match wave-explorer.html exactly)

- Background `#f5f6f8`, surface `#ffffff`, text `#1a1d24`, muted `#7a8094`
- Accent blue `#2372d4` (primary), green `#0f9e6a` (secondary), orange `#d45f10` (curvature/warnings)
- Object: blue `#2372d4`
- Image (real): red `#c0392b` solid
- Image (virtual): red `#c0392b` dashed, 0.6 opacity
- Rays: three distinct colors — Ray 1 orange `#d45f10`, Ray 2 teal `#0f9e6a`, Ray 3 purple `#7F77DD`
- Virtual extensions: dashed (5,3), 0.5 opacity
- Same header / sidebar / metric card / insight bar structure as wave-explorer

## Workflow notes for the developer (you, Claude Code)

- Build in one HTML file, but DEVELOP it in phases. After Phase 1, open the file in the browser and check the console — assertions should all pass before you start drawing anything.
- After each phase, the file should still render correctly. Don't leave broken intermediate states.
- If a ray looks visually wrong, FIRST check the math layer (does `computeImage` give correct values?). If math is right, the bug is in `toCanvas` or in the ray equation implementation.
- When in doubt, log physics coords to the console and verify by hand before rendering.
