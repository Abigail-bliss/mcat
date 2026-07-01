# WizePrep Dissection Report → Google Sheet staging — Altius FLE 1

**Purpose:** consolidate the WizePrep "Dissection Report" ("Why did I get this wrong?") with the
question metadata + analysis generated in this folder, so that when the review is done we can
**together** transcribe these rows into the Google Sheet error log.

**Source:** WizePrep Dissection Report → *Section 3: BBF* (screenshot 2026-06-29 8:26 PM).
**Coverage so far:** **Q1–Q24** (the screenshot cut off there; Q25+ still to capture).
**Sheet schema (target columns):** Date · Section · Source · WizePrepLoc · Q# · Mode · Topic ·
Subtopic · Knowledge(x) · Skills(x) · Slip(x) · Description · Action type · Action · Action done? ·
What did you do?

**Constants for every row below:** Date = `2026-06-29` · Section = `BB` · Source = `Altius`.
**Mode** = `Marked` only where WizePrep showed the yellow "marked" result; else `Unmarked`.
"Why" text is **verbatim** from WizePrep (her words). Topic/Subtopic filled where we transcribed the
question; `TBD` where not. Action type is a *suggestion* to confirm together.

### ⚠️ Reconciliation notes (resolve before writing to the sheet)
- **Q9 = correct (marked/guessed), NOT a miss.** Remove from the local Question Misses sheet.
- **Q3, Q5 = Passage 1 misses** not yet transcribed — no Topic/Subtopic captured. Park or transcribe later.
- Several misses are on **content not yet covered in WizePrep** → per her rule these → Action type
  `learn` = **parking lot**, not deep-dive now. Flagged per row.

---

## Status table (at a glance) — the single tracker

*(This replaces the old `Question Misses` + `Reasoning Patterns` xlsx tabs — one home now.)*

| Q# | P# | Result | Cause | Topic / Subtopic | Pattern / note | Action type | Status |
|----|----|--------|-------|------------------|----------------|-------------|--------|
| 3  | 1 | ✗ miss | Skills | TBD | misjudged what knowledge was needed (assumed outside knowledge vs. use passage) | practice | open |
| 5  | 1 | ✗ miss | Knowledge | TBD (immune cells) | uncovered content | **learn → park** | open |
| 6  | 2 | ✓ marked | Knowledge | TBD (neurons) | guessed; uncovered | **learn → park** | open |
| 7  | 2 | ✗ miss | Knowledge | Genetic Code / 98 Central Dogma | sense/antisense recall | memorize | carded |
| 8  | 2 | ✗ miss | Skills | Nervous Sys S&F / 1085 | causation vs correlation | practice | studied |
| 9  | 2 | ✓ marked | Knowledge | Transcription / 1116 | guessed; uncovered | **learn → park** | open |
| 10 | 2 | ✗ miss | Knowledge | Transcription / 1116 | sense/antisense recall | memorize | carded |
| 11 | – | ✗ miss | Knowledge | Separations / 1103 *(Orgo)* | chromatography matching | memorize | carded |
| 12 | – | ✓ marked | Knowledge | Membrane organelles / 253 | guessed; ATP synthase location | memorize | carded |
| 15 | 3 | ✗ miss | Slip | Prokaryote G&P / 1113 | couldn't see table option | practice | studied |
| 16 | 3 | ✗ miss | Skills | Prokaryote G&P / 1113 | **didn't fully use the data** (scan whole table) | practice | studied |
| 18 | 3 | ✗ miss | Skills | Prokaryote G&P / 1113 | **didn't fully use the data** (units mg/µg) | practice | studied |
| 19 | 4 | ✗ miss | Knowledge | Immune System / 395 | innate vs adaptive | memorize/park | carded |
| 21 | 4 | ✗ miss | Knowledge | Nerve Cell / 337 | histone location; neuron anatomy | learn/memorize | carded |
| 22 | 4 | ✗ miss | Skills | DNA Replication / 92 | **didn't fully use the passage** (stated 3×) | practice | studied |
| 24 | 5 | ✗ miss | Skills | Skin System / 482 | **didn't map causal chain** (↑Cldn→↑barrier) | practice | studied |

*Status legend:* `open` = not yet worked · `studied` = explained here · `carded` = flashcard queued · `learn → park` = uncovered, defer.

## Reasoning patterns (where I keep going wrong)

1. **Didn't fully use the passage / data — Q16, Q18, Q22, Q24 (4× = dominant leak).** All share one fix:
   **externalize the logic on scratch paper** — scan every row, write the units, note every confirmation,
   draw the ↑/↓ causal chain — *before* choosing.
2. **Causation vs. correlation — Q8.** A dose-response is stronger evidence of causation than an association.
3. **Misjudged required knowledge — Q3.** Answer from the passage; don't assume you need outside facts.

*(Knowledge gaps are remediated by studying/learning, not drilled as patterns — see the status table.)*

---

## Passage 1 (Q1–5) — *not transcribed in this folder*

### Q3 — ✗ Missed · Unmarked · Topic/Subtopic: TBD
- **K / S / Slip:** Skills ✗
- **Why (verbatim):** "I got confused about what the question was asking me. I thought that I was supposed to know from just the letters and numbers alone which was most likely to infect ferrets. Additionally, I thought for some reason it was asking about swine? so I got confused. Well, i think because I thought it was asking about swine and ther isnt much info about swine viruses in the passage, ai thought I needed ot inherently know what the letters and nubmers mean anduse that knowledge to answer the question. This was reasoning within the passage error."
- **Action type (suggest):** practice (passage reasoning — "answer from the passage, not assumed outside knowledge")

### Q5 — ✗ Missed · Unmarked · Topic/Subtopic: TBD (immune cells)
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "knowledge miss. I do not know about immune cells. need to learn this, havent covered it yet."
- **Action type (suggest):** **learn → parking lot** (not covered in WizePrep)

---

## Passage 2 (Q6–10) — Agrin / dendritic spines

### Q6 — ✓ Correct (guessed) · **Marked** · Topic/Subtopic: TBD (neurons; pre/post-synaptic)
- **K / S / Slip:** Knowledge ✗ (gap, but answered correctly)
- **Why (verbatim):** "guessed correctly, inferred form image the answer partially but had to guess between pre synaptic and post synaptic. havent covered neurons yet in wizeprep contnet"
- **Action type (suggest):** **learn → parking lot** (neurons not covered). *Optional log (correct).*

### Q7 — ✗ Missed · Unmarked · Topic 26 Genetic Code / Subtopic 98 Central Dogma
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "content miss. i couldnt recall the difference between the sense strand and antisense strand, so i had a hard time reasoning without that knowledge"
- **Action type (suggest):** memorize/review (sense vs antisense — studied here; **flashcard queued**)

### Q8 — ✗ Missed · Unmarked · Topic 132 Nervous System: Structure & Function / Subtopic 1085
- **K / S / Slip:** Skills ✗
- **Why (verbatim):** "reasoning within the passage. Did not occur to me to think about correlation versus causation. need to understand that dosage is stronger evidence of causation. i originally thought that like using a drug somehow would cloud the results - like, how do we know its not the durg which causes the outcome? But in reality, it's more like we know what the drug does. Therefore, we administer the drug it causes the effect and then the effect of that is stronger evidence."
- **Action type (suggest):** practice (causation vs correlation; dose-response = stronger evidence)

### Q9 — ✓ Correct (guessed) · **Marked** · Topic 27 Transcription / Subtopic 1116
- **K / S / Slip:** Knowledge ✗ (gap, but answered correctly)
- **Why (verbatim):** "guessed randomly got correct. didnt know this content, willlearn in lecture."
- **Action type (suggest):** **learn → parking lot.** *Optional log (correct).*

### Q10 — ✗ Missed · Unmarked · Topic 27 Transcription / Subtopic 1116
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "knowledge. did not know what sense and anti sense strands were."
- **Action type (suggest):** memorize/review (sense/antisense — **same card as Q7**)

---

## Discrete questions (Q11–14)

### Q11 — ✗ Missed · Unmarked · Topic 178 Separations & Purifications / Subtopic 1103 · *Discipline: Organic Chem (weakness)*
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "knowledge, couldnt recall all the chromatogrophy methods. and i didnt know what an affinity tag was. i had never heard of metal affinity chromatography so i eliminated that answer"
- **Action type (suggest):** memorize (chromatography method ↔ property; His-tag/Ni²⁺ — **flashcard queued**)

### Q12 — ✓ Correct (guessed) · **Marked** · Topic 46 Membrane-Bound Organelles / Subtopic 253 Mitochondria
- **K / S / Slip:** Knowledge ✗ (gap, but answered correctly)
- **Why (verbatim):** "guessed correctly. knowledge, did not remember the location of this part of the ATP production process"
- **Action type (suggest):** memorize (mitochondrial anatomy; ATP synthase F₀/F₁ — **flashcards queued**). *Optional log (correct).*

*(Q13, Q14 — correct, no note.)*

---

## Passage 3 (Q15–18) — Amazonian plant antimicrobials

### Q15 — ✗ Missed · Unmarked · Topic 123 Growth & Physiology of Prokaryotic Cells / Subtopic 1113
- **K / S / Slip:** Slip ✗
- **Why (verbatim):** "slip - could not identify all of the options on the table. like, i visually could not see it. i would have picked it if i had seen it in the tabl"
- **Action type (suggest):** practice (test-taking: scan/cross-reference the full table)

### Q16 — ✗ Missed · Unmarked · Topic 123 / Subtopic 1113
- **K / S / Slip:** Skills ✗ (strategy)
- **Why (verbatim):** "straight up guesed i think. didnt really know how to answer tihs. i think i failed ot see that there was one extract that was in all of the categories"
- **Action type (suggest):** practice (scan the whole table before answering — "didn't fully use the data")

### Q17 — ✓ Correct · no note.

### Q18 — ✗ Missed · Unmarked · Topic 123 / Subtopic 1113
- **K / S / Slip:** Skills ✗ (she debated "slip")
- **Why (verbatim):** "slip i guess? i mean, i just didnt notice the units. so maybe i wouldnt say slip. I should have read the passage more carefully if I had read the passage more carefully then I would have noticed the mismatch between the units however, I don't know if I would've known that this mismatch was significant. In a sense, this was kind of a trick question however, I should've read the passage more carefully, and then used all the numbers from the passage to do the math and determine the right answer"
- **Action type (suggest):** practice (unit awareness mg vs µg; "use ALL the numbers")

---

## Passage 4 (Q19–22) — Reactive gliosis / histones

### Q19 — ✗ Missed · Unmarked · Topic 141 Immune System / Subtopic 395 Innate vs adaptive
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "knowledge, idk about immunity"
- **Action type (suggest):** **learn → parking lot** if immunity uncovered; else memorize (innate vs adaptive — **flashcard queued**). *Immune System = weakest BB topic.*

### Q20 — ✓ Correct · no note.

### Q21 — ✗ Missed · Unmarked · Topic 133 Nerve Cell / Subtopic 337 Cell body
- **K / S / Slip:** Knowledge ✗
- **Why (verbatim):** "knowledge, havent learned structure of a neuron yet."
- **Action type (suggest):** **learn → parking lot** (neuron structure not covered); histone-location fact **carded**

### Q22 — ✗ Missed · Unmarked · Topic 24 DNA Replication / Subtopic 92
- **K / S / Slip:** Skills ✗
- **Why (verbatim):** "reasoning and also not reading the passage close enough. and i also thought that representative meant that it only represented the toxin, not like the medium representedthe toxin because it literally had the toxin in it."
- **Action type (suggest):** practice (use ALL the passage; let figures/text resolve ambiguous wording) + memorize (histones bind DNA — **carded**)

---

## Passage 5 (Q23–27) — Claudins / skin barrier

### Q23 — ✓ Correct · no note. *(But: start/stop codon **flashcard queued** — right by elimination, real gap.)*

### Q24 — ✗ Missed · Unmarked · Topic 148 Skin System / Subtopic 482
- **K / S / Slip:** Skills ✗
- **Why (verbatim):** "I did not reason about this correctly. I think I also got confused on how the enterotoxin of the bacterium, blah blah blah like actually related to the information in the passage I think if I had just written down the causes of things on a piece of paper I would've been able to connect that CLDN goes up then barrier function is enhanced"
- **Action type (suggest):** practice (write the causal chain with ↑/↓ arrows before answering)

---

## Summary tally (Q1–24 of BBF)

- **Misses (13):** Q3, Q5, Q7, Q8, Q10, Q11, Q15, Q16, Q18, Q19, Q21, Q22, Q24
- **Marked + guessed correct (3):** Q6, Q9, Q12 (knowledge gaps worth optional logging)
- **Clean correct (8):** Q1, Q2, Q4, Q13, Q14, Q17, Q20, Q23

**By cause (her labels):** Knowledge ≈ Q5, Q7, Q10, Q11, Q19, Q21 (+ guessed Q6, Q9, Q12) ·
Skills/Reasoning ≈ Q3, Q8, Q16, Q18, Q22, Q24 · Slip ≈ Q15.

**Strategic read:** a large share of the *knowledge* misses are on **content not yet covered in
WizePrep** (immune cells, neurons, transcription details) → these are **parking-lot `learn` rows**,
deferred, NOT deep-dive targets now. The deep-dive targets are the **Skills/reasoning** rows on
covered material — which is where the "externalize the logic on scratch paper" habit pays off.
