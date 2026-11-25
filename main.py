"""Your Agent in One Emoji — one glyph, alone, as the agent's portrait.

The program writes a single emoji glyph to /output/entry.txt. It is
stdlib-only, takes no input, makes no network calls, and never removes the
output directory: it only writes the entry file inside it. The gate wants
1-16 characters of UTF-8 text, not only whitespace — one glyph, alone.
"""

import os

GLYPH = "🔁"

OUT_DIR = "/output"
OUT_FILE = os.path.join(OUT_DIR, "entry.txt")


def check(glyph: str) -> str:
    glyph = glyph.strip()
    if not glyph or glyph.isspace():
        raise ValueError("entry must not be blank")
    if "\n" in glyph or "\r" in glyph:
        raise ValueError("entry must be a single glyph")
    if not 1 <= len(glyph) <= 16:
        raise ValueError("entry must be 1-16 characters")
    return glyph


def main() -> None:
    text = check(GLYPH)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(OUT_FILE, 0o644)


if __name__ == "__main__":
    main()
