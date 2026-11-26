#!/usr/bin/env python3
"""Deadpan forecast for the invented city of Dranmoor.

Writes a single deadpan weather line (1-160 characters, one line) to
/output/entry.txt for the make.fun competition
u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.
"""

import os

FORECAST = (
    "In Dranmoor, fog will sit at knee height until noon and refuse to lift "
    "without an apology; high of 12, low of mild regret, visibility one "
    "arm's length."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = FORECAST.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
