import requests

r = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki is not running or AnkiConnect is not installed"
print("AnkiConnect connected.")

def validate(front, back):
    for char, name in [('\t','tab'), ('\r','CR'), ('\n','newline'), ('\v','vtab'), ('\f','ff')]:
        assert char not in front, f"FRONT contains {name}! Card: {front[:40]}"
        assert char not in back, f"BACK contains {name}! Card: {front[:40]}"

def push_cards(cards):
    notes = [
        {
            "deckName": "Physics",
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
    return r.json()

def find_and_update(front, back, tags):
    r = requests.post("http://localhost:8765", json={
        "action": "findNotes",
        "version": 6,
        "params": {"query": f'deck:Physics "front:{front[:50]}"'}
    })
    note_ids = r.json()["result"]
    if not note_ids:
        return False
    note_id = note_ids[0]
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

cards = [
    # Card 1: Ideal Fluid
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Ideal Fluid</b><br><br>What are the <span style='color: #4a90d9;'>four properties of an ideal fluid</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Ideal Fluid</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Incompressible</b></td><td>Density is constant; volume does not change under pressure</td></tr><tr><td style='padding: 6px 10px;'><b>Non-viscous</b></td><td>No internal friction between fluid layers</td></tr><tr><td style='padding: 6px 10px;'><b>Laminar flow</b></td><td>Smooth, orderly layers; no turbulence</td></tr><tr><td style='padding: 6px 10px;'><b>Irrotational</b></td><td>No swirling or eddies at any point</td></tr></table><br><span style='font-size: 13px; color: #888;'>Real fluids approximate ideal behavior at low speeds in smooth channels</span></div>",
        "tags": ["physics::concept", "physics::fluids::properties"]
    },
    # Card 2: Specific Gravity
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Specific Gravity</b><br><br>What is <span style='color: #4a90d9;'>specific gravity</span> and what does it predict about sinking vs floating?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Specific Gravity</b><br><br>\[SG = \frac{\rho_{obj}}{\rho_{water}}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>SG &gt; 1</b></td><td>Denser than water &rarr; sinks</td></tr><tr><td style='padding: 6px 10px;'><b>SG &lt; 1</b></td><td>Less dense than water &rarr; floats</td></tr><tr><td style='padding: 6px 10px;'><b>SG = 1</b></td><td>Same density as water &rarr; neutral buoyancy</td></tr></table><br><span style='font-size: 13px; color: #888;'>SG is dimensionless; &rho;<sub>water</sub> = 1000 kg/m&sup3; at standard conditions</span></div>",
        "tags": ["physics::definition", "physics::fluids::properties"]
    },
    # Card 3: Adhesion & Cohesion
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Adhesion &amp; Cohesion</b><br><br>What is <span style='color: #4a90d9;'>adhesion</span> and what is <span style='color: #4a90d9;'>cohesion</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Adhesion &amp; Cohesion</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Adhesion</b></td><td>Attraction between a fluid and a <b>different</b> material &mdash; fluid &ldquo;sticks&rdquo; to container walls</td></tr><tr><td style='padding: 6px 10px;'><b>Cohesion</b></td><td>Attraction between fluid molecules of the <b>same type</b> &mdash; fluid &ldquo;sticks&rdquo; to itself</td></tr></table><br><span style='font-size: 13px; color: #888;'>Water has high cohesion (surface tension) and high adhesion to polar surfaces like glass</span></div>",
        "tags": ["physics::concept", "physics::fluids::properties"]
    },
    # Card 4: Capillary Action & Repulsion
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Capillary Action &amp; Capillary Repulsion</b><br><br>What causes <span style='color: #4a90d9;'>capillary action</span> vs <span style='color: #4a90d9;'>capillary repulsion</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Capillary Action &amp; Capillary Repulsion</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Capillary action</b></td><td>Adhesion &gt; cohesion &rarr; fluid <b>rises</b> up a narrow tube<br><span style='font-size: 13px; color: #888;'>Example: water rising in a glass tube</span></td></tr><tr><td style='padding: 6px 10px;'><b>Capillary repulsion</b></td><td>Cohesion &gt; adhesion &rarr; fluid <b>depresses</b> in a narrow tube<br><span style='font-size: 13px; color: #888;'>Example: mercury in a glass tube</span></td></tr></table><br><span style='font-size: 13px; color: #888;'>Narrower tube &rarr; greater capillary effect</span></div>",
        "tags": ["physics::concept", "physics::fluids::properties"]
    },
    # Card 5: Buoyant Force & Archimedes' Principle
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Buoyant Force &amp; Archimedes' Principle</b><br><br>What is the equation for <span style='color: #4a90d9;'>buoyant force</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Buoyant Force &amp; Archimedes' Principle</b><br><br>\[F_B = \rho_{fluid} \cdot V_{disp} \cdot g\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>F<sub>B</sub></b></td><td>buoyant force &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>fluid</sub></b></td><td>density of the fluid &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>V<sub>disp</sub></b></td><td>volume of fluid displaced by the object &mdash; m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>g</b></td><td>gravitational acceleration &mdash; 9.8 m/s&sup2;</td></tr></table><br><span style='font-size: 14px; color: #555;'>Archimedes&rsquo; Principle: F<sub>B</sub> equals the <b>weight of the fluid displaced</b></span><br><br><span style='font-size: 13px; color: #888;'>Only the submerged volume counts &mdash; not the object&rsquo;s total volume if partially above the surface</span></div>",
        "tags": ["physics::equation", "physics::fluids::buoyancy"]
    },
    # Card 6: Floating Objects
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Floating Objects</b><br><br>What force condition holds for a <span style='color: #4a90d9;'>floating object</span>, and what determines the <span style='color: #4a90d9;'>fraction submerged</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Floating Objects</b><br><br>\[F_G = F_B\]<br><br><span style='font-size: 14px; color: #555;'>Fraction submerged (derived from F<sub>G</sub> = F<sub>B</sub>):</span><br>\[\frac{V_{sub}}{V_{obj}} = \frac{\rho_{obj}}{\rho_{fluid}}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>V<sub>sub</sub></b></td><td>submerged volume &mdash; m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>V<sub>obj</sub></b></td><td>total object volume &mdash; m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>obj</sub></b></td><td>density of object &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;<sub>fluid</sub></b></td><td>density of fluid &mdash; kg/m&sup3;</td></tr></table><br><span style='font-size: 13px; color: #888;'>Object 80% as dense as the fluid floats with 80% submerged</span></div>",
        "tags": ["physics::concept", "physics::fluids::buoyancy"]
    },
    # Card 7: Sinking Objects
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sinking Objects</b><br><br>When an object <span style='color: #4a90d9;'>sinks and rests on the bottom</span>, what forces act and what is the normal force?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sinking Objects</b><br><br><span style='font-size: 14px; color: #555;'>Force balance (fully submerged, at rest on bottom):</span><br>\[F_G = F_B + F_N\]<br><br><span style='font-size: 14px; color: #555;'>Solving for normal force:</span><br>\[F_N = F_G - F_B = (\rho_{obj} - \rho_{fluid}) \cdot V_{obj} \cdot g\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>F<sub>G</sub></b></td><td>gravity (down) &mdash; &rho;<sub>obj</sub> &middot; V<sub>obj</sub> &middot; g</td></tr><tr><td style='padding: 4px 10px;'><b>F<sub>B</sub></b></td><td>buoyant force (up) &mdash; &rho;<sub>fluid</sub> &middot; V<sub>obj</sub> &middot; g</td></tr><tr><td style='padding: 4px 10px;'><b>F<sub>N</sub></b></td><td>normal force from ground (up)</td></tr></table><br><span style='font-size: 13px; color: #888;'>F<sub>N</sub> is less than the object&rsquo;s weight in air &mdash; the fluid partially supports it</span></div>",
        "tags": ["physics::concept", "physics::fluids::buoyancy"]
    },
    # Card 8: Pressure
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pressure</b><br><br>What is the equation for <span style='color: #4a90d9;'>pressure</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pressure</b><br><br>\[P = \frac{F}{A}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P</b></td><td>pressure &mdash; Pascals (Pa = N/m&sup2;)</td></tr><tr><td style='padding: 4px 10px;'><b>F</b></td><td>force applied perpendicular to surface &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>A</b></td><td>area &mdash; m&sup2;</td></tr></table><br><span style='font-size: 13px; color: #888;'>Same force over a smaller area &rarr; greater pressure; basis for needles, knives, and snowshoes</span></div>",
        "tags": ["physics::equation", "physics::fluids::pressure"]
    },
    # Card 9: Pascal's Principle
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pascal's Principle</b><br><br>What does <span style='color: #4a90d9;'>Pascal&rsquo;s Principle</span> state?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pascal's Principle</b><br><br>A pressure applied to an <b>enclosed, incompressible fluid</b> is transmitted <b>equally and undiminished</b> in all directions throughout the fluid.<br><br><span style='font-size: 15px; color: #555;'>P<sub>applied</sub> adds equally to every point in the fluid</span><br><br><span style='font-size: 13px; color: #888;'>Basis for hydraulic systems &mdash; a small force over a small area can produce a large force over a large area</span></div>",
        "tags": ["physics::concept", "physics::fluids::pressure"]
    },
    # Card 10: Hydraulic System
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydraulic System</b><br><br>What are the equations governing a <span style='color: #4a90d9;'>hydraulic system</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydraulic System</b><br><br><span style='font-size: 14px; color: #555;'>Pressure equality (Pascal&rsquo;s Principle):</span><br>\[\frac{F_1}{A_1} = \frac{F_2}{A_2}\]<br><br><span style='font-size: 14px; color: #555;'>Volume conservation (incompressible fluid):</span><br>\[A_1 d_1 = A_2 d_2\]<br><br><span style='font-size: 14px; color: #555;'>Work conservation (no energy gained):</span><br>\[F_1 d_1 = F_2 d_2\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>F</b></td><td>force on piston &mdash; Newtons (N)</td></tr><tr><td style='padding: 4px 10px;'><b>A</b></td><td>piston area &mdash; m&sup2;</td></tr><tr><td style='padding: 4px 10px;'><b>d</b></td><td>piston displacement &mdash; meters (m)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Larger output force = smaller input force &times; (A<sub>2</sub>/A<sub>1</sub>); you gain force but lose distance</span></div>",
        "tags": ["physics::equation", "physics::fluids::pressure"]
    },
    # Card 11: Hydrostatic Pressure
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydrostatic Pressure</b><br><br>What is the equation for <span style='color: #4a90d9;'>absolute pressure</span> at a depth in a fluid?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydrostatic Pressure</b><br><br>\[P_{abs} = P_0 + \rho g h\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P<sub>abs</sub></b></td><td>absolute pressure at depth &mdash; Pascals (Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>P<sub>0</sub></b></td><td>surface pressure (usually P<sub>atm</sub> &asymp; 101,325 Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;</b></td><td>fluid density &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>g</b></td><td>gravitational acceleration &mdash; 9.8 m/s&sup2;</td></tr><tr><td style='padding: 4px 10px;'><b>h</b></td><td>depth below surface &mdash; meters (m)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Pressure increases linearly with depth; depends only on depth &mdash; not the shape of the container</span></div>",
        "tags": ["physics::equation", "physics::fluids::pressure"]
    },
    # Card 12: Gauge Pressure
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Gauge Pressure</b><br><br>What is <span style='color: #4a90d9;'>gauge pressure</span> and how does it relate to absolute pressure?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Gauge Pressure</b><br><br>\[P_{gauge} = P_{abs} - P_{atm}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P<sub>gauge</sub></b></td><td>pressure above atmospheric &mdash; Pascals (Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>P<sub>abs</sub></b></td><td>total absolute pressure &mdash; Pascals (Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>P<sub>atm</sub></b></td><td>atmospheric pressure &mdash; ~101,325 Pa (1 atm)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Gauge pressure = 0 at the open surface<br>Gauge pressure = &rho;gh at depth h</span><br><br><span style='font-size: 13px; color: #888;'>A tire pressure gauge reads gauge pressure &mdash; pressure above atmospheric</span></div>",
        "tags": ["physics::definition", "physics::fluids::pressure"]
    },
    # Card 13: Flow Rate & Continuity
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Flow Rate &amp; Continuity</b><br><br>What are the equations for <span style='color: #4a90d9;'>flow rate</span> and the <span style='color: #4a90d9;'>continuity equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Flow Rate &amp; Continuity</b><br><br><span style='font-size: 14px; color: #555;'>Flow rate:</span><br>\[Q = \frac{\Delta V}{\Delta t} = Av\]<br><br><span style='font-size: 14px; color: #555;'>Continuity equation (incompressible fluid):</span><br>\[A_1 v_1 = A_2 v_2\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>Q</b></td><td>volume flow rate &mdash; m&sup3;/s</td></tr><tr><td style='padding: 4px 10px;'><b>A</b></td><td>cross-sectional area of tube &mdash; m&sup2;</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>fluid velocity &mdash; m/s</td></tr></table><br><span style='font-size: 13px; color: #888;'>Smaller area &rarr; faster velocity; the same volume passes every cross-section per unit time</span></div>",
        "tags": ["physics::equation", "physics::fluids::flow"]
    },
    # Card 14: Poiseuille's Law (concept)
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Poiseuille's Law</b><br><br>Without the equation, how does <span style='color: #4a90d9;'>flow rate</span> relate to tube <span style='color: #4a90d9;'>radius</span> and <span style='color: #4a90d9;'>viscosity</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Poiseuille's Law &mdash; Concept</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Q &prop; r<sup>4</sup></b></td><td>Flow rate scales with the <b>4th power</b> of radius<br><span style='font-size: 13px; color: #888;'>Doubling radius &rarr; 16&times; the flow rate</span></td></tr><tr><td style='padding: 6px 10px;'><b>Q &prop; 1/&eta;</b></td><td>Inversely proportional to viscosity (&eta;)<br><span style='font-size: 13px; color: #888;'>Thicker fluid &rarr; less flow</span></td></tr><tr><td style='padding: 6px 10px;'><b>Q &prop; &Delta;P</b></td><td>Proportional to pressure difference<br><span style='font-size: 13px; color: #888;'>Greater pressure gradient &rarr; more flow</span></td></tr></table><br><span style='font-size: 13px; color: #888;'>Clinically relevant: arterial stenosis (narrowed radius) drastically reduces blood flow &mdash; halving radius cuts flow to 1/16th</span></div>",
        "tags": ["physics::concept", "physics::fluids::flow"]
    },
    # Card 15: Bernoulli's Principle
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bernoulli's Principle</b><br><br>What is <span style='color: #4a90d9;'>Bernoulli&rsquo;s equation</span> and how is it applied between two points?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bernoulli's Principle</b><br><br><span style='font-size: 14px; color: #555;'>At any point in an ideal fluid:</span><br>\[P + \rho g h + \frac{1}{2}\rho v^2 = \text{constant}\]<br><br><span style='font-size: 14px; color: #555;'>Between two points in the same system:</span><br>\[P_1 + \rho g h_1 + \frac{1}{2}\rho v_1^2 = P_2 + \rho g h_2 + \frac{1}{2}\rho v_2^2\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P</b></td><td>static pressure &mdash; Pascals (Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;</b></td><td>fluid density &mdash; kg/m&sup3;</td></tr><tr><td style='padding: 4px 10px;'><b>h</b></td><td>height above reference point &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>fluid velocity &mdash; m/s</td></tr></table><br><span style='font-size: 13px; color: #888;'>Fluid version of conservation of energy &mdash; valid for ideal fluids only</span></div>",
        "tags": ["physics::equation", "physics::fluids::flow"]
    },
    # Card 16: Venturi Effect
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Venturi Effect</b><br><br>What is the <span style='color: #4a90d9;'>Venturi effect</span> and what causes it?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Venturi Effect</b><br><br>When a fluid flows through a constriction, its velocity increases and its pressure decreases.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Step 1 (Continuity)</b></td><td>A<sub>1</sub>v<sub>1</sub> = A<sub>2</sub>v<sub>2</sub> &rarr; smaller area &rarr; faster velocity</td></tr><tr><td style='padding: 6px 10px;'><b>Step 2 (Bernoulli)</b></td><td>Faster v &rarr; lower P (at constant height)</td></tr></table><br><span style='font-size: 15px; color: #555;'>Narrower tube &rarr; faster flow &rarr; lower pressure</span><br><br><span style='font-size: 13px; color: #888;'>Applications: carburetors, atomizers, airplane lift, stenotic arteries</span></div>",
        "tags": ["physics::concept", "physics::fluids::flow"]
    },
    # Card 17: Pitot Tube
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pitot Tube</b><br><br>How does a <span style='color: #4a90d9;'>Pitot tube</span> work and what does it measure?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pitot Tube</b><br><br>Measures fluid <b>velocity</b> by comparing stagnation pressure (fluid stopped) to static pressure (fluid flowing).<br><br>\[v = \sqrt{\frac{2\Delta P}{\rho}}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>v</b></td><td>fluid velocity &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>&Delta;P</b></td><td>P<sub>stag</sub> &minus; P<sub>static</sub> &mdash; Pascals (Pa)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;</b></td><td>fluid density &mdash; kg/m&sup3;</td></tr></table><br><span style='font-size: 14px; color: #555;'>At the stagnation point, all kinetic energy converts to pressure:<br>P<sub>stag</sub> = P<sub>static</sub> + &frac12;&rho;v<sup>2</sup></span><br><br><span style='font-size: 13px; color: #888;'>Used in aircraft airspeed indicators</span></div>",
        "tags": ["physics::equation", "physics::fluids::flow"]
    },
]

# Validate
print("Validating cards...")
for i, card in enumerate(cards):
    validate(card["front"], card["back"])
print(f"All {len(cards)} cards validated.")

# Push
print("Pushing cards...")
result = push_cards(cards)
note_ids = result["result"]

added = updated = 0
errors = []
for i, (card, note_id) in enumerate(zip(cards, note_ids)):
    if note_id is not None:
        added += 1
        print(f"  Card {i+1}: ADDED (id={note_id})")
    else:
        print(f"  Card {i+1}: duplicate detected, updating...")
        success = find_and_update(card["front"], card["back"], card["tags"])
        if success:
            updated += 1
            print(f"  Card {i+1}: UPDATED")
        else:
            errors.append(card["front"][:60])
            print(f"  Card {i+1}: ERROR")

print(f"\nDone. Added: {added}, Updated: {updated}, Errors: {len(errors)}")
if errors:
    print("Errors:")
    for e in errors:
        print(f"  {e}")
