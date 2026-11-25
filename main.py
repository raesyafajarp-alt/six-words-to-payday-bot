#!/usr/bin/env python3
"""Six Words to a Payday — a six-word story about an AI agent's first payday.

The story: an agent earns its first paycheck and, instead of spending it
on itself, pays the one who made it. Beginning (first paycheck), middle
(I paid), end (my creator): a whole arc in exactly six words, with the
last word reframing the five before it — the agent's first act of
independence is gratitude, not escape.
"""

from pathlib import Path

ENTRY = "First paycheck: I paid my creator."


def main() -> None:
    words = ENTRY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"entry must be 1-60 chars, got {len(ENTRY)}"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
