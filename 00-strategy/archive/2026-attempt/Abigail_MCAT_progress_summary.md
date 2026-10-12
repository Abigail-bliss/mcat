# Abigail — MCAT Progress Summary

*Compiled 2026-06-28 from all stored memory, the study-plan documents, the AnKing-unsuspend progress log, and the project directives. This is the full picture — everything currently on record.*

---

## 1. Who Abigail Is

- **Email:** abbydbliss@gmail.com
- **Profession:** Software engineer (works full-time, WFH during Phase 1).
- **Cognitive profile:** Exceptional. IQ 123, a fast and strong memorizer. Picks things up quickly.
- **Has ADHD** — passive lecture-watching is a known failure mode (gets distracted, disengages). Needs *active* tasks tied to every input to stay focused.
- **Self-styled target is aggressive** — aiming well above her diagnostic, banking on raw ability + a disciplined system.

### Learning preferences & working style (confirmed)
- **Anki, white background / dark text only.** Dislikes night mode. Cards should be styled for a light background — no dark-mode handling, no white-container wrappers behind images.
- **Beginner at organic chemistry** — never taken it. Doesn't yet know foundational classifications (e.g. didn't know benzene is aromatic). Orgo cards must *teach from the ground up*, name the functional group/class explicitly, prefer name→structure (learning) over structure→name (drilling) while on basics.
- **Sometimes wants one dense, long card on purpose** (esp. Biochem) to train recall of larger multi-part chunks — not always atomic one-fact cards. Offer the split, but build the combined card without pushing back when she asks.
- **Keeps an error/miss log in a Google Sheet** (`00-strategy/data/Error Log.xlsx`, "Error Log" sheet). That log owns the *"why I missed it"* — Anki tags are kept lean and never duplicate that reasoning.

---

## 2. The Exam

- **Test date: 2026-09-03** (Thursday).
- **As of this summary (2026-06-28): ~67 days out.** (Plan was written 2026-06-20 at ~75 days out.)
- **Target score: 520.** Aggressive. At 520, almost nothing in the sciences is skippable.

### Score history
| Date | Test | Maker | Composite | C/P · CARS · B/B · P/S |
|------|------|-------|-----------|------------------------|
| 2026-05-16 | Diagnostic | **AAMC** FL1 | **496** (36%) | 123 · 128 · 121 · 124 |
| 2026-06-28 | FL #2 | **Altius** FLE1 | **496** (~35%) | 122 · 126 · 123 · 125 |

The two 496s are **not a plateau**: different makers (AAMC vs. harder/noisier Altius), only partway through content, and near-zero review done yet. B/B even rose 121→123 where content was added. The score-moving engine (review) hasn't been switched on — see the strategy pivot below and `progress/progress-log.md`.

### Knowledge map (strengths → weaknesses)
| Area | Status |
|------|--------|
| **CARS** | **Strong — 90th percentile.** A protected asset; maintenance only, do not over-invest. |
| **Gen Chem** | Solid. |
| **Psych/Soc** | Familiar (took it years ago). |
| **Physics** | Partial — took it long ago, needs reinforcement. |
| **Bio** | New/weak — priority sink. |
| **Biochem** | New/weak — priority sink. |
| **Organic Chemistry** | **New/weak — #1 weakness.** Never taken. |

**Weakness-first priority order:** Orgo + Biochem → Bio → Physics → Gen Chem → Psych/Soc.

### Error log insight (2026-06-20 snapshot)
- 98 total misses; 97 of them C/P.
- **Orgo = 32 misses → her single biggest weakness** (validates weakness-first).
- 69 of the misses were knowledge gaps; 82 were still "not done" (unaddressed) at that time.
- Read the log via `uv run --python 3.13 --with openpyxl`.

---

## 3. The Core Diagnosis (what was failing, and the fix)

**The trap:** Her old loop was passive lecture (distracted, ADHD) → quiz (~50%) → *make Anki cards she then never reviewed* → nothing encoded. **Card-MAKING was the problem** — it's production, not retrieval. She spent enormous time hand-building physics/chem/biochem decks and barely reviewed them. SRS value comes from *reviews*, not card creation, so custom-deck building was net-negative ROI.

**The fix (decided 2026-06-20):** Active retrieval is how she both learns and reviews, from the very first pass.
- The premade **AnKing MCAT Deck** becomes the **daily-review backbone**.
- **UWorld** becomes the daily learn-by-questions engine.
- **Custom card-making stops** — reserved only for genuine misses and true gaps AnKing doesn't cover.

**ADHD lecture fix:** Reframe the first content pass as *exposure, not memorization* (kills the "why pay attention" doom loop). Watch lectures at 1.25–1.5× with an immediate active task (do the quiz right after). Full lectures only for Bio/Biochem/Orgo; skim/skip Gen Chem & Psych/Soc to reclaim time for questions.

---

## 4. Timeline & Two-Phase Plan

### Phase 1 — now → ~Aug 1 (working full-time, WFH)
- WizePrep course finishes end of July (4 lectures/weekend, ~3h each).
- **Goal:** finish first pass on ALL content, start the SRS clock, build the daily-questions habit. **Exposure, not mastery.**
- AnKing: ~50 new/day (already the deck's limit / AnkiHub preset).
- C/P kept warm via UWorld even though AnKing C/P isn't formally introduced yet.

### Phase 2 — Aug 1 → Sept 3 (5 weeks PTO, full-time study, ~8–10 hr/day)
- The real engine where 496 → 520 happens.
- Heavy UWorld → AAMC, full-lengths ~2/week each with a full review day, missed-question review as the primary content review, AnKing maturing.
- Ramp AnKing new/day from 50 → ~100–120 (via deck config) at PTO start.
- **Hard stop on NEW AnKing cards ~Aug 20** (~2 weeks out) → pure review + practice after.
- Final ~10 days: AAMC-only, light review, **protect sleep**, taper volume.

---

## 5. Resources On Hand

- **UWorld** — daily learning-by-questions engine *now*. Tutor/untimed, by covered topic; every miss → her log. This *is* her content review.
- **Full AAMC bundle** (FLs + question packs + sample) — saved for the **final ~3 weeks** (most predictive). End on AAMC.
- **10 Altius full-lengths** — used in Phase 1 / early Phase 2.
- **WizePrep** course (quizzes + reviews) — drives her content *sequence*.
- **AnKing MCAT Deck** — premade, vetted, ~2,500 content notes (~6,400 cards); the review backbone.

### Full-length cadence
- FLs are diagnostic tools, not boxes to tick — **worthless before B/B content exists.** Do **not** chase WizePrep's FL schedule.
- Phase 1: ~1 around mid-July if caught up (Altius), else none → first FL = Aug 1 baseline.
- Phase 2: ~2/week, each followed by a full review day. **Altius first; save all AAMC FLs + sample for the final ~3 weeks. End on AAMC.**
- Every FL: review *every* miss — including lucky-right answers — into the log. The review is the point.

---

## 6. Current Progress (as of last update, 2026-06-20/21)

### AnKing unsuspend status
- **Step 0 (2026-06-20):** bulk-suspended all 6,342 unseen AnKing cards (`is:new -is:suspended`). 93 already-studied cards left untouched. New/day already = 50 (AnkiHub preset).
- **Batch 1 (2026-06-20):** unsuspended **884 cards** — all Orgo (`OChem::*`) + BBF I Ch1 Biochem (amino acids, proteins, lipids, carbohydrates, enzymes, nucleic acids). Weakness-first.
- **5,458 cards still suspended**, awaiting WizePrep coverage.

### WizePrep coverage checklist (mirrors her content sequence)
**CPF I & II (Chem/Phys) — all pending EXCEPT:**
- ✅ CPF II Ch5 — Organic Chemistry intro *(via OChem unsuspend 6/20)*
- ✅ CPF II Ch6 — Aldehydes, Ketones, Alcohols *(via OChem unsuspend 6/20)*
- 🔶 CPF II Ch7 — Carboxylic Acids, Derivatives, Macromolecules *(OChem cards done; biochem macromolecule overlap pending)*
- ⬜ Everything else: CPF I Ch1–8 (motion, atomic world, waves, optics, reactions/bonds, E&M, acids/bases/equilibrium, kinetics/thermo) and CPF II Ch1–4 (work & energy, solutions/electrochem, gases/KMT, fluids).

**BBF I & II (Bio/Biochem):**
- ✅ BBF I Ch1 — Biomolecules *(unsuspended 6/20)* ← **her current position as of 2026-06-20**
- ⬜ BBF I Ch2–6 (cells, central dogma, cell division/genetics, energy metabolism, molecular techniques)
- ⬜ BBF II Ch1–5 (neuro, endocrine, respiration/circulation, digestion/excretion, muscles/bones/skin/immunity)

**Cross-cutting (pending):** IFD High-Yield set (47 cards, suggested first slice), Essential-Equations subdeck (95 cards).

**Psych/Soc:** no WizePrep P/S reference exists yet — sequence TBD (fall back to AnKing's Behavioral order when reached).

### Catch-up status (2026-06-20)
- **Behind on BBF I lectures 1.2–1.4** (1.5 was assigned next).
- **2 full-lengths behind** (but FLs intentionally deferred — see above).
- **~82 misses to clear.**
- Plan: catch lectures (1/weeknight at 1.5×) + ~15 misses/day (Orgo + knowledge-gap first) + daily AnKing. No FL that week.

> ⚠️ This progress snapshot is ~8 days old (as of 2026-06-28). Confirm her current WizePrep chapter and miss-backlog count before acting on it.

---

## 7. AnKing Deck Structure (mapped 2026-06-20)

Slices **cleanly by subject (subdeck), messily by topic (tags).**

### Subdecks — the reliable subject axis (`AnKing MCAT Deck::…`)
| Subdeck | Cards | WizePrep home |
|---|---|---|
| `Physics-and-Math` | 328 | CPF I & II physics |
| `General-Chemistry` | 290 | CPF I & II gen chem |
| `Organic-Chemistry` | 306 | CPF II Ch 5–7 |
| `Biochemistry` | 541 | BBF I |
| `Biology` | 695 | BBF I & II |
| `Behavioral` | 1,584 | Psych/Soc |
| `Essential-Equations` | 95 | C/P equation drilling |

### Tags — two parallel layers
1. **Source layer** `#AK_MCAT_v2::<source>::…` — by origin (`#UWorld` biggest, `#KhanAcademy`, `#Kaplan`, `#IFD_High_Yield`, `#AAMC`, etc.). UWorld is tagged only by numeric per-card IDs → **useless for topic slicing.**
2. **⭐ Topic layer (PRIMARY axis)** `#AK_MCAT_v2::AK_Original_Decks::MileDown::<Subject>::<Topic>[::<Subtopic>]` — clean fine-grained hierarchy covering **~98% of the deck (6,315 / 6,435 cards)**, subtopics mapping onto WizePrep chapters. Per-chapter unsuspending = a clean union of a few MileDown tags.

MileDown subject branches: Physics 650 · General_Chemistry 539 · OChem 574 · Biochemistry 1,057 · Biology 1,188 · Behavioral 2,437. *(Card counts, not notes — cloze note types generate multiple cards per note.)*

### Unsuspend mechanism
- Per WizePrep chapter, unsuspend the union of matching MileDown topic tags. Keyword-within-subdeck only a fallback for the ~2% untagged.
- Query form: `tag:#AK_MCAT_v2::AK_Original_Decks::MileDown::<Subject>::<Topic>*` (leading `*` so `#` matches, trailing `*` to include subtopics).
- Use `findCards` + `areSuspended` + `unsuspend` (card IDs, not note IDs).
- **Hard rules:** never read AnKing card content (IDs/counts only); preview counts per query + total and wait for approval; respect the daily new-card cap; stay in step with WizePrep; log every batch in `progress.md`.

---

## 8. AnKing Rollout / Throttle Plan

- **AnKing every single day** is the non-negotiable spine — clear all due reviews, take the day's new cards.
- ~50 new/day in Phase 1; ramp to ~100–120 at PTO (~Aug 1) via deck config; hard new-card cutoff ~Aug 20.
- **Weakness-first introduction order:** Orgo + Biochem → Bio → Physics → Gen Chem → Psych/Soc.
- **Physics + Gen Chem unsuspend trigger = CAPACITY, not calendar.** They were already covered in CPF I/II (May/June), so they're not WizePrep-gated — only gated by weakness-first sequencing + the 50/day throttle. Unlock them the moment daily new-card intake would otherwise run out of B/B material (likely **mid-to-late July**). Claude monitors remaining B/B `is:new` supply and pings at ~3 days of runway. **Order: Physics first, Gen Chem last** (strongest, needs least reinforcement).
- **Behavioral / Psych-Soc (2,462 cards):** biggest chunk, her familiar area, not in WizePrep yet → **triage to a high-yield subset, introduce last.**

### Amino-acid structure-ID cards (done 2026-06-21)
The 40 "*This amino acid is ___*" structure-recognition cards were spread ~2/day across 20 days via `setDueDate days="1-20"` so she isn't slammed with all amino-acid structures at once. They surface under "due" (not "new") — expected. The other ~117 amino-acid cards flow normally at 50/day. This was a one-off for structure recognition — **no general "spread every dense topic" rule.**

---

## 9. The Eight Non-Negotiables for 520

1. **AnKing every single day** — all due reviews cleared, no exceptions. The spine.
2. **UWorld daily** (even 15 Q) with every miss reviewed into the log. Practice = content review.
3. **Finish WizePrep first pass on time** — don't fall further behind on lectures.
4. **Weakness-first** — disproportionate time into Bio / Biochem / Orgo (log proves Orgo is #1).
5. **CARS maintenance** — a few passages/week so the 90th-percentile asset doesn't decay. Don't over-invest.
6. **Phase 2: 2 FLs/week + full review days; AAMC saved for the last 3 weeks; end on AAMC.**
7. **Stop new AnKing cards ~Aug 20; protect sleep the final week.**
8. **No more card-MAKING** — premade AnKing review + questions only. Custom cards only for true gaps.

---

## 10. Custom Card-Building System (for the rare genuine gaps/misses)

When custom cards *are* warranted (a real miss or gap AnKing lacks), the established machinery:

- **Decks:** MCAT Physics, MCAT Chemistry, MCAT Math, MCAT Organic Chemistry, MCAT Biochemistry. (MCAT Psych Soc / MCAT CARS to be created when first needed.)
- **Pushed directly to Anki via AnkiConnect** (`localhost:8765`) — never `.txt` import files. Note type "Basic"; HTML fields; LaTeX via `\[...\]` only (never `$$`); always Python raw strings `r"..."`.
- **Tags:** two per card — a type tag (`::definition`/`::equation`/`::concept`/etc.) + a subtopic tag. `math::*` is a cross-deck unifying tag.
- **Misses workflow:** misses are surfaced through a filtered deck "MCAT Question Misses" (search `tag:missed::*`) — never a separate physical deck, never a duplicated card. One fact = one card in its subject deck, tagged. Required missed tags: `missed::src::<source>`, `missed::sec::<cp|bb|ps|cars>`, auto `missed::date::YYYY-MM-DD`, auto `missed::week::YYYY-Www`.
- **Existence checks** are scoped to *her own* decks — **never read AnKing cards** (they aren't hers; IDs/counts only).

### Media-card pipelines
- **Organic skeletal structures:** RDKit from SMILES → stored as Anki media → plain `<img>`. Run under `uv run --python 3.13 --with rdkit --with requests`. Helpers in `orgo_helpers.py`, pattern in `push_orgo_cards.py`.
- **Fischer projections / cyclohexane chairs:** hand-built SVG (RDKit can't do these), verified by rasterizing with `qlmanage -t -s 900 -o . file.svg` then reading the PNG (cairosvg/svglib don't work here). Helpers: `build_stereo_svgs.py`, `build_sugar_svgs.py`, `build_chair_svg.py`.
- **Biochem cards:** screenshots routed into `biochem_images/`, pinned by timestamp substring, stored via `biochem_helpers.py`. Two-way recognition cards use "Basic (and reversed card)". Image-only-front cards must be pushed delete-first + `allowDuplicate` (Anki strips media before the dup check, so same front text collapses to one key).
- **`math::statistics`** is an established subtopic tag (box-and-whisker, central tendency) even though it's not in the original CLAUDE.md enumerated list.

---

## 11. Key File / Project Map

The repo is a numbered pipeline: **`00-strategy` → `01-reference` → `02-review` → `03-consolidate`.**

**00-strategy/** (this journey — strategy, plans, progress, data)
- `Abigail_MCAT_progress_summary.md` — this document (the master summary).
- `study-plan/master-study-plan.md` — the full written schedule (catch-up plan, Phase 1 & 2 weekly templates, FL schedule, the 8 non-negotiables).
- `weekly-plans/` — `phase1-weekly-template.md`, the past catch-up week, and `this-week-plan.html` (printable).
- `progress/progress-log.md` — dated log of scores, decisions, milestones.
- `data/Error Log.xlsx` ("Error Log" sheet) — her miss log; owns the "why."

**01-reference/** (read-mostly source material)
- `WizePrepChaptersReference/` — content sequence reference (CPF I/II + BBF I/II; no Psych/Soc yet).
- `Study Materials/` — reference PDFs. `Accomodations/` — sensitive personal paperwork (leave alone).

**02-review/** (FL dissection / question review)
- Per-exam folders (PDFs + per-passage transcripts + `WizePrep_Dissection_Consolidated.md`), plus `Screenshots/` (transcription inbox). See `02-review/CLAUDE.md`.

**03-consolidate/** (the daily-review pair)
- `Anki/` — `CLAUDE.md` (card-creation directives); `card-creation/` (build/push scripts + helpers, with `biochem_images/` the screenshot destination at the `Anki/` root); `anking-unsuspend/` (the AnKing unsuspend mechanism — its own `CLAUDE.md` + `progress.md` batch log; *unsuspending the right cards in survivable batches*, NOT making cards).
- `Flash Sheets/` — concept-fluency free-recall sheets (`_index.md` spaced-rep tracker).

**Memory store:** `~/.claude/projects/-Users-abigailbliss-Documents-mcat/memory/` (keyed on the repo root, unaffected by the restructure).

---

*One-line mission across everything: **Reviewing >> creating.** Surface premade AnKing content matched to what she's covered, gated so the daily queue never buries her before 2026-09-03 — and pour disproportionate effort into Orgo, Biochem, and Bio.*
