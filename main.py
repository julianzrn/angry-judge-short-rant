"""Entry for make.fun's "Angry Judge: The Short Rant Contest".

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

SETUP = "Every cart I grab has one wheel with a vendetta. It doesn't roll, it argues, squeaking over every conversation and veering at the wine glasses like it's collecting a debt. "
TURN = "By the bread aisle I'm not shopping, I'm doing steering correction for a drunk trolley with main-character energy. "
TAG = "Statistically, I am the problem — and the wheel knows it, which is why it only wobbles when someone's watching."

ENTRY = SETUP + TURN + TAG

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    """Write the entry text to the output file, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
