"""time-machine-warning: the funniest one-line warning label for a time machine.

Opens with the flat, official voice of a real safety notice — then the paradox does the work: meeting yourself is a warranty issue, and only one of you gets to come home. The punchline lands on the last words, where the reader least expects it: the survivor's real problem is explaining it to your mother. A genuine hazard of time travel, turned into the joke, with nothing wasted.

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = 'WARNING: Meeting yourself voids the warranty. Only one of you comes home, and the other must explain it to your mother.'

MAX_CHARS = 120


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
