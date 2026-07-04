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

# Load cards from file (tab-separated: front \t back \t tag1 tag2)
cards = []
with open("cards text files/optics_cards.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        front, back, tag_str = parts[0], parts[1], parts[2]
        tags = tag_str.split()
        # Extract a short keyword from the front for duplicate lookup
        import re
        title_match = re.search(r'<b>(.*?)</b>', front)
        keyword = title_match.group(1).replace("&amp;", "").replace(" ", "_")[:20] if title_match else "unknown"
        cards.append({"front": front, "back": back, "tags": tags, "keyword": keyword})

# New sign convention card (card 15)
cards.append({
    "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Optics Sign Convention</b><br><br>What do the signs of <span style='color: #4a90d9;'>f</span>, <span style='color: #4a90d9;'>d<sub>i</sub></span>, and <span style='color: #4a90d9;'>m</span> tell you in mirrors and lenses?</div>",
    "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Optics Sign Convention</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>f &gt; 0</b></td><td>Concave mirror &nbsp;|&nbsp; Converging (convex) lens</td></tr><tr><td style='padding: 5px 10px;'><b>f &lt; 0</b></td><td>Convex mirror &nbsp;|&nbsp; Diverging (concave) lens</td></tr><tr><td style='padding: 5px 10px; border-top: 1px solid #ddd;'><b>d<sub>i</sub> &gt; 0</b></td><td>Real image</td></tr><tr><td style='padding: 5px 10px;'><b>d<sub>i</sub> &lt; 0</b></td><td>Virtual image</td></tr><tr><td style='padding: 5px 10px; border-top: 1px solid #ddd;'><b>m &gt; 0</b></td><td>Upright image</td></tr><tr><td style='padding: 5px 10px;'><b>m &lt; 0</b></td><td>Inverted image</td></tr></table><br><span style='font-size: 14px; color: #555;'>Real image &rarr; always inverted (m &lt; 0) &nbsp;|&nbsp; Virtual image &rarr; always upright (m &gt; 0)</span><br><br><table style='margin: auto; text-align: left; font-size: 14px;'><tr><td style='padding: 4px 10px;'><b>Mirrors:</b></td><td>Real image forms <b>in front</b> (same side as object)</td></tr><tr><td style='padding: 4px 10px;'><b>Lenses:</b></td><td>Real image forms on <b>opposite side</b> from object</td></tr></table><br><span style='font-size: 13px; color: #888;'>d<sub>o</sub> is always positive for a real object &nbsp;&bull;&nbsp; convex mirror and concave lens always produce virtual images</span></div>",
    "tags": ["physics::concept", "physics::optics::lenses"],
    "keyword": "Optics_Sign"
})

print(f"Loaded {len(cards)} cards. Validating...")
for i, c in enumerate(cards):
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
