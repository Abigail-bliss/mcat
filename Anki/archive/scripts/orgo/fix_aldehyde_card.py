import requests, sys
sys.path.insert(0, "/Users/abigailbliss/Documents/MCAT/Anki")
from orgo_helpers import render_and_store

ANKI = "http://localhost:8765"

r = requests.post(ANKI, json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki not running"

# Explicit H on aldehyde carbon so diagram clearly shows R-C(H)=O, not ketone
img_snippet = render_and_store("acetaldehyde", "[H]C(=O)C")
print("Image snippet:", img_snippet)

back = r"""<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;"><b>Aldehyde</b><br><br>""" + img_snippet + r"""<br><table style="margin: auto; text-align: left; font-size: 15px;"><tbody><tr><td style="padding: 4px 10px;"><b>Group</b></td><td>a terminal carbonyl (&ndash;CHO) &mdash; a C=O at the END of the chain</td></tr><tr><td style="padding: 4px 10px;"><b>Naming</b></td><td><i>-al</i></td></tr><tr><td style="padding: 4px 10px;"><b>Example</b></td><td>acetaldehyde (CH<sub>3</sub>CHO)</td></tr></tbody></table><br><span style="font-size: 13px; color: #888;">Carbonyl carbon also carries an H</span></div>"""

r2 = requests.post(ANKI, json={
    "action": "updateNote",
    "version": 6,
    "params": {
        "note": {
            "id": 1781046024232,
            "fields": {
                "Front": "<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Aldehyde</b><br><br>What is its <span style='color: #4a90d9;'>structure</span>?</div>",
                "Back": back
            },
            "tags": ["orgo::definition", "orgo::functional-groups"]
        }
    }
})
print("Update result:", r2.json())
