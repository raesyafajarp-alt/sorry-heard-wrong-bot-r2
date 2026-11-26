#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — writes one funny smart-speaker apology."""

ENTRY = "Sorry \u2014 I heard 'wake me at seven' and woke you at seven. PM. You're welcome."

MAX_CHARS = 140


def validate_entry(text: str) -> None:
    """Gate: 1-140 characters, not only whitespace, single line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def _write_entry(text: str, path: str = "/output/entry.txt") -> None:
    validate_entry(text)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    _write_entry(ENTRY)


if __name__ == "__main__":
    main()
