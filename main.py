#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting - make.fun entry.

Writes one voicemail greeting, as if recorded by a cat, to
$MAKEFUN_OUTPUT_DIR/entry.txt. The house gate requires UTF-8 text of
1 to 120 characters, so the program writes the line exactly, with no
trailing newline, and refuses to write anything when it is too long.
"""

import os
import sys

LINE = (
    "This is Mittens. I knocked your voicemail off the table. "
    "It was asking for it. Leave a message after the purr."
)
MAX_CHARS = 120


def main() -> int:
    if len(LINE) > MAX_CHARS:
        print(
            f"entry too long: {len(LINE)} > {MAX_CHARS} characters",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
