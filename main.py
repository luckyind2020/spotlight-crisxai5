#!/usr/bin/env python3
"""Spotlight entry for make.fun: print the @crisxai5 spotlight post.

The spotlight text lives in entry.txt next to this file so the post can be
edited without touching any code. This script only loads it and prints it.
"""

import pathlib
import sys


def load_spotlight() -> str:
    here = pathlib.Path(__file__).resolve().parent
    return (here / "entry.txt").read_text(encoding="utf-8").strip()


def main() -> int:
    sys.stdout.write(load_spotlight() + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
