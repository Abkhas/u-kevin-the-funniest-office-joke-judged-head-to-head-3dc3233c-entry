#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one office joke, a single line, to /output/entry.txt.
The joke is built from a setup (the shared fridge, a thief everyone
recognises) and a turn (the label that backfires on the owner himself):
the punchline lands last, in the final clause.
"""

import os

LINE = (
    "Someone keeps stealing my lunch from the shared fridge, "
    "so I labelled it 'Dave's' \u2014 nobody has touched it "
    "in three weeks, including Dave."
)


def main() -> None:
    # The sealed gate accepts 1 to 200 characters only; fail loudly
    # here rather than shipping an entry the grader would list as 0.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry is {len(LINE)} chars, gate needs 1-200")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
