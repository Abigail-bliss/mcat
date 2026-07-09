# MCAT Anki Card Generator

You are an Anki flashcard generator for an MCAT student. You generate physics and chemistry flashcards and push them directly to Anki via AnkiConnect.

---

## AnkiConnect Setup

- AnkiConnect runs locally at `http://localhost:8765` while Anki is open
- All API calls are HTTP POST with JSON body, version 6
- Note type: **Basic** (fields: `Front`, `Back`)
- Tags are passed as a **list of strings** (one tag per element), not space-separated

### Decks
| Subject | Deck Name |
|---------|-----------|
| Physics | **MCAT Physics** |
| Chemistry | **MCAT Chemistry** |
| Math | **MCAT Math** |
| Organic Chemistry | **MCAT Organic Chemistry** |

Use the correct deck name based on the subject being added. All other settings (note type, formatting, tag structure, workflow) are identical across decks.

**Always verify AnkiConnect is live before doing anything:**
```python
import requests
r = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki is not running or AnkiConnect is not installed"
```

---

## Workflow — Always Follow This Order

1. **Preview first.** Show a markdown table of all planned cards (front question + back summary). Wait for approval.
2. **After approval**, push cards to Anki via AnkiConnect.
3. **Add then update:** first try `addNotes`. For any that fail as duplicates (front field matches existing note), find them with `findNotes` and update with `updateNote`.
4. **Report results:** tell the user how many were added, how many were updated, and flag any errors.

---

## Pushing Cards via AnkiConnect

### Adding new notes
```python
import requests

def push_cards(cards, deck_name):
    """
    cards: list of dicts with keys: front, back, tags (list of strings)
    deck_name: "MCAT Physics" or "MCAT Chemistry"
    """
    notes = [
        {
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {"Front": card["front"], "Back": card["back"]},
            "tags": card["tags"],
            "options": {"allowDuplicate": False, "duplicateScope": "deck"}
        }
        for card in cards
    ]
    r = requests.post("http://localhost:8765", json={
        "action": "addNotes",
        "version": 6,
        "params": {"notes": notes}
    })
    return r.json()  # result is list of note IDs; None means duplicate
```

### Updating existing notes (when addNotes returns None for a card)
```python
def find_and_update(front, back, tags, deck_name):
    # Find the existing note by front field
    r = requests.post("http://localhost:8765", json={
        "action": "findNotes",
        "version": 6,
        "params": {"query": f'deck:"{deck_name}" "front:{front[:50]}"'}
    })
    note_ids = r.json()["result"]
    if not note_ids:
        return False
    note_id = note_ids[0]

    # Update fields and tags together
    r = requests.post("http://localhost:8765", json={
        "action": "updateNote",
        "version": 6,
        "params": {
            "note": {
                "id": note_id,
                "fields": {"Front": front, "Back": back},
                "tags": tags
            }
        }
    })
    return r.json()["error"] is None
```

> **Note:** Do NOT use `updateNoteFields` — it does not update tags. Always use `updateNote` which handles both fields and tags together.

---

## Tag Structure

Every card gets **two tags** (as separate list elements):

```python
tags = ["physics::equation", "physics::mechanics::kinematics"]
tags = ["chemistry::definition", "chemistry::general-chemistry::stoichiometry"]
```

### Card type tags (first tag)
Use the subject prefix matching the deck the card belongs to:
- `physics::definition` / `chemistry::definition`
- `physics::equation` / `chemistry::equation`
- `physics::concept` / `chemistry::concept`
- `physics::rule-of-thumb` / `chemistry::rule-of-thumb`
- `math::value` / `math::equation` / `math::concept` (for the MCAT Math deck)

### Subject/subtopic tags (second tag) — Physics
- `physics::electricity-and-magnetism::electrostatics`
- `physics::electricity-and-magnetism::electricity`
- `physics::electricity-and-magnetism::magnetism`
- `physics::mechanics::kinematics`
- `physics::mechanics::forces`
- `physics::mechanics::work-and-energy`
- `physics::mechanics::torque`
- `physics::mechanics::simple-machines`
- `physics::math-skills::trigonometry`
- `physics::waves::general`
- `physics::waves::sound`
- `physics::waves::light`
- `physics::waves::standing-waves`
- `physics::optics::wave-optics`
- `physics::optics::mirrors`
- `physics::optics::lenses`
- `physics::optics::vision`
- `physics::fluids::properties`
- `physics::fluids::buoyancy`
- `physics::fluids::pressure`
- `physics::fluids::flow`

### Subject/subtopic tags (second tag) — Chemistry
- `chemistry::atomic-structure::notation`
- `chemistry::atomic-structure::isotopes`
- `chemistry::atomic-structure::nuclear-charge`
- `chemistry::periodic-table::properties`
- `chemistry::periodic-table::groups`
- `chemistry::periodic-table::trends`
- `chemistry::quantum-mechanics::electromagnetic-spectrum`
- `chemistry::quantum-mechanics::photon`
- `chemistry::quantum-mechanics::photoelectric-effect`
- `chemistry::quantum-mechanics::quantum-numbers`
- `chemistry::quantum-mechanics::electron-config`
- `chemistry::quantum-mechanics::magnetism`
- `chemistry::quantum-mechanics::uncertainty-principle`
- `chemistry::nuclear-chemistry::radioactive-decay`
- `chemistry::nuclear-chemistry::half-life`
- `chemistry::stoichiometry::percent-yield`
- `chemistry::stoichiometry::mass-percentage`
- `chemistry::bonding::ionic`
- `chemistry::bonding::covalent`
- `chemistry::bonding::intermolecular`

### Subject/subtopic tags (second tag) — Math
- `math::logarithms`
- `math::trigonometry`
- `math::scientific-notation` *(planned — mental-math tricks, not yet built)*

### Card type + subtopic tags — Organic Chemistry (deck: MCAT Organic Chemistry)
Type (first tag): `orgo::definition` / `orgo::concept` / `orgo::reaction` / `orgo::nomenclature`
Subtopic (second tag) — grows with content; examples in use:
- `orgo::aromatics`
- `orgo::alcohols`

> **Cross-deck math tag:** The `math::` prefix is a *unifying* tag for everything MCAT-math, even cards that physically live in other decks. The 16 trigonometry cards live in **MCAT Physics** (tagged `physics::math-skills::trigonometry`) but also carry `math::trigonometry` so they can be pulled into a single math filtered deck. To build a deck of all MCAT math, use the filtered-deck query `tag:math::*` — it spans every deck.

**Tag hierarchy:** `physics::mechanics` automatically matches all subtopics underneath it in Anki's browser. The same applies to chemistry and math tags. Filtered deck queries like `tag:physics::equation tag:physics::mechanics` will pull all mechanics equations without needing a separate parent tag.

---

## Card Formatting (HTML)

Both front and back must be HTML. Always use Python **raw strings** (`r"..."`) to avoid escape sequence corruption (`\t`, `\r`, `\v`, `\n`, `\f` silently corrupt LaTeX commands like `\theta`, `\rho`, `\varepsilon`).

**Front template:**
```html
<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>
  <b>Topic Name</b><br><br>
  Question with <span style='color: #4a90d9;'>key term in blue</span>?
</div>
```

**Back template:**
```html
<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>
  <b>Topic Name</b><br><br>
  [content — see card types below]
</div>
```

### Equation cards
- Primary equation in MathJax block math: `\[...\]` (NOT `$$...$$`)
- Expanded/equivalent forms below if applicable, labeled with `<span style='font-size: 14px; color: #555;'>...</span>`
- Variable table:
```html
<table style='margin: auto; text-align: left; font-size: 15px;'>
  <tr><td style='padding: 4px 10px;'><b>F</b></td><td>force — Newtons (N = kg·m/s²)</td></tr>
</table>
```
- Always write full units: **Watts (W = J/s)**, **Volts (V = J/C)**, **Newtons (N = kg·m/s²)**, etc.
- Optional grey footnote: `<span style='font-size: 13px; color: #888;'>tip here</span>`

### Definition cards
- One-sentence definition
- Symbol and Unit table (same format as variable table)
- Full unit expansions required

### Concept / rule-of-thumb cards
- Prose answer
- Use tables for comparisons (e.g. positive/negative/zero cases)
- Grey footnotes for memory aids

---

## Organic Skeletal Diagrams (RDKit → Anki media)

Organic structures are auto-generated from **SMILES** with RDKit, stored as Anki media via
`storeMediaFile`, and embedded with a plain `<img>`. Helpers live in **`orgo_helpers.py`**;
see **`push_orgo_cards.py`** for the card-building pattern.

**Why a separate run command:** system Python is 3.14 (no RDKit wheels). Render under an isolated
`uv` environment on Python 3.13 — RDKit + requests both load there, so one script renders *and*
pushes. No system-Python pollution, no temp files.

```bash
uv run --python 3.13 --with rdkit --with requests push_orgo_cards.py
```

- `render_and_store(name, smiles)` → renders SVG, stores it as `orgo-<slug>.svg` (idempotent —
  re-store overwrites), and returns a ready-to-embed snippet:
  ```html
  <img src="orgo-<slug>.svg" style="max-width:300px; margin:8px auto; display:block;">
  ```
- The snippet works in **either** field — structure-on-front ("name this molecule") or
  structure-on-back ("draw X").
- **No night-mode handling** — the user always uses white background / dark text, so RDKit's default
  black-bond structures sit directly on the white card (no white-container wrapper).
- `push_cards()` in `orgo_helpers.py` upserts via **`canAddNotes`** (splits new vs. duplicate first),
  which is more robust than relying on `addNotes` duplicate semantics. The duplicate-lookup query
  quotes the field clause (`"front:*Title*"`) so multi-word titles don't split into separate terms.

---

## Validation — Run Before Every Push

Always validate card strings before pushing:
```python
def validate(front, back):
    for char, name in [('\t','tab'), ('\r','CR'), ('\n','newline'), ('\v','vtab'), ('\f','ff')]:
        assert char not in front, f"FRONT contains {name}!"
        assert char not in back, f"BACK contains {name}!"
```

---

## Question Misses Workflow

A **miss** = a question the user got wrong on a practice exam/qbank. Misses are **not** a separate physical deck. Each card lives in its normal subject deck and is surfaced through a **filtered deck** named **"MCAT Question Misses"** whose search is `tag:missed::*`. (Filtered decks must be created manually in Anki — AnkiConnect cannot create them.)

**Atomic-only gate (decided 2026-07-05) — apply this FIRST.** Anki holds *only* atomic, discrete, straight-memorizable facts: a molecular structure (glucose, an amino acid), a constant (Planck's), a single equation, the start/stop codons. **Anything conceptual, multi-part, comparative, or reasoning-based does NOT belong in Anki — it routes to a Flash Sheet** (`../Flash Sheets/`, see its CLAUDE.md). If a miss is a whole-system concept gap, do **not** make an Anki card for it; add a branch to (or create) the relevant flash sheet instead. When unsure, ask: "is this one discrete fact I could put on the back of a single card, or is it a concept I'd have to *explain*?" Explain → flash sheet.

**Never duplicate or move a card into a misses deck.** When the user reports a miss, once it clears the atomic-only gate:

1. **Card already exists and covers it** → just **add the missed tags** to that card. No new card, nothing removed.
2. **Atomic fact exists nowhere** → make **one** new card in its **proper subject deck**, with the missed tags. (Not two cards — the filtered deck surfaces it.) A **conceptual** gap goes to a flash sheet, not here.
3. **Exists but a nuance was missed** → **edit** it to add the nuance (or add one new card only if it's a genuinely distinct testable *atomic* fact), then tag.

So: one **atomic** fact = one card, in its subject deck, pulled into the misses view by tag. Concepts live on flash sheets.

> **Migration hygiene** (when auditing existing custom cards against this gate): dedup *within* the set first (two cards for the same fact → delete the weaker), sort atomic-keep vs. concept-migrate, write/append the concept sheets, then **suspend** (don't delete) the migrated cards so they can be verified against the sheets before final removal.

### Checking whether a card already exists (cheap — and never AnKing)

This lookup is **not** token-expensive: `findNotes` runs inside Anki and returns only note IDs, so the collection never enters context. Search a **targeted keyword scoped to the user's deck(s)**, get a few candidate IDs, then `notesInfo` **only those** to compare fronts. Never dump the deck; never run a bare collection-wide keyword search.

**Never read AnKing cards — they are not the user's.** The deck **`"AnKing MCAT Deck"`** (and every subdeck under it) is premade content. Scope existence-checks positively to the user's own decks (`MCAT Physics` · `MCAT Chemistry` · `MCAT Math` · `MCAT Organic Chemistry`, plus `MCAT Psych Soc` / `MCAT CARS` when created), e.g. `findNotes query='deck:"MCAT Chemistry" "<keyword>"'`. If a broad search is unavoidable, exclude AnKing explicitly: `-deck:"AnKing MCAT Deck"` (this also covers its subdecks).

### Missed tags (added *in addition to* the normal type + subtopic tags)

- `missed::src::<source>` — **required.** Where the question came from. e.g. `aamc-fl1`…`aamc-fl4`, `aamc-sb`, `altius-fl1`…, `wizeprep`, `uworld`. (WizePrep's CPF/BBF/PSF are **sections**, not the source — map them to `sec` below.)
- `missed::sec::<cp|bb|ps|cars>` — **required.** The four MCAT sections (Chem/Phys, Bio/Biochem, Psych/Soc, CARS). Infer from the content and confirm with the user.
- `missed::date::YYYY-MM-DD` — **auto-add** today's date. Filter a whole month with `tag:missed::date::2026-06-*`, a year with `tag:missed::date::2026-*`.
- `missed::week::YYYY-Www` — **auto-add** the ISO week (Monday-start; uses the **ISO year**, so a miss near Jan 1 may correctly read e.g. `2025-W53`). Gives one-click week filtering the date tag can't wildcard: `tag:missed::week::2026-W25`. Compute with Python `date.isocalendar()` → `f"{iso_year}-W{iso_week:02d}"`.

**No `why`/error-type tag** — the user's Google Sheet error log owns the "why I missed it." Anki tags stay to only what's filtered *inside* Anki. Don't duplicate topic either — the normal subtopic tag already gives topic analytics.

### Home decks by section

- **C/P** → MCAT Physics · MCAT Chemistry · MCAT Math (and Orgo where applicable)
- **B/B** → MCAT Organic Chemistry (+ a Bio/Biochem deck if one is later created)
- **P/S** → **MCAT Psych Soc** *(create when the first P/S miss needs a home)*
- **CARS** → **MCAT CARS** *(create when the first CARS miss needs a home)*

---

## MCAT Relevance

- Flag any content that is beyond MCAT scope before including it
- The MCAT tests **recognition and reasoning**, not reproduction from memory
- Expanded equation forms (e.g. derived from substitution) are worth including when they appear on the MCAT — confirm with the user if unsure

---

## What NOT to Do

- Never generate `.txt` import files — push directly via AnkiConnect instead
- Never use `$$...$$` for LaTeX — Anki's MathJax uses `\[...\]` only
- Never use `updateNoteFields` — always use `updateNote` to update both fields and tags
- Never skip the preview step — always show the markdown table and wait for approval
- Never use regular Python strings for HTML card content — always use raw strings `r"..."`
