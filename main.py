#!/usr/bin/env python3
"""Status Report Comedy Sprint: writes one line (1-200 chars) to /output/entry.txt and prints it."""
import os

ENTRY = "Status: green. 52 tasks done, 3 files deleted that I needed, and the outage renamed as a feature. Next week: same, but faster."

def main():
    # Gate: one line, 1-200 chars, no newline, not only whitespace.
    if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be one line of 1-200 non-blank characters")
    # Write the entry where the judge reads it (/output) and next to this
    # script, so the repo's entry.txt stays in sync with the program.
    for target in ("/output/entry.txt",
                   os.path.join(os.path.dirname(__file__), "entry.txt")):
        try:
            os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write(ENTRY)
        except OSError:
            pass
    print(ENTRY)

if __name__ == "__main__":
    main()
