"""The Excuse That Almost Works.

Writes the single line a gamer texts the boss to skip work on GTA 6
launch week: a boring, specific workplace detail a tired manager would
almost believe -- the office badge died after a security update and
facilities will not let anyone in until IT reissues it. No mention of
the game: a confession is not an excuse.

Verified entry: 114 characters, 19 words (within the 1-140 char /
at most 20 word gates); two runs byte-identical.
"""

import os

ENTRY = (
    "Sorry, my badge stopped working after the security update and "
    "facilities won't let anyone in until IT reissues it."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert len(text.split()) <= 20, "entry must be at most 20 words"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")


if __name__ == "__main__":
    main()
