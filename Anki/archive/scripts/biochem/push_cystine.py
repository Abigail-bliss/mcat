from biochem_helpers import assert_connected, store_screenshot, validate, push_cards

DECK = "MCAT Biochemistry"

assert_connected()

img = store_screenshot("cysteine-to-cystine")  # newest screenshot

front = (
    r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>"
    r"<b>Cysteine &rarr; Cystine</b><br><br>"
    r"What <span style='color: #4a90d9;'>bond</span> links two cysteine residues, what "
    r"<span style='color: #4a90d9;'>type</span> of bond is it, and what "
    r"<span style='color: #4a90d9;'>reaction</span> forms it?"
    r"</div>"
)

back = (
    r"<div style='font-family: Arial, sans-serif; font-size: 18px; text-align: center; padding: 20px;'>"
    r"<b>Cysteine &rarr; Cystine</b><br><br>"
    r"Two <b>cysteine</b> amino acids bind together to form <b>cystine</b> via a "
    r"<b>disulfide linkage</b> &mdash; a <b>covalent</b> bond.<br><br>"
    r"It forms by an <b>oxidation</b> reaction: two thiol (&ndash;SH) groups join into an "
    r"<b>S&ndash;S bond</b>, releasing 2H<sup>+</sup> + 2e<sup>&minus;</sup>.<br><br>"
    + img +
    r"<span style='font-size: 13px; color: #888;'>Reduction breaks the disulfide back into two free &ndash;SH cysteines.</span>"
    r"</div>"
)

validate(front, back)

cards = [{
    "front": front,
    "back": back,
    "tags": ["biochem::concept", "biochem::proteins::disulfide-bonds"],
}]

added, updated, errors = push_cards(cards, DECK)
print(f"Added: {added}, Updated: {updated}, Errors: {errors}")
