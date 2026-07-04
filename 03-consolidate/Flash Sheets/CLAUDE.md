# Flash Sheets — operating manual

A chat working in this folder is building or maintaining Abigail's **flash sheets**: concept-level
**free-recall** sheets that are her primary content-consolidation artifact. This file is the operating
manual; `README.md` next to it carries the fuller method write-up and the study routine. Broader
context is at the repo root `../../CLAUDE.md`; the FL-review side is `../../02-review/CLAUDE.md`.

## What a flash sheet is (and the one rule that makes it work)

One file per concept. A `# [CLUE]` header, then an **indented outline of everything about that
concept**, written so she can cover the page, read only the clue, and **lecture the rest from
memory**. The indentation *is* the lecture outline. `Note:` lines carry mnemonics, intuition, and
links — they're what makes a fact stick, not filler.

**The recall half is the score-mover, and it is HERS.** Reading a sheet is not studying it; reciting
it from the clue is. Building sheets is the *cheap* half and it rides on FL review (below) — never let
sheet-building become a standalone intake session. That is her documented trap (produce, never
consolidate). If she's spending flash-sheet time *writing* instead of *reciting*, say so.

## Format rules

- File: one concept per file. Header `# [CLUE] <concept + parenthetical of what's inside>`, then a
  `> Cover everything below and lecture it from memory.` line, then the outline.
- Use nested `-` bullets. Bold the key term at each branch. Put mnemonics/intuition on `Note:` lines.
- If the sheet came from a specific miss, add a one-line provenance under the clue
  (e.g. `> (From Altius FLE 1 Q58 — Bio weakness, missed. Fell for the "missense" trap.)`).
- Keep it recitable — a sheet so long she can't lecture it in one pass should be split by clue.
- Match the seeded examples in `biochem/` and `bio/`.

## Layout

- `_index.md` — the spaced-rep tracker (sheet · subject · bucket 🔴daily/🟡weekly/🟢monthly · last
  recited · source). **Every new sheet gets a row.** "Last recited" tracks *reciting*, not editing.
- Subject subfolders: `biochem/`, `bio/`, `orgo/`, `gen-chem/`, `physics/`, `psych-soc/`. Create on
  first use.

## How misses become sheets (the routing rule)

This is the receiving end of the FL-review loop (`../../02-review/CLAUDE.md`). At the
**end-of-review batch**, each miss routes by type:

- **Concept gap** — couldn't explain a whole system, esp. a weakness subject (Orgo / Biochem / Bio)
  → **here**: find the relevant sheet and add a branch, or create a new sheet + `_index.md` row.
- **Atomic high-yield fact** ("AUG = start codon") → Anki (`../../02-review/<exam>/Flashcards_To_Make.md`).
- **One-off passage vocab** → stays in that passage's `## Terms & Notes`; promoted to nothing.

Source material for a sheet = the WizePrep/AAMC explanation of the miss (same content she's already
reading live). When adding to an existing sheet, only add the *new* branch — don't rewrite what's there.

## Relationship to her other artifacts

- **Flash sheets REPLACED the per-exam `glossary.md`** (decided 2026-07-01). Old glossaries are frozen
  records — don't feed them.
- **Per-passage `## Terms & Notes` STAYS** — she wants it. That's the passage-local first-pass capture;
  the flash sheet is the durable cross-exam recall target. A concept gap gets written *both* places
  (local Terms & Notes during live review, then promoted to a sheet at the batch).
- **Anki** is the peer modality: atomic retrieval. Flash sheets = whole-concept fluency. Both are
  daily review; they don't overlap.

## Don'ts

- Don't build sheets outside the FL-review flow as a standalone "make a bunch of sheets" session — that
  reintroduces the intake trap. Card/sheet *selectively*.
- Don't feed the frozen glossaries.
- Don't confuse editing with studying — the `_index.md` "last recited" column is the real progress
  signal, not sheet count.
