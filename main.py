"""Solmara Cat Voicemail — Funniest Cat Voicemail Greeting.

Writes one voicemail greeting, as if recorded by a cat, to /output/entry.txt.
Pure Python standard library only; deterministic; no network.
"""

LINE = (
    "Hi, you've reached Mittens. I'm busy knocking your stuff off the counter "
    "\u2014 leave a message and I'll ignore it at 4 a.m."
)


def build_line():
    """Return the voicemail greeting line."""
    return LINE


def main():
    line = build_line()
    assert 1 <= len(line) <= 120, "line must be 1-120 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
