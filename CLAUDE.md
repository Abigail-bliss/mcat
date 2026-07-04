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
timeline, two-phase plan, scores — is in **`00-strategy/Abigail_MCAT_progress_summary.md`**. Read that
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

The top level is organized as a **pipeline**, numbered in the order information flows:
**`01-reference` (what to learn from) → `02-review` (practice + find misses) → `03-consolidate`
(make it stick), all steered by `00-strategy` (the why & when).**

| Folder | What's in it | Nested `CLAUDE.md`? |
|--------|--------------|---------------------|
| `00-strategy/` | **The study journey** (was `mcat-journey/`) — strategy, plans, progress, data. Master summary, `study-plan/`, `weekly-plans/`, `progress/progress-log.md`, `data/Error Log.xlsx`. Start at its `README.md`. | — |
| `01-reference/` | **Source material — read-mostly inputs.** Holds `WizePrepChaptersReference/` (her course content sequence — `wizeprep_reference.html` is the canonical chapter/subtopic checklist, drives unsuspend order), `Study Materials/` (reference PDFs — AAMC "What's on the MCAT", review books), and `Accomodations/` (personal accommodation paperwork — **not study content, leave alone unless she asks**). | — |
| `02-review/` | **FL dissection / question review** (was `Practice Exams/`). Per-exam folders (PDFs + per-passage transcripts + `WizePrep_Dissection_Consolidated.md`), plus `Screenshots/` (the transcription inbox). This is where misses are found. | ✅ `02-review/CLAUDE.md` (the FL-dissection workflow, error-log routing) |
| `03-consolidate/` | **Making it stick — the daily-review pair.** Holds `Anki/` (**card creation + the AnKing suspend/unsuspend mechanism** — build scripts in `card-creation/`, screenshots in `biochem_images/`, unsuspend project in `anking-unsuspend/`, old runs in `archive/`) and `Flash Sheets/` (**concept-fluency free-recall sheets** — one file per concept, `_index.md` tracks spaced-rep buckets; replaced the per-exam glossaries 2026-07-01). | ✅ `03-consolidate/Anki/CLAUDE.md` + `03-consolidate/Anki/anking-unsuspend/CLAUDE.md`; ✅ `03-consolidate/Flash Sheets/CLAUDE.md` + `Flash Sheets/README.md` |

**How the flow works:** the WizePrep sequence (`01-reference/`) defines what's "covered" → FL
dissection (`02-review/`) surfaces misses → each miss routes to `03-consolidate/` (concept gap →
Flash Sheets, atomic fact → Anki) and to the Error Log (the "why"). Flash Sheets + Anki are the
daily backbone. `00-strategy/` decides the sequencing and tracks progress across all of it.

## Where to look first

- **Anything strategic / "what should she do":** `00-strategy/Abigail_MCAT_progress_summary.md`, then `00-strategy/study-plan/master-study-plan.md`.
- **Scores, decisions, this week's plan:** `00-strategy/progress/progress-log.md` and `00-strategy/weekly-plans/`.
- **Making/pushing cards:** `03-consolidate/Anki/CLAUDE.md` (AnkiConnect at `localhost:8765`, Basic note type, HTML+MathJax, tag structure, the misses workflow).
- **Unsuspending AnKing content:** `03-consolidate/Anki/anking-unsuspend/CLAUDE.md` + its `progress.md` batch log.
- **Flash sheets (concept recall) + how misses route into them:** `03-consolidate/Flash Sheets/README.md`.
- **Reviewing practice exams / dissecting misses:** `02-review/CLAUDE.md`.
- **What she's covered in the course:** `01-reference/WizePrepChaptersReference/wizeprep_reference.html`.

## Global do-nots

- **Never read AnKing card content.** The `AnKing MCAT Deck` (and subdecks) is premade and not hers — use `findNotes`/`findCards` for IDs/counts only; existence-check against her own decks (`MCAT Physics/Chemistry/Math/Organic Chemistry/Biochemistry`).
- **Don't nudge toward bulk card-making** — it's her trap. Default to reviewing premade content.
- **Don't touch `01-reference/Accomodations/`** as study material — it's sensitive personal paperwork.
- **Don't duplicate the "why I missed it"** into Anki — the Error Log (`00-strategy/data/Error Log.xlsx`) owns that.
