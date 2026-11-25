"""Entry for make.fun competition: u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.

Running this program writes the entry rant to /output/entry.txt
as UTF-8 with no trailing newline.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

FIRST = "Every cart I grab has one wheel with a vendetta. It doesn't roll, it argues, squeaking over every conversation and veering at the wine glasses like it's collecting a debt. "
SECOND = "By the bread aisle I'm not shopping, I'm doing steering correction for a drunk trolley with main-character energy. "
THIRD = "Statistically, I am the problem — and the wheel knows it, which is why it only wobbles when someone's watching."

ENTRY = FIRST + SECOND + THIRD


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry rant to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()

# Re-verified before submission: the program output is byte-identical to the finalized entry.
