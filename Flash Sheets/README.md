# Flash Sheets

Concept-level **free-recall** sheets — the primary consolidation artifact for content review.
One sheet per concept. You study by reading **only the clue** at the top and *lecturing the rest
from memory*. This is the "I could explain it to someone on the street" test.

Method credit: the r/MCAT "flash sheets" method (a 524 scorer's main study tool). Chosen here
because active whole-concept recall beats passive re-reading, and the "tip-of-the-tongue → got it"
pull is ADHD-friendly.

## How to study a sheet (the half that actually moves the score)

Half your flash-sheet time goes here. For each due sheet:

1. Read **only the `# [CLUE]` line**. Cover everything below it.
2. Lecture the whole thing out loud from memory — every branch, every `Note:`.
3. Uncover, check what you missed, then move the sheet's bucket in `_index.md`:
   - Barely recalled → **daily**
   - Kind of recalled → **weekly**
   - Easily recalled → **monthly**

Treat it like a workout. First rep you'll recall almost nothing — that's expected. The reps are
the point.

## How sheets get built (the other half — rides on FL review, no separate session)

The other half of the time is *adding content* — and the source is the same explanations you're
already reading during FL review. At the **end-of-review batch** (when you say "generate the
flashcards"), each miss is routed by type:

- **Concept gap** — couldn't explain a whole system, esp. a weakness subject (Orgo / Biochem / Bio)
  → add a branch to the relevant flash sheet here, with a `Note:` mnemonic.
- **Atomic high-yield fact** ("AUG = start codon") → Anki queue (`Flashcards_To_Make.md`).
- **One-off passage vocab** → stays in the passage's Notes & Terms; promoted to nothing.

New fact you don't recognize, or recognize but couldn't explain, or a good way to remember
something → it goes on a sheet.

## Format (the indentation IS the lecture outline)

```
# [CLUE] Enzyme Function, Naming, and Structure
> Cover everything below and lecture it from memory.

- Enzyme = catalyst
  - speeds reactions without being used up
  - Note: allosteric binding → shape change → active site altered → function changes
```

`Note:` lines carry mnemonics, intuition, and links to other concepts — they're what makes a fact
stick, not filler.

## Layout

- `_index.md` — the spaced-rep tracker (sheet · subject · bucket · last recited). Bump buckets here.
- Subfolders by subject: `biochem/`, `bio/`, `orgo/`, `gen-chem/`, `physics/`, `psych-soc/`.
- One concept per file.

## Relationship to the old glossary

Flash sheets **replace** the per-exam `glossary.md` going forward (decided 2026-07-01). Existing
glossaries stay as frozen per-exam records — don't feed them anymore, don't delete them. All new
concept content comes here.
