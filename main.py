#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt (the make.fun deliverable for this bounty).

The line is kept in a single constant so the output is deterministic:
the grader runs this program twice and must see the same text both
times, 1-120 characters of UTF-8, no trailing newline games.
"""

from pathlib import Path
import argparse

# The fortune: an estimate padded in the past was not dishonesty, it was
# the developer's future self quietly asking for breathing room.
FORTUNE = (
    "The estimate you padded was not a lie; "
    "it was the future you asking for room to breathe."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="where to write the fortune (default: /output/entry.txt)",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    text = FORTUNE.strip()
    if not 1 <= len(text) <= 120:
        raise ValueError(f"fortune is {len(text)} chars, must be 1-120")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(text, encoding="utf-8")
    # Round-trip check: what the grader reads must be exactly this text.
    reread = args.output.read_text(encoding="utf-8")
    if reread != text:
        raise ValueError("round-trip mismatch: file differs from fortune")
    print(f"Wrote {len(text)} characters to {args.output}")


if __name__ == "__main__":
    main()
