"""Entry for make.fun: Notes From a Passive-Aggressive Fridge.

Writes one passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Deterministic: no randomness, no network, no input.
"""

import os

ENTRY = (
    # One line, 114 characters: the fridge brags about its temperature
    # sensor, then lands the sting on the owner's standards.
    "Your leftovers turned nine today. I kept them at exactly 4\u00b0C the whole "
    "time \u2014 I have standards, even if you don't."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must fit the 200-character gate"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
