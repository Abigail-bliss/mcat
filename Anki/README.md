# MCAT Anki — Folder Layout

Everything for **making cards** and **driving the AnKing deck** lives here. The study
*journey* (plans, progress, scores, error log) now lives in a sibling folder,
`../mcat-journey/`. See `CLAUDE.md` for the full card workflow, tags, and formatting rules.

## Layout

| File / folder | Purpose |
|---------------|---------|
| `CLAUDE.md` | Card-creation instructions (workflow, decks, tags, formatting). |
| `card-creation/` | All build/push scripts + helpers (grouped). |
| `biochem_images/` | **Screenshot destination** — macOS screenshots auto-save here; build scripts pin them by timestamp. `used/` holds processed shots. **Do not move** (helpers resolve it one level up via `__file__`). |
| `anking-unsuspend/` | The AnKing **suspend/unsuspend mechanism**: its own `CLAUDE.md` directive + `progress.md` batch log. |
| `archive/` | Historical, run-once material (see below). |

### card-creation/
| File | Purpose |
|------|---------|
| `push_biochem_cards.py` | **Active** build/push for the MCAT Biochemistry deck. Run: `cd card-creation && uv run --python 3.13 --with rdkit --with requests push_biochem_cards.py` |
| `biochem_helpers.py` | Biochem helpers (screenshot media, RDKit render, upsert). Imported by `push_biochem_cards.py`. |
| `orgo_helpers.py` | Organic Chemistry helpers (RDKit skeletal structures). |
| `push_orgo_cards.py` | Reference pattern for the MCAT Organic Chemistry deck. |

> Run scripts **from inside `card-creation/`** so co-located `import orgo_helpers` /
> `import biochem_helpers` resolve. The helpers find `biochem_images/` at the `Anki/` root.

## archive/

Historical, run-once material. The cards these created already live in Anki — the
source of truth is the Anki collection, not these scripts.

- `scripts/{physics,chemistry,orgo,biochem}/` — one-time push/build/fix scripts, by subject.
- `assets/svg/` — generated diagram sources (Fischer/stereo/chair/sugar SVGs).
- `assets/verify-renders/` — verification SVG→PNG renders.
- `assets/images/` — scratch images.
- `text-imports/` — old `.txt` card files (superseded; cards are now pushed directly).
- `misc/` — old deck export (`Physics.apkg`), old instruction doc.

> Archived scripts import the root helpers and were run from the old root. To rerun one,
> copy it next to the helpers in `card-creation/` so its `import orgo_helpers` /
> `import biochem_helpers` resolves.

## Sibling: ../mcat-journey/

Study-journey docs that used to live here have moved:

- `Abigail_MCAT_progress_summary.md` → `../mcat-journey/`
- study plan → `../mcat-journey/study-plan/master-study-plan.md`
- weekly templates + this-week plan → `../mcat-journey/weekly-plans/`
- `Error Log.xlsx` → `../mcat-journey/data/`
