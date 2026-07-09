# AnKing Unsuspend — Project Directive

This project is **separate from card creation.** The card-creation rules live in the parent
`../CLAUDE.md` ("Create Anki" directions) and still load here because this is a subfolder — that's
intentional, so the **Question Misses** workflow stays available. But the *primary activity of this
project is NOT making cards.* It is **unsuspending the right AnKing cards**, so the user reviews
premade high-quality content instead of building her own.

> **Trigger change (2026-07-05):** unsuspending is now **on-encounter, not bulk.** Even topic-by-topic
> chapter unsuspending surfaced too many cards to survive. **The new rule: unsuspend an AnKing card
> only when its exact topic comes up in a *missed question* during FL dissection.** The miss is the
> trigger; WizePrep coverage is now only the *eligibility gate* (don't unsuspend ahead of what she's
> covered), not the driver. The chapter-batch machinery below is retained as reference but is no
> longer the default rollout — see **The unsuspend mechanism**.

> One-line mission: **Reviewing >> creating.** Surface *just* the AnKing card that matches a real miss,
> so the daily queue only grows with content she has demonstrably needed.

---

## Context (why this project exists)

- **Test date: 2026-09-03** (~75 days out as of 2026-06-20).
- The user spent a lot of time hand-building her own physics/chem/biochem decks but was **barely
  reviewing them** — net negative ROI, since SRS value comes from *reviews*, not card creation.
- She owns the full **AnKing MCAT Deck** (premade, vetted, ~2,500 content cards) but it ships mostly
  **suspended**, and doing "all of it" is impossible in 75 days.
- **Decision (updated 2026-07-05):** AnKing is the daily-review backbone, but we unsuspend it
  **on-encounter from misses** — when a missed question surfaces a topic, unsuspend the narrow AnKing
  slice for *that* topic (a MileDown subtopic tag, often just a card or few), provided WizePrep has
  covered it. The earlier plan (unsuspend in WizePrep-sized chapter chunks as she covers each topic)
  still buried the queue, so it's demoted to a fallback. Custom cards are reserved for genuine
  *atomic* misses/gaps only (parent CLAUDE.md's `missed::*` workflow + atomic-only gate).

---

## The user's content sequence — WizePrep

Her study order is driven by the WizePrep textbooks, mapped in:

```
/Users/abigailbliss/Documents/mcat/01-reference/WizePrepChaptersReference/wizeprep_reference.html
```

That file (a self-contained HTML checklist) lists every chapter + subtopic for the four content
volumes, with assigned/due dates:

- **CPF I & II** — *Content Prep* (Chem/Phys): physics, gen chem, and intro orgo (CPF II Ch 5–7).
- **BBF I & II** — *Bio & Biochem Foundations*: biomolecules, cells, central dogma, metabolism, and
  organ-system physiology.
- **Psych/Soc is NOT in that file yet** (no WizePrep P/S reference built). When P/S unsuspending
  starts, we'll need either the WizePrep P/S sequence or fall back to AnKing's own Behavioral order.

**WizePrep is now the eligibility gate, not the trigger.** Don't unsuspend a topic she hasn't reached
in WizePrep — but reaching it in WizePrep no longer *by itself* means unsuspend. The trigger is a
**miss** on that topic (see the on-encounter flow below). Confirm coverage before unsuspending.

---

## AnKing deck structure (mapped 2026-06-20)

AnKing slices **cleanly by subject (subdeck), messily by topic (tags).**

### Subdecks = the reliable subject axis (covers every card)

| Subdeck (`AnKing MCAT Deck::…`) | Cards | WizePrep home |
|---|---|---|
| `Physics-and-Math`   | 328  | CPF I & II physics chapters |
| `General-Chemistry`  | 290  | CPF I & II gen chem chapters |
| `Organic-Chemistry`  | 306  | CPF II Ch 5–7 |
| `Biochemistry`       | 541  | BBF I (biomolecules, metabolism) |
| `Biology`            | 695  | BBF I & II (cells, systems, physiology) |
| `Behavioral`         | 1584 | Psych/Soc |
| `Essential-Equations`| 95   | C/P equation drilling (cross-cutting) |

### Tags = TWO parallel layers: source AND topic

There are two independent tagging layers on the same cards:

**1. Source layer** `#AK_MCAT_v2::<source>::…` — organizational, by where the card came from:
`#UWorld` (biggest) · `#KhanAcademy` · `#UWorld_Books` · `#Kaplan` · `#Pixorize_MCAT` ·
`#IFD_High_Yield` · `#AAMC` · others. UWorld is tagged only by per-card numeric IDs → **useless for
topic slicing.** Small subsets (Kaplan `Subject::Ch-NN`, IFD `NN-<Topic>`) do have topic structure
but cover few cards.

**2. ⭐ Topic layer — `#AK_MCAT_v2::AK_Original_Decks::MileDown::<Subject>::<Topic>[::<Subtopic>]`**
This is the **PRIMARY slicing axis.** It is a clean, fine-grained topic hierarchy that covers
**~98% of the deck (6,315 / 6,435 cards)** across every subject:

| MileDown subject branch | Cards |
|---|---|
| `…::Physics` | 650 |
| `…::General_Chemistry` | 539 |
| `…::OChem` | 574 |
| `…::Biochemistry` | 1057 |
| `…::Biology` | 1188 |
| `…::Behavioral` | 2437 |

…each split into precise subtopics, e.g. `…::Biochemistry::Amino_Acids` (130),
`…::Biochemistry::Metabolism::Glycolysis`, `…::Physics::Fluids` (61),
`…::Biology::Nervous_System::Action_Potential`. Subtopics map cleanly onto WizePrep chapter topics.

> **Counts are CARDS, not notes.** AnKing note types (cloze etc.) generate multiple cards per note,
> so card counts run higher than the per-subdeck *note* counts in the table above.

**Consequence:** per-WizePrep-chapter unsuspending is a **clean union of a few MileDown topic tags** —
precise, no fuzzy keyword matching needed. Keyword-within-subdeck is now only a *fallback* for the
~2% of cards lacking a MileDown tag, or to sanity-check a topic's coverage.

---

## The unsuspend mechanism

**Default = on-encounter (per-miss).** When FL dissection surfaces a miss:

1. Identify the specific topic of the miss (e.g. "wobble hypothesis", "ATP synthase location").
2. Check WizePrep has covered it (eligibility gate).
3. `findCards` the **narrowest matching MileDown subtopic tag** scoped to the right subdeck → show the
   count (often 1–several cards). Preview, no content.
4. On approval, `unsuspend` just that slice. Log it in `progress.md` with the source miss.

This keeps the queue growing only with content a real miss proved she needs. The chapter-batch method
below is retained as a **fallback** — use it only if the user explicitly wants to pre-load a topic.

### Fallback: chapter-batch unsuspend

For a whole WizePrep chapter we unsuspend the **union of the matching MileDown topic tags** (primary
axis). Keyword-within-subdeck is only a fallback for the ~2% of cards without a MileDown tag, or to
verify a topic's coverage.

MileDown topic-tag prefix (use the leading `*` so tag-with-`#` matches, and trailing `*` to include
subtopic children):
```
"tag:#AK_MCAT_v2::AK_Original_Decks::MileDown::<Subject>::<Topic>*"
```

### Hard rules

- **NEVER read AnKing card content.** `findNotes` runs inside Anki and returns only note IDs — the
  collection never enters context. Use it freely; never `notesInfo`/dump AnKing fronts to "check"
  them. (Same rule as parent CLAUDE.md.)
- **Preview before acting.** For every batch, show the **count per query** and the total going into
  the queue. Wait for approval before unsuspending. Never dump a whole subdeck at once.
- **Respect the daily cap.** Unsuspending makes cards available, but the queue is governed by the
  deck's *new-cards/day* limit. Keep batches sized so the backlog stays survivable to 2026-09-03
  (target cap TBD with user — see Open Questions).
- **Stay in step with WizePrep.** Confirm the current chapter; don't unsuspend ahead of coverage.
- **Log every batch** in `progress.md` (chapter, queries used, counts, date) so we never double-do a
  chapter and can see coverage at a glance.

### AnkiConnect calls used here

- `findNotes` query=`'deck:"AnKing MCAT Deck::<Subdeck>" "<keyword>"'` → candidate IDs (count only).
- `areSuspended` / filter to currently-suspended IDs.
- `unsuspend` cards=[...] → the action. (Cards, not notes — convert via `cardsInfo`/`notesInfo` IDs
  → card IDs, or query cards directly with `findCards`.)
- Use **`findCards`** (not findNotes) when the next step is unsuspend, since unsuspend takes card IDs.

### Per-batch flow

1. Confirm WizePrep chapter she's covered.
2. Pick the matching **MileDown topic tags** for that chapter's subtopics (from the WizePrep `topics`
   list). Keyword fallback only if a topic has no MileDown tag.
3. `findCards` per tag → **show counts, deduped total** (preview, no content).
4. On approval, `unsuspend` the deduped card IDs.
5. Append a row to `progress.md`.

---

## Workflow order (always)

1. **Preview** counts per query + total. Wait for approval.
2. **Unsuspend** the approved card IDs.
3. **Log** the batch in `progress.md`.
4. **Report** how many newly unsuspended (vs. already active) and the new total active count.

---

## Rollout (updated 2026-07-05)

**No bulk rollout by default.** The deck stays mostly suspended and grows on-encounter from misses
(see mechanism above). Only pre-load a slice if the user explicitly asks — e.g. the **IFD High-Yield
(47 cards)** set as a one-time highest-yield seed. The old "IFD, then chapter-by-chapter off WizePrep"
plan is superseded because chapter-sized batches buried the queue.

---

## Open questions to settle with the user

- **Daily new-card cap** per deck (drives batch sizing; needs a number that clears the backlog by
  2026-09-03 without overload).
- **Keyword lists per chapter** — co-author these from the WizePrep `topics` arrays.
- **Psych/Soc sequence** — no WizePrep P/S reference yet; decide source order when P/S starts.
- **Suspend-back policy** — if a batch proves too broad, how we trim.

---

## What NOT to do

- Don't read or dump AnKing card fronts/backs into context (IDs and counts only).
- Don't unsuspend a whole subdeck, a whole chapter by default, or run ahead of WizePrep coverage.
  Unsuspend the narrow slice a **miss** points to (on-encounter); chapter-batching is fallback-only.
- Don't make new cards here as the default — that's the parent project. Custom cards only for genuine
  misses/gaps via the `missed::*` workflow.
- Don't skip the preview/approval step before unsuspending.
