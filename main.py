"""Sorry, I Heard That Wrong — round 2 entry writer.

A small deterministic program: it keeps the one-line joke, checks the
length sits inside the contest window, and writes it with no trailing
newline to /output/entry.txt. Nothing random, nothing fetched.
"""

from pathlib import Path

ENTRY = "Sorry — I heard 'wake me at seven' and woke you at seven. PM. You're welcome."
LOWER = 1
UPPER = 140
TARGET = Path("/output") / "entry.txt"


def length_ok(text):
    """True when the text fits the 1-140 character window."""
    return LOWER <= len(text) <= UPPER


def save_entry(text):
    """Check the entry, then write it exactly, no trailing newline."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be one line only")
    if not length_ok(text):
        raise ValueError(
            "entry must be %d-%d chars, got %d" % (LOWER, UPPER, len(text))
        )
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text, encoding="utf-8")


def main():
    save_entry(ENTRY)


if __name__ == "__main__":
    main()
