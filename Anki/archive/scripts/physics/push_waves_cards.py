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
    # Card 1: Double-Slit Equation
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Young's Double-Slit Experiment</b><br><br>What is the equation for <span style='color: #4a90d9;'>fringe spacing</span> &Delta;Y?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Young's Double-Slit Experiment</b><br><br>\[\Delta Y = \frac{L\lambda}{D}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>&Delta;Y</b></td><td>fringe spacing (distance between adjacent bright or dark fringes) &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>L</b></td><td>distance from slits to screen &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>&lambda;</b></td><td>wavelength of light &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>D</b></td><td>distance between slits &mdash; meters (m)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Wider slits (larger D) or shorter wavelength &rarr; tighter fringes</span></div>",
        "tags": ["physics::equation", "physics::waves::light"]
    },
    # Card 2: Double-Slit Interference Pattern
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Young's Double-Slit Experiment</b><br><br>What does the <span style='color: #4a90d9;'>interference pattern</span> look like, and what causes bright vs. dark fringes?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Double-Slit Interference Pattern</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Zero-order maximum</b></td><td>Brightest fringe at the center; path difference = 0</td></tr><tr><td style='padding: 6px 10px;'><b>Bright fringes (maxima)</b></td><td>Constructive interference; path difference = n&lambda; (n = 0, 1, 2&hellip;)</td></tr><tr><td style='padding: 6px 10px;'><b>Dark fringes (minima)</b></td><td>Destructive interference; path difference = (n + &frac12;)&lambda;</td></tr></table><br><span style='font-size: 13px; color: #888;'>Fringes are equally spaced; brightness decreases further from center</span></div>",
        "tags": ["physics::concept", "physics::waves::light"]
    },
    # Card 3: Transverse vs Longitudinal Waves
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Types</b><br><br>What is the difference between <span style='color: #4a90d9;'>transverse</span> and <span style='color: #4a90d9;'>longitudinal</span> waves?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Transverse vs. Longitudinal Waves</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'></td><td style='padding: 6px 10px;'><b>Transverse</b></td><td style='padding: 6px 10px;'><b>Longitudinal</b></td></tr><tr><td style='padding: 6px 10px;'><b>Displacement</b></td><td style='padding: 6px 10px;'>Perpendicular (&perp;) to propagation</td><td style='padding: 6px 10px;'>Parallel (&#8741;) to propagation</td></tr><tr><td style='padding: 6px 10px;'><b>Pattern</b></td><td style='padding: 6px 10px;'>Crests and troughs</td><td style='padding: 6px 10px;'>Compressions and rarefactions</td></tr><tr><td style='padding: 6px 10px;'><b>Can polarize?</b></td><td style='padding: 6px 10px;'>Yes</td><td style='padding: 6px 10px;'>No</td></tr><tr><td style='padding: 6px 10px;'><b>Examples</b></td><td style='padding: 6px 10px;'>Light, water waves</td><td style='padding: 6px 10px;'>Sound, seismic P-waves</td></tr></table><br><span style='font-size: 13px; color: #888;'>Sound waves are longitudinal &mdash; air molecules compress and expand along the direction of travel</span></div>",
        "tags": ["physics::concept", "physics::waves::general"]
    },
    # Card 4: Universal Wave Equation
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Universal Wave Equation</b><br><br>What is the <span style='color: #4a90d9;'>universal wave equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Universal Wave Equation</b><br><br>\[v = f\lambda\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>v</b></td><td>wave speed &mdash; meters per second (m/s)</td></tr><tr><td style='padding: 4px 10px;'><b>f</b></td><td>frequency &mdash; Hertz (Hz = 1/s)</td></tr><tr><td style='padding: 4px 10px;'><b>&lambda;</b></td><td>wavelength &mdash; meters (m)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Applies to all wave types; v is set by the medium, f is set by the source</span></div>",
        "tags": ["physics::equation", "physics::waves::general"]
    },
    # Card 5: Period & Frequency
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Period &amp; Frequency</b><br><br>What is the equation for the <span style='color: #4a90d9;'>period</span> of a wave?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Period &amp; Frequency</b><br><br>\[T = \frac{1}{f} \qquad f = \frac{1}{T}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>T</b></td><td>period (time for one complete cycle) &mdash; seconds (s)</td></tr><tr><td style='padding: 4px 10px;'><b>f</b></td><td>frequency (cycles per second) &mdash; Hertz (Hz = 1/s)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Higher frequency &rarr; shorter period; they are reciprocals</span></div>",
        "tags": ["physics::equation", "physics::waves::general"]
    },
    # Card 6: Wave Speed in Different Media
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Speed in Different Media</b><br><br>How does <span style='color: #4a90d9;'>wave speed</span> change in a denser medium? What changes and what stays the same?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Speed in Different Media</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Speed (v)</b></td><td>Changes &mdash; set by the medium</td></tr><tr><td style='padding: 6px 10px;'><b>Frequency (f)</b></td><td>Unchanged &mdash; set by the source</td></tr><tr><td style='padding: 6px 10px;'><b>Wavelength (&lambda;)</b></td><td>Changes with v (since v = f&lambda;)</td></tr></table><br><span style='font-size: 15px; color: #555;'>Light entering a denser medium: v &darr;, &lambda; &darr;, f unchanged</span><br><br><span style='font-size: 13px; color: #888;'>This is why light bends (refracts) at a boundary &mdash; one side slows before the other</span></div>",
        "tags": ["physics::rule-of-thumb", "physics::waves::general"]
    },
    # Card 7: Speed of Sound
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Speed of Sound</b><br><br>What is the equation for the <span style='color: #4a90d9;'>speed of sound</span> and what factors affect it?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Speed of Sound</b><br><br>\[v = \sqrt{\frac{B}{\rho}}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of sound &mdash; m/s (~343 m/s in air at room temp)</td></tr><tr><td style='padding: 4px 10px;'><b>B</b></td><td>bulk modulus (stiffness of medium) &mdash; Pascals (Pa = N/m&sup2;)</td></tr><tr><td style='padding: 4px 10px;'><b>&rho;</b></td><td>density of medium &mdash; kg/m&sup3;</td></tr></table><br><span style='font-size: 14px; color: #555;'>Speed order: solids &gt; liquids &gt; gases (stiffness dominates over density)</span><br><br><span style='font-size: 13px; color: #888;'>Speed increases with temperature &mdash; higher temp &rarr; molecules move faster &rarr; compressions travel faster</span></div>",
        "tags": ["physics::equation", "physics::waves::sound"]
    },
    # Card 8: Wave Interference
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Interference</b><br><br>What are the conditions for <span style='color: #4a90d9;'>constructive</span> and <span style='color: #4a90d9;'>destructive</span> interference?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Interference</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Constructive</b></td><td style='padding: 6px 10px;'>Waves in phase; path difference = n&lambda; (n = 0, 1, 2&hellip;)<br>Amplitudes <b>add</b> &rarr; larger resultant wave</td></tr><tr><td style='padding: 6px 10px;'><b>Destructive</b></td><td style='padding: 6px 10px;'>Waves out of phase by 180&deg;; path difference = (n + &frac12;)&lambda;<br>Amplitudes <b>cancel</b> &rarr; smaller or zero resultant wave</td></tr></table><br><span style='font-size: 13px; color: #888;'>Superposition principle: total displacement = sum of individual displacements at every point</span></div>",
        "tags": ["physics::concept", "physics::waves::general"]
    },
    # Card 9: Pitch & Frequency
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pitch &amp; Frequency</b><br><br>What is <span style='color: #4a90d9;'>pitch</span> and how does it relate to frequency?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Pitch &amp; Frequency</b><br><br>Pitch is the <b>subjective perception</b> of the frequency of a sound.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Higher frequency</b></td><td>&rarr; higher pitch</td></tr><tr><td style='padding: 6px 10px;'><b>Lower frequency</b></td><td>&rarr; lower pitch</td></tr></table><br><span style='font-size: 13px; color: #888;'>Analogous to color and light: color is the perception of light frequency. Loudness is the perception of amplitude &mdash; not frequency.</span></div>",
        "tags": ["physics::definition", "physics::waves::sound"]
    },
    # Card 10: Standing Waves
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Standing Waves</b><br><br>What are <span style='color: #4a90d9;'>standing waves</span>, and what are <span style='color: #4a90d9;'>nodes</span> and <span style='color: #4a90d9;'>antinodes</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Standing Waves</b><br><br>Formed by superposition of two identical waves traveling in <b>opposite directions</b> &mdash; the pattern appears stationary.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Nodes</b></td><td>Points of zero displacement; always stationary</td></tr><tr><td style='padding: 6px 10px;'><b>Antinodes</b></td><td>Points of maximum displacement; halfway between nodes</td></tr><tr><td style='padding: 6px 10px;'><b>Harmonics</b></td><td>Resonant frequencies at which standing waves form</td></tr></table><br><span style='font-size: 13px; color: #888;'>Fixed / closed ends are always nodes; open ends are always antinodes</span></div>",
        "tags": ["physics::concept", "physics::waves::standing-waves"]
    },
    # Card 11: Resonance Tube — One Open, One Closed
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; One Open, One Closed End</b><br><br>What harmonics are supported and what is the <span style='color: #4a90d9;'>resonant frequency equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; One Open, One Closed End</b><br><br>\[f_n = \frac{nv}{4L} \quad (n = 1, 3, 5, \ldots)\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>f<sub>n</sub></b></td><td>resonant frequency &mdash; Hertz (Hz)</td></tr><tr><td style='padding: 4px 10px;'><b>n</b></td><td>harmonic number (odd integers only: 1, 3, 5&hellip;)</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of sound &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>L</b></td><td>length of tube &mdash; meters (m)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Closed end = node; open end = antinode &mdash; only <b>odd harmonics</b> fit</span><br><br><span style='font-size: 13px; color: #888;'>Fundamental (n=1): f<sub>1</sub> = v/4L; next resonances at 3f<sub>1</sub>, 5f<sub>1</sub>&hellip;</span></div>",
        "tags": ["physics::equation", "physics::waves::standing-waves"]
    },
    # Card 12: Resonance Tube — Two Open Ends
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; Two Open Ends</b><br><br>What harmonics are supported and what is the <span style='color: #4a90d9;'>resonant frequency equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; Two Open Ends</b><br><br>\[f_n = \frac{nv}{2L} \quad (n = 1, 2, 3, \ldots)\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>f<sub>n</sub></b></td><td>resonant frequency &mdash; Hertz (Hz)</td></tr><tr><td style='padding: 4px 10px;'><b>n</b></td><td>harmonic number (all integers: 1, 2, 3&hellip;)</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of sound &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>L</b></td><td>length of tube &mdash; meters (m)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Both ends = antinodes &mdash; <b>all harmonics</b> are supported</span><br><br><span style='font-size: 13px; color: #888;'>Fundamental (n=1): f<sub>1</sub> = v/2L; harmonics at 2f<sub>1</sub>, 3f<sub>1</sub>, 4f<sub>1</sub>&hellip;</span></div>",
        "tags": ["physics::equation", "physics::waves::standing-waves"]
    },
    # Card 13: Resonance Tube — Two Closed Ends
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; Two Closed Ends</b><br><br>What harmonics are supported and what is the <span style='color: #4a90d9;'>resonant frequency equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Tube &mdash; Two Closed Ends</b><br><br>\[f_n = \frac{nv}{2L} \quad (n = 1, 2, 3, \ldots)\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>f<sub>n</sub></b></td><td>resonant frequency &mdash; Hertz (Hz)</td></tr><tr><td style='padding: 4px 10px;'><b>n</b></td><td>harmonic number (all integers: 1, 2, 3&hellip;)</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of sound &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>L</b></td><td>length of tube &mdash; meters (m)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Both ends = nodes &mdash; <b>all harmonics</b> are supported</span><br><br><span style='font-size: 13px; color: #888;'>Same equation as two open ends &mdash; different node/antinode positions but identical harmonic series</span></div>",
        "tags": ["physics::equation", "physics::waves::standing-waves"]
    },
    # Card 14: Sound Intensity & Decibels
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sound Intensity &amp; Decibels</b><br><br>What is the equation for <span style='color: #4a90d9;'>sound intensity level</span> in decibels?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Sound Intensity &amp; Decibels</b><br><br>\[\beta = 10 \log\left(\frac{I}{I_0}\right)\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>&beta;</b></td><td>sound intensity level &mdash; decibels (dB)</td></tr><tr><td style='padding: 4px 10px;'><b>I</b></td><td>intensity of the sound &mdash; Watts per m&sup2; (W/m&sup2;)</td></tr><tr><td style='padding: 4px 10px;'><b>I<sub>0</sub></b></td><td>threshold of hearing &mdash; 10<sup>&minus;12</sup> W/m&sup2;</td></tr></table><br><span style='font-size: 14px; color: #555;'>Every +10 dB = 10&times; intensity &nbsp;|&nbsp; Every +3 dB &asymp; 2&times; intensity</span><br><br><span style='font-size: 13px; color: #888;'>0 dB = threshold of hearing; 120 dB = threshold of pain</span></div>",
        "tags": ["physics::equation", "physics::waves::sound"]
    },
    # Card 15: Doppler Effect
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Doppler Effect</b><br><br>What is the <span style='color: #4a90d9;'>Doppler effect equation</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Doppler Effect</b><br><br>\[f' = f \cdot \frac{v \pm v_{obs}}{v \mp v_{src}}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>f&prime;</b></td><td>observed frequency &mdash; Hertz (Hz)</td></tr><tr><td style='padding: 4px 10px;'><b>f</b></td><td>source frequency &mdash; Hertz (Hz)</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of sound &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>v<sub>obs</sub></b></td><td>speed of observer &mdash; m/s</td></tr><tr><td style='padding: 4px 10px;'><b>v<sub>src</sub></b></td><td>speed of source &mdash; m/s</td></tr></table><br><span style='font-size: 14px; color: #555;'>Numerator: + when observer moves <b>toward</b> source; &minus; when moving away<br>Denominator: &minus; when source moves <b>toward</b> observer; + when moving away</span><br><br><span style='font-size: 13px; color: #888;'>Toward = higher f&prime;; away = lower f&prime;</span></div>",
        "tags": ["physics::equation", "physics::waves::sound"]
    },
]

# Validate
print("Validating cards...")
for i, card in enumerate(cards):
    validate(card["front"], card["back"])
print("All 15 cards validated.")

# Push
print("Pushing cards...")
result = push_cards(cards)
note_ids = result["result"]

added = 0
updated = 0
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
