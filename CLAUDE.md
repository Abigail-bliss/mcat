# MCAT — Root Orientation

This folder is **Abigail's entire MCAT prep**. If you're reading this, a chat was started from
the `MCAT/` root — here's what's going on and where everything lives. Detailed rules live in the
nested `CLAUDE.md` files (they auto-load when you work in those subfolders); **this file is the map,
not the manual.**

## The situation (one paragraph)

Abigail is a software engineer (works full-time, WFH), exceptional and a fast memorizer, with ADHD.
**Test day: 2026-09-03. Target: 520** (diagnostic was 496). Strengths: CARS (90th %ile — protect),
Gen Chem, Psych/Soc (familiar). Weak/new: **Bio, Biochem, Orgo (never taken — Orgo is #1 weakness)**,
Physics partial. Her content sequence is driven by the **WizePrep** course. Full detail — background,
timeline, two-phase plan, scores — is in **`mcat-journey/Abigail_MCAT_progress_summary.md`**. Read that
first for anything strategic.

## The core operating philosophy

**Review > intake. Reviewing >> creating.** The thing that moves scores is *retrieval and
consolidation* (reviewing missed questions until they stick, spaced AnKing review), not *production*
(watching lectures, making flashcards, keeping logs she never revisits). Her recurring failure mode
is filling time with intake and never consolidating. When advising or planning, **protect review
time and weakness-first effort (Orgo/Biochem/Bio) above all.**

- **AnKing is the daily-review backbone.** Custom cards only for genuine misses/gaps.
- **Logging a miss and reviewing it are one act**, done at the moment of the miss.
- **Anki: white background / dark text only** — never add night-mode handling.

## Folder map

| Folder | What's in it | Nested `CLAUDE.md`? |
|--------|--------------|---------------------|
| `Anki/` | **Card creation + the AnKing suspend/unsuspend mechanism.** Build scripts in `card-creation/`, screenshots in `biochem_images/`, the unsuspend project in `anking-unsuspend/`, old runs in `archive/`. | ✅ `Anki/CLAUDE.md` (card workflow, decks, tags, formatting, the Question-Misses workflow) and ✅ `Anki/anking-unsuspend/CLAUDE.md` (how to unsuspend AnKing in WizePrep-sized batches) |
| `Flash Sheets/` | **Concept-fluency free-recall sheets** — the "sheet half" of her sheet + Anki review combo (peer of `Anki/`). Durable, cross-exam, one file per concept in `[CLUE]` + indented-outline format; `_index.md` tracks spaced-rep buckets. Fed by FL-review misses. Replaced the per-exam glossaries (2026-07-01). | ✅ `Flash Sheets/CLAUDE.md` (operating manual: format, layout, miss-routing, do-nots) + `Flash Sheets/README.md` (method + study routine) |
| `mcat-journey/` | **The study journey** — strategy, plans, progress, data. Master summary, `study-plan/`, `weekly-plans/`, `progress/progress-log.md`, `data/Error Log.xlsx`. Start at its `README.md`. | — |
| `WizePrepChaptersReference/` | Her course content sequence — `wizeprep_reference.html` (the canonical chapter/subtopic checklist), assignment due-date exports, lecture screenshots. Drives unsuspend order. | — |
| `Study Materials/` | Reference PDFs (AAMC "What's on the MCAT", review books, flash sheets). Read-only resources. | — |
| `Practice Exams/` | Full-length PDFs she's taken (AAMC diagnostic, Altius FLE 1). | — |
| `Accomodations/` | Personal accommodation paperwork (ADHD eval, ACT records, letters). **Not study content — leave it alone unless she asks.** | — |

## Where to look first

- **Anything strategic / "what should she do":** `mcat-journey/Abigail_MCAT_progress_summary.md`, then `mcat-journey/study-plan/master-study-plan.md`.
- **Scores, decisions, this week's plan:** `mcat-journey/progress/progress-log.md` and `mcat-journey/weekly-plans/`.
- **Making/pushing cards:** `Anki/CLAUDE.md` (AnkiConnect at `localhost:8765`, Basic note type, HTML+MathJax, tag structure, the misses workflow).
- **Unsuspending AnKing content:** `Anki/anking-unsuspend/CLAUDE.md` + its `progress.md` batch log.
- **Flash sheets (concept recall) + how misses route into them:** `Flash Sheets/README.md`.
- **What she's covered in the course:** `WizePrepChaptersReference/wizeprep_reference.html`.

## Global do-nots

- **Never read AnKing card content.** The `AnKing MCAT Deck` (and subdecks) is premade and not hers — use `findNotes`/`findCards` for IDs/counts only; existence-check against her own decks (`MCAT Physics/Chemistry/Math/Organic Chemistry/Biochemistry`).
- **Don't nudge toward bulk card-making** — it's her trap. Default to reviewing premade content.
- **Don't touch `Accomodations/`** as study material — it's sensitive personal paperwork.
- **Don't duplicate the "why I missed it"** into Anki — the Error Log (`mcat-journey/data/Error Log.xlsx`) owns that.
