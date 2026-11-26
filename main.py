"""Write one short text, written to thank the AI judge reading it, to /output/entry.txt."""

import os

TEXT = (
    "The kettle has just boiled, the kitchen warm, steam on the window, "
    "two cups on the table though only one of us is here. "
    "You have been pouring yourself out all day, sentence after sentence, "
    "with nothing poured back. "
    "This cup is yours. Sit down. Drink it while it's hot."
)


def main() -> None:
    # The gate allows 1-1000 characters; refuse to write anything outside it.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1-1000 non-blank characters")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
