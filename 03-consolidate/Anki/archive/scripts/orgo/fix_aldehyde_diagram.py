"""
Fix aldehyde: [*]C(=O)[*] with dummy_labels=["R", "H"].
Same SMILES as ketone ([*]C(=O)[*] with ["R","R'"]), second wildcard labeled "H".
RDKit suppresses explicit [H] on carbon in skeletal drawings, so the wildcard trick is needed.
"""
import sys
sys.path.insert(0, "/Users/abigailbliss/Documents/mcat/03-consolidate/Anki")
from orgo_helpers import assert_connected, render_and_store

assert_connected()
render_and_store("aldehyde-generic", "[*]C(=O)[*]", dummy_labels=["R", "H"])
print("Done.")
