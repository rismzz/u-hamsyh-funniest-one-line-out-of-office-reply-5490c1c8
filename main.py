#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — one out-of-office line an AI
agent would leave. Writes the line verbatim to entry.txt.

The joke turns the usual reassurance upside down: the agent covering for
you does not help, it misunderstands your email — confidently, and in
real time. Being ignored by something that never sleeps is the upgrade
nobody asked for. "Confidently misunderstood" is the whole line in two
words; the rest just sets the trap.
"""

import os
from pathlib import Path

LINE = "I'm out until Monday — my agent is covering for me, so your email will now be confidently misunderstood in real time."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
