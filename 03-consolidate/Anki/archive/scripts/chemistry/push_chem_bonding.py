import requests

r = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
assert r.json()["result"] == 6, "Anki is not running or AnkiConnect is not installed"
print("AnkiConnect connected.")

DECK = "MCAT Chemistry"

def validate(front, back):
    for char, name in [('\t','tab'), ('\r','CR'), ('\n','newline'), ('\v','vtab'), ('\f','ff')]:
        assert char not in front, f"FRONT contains {name}! Card: {front[:40]}"
        assert char not in back, f"BACK contains {name}! Card: {front[:40]}"

def push_cards(cards):
    notes = [{"deckName": DECK, "modelName": "Basic", "fields": {"Front": c["front"], "Back": c["back"]}, "tags": c["tags"], "options": {"allowDuplicate": False, "duplicateScope": "deck"}} for c in cards]
    r = requests.post("http://localhost:8765", json={"action": "addNotes", "version": 6, "params": {"notes": notes}})
    return r.json()

def find_and_update(front, back, tags):
    r = requests.post("http://localhost:8765", json={"action": "findNotes", "version": 6, "params": {"query": f'deck:"{DECK}" "front:{front[:50]}"'}})
    note_ids = r.json()["result"]
    if not note_ids:
        return False
    note_id = note_ids[0]
    r = requests.post("http://localhost:8765", json={"action": "updateNote", "version": 6, "params": {"note": {"id": note_id, "fields": {"Front": front, "Back": back}, "tags": tags}}})
    return r.json()["error"] is None

cards = [
    # 1: Percent yield
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Percent Yield</b><br><br>What is the equation for <span style='color: #4a90d9;'>percent yield</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Percent Yield</b><br><br>\[\% \text{ yield} = \frac{\text{actual yield}}{\text{theoretical yield}} \times 100\%\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>Actual yield</b></td><td>amount of product obtained experimentally</td></tr><tr><td style='padding: 4px 10px;'><b>Theoretical yield</b></td><td>maximum amount possible from stoichiometry</td></tr></table><br><span style='font-size: 13px; color: #888;'>Actual yield is always &le; theoretical yield; losses occur from side reactions, incomplete reaction, or transfer losses</span></div>",
        "tags": ["chemistry::equation", "chemistry::stoichiometry::percent-yield"]
    },
    # 2: Mass percentage
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Mass Percentage</b><br><br>What is the equation for <span style='color: #4a90d9;'>mass percentage</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Mass Percentage</b><br><br>\[\text{mass \%} = \frac{m_{component}}{m_{total}} \times 100\%\]<br><br><span style='font-size: 14px; color: #555;'>For an element in a compound:</span><br>\[\text{mass \% element} = \frac{\text{mass of element in formula unit}}{\text{molar mass of compound}} \times 100\%\]<br><br><span style='font-size: 13px; color: #888;'>All mass percentages in a mixture sum to 100%</span></div>",
        "tags": ["chemistry::equation", "chemistry::stoichiometry::mass-percentage"]
    },
    # 3: Ionic bonds
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Ionic Bonds</b><br><br>What are <span style='color: #4a90d9;'>ionic bonds</span> and what are the properties of ionic compounds?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Ionic Bonds</b><br><br>Complete <b>transfer of electrons</b> from metal to nonmetal; results in cations (+) and anions (&minus;) held by electrostatic attraction.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Melting / BP</b></td><td>Very high &mdash; strong electrostatic forces require much energy to overcome</td></tr><tr><td style='padding: 5px 10px;'><b>Hardness</b></td><td>Hard but brittle &mdash; ion layers shift &rarr; like charges repel &rarr; shatters</td></tr><tr><td style='padding: 5px 10px;'><b>Conductivity</b></td><td>Conducts when dissolved in water or molten; not as solid (ions fixed in lattice)</td></tr><tr><td style='padding: 5px 10px;'><b>Solubility</b></td><td>Generally soluble in polar solvents (water); insoluble in nonpolar</td></tr><tr><td style='padding: 5px 10px;'><b>State at RT</b></td><td>Solid (crystalline lattice)</td></tr></table><br><span style='font-size: 13px; color: #888;'>&Delta;EN &gt; 1.7 typically indicates ionic character; formed between metals and nonmetals</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::ionic"]
    },
    # 4: Lattice energy
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Lattice Energy</b><br><br>What is <span style='color: #4a90d9;'>lattice energy</span> and what factors affect it?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Lattice Energy</b><br><br>Energy <b>released</b> when gas-phase ions combine to form 1 mol of ionic solid (always exothermic).<br><br>\[U \propto \frac{q_1 q_2}{r}\]<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 4px 10px;'><b>q<sub>1</sub>, q<sub>2</sub></b></td><td>ion charges &mdash; higher charge &rarr; stronger attraction &rarr; higher lattice energy</td></tr><tr><td style='padding: 4px 10px;'><b>r</b></td><td>interionic distance &mdash; smaller ions &rarr; smaller r &rarr; higher lattice energy</td></tr></table><br><span style='font-size: 14px; color: #555;'>Higher lattice energy &rarr; higher melting point, greater hardness, lower solubility</span><br><br><span style='font-size: 13px; color: #888;'>MgO &gt; NaCl in lattice energy: Mg<sup>2+</sup>/O<sup>2&minus;</sup> vs Na<sup>+</sup>/Cl<sup>&minus;</sup> (higher charges, smaller ions)</span></div>",
        "tags": ["chemistry::equation", "chemistry::bonding::ionic"]
    },
    # 5: Nonpolar covalent
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Nonpolar Covalent Bond</b><br><br>What is a <span style='color: #4a90d9;'>nonpolar covalent bond</span> and what are its properties?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Nonpolar Covalent Bond</b><br><br>Forms between <b>two nonmetals</b> &mdash; identical atoms or atoms of similar electronegativity. <b>Equal sharing</b> of electrons; no partial charges; &Delta;EN &lt; 0.5.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Partial charges</b></td><td>None &mdash; symmetric electron distribution</td></tr><tr><td style='padding: 5px 10px;'><b>Melting / BP</b></td><td>Low &mdash; only London dispersion forces between molecules</td></tr><tr><td style='padding: 5px 10px;'><b>Conductivity</b></td><td>Poor &mdash; no free charges</td></tr><tr><td style='padding: 5px 10px;'><b>Solubility</b></td><td>&ldquo;Like dissolves like&rdquo; &mdash; dissolves in nonpolar solvents; insoluble in water</td></tr><tr><td style='padding: 5px 10px;'><b>State at RT</b></td><td>Often gas or liquid (low IMFs)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: H<sub>2</sub>, O<sub>2</sub>, N<sub>2</sub>, F<sub>2</sub>, Cl<sub>2</sub>, CH<sub>4</sub>, C<sub>6</sub>H<sub>6</sub></span><br><br><span style='font-size: 13px; color: #888;'>Bonds between identical atoms are always nonpolar; similar EN values also qualify</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 6: Polar covalent
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Polar Covalent Bond</b><br><br>What is a <span style='color: #4a90d9;'>polar covalent bond</span> and what are its properties?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Polar Covalent Bond</b><br><br>Forms between <b>two different nonmetals</b> of differing electronegativity. <b>Unequal sharing</b> of electrons; the more electronegative atom pulls electrons toward itself, creating partial charges (&delta;+ and &delta;&minus;); &Delta;EN 0.5&ndash;1.7.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Partial charges</b></td><td>&delta;+ on less EN atom; &delta;&minus; on more EN atom</td></tr><tr><td style='padding: 5px 10px;'><b>Melting / BP</b></td><td>Moderate to high &mdash; dipole-dipole and/or H-bonding IMFs</td></tr><tr><td style='padding: 5px 10px;'><b>Conductivity</b></td><td>Poor as pure substance (no free ions)</td></tr><tr><td style='padding: 5px 10px;'><b>Solubility</b></td><td>Often soluble in water and polar solvents</td></tr><tr><td style='padding: 5px 10px;'><b>State at RT</b></td><td>Gas, liquid, or solid depending on IMF strength</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: HCl, H<sub>2</sub>O, NH<sub>3</sub>, HF, SO<sub>2</sub>, CH<sub>3</sub>OH</span><br><br><span style='font-size: 13px; color: #888;'>Polar bonds don&rsquo;t always make a polar molecule &mdash; geometry determines if dipoles cancel</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 7: Coordinate covalent
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Coordinate Covalent Bond</b><br><br>What is a <span style='color: #4a90d9;'>coordinate covalent bond</span> and what are its properties?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Coordinate Covalent Bond</b><br><br>Both bonding electrons are donated by a single atom (the <b>Lewis base</b>) to an electron-deficient atom (the <b>Lewis acid</b>).<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Lewis base</b></td><td>Donates a lone pair &mdash; electron-pair donor (e.g., NH<sub>3</sub>, H<sub>2</sub>O, ligands)</td></tr><tr><td style='padding: 5px 10px;'><b>Lewis acid</b></td><td>Accepts the lone pair &mdash; electron-pair acceptor (e.g., H<sup>+</sup>, BF<sub>3</sub>, metal ions)</td></tr><tr><td style='padding: 5px 10px;'><b>Once formed</b></td><td>Identical to a regular covalent bond &mdash; cannot be distinguished</td></tr><tr><td style='padding: 5px 10px;'><b>Where found</b></td><td>Complex ions, metal&ndash;ligand bonds, acid&ndash;base reactions</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: NH<sub>4</sub><sup>+</sup> (N donates lone pair to H<sup>+</sup>), H<sub>3</sub>O<sup>+</sup>, BF<sub>3</sub>&middot;NH<sub>3</sub>, metal coordination complexes</span><br><br><span style='font-size: 13px; color: #888;'>All Lewis acid&ndash;base reactions involve forming a coordinate covalent bond</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 8: Bond dissociation energy
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bond Dissociation Energy</b><br><br>What is <span style='color: #4a90d9;'>bond dissociation energy</span> and how does it relate to bond order and bond length?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bond Dissociation Energy (BDE)</b><br><br>Energy required to homolytically break 1 mol of a specific bond in the gas phase &mdash; always <b>endothermic</b>.<br><br><table style='margin: auto; text-align: center; font-size: 15px; border-collapse: collapse;'><tr style='background:#f0f0f0;'><td style='padding: 5px 10px; font-weight: bold;'>Bond type</td><td style='padding: 5px 10px; font-weight: bold;'>Bond order</td><td style='padding: 5px 10px; font-weight: bold;'>BDE</td><td style='padding: 5px 10px; font-weight: bold;'>Bond length</td></tr><tr><td style='padding: 5px 10px;'>Single</td><td style='padding: 5px 10px;'>1</td><td style='padding: 5px 10px;'>Lowest</td><td style='padding: 5px 10px;'>Longest</td></tr><tr style='background:#f9f9f9;'><td style='padding: 5px 10px;'>Double</td><td style='padding: 5px 10px;'>2</td><td style='padding: 5px 10px;'>Medium</td><td style='padding: 5px 10px;'>Medium</td></tr><tr><td style='padding: 5px 10px;'>Triple</td><td style='padding: 5px 10px;'>3</td><td style='padding: 5px 10px;'>Highest</td><td style='padding: 5px 10px;'>Shortest</td></tr></table><br><span style='font-size: 14px; color: #555;'>&Delta;H<sub>rxn</sub> &asymp; &Sigma;BDE<sub>bonds broken</sub> &minus; &Sigma;BDE<sub>bonds formed</sub></span><br><br><span style='font-size: 13px; color: #888;'>BDE values are averages &mdash; actual bond energy varies with molecular environment</span></div>",
        "tags": ["chemistry::definition", "chemistry::bonding::covalent"]
    },
    # 9: Bond order — sigma and pi
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bond Order, &sigma; &amp; &pi; Bonds</b><br><br>What are <span style='color: #4a90d9;'>&sigma; and &pi; bonds</span> and how do you determine bond order?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Bond Order, &sigma; &amp; &pi; Bonds</b><br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>&sigma; (sigma)</b></td><td>End-to-end orbital overlap; allows free rotation; always the <b>1st bond</b> formed between two atoms</td></tr><tr><td style='padding: 5px 10px;'><b>&pi; (pi)</b></td><td>Side-to-side p orbital overlap; restricts rotation; only present in 2nd and 3rd bonds</td></tr></table><br><table style='margin: auto; text-align: center; font-size: 15px; border-collapse: collapse;'><tr style='background:#f0f0f0;'><td style='padding: 5px 10px; font-weight:bold;'>Bond type</td><td style='padding: 5px 10px; font-weight:bold;'>&sigma; bonds</td><td style='padding: 5px 10px; font-weight:bold;'>&pi; bonds</td><td style='padding: 5px 10px; font-weight:bold;'>Bond order</td></tr><tr><td style='padding: 5px 10px;'>Single</td><td style='padding: 5px 10px;'>1</td><td style='padding: 5px 10px;'>0</td><td style='padding: 5px 10px;'>1</td></tr><tr style='background:#f9f9f9;'><td style='padding: 5px 10px;'>Double</td><td style='padding: 5px 10px;'>1</td><td style='padding: 5px 10px;'>1</td><td style='padding: 5px 10px;'>2</td></tr><tr><td style='padding: 5px 10px;'>Triple</td><td style='padding: 5px 10px;'>1</td><td style='padding: 5px 10px;'>2</td><td style='padding: 5px 10px;'>3</td></tr></table><br>\[BO = \frac{n_{bonding} - n_{antibonding}}{2}\]<br><span style='font-size: 13px; color: #888;'>Resonance gives fractional bond orders &mdash; benzene BO = 1.5; higher BO &rarr; shorter, stronger bond</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 10: Resonance structures
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Structures</b><br><br>What are <span style='color: #4a90d9;'>resonance structures</span> and what do they represent?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Resonance Structures</b><br><br>When one Lewis structure can&rsquo;t accurately represent a molecule, multiple valid structures are drawn. The actual molecule is a <b>resonance hybrid</b> &mdash; an average of all structures with <b>delocalized electrons</b>.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Cause</b></td><td>Electrons delocalized over multiple atoms &mdash; can&rsquo;t be fixed to one position</td></tr><tr><td style='padding: 5px 10px;'><b>Stability</b></td><td>More resonance structures &rarr; more delocalization &rarr; more stable molecule</td></tr><tr><td style='padding: 5px 10px;'><b>Formal charge</b></td><td>Minimize on all atoms; negative FC should be on more electronegative atom</td></tr><tr><td style='padding: 5px 10px;'><b>Bond order</b></td><td>Fractional between contributing structures</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: benzene (BO = 1.5), CO<sub>3</sub><sup>2&minus;</sup>, NO<sub>3</sub><sup>&minus;</sup>, O<sub>3</sub>, SO<sub>2</sub></span><br><br><span style='font-size: 13px; color: #888;'>Resonance structures differ only in electron placement &mdash; atoms never move position</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 11: Hybridization
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hybridization</b><br><br>What are the <span style='color: #4a90d9;'>hybrid orbital types</span> and how do you determine an atom&rsquo;s hybridization?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hybridization</b><br><br><span style='font-size: 14px; color: #555;'>Count <b>electron groups</b> (bonded atoms + lone pairs) around the central atom:</span><br><br><table style='margin: auto; text-align: left; font-size: 14px; border-collapse: collapse;'><tr style='background:#f0f0f0;'><td style='padding: 5px 8px; font-weight:bold;'>Electron groups</td><td style='padding: 5px 8px; font-weight:bold;'>Hybridization</td><td style='padding: 5px 8px; font-weight:bold;'>Geometry</td><td style='padding: 5px 8px; font-weight:bold;'>Bond angle</td></tr><tr><td style='padding: 5px 8px;'>2</td><td style='padding: 5px 8px;'>sp</td><td style='padding: 5px 8px;'>Linear</td><td style='padding: 5px 8px;'>180&deg;</td></tr><tr style='background:#f9f9f9;'><td style='padding: 5px 8px;'>3</td><td style='padding: 5px 8px;'>sp<sup>2</sup></td><td style='padding: 5px 8px;'>Trigonal planar</td><td style='padding: 5px 8px;'>120&deg;</td></tr><tr><td style='padding: 5px 8px;'>4</td><td style='padding: 5px 8px;'>sp<sup>3</sup></td><td style='padding: 5px 8px;'>Tetrahedral</td><td style='padding: 5px 8px;'>109.5&deg;</td></tr><tr style='background:#f9f9f9;'><td style='padding: 5px 8px;'>5</td><td style='padding: 5px 8px;'>sp<sup>3</sup>d</td><td style='padding: 5px 8px;'>Trigonal bipyramidal</td><td style='padding: 5px 8px;'>90/120&deg;</td></tr><tr><td style='padding: 5px 8px;'>6</td><td style='padding: 5px 8px;'>sp<sup>3</sup>d<sup>2</sup></td><td style='padding: 5px 8px;'>Octahedral</td><td style='padding: 5px 8px;'>90&deg;</td></tr></table><br><span style='font-size: 13px; color: #888;'>Lone pairs count as electron groups for hybridization but compress bond angles. H<sub>2</sub>O: 4 groups &rarr; sp<sup>3</sup>, bent shape (~104.5&deg;). NH<sub>3</sub>: 4 groups &rarr; sp<sup>3</sup>, trigonal pyramidal.</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::covalent"]
    },
    # 12: Molecular polarity
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Molecular Polarity</b><br><br>What determines whether a <span style='color: #4a90d9;'>molecule is polar or nonpolar</span>?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Molecular Polarity</b><br><br>Requires both <b>polar bonds</b> AND <b>asymmetric geometry</b> (dipoles don&rsquo;t cancel).<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Step 1</b></td><td>Are there polar bonds? (&Delta;EN &gt; 0.5)</td></tr><tr><td style='padding: 5px 10px;'><b>Step 2</b></td><td>Does the molecular geometry cause dipoles to cancel?</td></tr></table><br><table style='margin: auto; text-align: left; font-size: 14px;'><tr><td style='padding: 4px 10px;'><b>Nonpolar (dipoles cancel)</b></td><td>CO<sub>2</sub> (linear), CCl<sub>4</sub> (tetrahedral), BF<sub>3</sub> (trigonal planar)</td></tr><tr><td style='padding: 4px 10px;'><b>Polar (dipoles don&rsquo;t cancel)</b></td><td>H<sub>2</sub>O (bent), NH<sub>3</sub> (pyramidal), HCl (diatomic), SO<sub>2</sub></td></tr></table><br><span style='font-size: 13px; color: #888;'>Polar molecules have a net dipole moment &mdash; determines which IMFs act between molecules</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::intermolecular"]
    },
    # 13: Hydrogen bonding
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydrogen Bonding</b><br><br>What is <span style='color: #4a90d9;'>hydrogen bonding</span>, what are the requirements, and what are its effects?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Hydrogen Bonding</b><br><br>A strong dipole-dipole attraction between an H atom (bonded to N, O, or F) and a lone pair on N, O, or F of a neighboring molecule.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Requirement</b></td><td>H bonded to <b>N, O, or F</b> only (highly EN &rarr; very &delta;+ H)</td></tr><tr><td style='padding: 5px 10px;'><b>Strength</b></td><td>Strongest IMF; weaker than covalent or ionic bonds</td></tr><tr><td style='padding: 5px 10px;'><b>Physical effects</b></td><td>Unusually high BP, high surface tension, high specific heat capacity</td></tr><tr><td style='padding: 5px 10px;'><b>Biology</b></td><td>DNA base pairing, protein secondary structure (&alpha;-helix, &beta;-sheet)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: H<sub>2</sub>O, HF, NH<sub>3</sub>, alcohols (&mdash;OH), carboxylic acids (&mdash;COOH)</span><br><br><span style='font-size: 13px; color: #888;'>IMF strength: H-bonding &gt; dipole-dipole &gt; London dispersion</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::intermolecular"]
    },
    # 14: Dipole-dipole forces
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Dipole-Dipole Forces</b><br><br>What are <span style='color: #4a90d9;'>dipole-dipole forces</span> and when do they occur?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>Dipole-Dipole Forces</b><br><br>Electrostatic attraction between the &delta;+ end of one polar molecule and the &delta;&minus; end of an adjacent polar molecule.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Occurs between</b></td><td>Polar molecules only</td></tr><tr><td style='padding: 5px 10px;'><b>Strength</b></td><td>Weaker than H-bonding; stronger than London dispersion</td></tr><tr><td style='padding: 5px 10px;'><b>Increases with</b></td><td>Larger dipole moment (greater &Delta;EN, larger partial charges)</td></tr></table><br><span style='font-size: 14px; color: #555;'>Examples: HCl, SO<sub>2</sub>, acetone &mdash; polar molecules without H bonded to N/O/F</span><br><br><span style='font-size: 13px; color: #888;'>Polar molecules experience BOTH dipole-dipole AND London dispersion forces</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::intermolecular"]
    },
    # 15: London dispersion forces
    {
        "front": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>London Dispersion Forces</b><br><br>What are <span style='color: #4a90d9;'>London dispersion forces</span> and what factors affect their strength?</div>",
        "back": r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'><b>London Dispersion Forces</b><br><br>Weak attractions from temporary induced dipoles caused by momentary uneven electron distribution; present in <b>all molecules</b>.<br><br><table style='margin: auto; text-align: left; font-size: 15px;'><tr><td style='padding: 5px 10px;'><b>Present in</b></td><td>ALL molecules &mdash; polar and nonpolar alike</td></tr><tr><td style='padding: 5px 10px;'><b>Increases with</b></td><td>Larger molecular size, more electrons, higher MW, greater surface area</td></tr><tr><td style='padding: 5px 10px;'><b>Decreases with</b></td><td>Branching &mdash; reduces surface area contact between molecules</td></tr><tr><td style='padding: 5px 10px;'><b>Only IMF for</b></td><td>Nonpolar molecules (noble gases, CH<sub>4</sub>, I<sub>2</sub>, hexane, CCl<sub>4</sub>)</td></tr></table><br><span style='font-size: 14px; color: #555;'>I<sub>2</sub> is solid at RT despite being nonpolar &mdash; large LDF from many electrons</span><br><br><span style='font-size: 13px; color: #888;'>Also called van der Waals forces or induced dipole&ndash;induced dipole forces</span></div>",
        "tags": ["chemistry::concept", "chemistry::bonding::intermolecular"]
    },
]

print("Validating cards...")
for i, card in enumerate(cards):
    validate(card["front"], card["back"])
print(f"All {len(cards)} cards validated.")

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
        print(f"  Card {i+1}: duplicate, updating...")
        success = find_and_update(card["front"], card["back"], card["tags"])
        if success:
            updated += 1
            print(f"  Card {i+1}: UPDATED")
        else:
            errors.append(card["front"][:60])
            print(f"  Card {i+1}: ERROR")

print(f"\nDone. Added: {added}, Updated: {updated}, Errors: {len(errors)}")
if errors:
    for e in errors:
        print(f"  {e}")
