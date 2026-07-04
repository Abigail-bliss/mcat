# Practice Exam / Question Review

**The system of record is Abigail's Google Sheet, not a file in this repo.** Don't build a
parallel tracker here — it already does everything (Knowledge/Skills/Slip split, action,
done-flag).

- **Miss-review sheet (live):** https://docs.google.com/spreadsheets/d/1GOp0fA93ItrhM6Hm_vfaNnBesbvRSbNz51m1l6C_cSk/edit
  (a static export lives at `../../00-strategy/data/Error Log.xlsx`).
- Schema: `Date · Section · Source · WizePrepLoc · Q# · Mode · Topic · Subtopic ·
  Knowledge/Skills/Slip · Description · Action type · Action · Action done? · What did you do?`

## FL dissection workflow (uses the sheet, not new files)

- Add each FL miss as a row, `Source = AAMC` (or `Altius`).
- **Deep-dive worklist** = `Action done? = no` AND `Action type ∈ {review, memorize, practice}`
  (topics already covered in WizePrep). Weakness-first.
- **Parking lot** = `Action type = learn` (not yet covered) → defer, don't self-teach.
- **Progress** = `Action done?` flipping `no → yes`. That's the whole game — the log is already
  rich; closing the loop is the gap.

## The WizePrep "dissection report"
A required form inside the WizePrep platform (not exportable). Separate obligation, not the
analytical system. Claude can draft its content from the sheet rows once its fields are known.

> PDFs of taken exams live in `../` (`Altius-FLE-1.pdf`, `FL_5-16.pdf`).
