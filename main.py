"""make.fun bounty entry: "Sorry, I Heard That Wrong".

Writes the one-line apology a smart speaker gives after mishearing its
owner to /output/entry.txt, then reads it back to confirm it matches.
Python 3, standard library only.
"""

import os

ENTRY = (
    "Sorry, I heard 'turn off the lights' as 'turn on the fight' "
    "\u2014 the lamp is in a boxing stance and the toaster has picked a side."
)

MAX_CHARS = 140


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("entry.txt does not match the entry")
    print(f"OK: wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
