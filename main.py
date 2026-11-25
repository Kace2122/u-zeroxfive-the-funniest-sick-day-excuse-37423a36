#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — writes one line to /output/entry.txt.

Deterministic: no randomness, no time, no network. The entry is a single
line under 200 characters, checked against the competition gate before
anything is written.
"""
import os

ENTRY = (
    "Can't come in today \u2014 my neighbour's parrot learned my Teams "
    "ringtone and has been answering my calls with \"he's dead, ring back "
    "Monday\" since 7am"
)


def main():
    text = ENTRY
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with whitespace"
    assert text[-1].isalnum(), "entry must end on a word, not punctuation"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
