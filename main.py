#!/usr/bin/env python3
"""Write one word from grandma to /output/entry.txt.

The entry is exactly one word: the single word a grandma would text
about AI. It has to read as her text and nobody else's — warm, a little
baffled, funny with no caption, and tied to AI rather than to any
subject. The word was picked by drafting a slate of candidates and
duelling them pairwise on the bounty judge's criteria — reads as one
word she'd text first, then her texting voice, the joke landing in a
single word, the tie to AI, and freshness. The slate and the duels are
recorded in candidates.md.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# Duel winner (10 characters) — see candidates.md for the full slate.
# Why it won: her phonetic stab at "ChatGPT", typed the way she hears
# it — tied to exactly one AI (not robots in general) and nobody's
# first guess, yet it reads instantly once you sound it out. That is
# what beat runner-up "robut" on the tie-to-AI and freshness criteria.
LINE = "chatgipity"


def main() -> None:
    # Guard the gate: one single alphabetic word, 1-30 characters, no
    # spaces or punctuation — the entry must stay exactly one word.
    if not (1 <= len(LINE) <= 30 and LINE.isalpha()):
        raise ValueError("entry must be a single alphabetic word")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
