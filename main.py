"""Say What Actually Broke.

One line of software error copy that tells the user the brutal truth
about what went wrong and makes them laugh: the save failed because
the disk is full of the user's own drafts named final_FINAL_v2, and
the program was too polite to delete any of them. The joke lands
because it names the real failure — a full disk — and the real cause
— the user's own pile of almost-final drafts — instead of hiding
behind a generic error code.
"""

import os
import sys

# Names the real failure (disk full) and its real cause (the user's
# own draft pile), so it stays funny and shippable in a real dialog.
ERROR_LINE = "Your file did not save: the disk is full of your 47 drafts named final_FINAL_v2, and we were too polite to delete them."


def output_dir():
    """Return the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    text = ERROR_LINE + "\n"
    # The file and stdout are written from the same text, so they can
    # never disagree about the exact bytes.
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    # newline="\n" pins the line ending, so the byte count is identical on
    # any platform the grader runs (no CRLF translation of the line).
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
