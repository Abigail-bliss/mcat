import requests

r = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki is not running or AnkiConnect is not installed"
print("AnkiConnect connected.")

DECK = "MCAT Physics"

def validate(front, back):
    for char, name in [('\t','tab'), ('\r','CR'), ('\n','newline'), ('\v','vtab'), ('\f','ff')]:
        assert char not in front, f"FRONT contains {name}!"
        assert char not in back, f"BACK contains {name}!"

def find_and_update(front, back, tags, keyword):
    r = requests.post("http://localhost:8765", json={
        "action": "findNotes",
        "version": 6,
        "params": {"query": f'deck:"{DECK}" front:{keyword}'}
    })
    note_ids = r.json()["result"]
    if not note_ids:
        return False
    note_id = note_ids[0]
    r = requests.post("http://localhost:8765", json={
        "action": "updateNote",
        "version": 6,
        "params": {"note": {"id": note_id, "fields": {"Front": front, "Back": back}, "tags": tags}}
    })
    return r.json()["error"] is None

cards = [
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Fraction Submerged</b><br><br>What is the equation for the <span style='color: #4a90d9;'>fraction of a floating object that is submerged</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Fraction Submerged</b><br><br>\[\frac{V_{sub}}{V_{obj}} = \frac{\rho_{obj}}{\rho_{fluid}}\]<br><span style='font-size: 14px; color: #555;'>Derived from the floating condition \(F_G = F_B\):</span><br><span style='font-size: 14px;'>\(\rho_{obj} \cdot V_{obj} \cdot g = \rho_{fluid} \cdot V_{sub} \cdot g\)</span><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>V<sub>sub</sub></b></td><td>volume submerged &mdash; m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>V<sub>obj</sub></b></td><td>total volume of object &mdash; m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>obj</sub></b></td><td>density of object &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>fluid</sub></b></td><td>density of fluid &mdash; kg/m&sup3;</td></tr></table><br><span style='font-size: 13px; color: #888;'>If &rho;<sub>obj</sub> = &rho;<sub>fluid</sub>, object is fully submerged and neutrally buoyant; if &rho;<sub>obj</sub> &gt; &rho;<sub>fluid</sub>, fraction &gt; 1 &rarr; object sinks</span></div>",
        "tags": ["physics::equation", "physics::fluids::buoyancy"],
        "keyword": "Fraction"
    },
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sinking Object — Normal Force</b><br><br>What is the <span style='color: #4a90d9;'>force balance</span> for an object resting on the bottom, and how do you find the normal force?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sinking Object — Normal Force</b><br><br><span style='font-size: 14px; color: #555;'>Force balance:</span><br>\[F_G = F_B + F_N\]<br><span style='font-size: 14px; color: #555;'>Expanded:</span><br><span style='font-size: 14px;'>\(\rho_{obj} \cdot V_{obj} \cdot g = \rho_{fluid} \cdot V_{obj} \cdot g + F_N\)</span><br><br><span style='font-size: 14px; color: #555;'>Solving for normal force:</span><br>\[F_N = (\rho_{obj} - \rho_{fluid}) \cdot V_{obj} \cdot g\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>F<sub>G</sub></b></td><td>gravitational force (weight) &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>F<sub>B</sub></b></td><td>buoyant force &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>F<sub>N</sub></b></td><td>normal force from bottom &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>obj</sub></b></td><td>density of object &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>fluid</sub></b></td><td>density of fluid &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>V<sub>obj</sub></b></td><td>volume of object &mdash; m&sup3;</td></tr></table><br><span style='font-size: 13px; color: #888;'>F<sub>N</sub> is the &ldquo;apparent weight loss&rdquo; &mdash; object feels lighter underwater by exactly F<sub>B</sub></span></div>",
        "tags": ["physics::equation", "physics::fluids::buoyancy"],
        "keyword": "Sinking"
    }
]

for c in cards:
    validate(c["front"], c["back"])
print("Validation passed.")

notes = [
    {
        "deckName": DECK,
        "modelName": "Basic",
        "fields": {"Front": c["front"], "Back": c["back"]},
        "tags": c["tags"],
        "options": {"allowDuplicate": False, "duplicateScope": "deck"}
    }
    for c in cards
]

r = requests.post("http://localhost:8765", json={"action": "addNotes", "version": 6, "params": {"notes": notes}})
results = r.json()["result"]

added, updated, errors = 0, 0, []
for i, (note_id, card) in enumerate(zip(results, cards)):
    if note_id is not None:
        print(f"Card {i+1} added: {note_id}")
        added += 1
    else:
        print(f"Card {i+1} duplicate — updating...")
        success = find_and_update(card["front"], card["back"], card["tags"], card["keyword"])
        if success:
            print(f"Card {i+1} updated.")
            updated += 1
        else:
            print(f"Card {i+1} ERROR: could not find to update.")
            errors.append(i+1)

print(f"\nDone: {added} added, {updated} updated, {len(errors)} errors.")
if errors:
    print(f"Failed cards: {errors}")
