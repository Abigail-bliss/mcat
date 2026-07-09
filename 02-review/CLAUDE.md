# 02-review — Orientation (FL dissection / question review)

A chat started here is for **reviewing practice exams and missed questions** for Abigail's MCAT
prep. This is `02-review/` (formerly `Practice Exams/`), the practice stage of the pipeline
(`00-strategy → 01-reference → 02-review → 03-consolidate`). This file is self-contained enough to
work from; broader context is one level up in `../CLAUDE.md` and `../00-strategy/`.

## Who / what / when
Abigail — software engineer, ADHD, fast memorizer. **Test 2026-09-03. Target 520** (diagnostic 496;
2nd FL also 496 but on harder Altius, so *not* a plateau). Strong: **CARS (90th %ile)**, Gen Chem,
Psych/Soc. Weak/new: **Bio, Biochem, Orgo (#1 weakness — never taken)**, Physics partial. Content
sequence follows the **WizePrep** course. Full story: `../00-strategy/Abigail_MCAT_progress_summary.md`.

## The one principle that governs review
**Review > intake. Close the loop > log more.** The score-mover is *consolidation* (reviewing a
miss until it sticks), not production (more lectures, more rows). Logging a miss and reviewing it are
**one act**, done at the moment of the miss. Pour effort weakness-first (Orgo/Biochem/Bio).

## The system of record = a live Google Sheet (NOT a file here)
Her miss / FL-dissection tracker is a Google Sheet, readable via the **Google Drive connector**:
- **Sheet ID:** `1GOp0fA93ItrhM6Hm_vfaNnBesbvRSbNz51m1l6C_cSk`
- **Tab gid:** `147763115`
- Use `mcp__claude_ai_Google_Drive__read_file_content` with `fileId` = the Sheet ID above to read it.

(Static export fallback: `../00-strategy/data/Error Log.xlsx`). **Do NOT build a parallel tracker — it already does everything.**

**You can READ/analyze the sheet but CANNOT write cells** (no Sheets-write tool). The workflow: Claude reads the staging file + sheet, formats the new rows in the correct schema, and presents them as a copy-paste-ready table. Abigail pastes them in.

### Column schema (left → right)

| # | Column | Type | Valid values / notes |
|---|--------|------|----------------------|
| 1 | Date | date | M/D/YYYY, e.g. `6/29/2026` |
| 2 | Section | enum | `C/P` · `B/B` · `CARS` · `P/S` |
| 3 | Source | enum | `WP` (WizePrep) · `AAMC` · `Altius` |
| 4 | WizePrepLoc | text | WizePrep chapter, e.g. `1.6`, `review 1`; blank for AAMC/Altius |
| 5 | Question # | text | single number or range, e.g. `6`, `16-18` |
| 6 | Mode | enum | `timed` · blank |
| 7 | Topic | text | broad topic, e.g. `Orgo`, `mechanics`, `Biochem` |
| 8 | Subtopic | text | specific subtopic, e.g. `chirality`, `torque` |
| 9 | Knowledge | flag | `x` if knowledge gap; blank otherwise |
| 10 | Skills | flag | `x` if skills/reasoning gap; blank otherwise |
| 11 | Slip | flag | `x` if careless error; blank otherwise |
| 12 | Description | text | Her verbatim "why I missed it" from WizePrep report |
| 13 | Action type | enum | `learn` · `review` · `memorize` · `practice` · `n/a` |
| 14 | Action | text | Specific thing to do; blank when Action type = n/a |
| 15 | Action done? | enum | `yes` · `no` · `n/a` (default `no` on first entry) |
| 16 | What did you do? | text | Fill in only when Action done? = yes; blank on first entry |

**Action type definitions:**
- `learn` = topic not yet covered in WizePrep — park it, don't self-teach now
- `review` = covered content, needs re-exposure (flash sheet, AnKing unsuspend, re-read)
- `memorize` = specific fact/formula to add to Anki
- `practice` = reasoning/strategy weakness — needs drilling, not a card
- `n/a` = slip or reasoning error with no discrete follow-up action

### Google Sheet update workflow

Runs **once at the end of an FL review batch**, not mid-session.

**Step 1 — Read current state**
```
mcp__claude_ai_Google_Drive__read_file_content(fileId="1GOp0fA93ItrhM6Hm_vfaNnBesbvRSbNz51m1l6C_cSk")
```
Scan for the most recent rows to find where to start appending (avoid duplicates).

**Step 2 — Read the staging file**
Read `{exam-folder}/WizePrep_Dissection_Consolidated.md` for all logged misses.
Cross-ref against the sheet to identify which rows are NEW (not yet entered).

**Step 3 — Format new rows**
For each new miss, produce a row in pipe-table format matching the 16-column schema:
```
| Date | Section | Source | WizePrepLoc | Q# | Mode | Topic | Subtopic | K | S | Slip | Description | Action type | Action | Action done? | What did you do? |
```
- Pull Description verbatim from her WizePrep "why" (staging file)
- Infer Action type from the miss category (K=knowledge → `learn`/`memorize`; S=skills → `practice`; Slip → `n/a`)
- Default Action done? to `no`; leave "What did you do?" blank

**Step 4 — Hand off**
Present the formatted rows. Abigail copies them into the sheet (append at bottom).
After she confirms pasted, the session is done.

## How FL dissection works (her rule)
**Only deep-dive content she has ALREADY covered in WizePrep.** Questions on un-covered topics →
*park them, don't self-teach* (that's intake, not review). As filters on the existing sheet:
- **🔬 Deep-dive worklist** = `Action done? = no` AND `Action type ∈ {review, memorize, practice}`
  (covered topics). Sort weakness-first.
- **🅿️ Parking lot** = `Action type = learn` (not covered yet) → defer.
- **Progress** = `Action done?` flipping no→yes. The log is already rich; closing the loop is the gap.
- Add new FL misses as rows with `Source = AAMC` (or `Altius`).

## Current FL work
- **Active dissection: Altius FLE 1** (taken 2026-06-29) → folder `6-29_ALTIUS_FLE_1/`. Working the
  **B/B section live, question-by-question** (per the streamlined loop below).
- **Per-exam progress lives in that folder's `WizePrep_Dissection_Consolidated.md`**, NOT here —
  check its status table to see what's done. (As of 2026-06-29: BBF passages 2–5 + some discretes
  transcribed through ~Q24; Q3/Q5 and discretes Q28/Q29 still to transcribe; Q25+ awaiting screenshots.)
- Don't read the two 496s as a plateau (diagnostic 496 was easier AAMC; 2nd was harder Altius).

## Also note
- **WizePrep "dissection report"** — a required form inside the WizePrep platform (not exportable).
  A separate obligation, not her analytical system. You can draft its content from the sheet rows
  once its fields are known.
- PDFs of taken exams live in this folder (`Altius-FLE-1.pdf`, `FL_5-16.pdf`).

## The per-exam teaching workspace (markdown method — built 2026-06-29)
Each FL gets its own folder (e.g. `6-29_ALTIUS_FLE_1/`). **This workspace is for *teaching herself
the material she got wrong* — it is NOT the error log.** The official error log lives in **WizePrep**
(the required dissection report) and gets transferred into the **Google Sheet**. The flow at the end
of a review: **she provides WizePrep-log screenshots → we fill the Google Sheet using those + the
material generated here.** So everything below is a *learning aid + record of what we covered*, which
feeds the sheet later; it does not replace the sheet.

**The streamlined loop (settled 2026-06-29):** She does content review **live, question-by-question,
in the session** (she is NOT deferring/parking topics to circle back to — that happens now). So:
1. **She maintains exactly ONE thing by hand: the WizePrep dissection report** (required anyway) —
   her "why did I get this wrong" in her own words. She screenshots it when she wants a sync.
2. **Claude does the teaching live** (define `{...}` marks, explain the miss) → updates the
   per-passage `.md` (Notes & Terms) and, at the end-of-review batch, routes each miss to its home:
   concept gap → `../03-consolidate/Flash Sheets/`; atomic fact → the Anki flashcard queue; one-off vocab
   → stays in Notes. (Glossary is frozen — don't feed it.)
3. **Claude mirrors tracking into ONE staging file** (`WizePrep_Dissection_Consolidated.md`) — no
   double-entry, no parallel xlsx tabs.
4. **Google Sheet = one batch at the END of the FL** (optional; "not necessary" per her). Fill it
   together in one sitting from the staging file. Never live, never mid-review.

**Screenshot transcription inbox (`02-review/Screenshots/`):** She drops question screenshots here
(macOS screenshots — filenames use a **U+202F narrow no-break space** before "PM", so match them with
globs like `Screenshot*"1.29.03"*.png`, not a typed regular space). To transcribe "the last N
screenshots," take the N most recent by mtime, transcribe each into the right `BBF_/CPF_Passage_N.MD`
(create the file if the passage is new; leave `_Screenshot not yet provided_` placeholders for
questions not yet captured). **After transcribing a screenshot, move it to `02-review/Screenshots/read/`**
(sibling `read/` subfolder) so the inbox only holds un-transcribed shots. Transcribe **verbatim** —
only the text/figures in the image, no added commentary. Mark result from the screenshot: red ✗ =
missed (tag `✗ (missed)`); yellow highlight = correct answer; the filled radio = her selected answer.

**Files in an exam folder:**
- `BBF_Passage_N.MD` (one per passage) / `BBF_Discrete_Questions.MD` (one per section, for
  passage-independent Qs) — transcribe the passage + table + Equation(s), then each question: stem,
  AAMC metadata line (*Subtopic · Topic · SIR skill · Discipline*), choices A–D with the correct one
  **bolded + ✓**, and the solution. Mark her wrong answers from the red ✗ in the screenshot. Each
  passage file ends with a **`## Terms & Notes`** section (definitions of her `{...}` marks) and a
  **`## Flashcards to Make`** section — both stay; see the annotation + routing rules below.
- `glossary.md` — **FROZEN as of 2026-07-01** (replaced by flash sheets, see below). Existing
  per-exam glossaries stay as records; **do NOT feed them anymore.** They were the cumulative
  by-subject term list; that job now belongs to the cross-exam flash sheets.
- **Flash sheets** (`../03-consolidate/Flash Sheets/`, sibling of `Anki/`) — **the concept-fluency consolidation artifact**,
  and the "sheet half" of her sheet + Anki combo (replaced the glossary). Durable, cross-exam, one
  file per concept in `[CLUE]` + indented free-recall-outline format (r/MCAT method). She studies by
  reciting the whole sheet from the clue. During FL review, concept-level misses (esp. weakness
  subjects) get routed here as new branches; see **`../03-consolidate/Flash Sheets/CLAUDE.md`** (operating manual) +
  `README.md` (method) for the routing rules and `_index.md` for the spaced-rep buckets.
- `Flashcards_To_Make.md` — consolidated **Anki** queue, grouped by source file, each item pointing
  back to its passage/Q. Mirrors a `## Flashcards to Make` section inside each source file. **Cards
  generated only at the END** ("generate the flashcards"), never mid-review. Anki = high-yield
  *retrieval* targets only; the flash sheets carry the rest.
- `WizePrep_Dissection_Consolidated.md` — **the single tracker + Google-Sheet staging file.** Holds:
  a **status table** (Q# · P# · result · cause K/S/Slip · topic/subtopic · pattern · action type ·
  status), a **reasoning-patterns** summary, and per-question **verbatim** WizePrep "why" text mapped
  to the sheet schema. Populated from her WizePrep screenshots. (Replaced the old `Question Misses` +
  `Reasoning Patterns` xlsx tabs — do NOT recreate those; one home now.)

**Annotation workflow (how she flags what she doesn't know):**
- In the passage/question markdown she wraps unknown text in **`{...}`**: `{term}` = "define it";
  `{term | her note/question}` = "define it AND answer my note." Braces stay in after defining; on
  re-runs only add *new* terms.
- VSCode keybindings (in her `keybindings.json`, markdown-only): **`Cmd+Shift+U`** wraps the
  selection in `{ }`; **`Shift+]`** (only when text is selected) wraps it in `{ word |  }` with the
  cursor after the `|`. (`Shift+]` still types a normal `}` when nothing is selected.)
- When she says "define the marks," scan `{...}` and write definitions into the file's **`## Terms &
  Notes`** section (bottom of each passage). **This per-passage Terms & Notes section STAYS — she
  wants it** (it's the passage-local record + first-pass definitions). Do NOT also write to
  `glossary.md` (frozen). Concept-level gaps get *additionally* promoted to a `../03-consolidate/Flash Sheets/` sheet at
  the end-of-review batch — the passage Terms & Notes is the local capture, the flash sheet is the
  durable cross-exam recall target.

**Flashcard discipline (guards her bulk-card trap):** card *selectively* — only genuine concept gaps,
weakness-subject misses, or **repeated** misses. NOT every vocab term (the passage `## Terms & Notes`
+ the flash sheets already carry the vocab/concept review). A reasoning/strategy habit (e.g. "didn't read units") is usually **not** a
flashcard — it's an error-pattern to drill, not a fact to retrieve. Defer all card creation to one
end-of-review batch.

**Error-type tracking:** in the staging file's status table, tag each miss with a coarse cause —
*Knowledge · Skills/Reasoning · Slip* + a short pattern note — to surface recurring leaks (she
explicitly wants to track skills/reasoning/slips to improve). **Her dominant reasoning leak = "didn't
fully use the passage/data"** (fix: externalize the logic on scratch paper — scan every row, write the
units, draw the ↑/↓ causal chain — before answering). The verbatim prose "why" is hers from WizePrep.

## Don't
- Don't build a second tracker. There is exactly ONE local tracker —
  `WizePrep_Dissection_Consolidated.md` per exam — and the canonical log is WizePrep → Google Sheet.
  Don't recreate the old `Question Misses` / `Reasoning Patterns` xlsx tabs (deleted on purpose).
- The verbatim "why I missed it" is hers (WizePrep); locally keep only the category + a short pattern
  note, never a parallel prose copy.
- Don't push her to pre-study un-covered topics during review.
- Don't treat a 496-vs-496 across different test makers as no progress.
- Don't make flashcards mid-review or card every vocab term — defer to one batch, card selectively.

## Useful first move
Offer to read the sheet and hand her a **prioritized deep-dive worklist** (covered + not-done +
weakness-first) so a session starts with a queue, not a blank stare.
