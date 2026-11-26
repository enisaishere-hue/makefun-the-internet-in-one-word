#!/usr/bin/env python3
"""The Internet in One Word -- make.fun entry.

Writes the one word that describes the whole internet, to entry.txt
inside the output directory.

The output directory comes from the MAKEFUN_OUTPUT_DIR environment
variable (default /output). A first command-line argument, if given,
overrides it, but the program never requires one: the grader runs it
with no arguments at all.
"""

import os
import sys

ONE_WORD = "Doomscrolling"


def read_back(path):
    """Read the entry back: it must be the word, one line, nothing else."""
    with open(path, "r", encoding="utf-8", newline="") as handle:
        text = handle.read()
    if text != ONE_WORD + "\n":
        print("entry.txt is not exactly the word", file=sys.stderr)
        return False
    return True


def entry(argv):
    # The brief wants one word and nothing else; refuse loudly if the
    # word ever stops being exactly that.
    if len(ONE_WORD.split()) != 1:
        print("entry must be a single word, got %r" % ONE_WORD,
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if len(argv) > 1:
        out_dir = argv[1]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ONE_WORD + "\n")
    if not read_back(path):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(entry(sys.argv))
