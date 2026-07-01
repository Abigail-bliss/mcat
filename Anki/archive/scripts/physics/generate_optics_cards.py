"""
Generates optics_cards.txt in the same tab-separated format as other card files.
Run this to regenerate the file. To push, use a separate push script.
Format: front [TAB] back [TAB] tags (space-separated)
"""

def validate(front, back):
    for char, name in [('\t','tab'), ('\r','CR'), ('\n','newline'), ('\v','vtab'), ('\f','ff')]:
        assert char not in front, f"FRONT contains {name}!"
        assert char not in back, f"BACK contains {name}!"

cards = [
    # Card 1: Reflection
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Reflection</b><br><br>What is the <span style='color: #4a90d9;'>law of reflection</span> and what are the types of reflection?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Wave Reflection</b><br><br>\[\theta_i = \theta_r\]<br><br><span style='font-size: 14px; color: #555;'>Angle of incidence = angle of reflection (both measured from the normal)</span><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Specular</b></td><td>Smooth surface; parallel rays reflect in parallel &rarr; clear image</td></tr><tr><td style='padding: 6px 10px;'><b>Diffuse</b></td><td>Rough surface; rays scatter in many directions &rarr; no clear image</td></tr></table><br><span style='font-size: 13px; color: #888;'>The normal is perpendicular to the surface at the point of reflection</span></div>",
        "tags": "physics::concept physics::optics::wave-optics"
    },
    # Card 2: Refraction
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Refraction</b><br><br>What is <span style='color: #4a90d9;'>refraction</span> and what is the <span style='color: #4a90d9;'>index of refraction</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Refraction</b><br><br>The bending of a wave as it passes from one medium to another due to a change in speed.<br><br>\[n = \frac{c}{v}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>n</b></td><td>index of refraction &mdash; dimensionless (&ge; 1)</td></tr><tr><td style='padding: 4px 10px;'><b>c</b></td><td>speed of light in vacuum &mdash; 3 &times; 10<sup>8</sup> m/s</td></tr><tr><td style='padding: 4px 10px;'><b>v</b></td><td>speed of light in the medium &mdash; m/s</td></tr></table><br><span style='font-size: 14px; color: #555;'>Denser medium &rarr; higher n &rarr; slower light &rarr; bends toward normal</span><br><br><span style='font-size: 13px; color: #888;'>n = 1 for vacuum; n &asymp; 1.33 for water; n &asymp; 1.5 for glass</span></div>",
        "tags": "physics::concept physics::optics::wave-optics"
    },
    # Card 3: Snell's Law
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Snell's Law</b><br><br>What is the equation for <span style='color: #4a90d9;'>Snell's Law</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Snell's Law</b><br><br>\[n_1 \sin\theta_1 = n_2 \sin\theta_2\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>n<sub>1</sub>, n<sub>2</sub></b></td><td>indices of refraction of medium 1 and 2 &mdash; dimensionless</td></tr><tr><td style='padding: 4px 10px;'><b>&theta;<sub>1</sub></b></td><td>angle of incidence in medium 1 (from normal)</td></tr><tr><td style='padding: 4px 10px;'><b>&theta;<sub>2</sub></b></td><td>angle of refraction in medium 2 (from normal)</td></tr></table><br><span style='font-size: 14px; color: #555;'>n<sub>1</sub> &lt; n<sub>2</sub>: light bends toward normal (&theta;<sub>2</sub> &lt; &theta;<sub>1</sub>)<br>n<sub>1</sub> &gt; n<sub>2</sub>: light bends away from normal (&theta;<sub>2</sub> &gt; &theta;<sub>1</sub>)</span></div>",
        "tags": "physics::equation physics::optics::wave-optics"
    },
    # Card 4: Total Internal Reflection
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Total Internal Reflection</b><br><br>What is <span style='color: #4a90d9;'>total internal reflection</span> and what is the equation for the <span style='color: #4a90d9;'>critical angle</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Total Internal Reflection</b><br><br>When light travels from a denser to a less dense medium at an angle &ge; the critical angle &mdash; all light reflects back; none transmits.<br><br>\[\sin\theta_c = \frac{n_2}{n_1}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>&theta;<sub>c</sub></b></td><td>critical angle</td></tr><tr><td style='padding: 4px 10px;'><b>n<sub>1</sub></b></td><td>index of denser medium (where light originates)</td></tr><tr><td style='padding: 4px 10px;'><b>n<sub>2</sub></b></td><td>index of less dense medium (n<sub>2</sub> &lt; n<sub>1</sub>)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Requires n<sub>1</sub> &gt; n<sub>2</sub>; basis for fiber optics and the sparkle of diamonds</span></div>",
        "tags": "physics::equation physics::optics::wave-optics"
    },
    # Card 5: Diffraction
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Diffraction</b><br><br>What is <span style='color: #4a90d9;'>diffraction</span> and when does it occur?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Diffraction</b><br><br>The bending and spreading of waves around obstacles or through openings.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Most pronounced when</b></td><td>wavelength (&lambda;) &asymp; size of opening or obstacle</td></tr><tr><td style='padding: 6px 10px;'><b>Less pronounced when</b></td><td>&lambda; &lt;&lt; opening size &rarr; more like straight-line travel</td></tr></table><br><span style='font-size: 14px; color: #555;'>Applies to all waves: light, sound, water</span><br><br><span style='font-size: 13px; color: #888;'>Sound (long &lambda;) bends around corners easily; visible light (short &lambda;) generally does not</span></div>",
        "tags": "physics::concept physics::optics::wave-optics"
    },
    # Card 6: Thin Lens / Mirror Equation
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Thin Lens &amp; Mirror Equation</b><br><br>What is the <span style='color: #4a90d9;'>thin lens and mirror equation</span> and what are the sign conventions?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Thin Lens &amp; Mirror Equation</b><br><br>\[\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>f</b></td><td>focal length &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>d<sub>o</sub></b></td><td>object distance &mdash; always positive for real objects</td></tr><tr><td style='padding: 4px 10px;'><b>d<sub>i</sub></b></td><td>image distance &mdash; positive = real image; negative = virtual</td></tr></table><br><span style='font-size: 14px; color: #555;'>f &gt; 0: converging (concave mirror, convex lens)<br>f &lt; 0: diverging (convex mirror, concave lens)</span><br><br><span style='font-size: 13px; color: #888;'>&ldquo;Real is positive&rdquo; &mdash; real images and objects have positive distances</span></div>",
        "tags": "physics::equation physics::optics::lenses"
    },
    # Card 7: Magnification
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Magnification</b><br><br>What is the equation for <span style='color: #4a90d9;'>magnification</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Magnification</b><br><br>\[m = -\frac{d_i}{d_o} = \frac{h_i}{h_o}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>m</b></td><td>magnification &mdash; dimensionless</td></tr><tr><td style='padding: 4px 10px;'><b>d<sub>i</sub></b></td><td>image distance &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>d<sub>o</sub></b></td><td>object distance &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>h<sub>i</sub></b></td><td>image height &mdash; meters (m)</td></tr><tr><td style='padding: 4px 10px;'><b>h<sub>o</sub></b></td><td>object height &mdash; meters (m)</td></tr></table><br><span style='font-size: 14px; color: #555;'>m &gt; 0: upright &nbsp;|&nbsp; m &lt; 0: inverted<br>|m| &gt; 1: enlarged &nbsp;|&nbsp; |m| &lt; 1: diminished</span></div>",
        "tags": "physics::equation physics::optics::lenses"
    },
    # Card 8: Power
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Power of a Lens</b><br><br>What is the equation for <span style='color: #4a90d9;'>lens power</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Power of a Lens</b><br><br>\[P = \frac{1}{f}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P</b></td><td>power &mdash; diopters (D = m<sup>&minus;1</sup>)</td></tr><tr><td style='padding: 4px 10px;'><b>f</b></td><td>focal length &mdash; must be in meters (m)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Converging lens: P &gt; 0 &nbsp;|&nbsp; Diverging lens: P &lt; 0</span><br><br><span style='font-size: 13px; color: #888;'>Shorter focal length = higher power = stronger lens; eyeglass prescriptions are written in diopters</span></div>",
        "tags": "physics::equation physics::optics::lenses"
    },
    # Card 9: Types of Mirrors
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Types of Mirrors</b><br><br>What are the properties of <span style='color: #4a90d9;'>concave</span> vs <span style='color: #4a90d9;'>convex</span> mirrors?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Types of Mirrors</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'></td><td style='padding: 6px 10px;'><b>Concave</b></td><td style='padding: 6px 10px;'><b>Convex</b></td></tr><tr><td style='padding: 6px 10px;'><b>Shape</b></td><td style='padding: 6px 10px;'>Curves inward (caves in)</td><td style='padding: 6px 10px;'>Curves outward (bulges out)</td></tr><tr><td style='padding: 6px 10px;'><b>Focal length</b></td><td style='padding: 6px 10px;'>Positive (f &gt; 0)</td><td style='padding: 6px 10px;'>Negative (f &lt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Behavior</b></td><td style='padding: 6px 10px;'>Converging</td><td style='padding: 6px 10px;'>Diverging</td></tr><tr><td style='padding: 6px 10px;'><b>Images</b></td><td style='padding: 6px 10px;'>Real or virtual (depends on position)</td><td style='padding: 6px 10px;'>Always virtual, upright, diminished</td></tr></table><br><span style='font-size: 13px; color: #888;'>Center of curvature C = 2f; focal point F = f (both in front of concave, behind convex)</span></div>",
        "tags": "physics::concept physics::optics::mirrors"
    },
    # Card 10: Mirror Images
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Mirror Images</b><br><br>When does a mirror produce a <span style='color: #4a90d9;'>real</span> vs <span style='color: #4a90d9;'>virtual</span> image?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Mirror Images</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Concave, d<sub>o</sub> &gt; f</b></td><td>Real, inverted, in front of mirror (d<sub>i</sub> &gt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Concave, d<sub>o</sub> &lt; f</b></td><td>Virtual, upright, magnified, behind mirror (d<sub>i</sub> &lt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Concave, d<sub>o</sub> = f</b></td><td>No image &mdash; reflected rays are parallel</td></tr><tr><td style='padding: 6px 10px;'><b>Convex (any d<sub>o</sub>)</b></td><td>Always virtual, upright, diminished, behind mirror</td></tr></table><br><span style='font-size: 13px; color: #888;'>Real images form in front of mirror and can be projected on a screen; virtual images cannot</span></div>",
        "tags": "physics::concept physics::optics::mirrors"
    },
    # Card 11: Types of Lenses
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Types of Lenses</b><br><br>What are the properties of <span style='color: #4a90d9;'>converging</span> vs <span style='color: #4a90d9;'>diverging</span> lenses?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Types of Lenses</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'></td><td style='padding: 6px 10px;'><b>Converging (convex)</b></td><td style='padding: 6px 10px;'><b>Diverging (concave)</b></td></tr><tr><td style='padding: 6px 10px;'><b>Shape</b></td><td style='padding: 6px 10px;'>Thicker at center</td><td style='padding: 6px 10px;'>Thinner at center</td></tr><tr><td style='padding: 6px 10px;'><b>Focal length</b></td><td style='padding: 6px 10px;'>Positive (f &gt; 0)</td><td style='padding: 6px 10px;'>Negative (f &lt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Effect on rays</b></td><td style='padding: 6px 10px;'>Bends rays inward</td><td style='padding: 6px 10px;'>Bends rays outward</td></tr><tr><td style='padding: 6px 10px;'><b>Images</b></td><td style='padding: 6px 10px;'>Real or virtual (depends on position)</td><td style='padding: 6px 10px;'>Always virtual, upright, diminished</td></tr></table><br><span style='font-size: 13px; color: #888;'>Convex lens = converging; concave lens = diverging &mdash; note: opposite naming convention from mirrors</span></div>",
        "tags": "physics::concept physics::optics::lenses"
    },
    # Card 12: Lens Images
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Lens Images</b><br><br>When does a lens produce a <span style='color: #4a90d9;'>real</span> vs <span style='color: #4a90d9;'>virtual</span> image?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Lens Images</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'><b>Converging, d<sub>o</sub> &gt; f</b></td><td>Real, inverted, opposite side of lens (d<sub>i</sub> &gt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Converging, d<sub>o</sub> &lt; f</b></td><td>Virtual, upright, magnified, same side as object (d<sub>i</sub> &lt; 0)</td></tr><tr><td style='padding: 6px 10px;'><b>Converging, d<sub>o</sub> = f</b></td><td>No image &mdash; transmitted rays are parallel</td></tr><tr><td style='padding: 6px 10px;'><b>Diverging (any d<sub>o</sub>)</b></td><td>Always virtual, upright, diminished, same side as object</td></tr></table><br><span style='font-size: 13px; color: #888;'>Key difference from mirrors: real lens images form on the opposite side from the object</span></div>",
        "tags": "physics::concept physics::optics::lenses"
    },
    # Card 13: Vision Correction
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Vision Correction</b><br><br>What is <span style='color: #4a90d9;'>myopia</span> and <span style='color: #4a90d9;'>hyperopia</span> physically, and what lens corrects each?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Vision Correction</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 6px 10px;'></td><td style='padding: 6px 10px;'><b>Myopia (nearsighted)</b></td><td style='padding: 6px 10px;'><b>Hyperopia (farsighted)</b></td></tr><tr><td style='padding: 6px 10px;'><b>Can see</b></td><td style='padding: 6px 10px;'>Near clearly</td><td style='padding: 6px 10px;'>Far clearly</td></tr><tr><td style='padding: 6px 10px;'><b>Physical cause</b></td><td style='padding: 6px 10px;'>Eye too long; image focuses in <b>front</b> of retina</td><td style='padding: 6px 10px;'>Eye too short; image focuses <b>behind</b> retina</td></tr><tr><td style='padding: 6px 10px;'><b>Correction</b></td><td style='padding: 6px 10px;'>Diverging lens (P &lt; 0)</td><td style='padding: 6px 10px;'>Converging lens (P &gt; 0)</td></tr></table><br><span style='font-size: 13px; color: #888;'>Myopia: diverging lens spreads rays so they focus farther back. Hyperopia: converging lens focuses rays sooner.</span></div>",
        "tags": "physics::concept physics::optics::vision"
    },
    # Card 14: Eye Power Equation
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Eye Power Equation</b><br><br>What is the equation for <span style='color: #4a90d9;'>corrected eye power</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Eye Power Equation</b><br><br>\[P_{total} = P_{eye} + P_{lens}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>P<sub>total</sub></b></td><td>total power of the corrected system &mdash; diopters (D)</td></tr><tr><td style='padding: 4px 10px;'><b>P<sub>eye</sub></b></td><td>power of the eye alone &mdash; diopters (D)</td></tr><tr><td style='padding: 4px 10px;'><b>P<sub>lens</sub></b></td><td>power of the corrective lens &mdash; diopters (D)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Myopia: P<sub>lens</sub> &lt; 0 (reduces total power)<br>Hyperopia: P<sub>lens</sub> &gt; 0 (increases total power)</span><br><br><span style='font-size: 13px; color: #888;'>Powers add directly when lenses are in contact &mdash; this is why prescriptions are written in diopters</span></div>",
        "tags": "physics::equation physics::optics::vision"
    },
]

# Validate all
print("Validating...")
for i, card in enumerate(cards):
    validate(card["front"], card["back"])
print(f"All {len(cards)} cards validated.")

# Write to file (tab-separated: front [TAB] back [TAB] tags)
output_path = "cards text files/optics_cards.txt"
with open(output_path, "w", encoding="utf-8") as f:
    for card in cards:
        f.write(card["front"] + "\t" + card["back"] + "\t" + card["tags"] + "\n")

print(f"Saved to {output_path}")
