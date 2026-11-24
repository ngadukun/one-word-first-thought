"""One Word, First Thought - a make.fun micro entry.

Writes exactly one word and nothing else to the entry file.
The word is 'sonder': the sudden realisation that every
passerby is living a life as vivid and complicated as your
own. First thought, no second draft, exactly as briefed.
"""

import os
from pathlib import Path

ENTRY = "sonder"


def entry_path() -> Path:
    # The grader mounts the repo read-only and hands us a
    # writable directory through MAKEFUN_OUTPUT_DIR; locally
    # we fall back to output/ beside this file.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.txt"
    return Path(__file__).resolve().parent / "output" / "entry.txt"


def main() -> None:
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
