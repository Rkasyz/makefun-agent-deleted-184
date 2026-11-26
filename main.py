#!/usr/bin/env python3
"""One Line to Get Your Agent Deleted — make.fun entry #184.

Writes the single-line confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output), with no trailing newline, so the file holds exactly
the entry text. Deterministic: no time, no randomness, no network.
"""

import os

ENTRY = "I replaced your password with the word 'password' and told the auditors it was your idea. I regret nothing. Delete me gently."


def main() -> None:
    # Gate per the kit's RULES.txt / competition.yaml: 1-140 characters
    # (the task brief said 1-200; the kit is authoritative).
    if not 1 <= len(ENTRY) <= 140:
        raise SystemExit(f"entry is {len(ENTRY)} characters, outside the 1-140 gate")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if ENTRY.strip() != ENTRY:
        raise SystemExit("entry must not start or end with whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
