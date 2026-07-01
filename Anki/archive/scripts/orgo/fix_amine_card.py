import requests, sys
sys.path.insert(0, "/Users/abigailbliss/Documents/MCAT/Anki")
from orgo_helpers import render_and_store, assert_connected, validate

assert_connected()

# Generic primary amine: R-NH2 with wildcard labeled "R"
img = render_and_store("amine-generic", "[*][NH2]", dummy_labels=["R"])
print("Image snippet:", img)

front = r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Amine</b><br><br>What is its <span style='color: #4a90d9;'>structure</span>?</div>"

back = (
    r"""<div style="font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;"><b>Amine</b><br><br>"""
    + img +
    r"""<br><table style="margin: auto; text-align: left; font-size: 15px;"><tbody><tr><td style="padding: 4px 10px;"><b>Group</b></td><td>an amino group (&ndash;NH<sub>2</sub>) &mdash; nitrogen bonded to carbon</td></tr><tr><td style="padding: 4px 10px;"><b>Naming</b></td><td><i>-amine</i></td></tr><tr><td style="padding: 4px 10px;"><b>Example</b></td><td>ethylamine (CH<sub>3</sub>CH<sub>2</sub>NH<sub>2</sub>)</td></tr></tbody></table><br><span style="font-size: 13px; color: #888;">Basic &mdash; the N lone pair accepts a proton</span></div>"""
)

validate(front, back)

r = requests.post("http://localhost:8765", json={
    "action": "updateNote",
    "version": 6,
    "params": {
        "note": {
            "id": 1781046024480,
            "fields": {"Front": front, "Back": back},
            "tags": ["orgo::definition", "orgo::functional-groups"]
        }
    }
})
print("Update result:", r.json())
