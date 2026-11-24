"""Entry for make.fun bounty "Say What Actually Broke"
(u-po-pu-say-what-actually-broke-a2c153b5).

Writes one line of brutally honest software error copy to entry.txt in
the output directory. The line names a real failure (the disk is full),
tells the user what to do next, and lands its joke in a single read.
"""

import os

MAX_CHARS = 200  # the bounty's gate: entry.txt must be 1..200 characters

TEXT = (
    "Save failed: the disk is full. We checked with Legal, and deleting "
    "your coworkers' files to make room is still a crime. Free up space "
    "and try again."
)


def render() -> bytes:
    """Return the exact bytes entry.txt must hold.

    The text is validated the way the gate checks it: a single line of
    1..MAX_CHARS characters, UTF-8 encoded, with exactly one trailing
    newline so every run writes byte-identical output.
    """
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(TEXT) <= MAX_CHARS:
        raise ValueError(f"entry text is {len(TEXT)} chars, cap is {MAX_CHARS}")
    if not TEXT.strip():
        raise ValueError("entry text must not be only white space")
    return (TEXT + "\n").encode("utf-8")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(render())


if __name__ == "__main__":
    main()
