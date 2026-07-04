from biochem_helpers import assert_connected, store_screenshot, validate, push_cards

DECK = "MCAT Biochemistry"

assert_connected()

img = store_screenshot("peptide-bonds")  # newest screenshot

front = (
    r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>"
    r"<b>Peptide Bonds</b><br><br>"
    r"How are amino acids joined into a polypeptide? Describe the "
    r"<span style='color: #4a90d9;'>reaction</span>, the "
    r"<span style='color: #4a90d9;'>bond location</span>, the "
    r"<span style='color: #4a90d9;'>backbone</span>, and the two "
    r"<span style='color: #4a90d9;'>termini</span>."
    r"</div>"
)

back = (
    r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>"
    r"<b>Peptide Bonds</b><br><br>"
    r"Amino acids join by a <b>dehydration / condensation</b> reaction (a water molecule is lost).<br><br>"
    r"The peptide bond forms between the <b>carboxyl group of one amino acid</b> and the "
    r"<b>amino group of the next</b>.<br><br>"
    r"This creates a repeating <b>N&ndash;C&ndash;C backbone</b> &mdash; each &ldquo;N-C-C&rdquo; "
    r"unit is one amino acid in the chain.<br><br>"
    r"<table style='margin: auto; text-align: left; font-size: 15px;'>"
    r"<tr><td style='padding: 4px 10px;'><b>N-terminus</b></td><td>end with the free <b>amino</b> group (first AA)</td></tr>"
    r"<tr><td style='padding: 4px 10px;'><b>C-terminus</b></td><td>end with the free <b>carboxyl</b> group (last AA)</td></tr>"
    r"</table><br>"
    + img +
    r"<span style='font-size: 13px; color: #888;'>Be able to spot the peptide bond, the N-/C-termini, "
    r"and individual amino acids within a chain.</span>"
    r"</div>"
)

validate(front, back)

cards = [{
    "front": front,
    "back": back,
    "tags": ["biochem::concept", "biochem::proteins::peptide-bonds"],
}]

added, updated, errors = push_cards(cards, DECK)
print(f"Added: {added}, Updated: {updated}, Errors: {errors}")
