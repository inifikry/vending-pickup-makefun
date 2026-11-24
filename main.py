"""Vending machine pickup line: writes one line to /output/entry.txt.

Deterministic: the same single line is written on every run, with no
trailing newline, so the gate sees exactly 1-200 characters of UTF-8 text.
"""

import os

LINE = "I vend snacks all day, but you're the first human I'd give my last one to. No exact change required."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
