import requests

r = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki is not running or AnkiConnect is not installed"
print("AnkiConnect connected.")

DECK = "MCAT Physics"

front = r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydraulic System</b><br><br>What are the equations governing a <span style='color: #4a90d9;'>hydraulic system</span>?</div>"

back = r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydraulic System</b><br><br><span style='font-size: 14px; color: #555;'>All-in-one relationship:</span><br>\[\frac{F_2}{F_1} = \frac{A_2}{A_1} = \frac{d_1}{d_2}\]<br><br><span style='font-size: 14px; color: #555;'>Component equations:</span><br><span style='font-size: 14px;'>Pressure (Pascal): &nbsp;\(\dfrac{F_1}{A_1} = \dfrac{F_2}{A_2}\)</span><br><span style='font-size: 14px;'>Volume conservation: &nbsp;\(A_1 d_1 = A_2 d_2\)</span><br><span style='font-size: 14px;'>Work conservation: &nbsp;\(F_1 d_1 = F_2 d_2\)</span><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>F</b></td><td>force on piston &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>A</b></td><td>piston area &mdash; m&sup2;</td></tr><tr><td style='padding: 4px 10px;'><b>d</b></td><td>piston displacement &mdash; meters (m)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Larger output force = smaller input force &times; (A<sub>2</sub>/A<sub>1</sub>); you gain force but lose distance</span></div>"

tags = ["physics::equation", "physics::fluids::pressure"]

note_id = 1780262264954  # Hydraulic System card
print(f"Updating note {note_id}")

# Update
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
result = r.json()
if result["error"] is None:
    print(f"Card {note_id} updated successfully.")
else:
    print(f"ERROR: {result['error']}")
