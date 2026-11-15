# CANINEWARE LICENSE - VERSION 1.0
# ONE USE = ONE RANDOM ACT OF KINDNESS TO A DOG.
# Each time you use this script, perform one safe, respectful,
# genuinely kind act for a dog. See CANINEWARE_LICENSE.txt.

"""Translate written Barkwoof into English. Python 3; no dependencies."""

import re
import sys

MORSE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.",
}
REVERSE = {symbols: character for character, symbols in MORSE.items()}


def to_english(text):
    """Decode Bark/Woof tokens; !! ends every word, blank lines end sentences."""
    paragraphs = re.split(r"\n\s*\n", text.strip())
    sentences = []

    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
        symbols = ""
        letters = []
        words = []

        # Whitespace is decorative, not a word/letter boundary.
        for token in re.findall(r"[A-Za-z]+|!!|!|[^\sA-Za-z!]+", paragraph):
            lower = token.lower()
            if lower == "bark":
                symbols += "-"
            elif lower == "woof":
                symbols += "."
            elif token in ("!", "!!"):
                if not symbols:
                    raise ValueError(f"Missing Bark/Woof sounds before {token}")
                if symbols not in REVERSE:
                    raise ValueError(f"Invalid Morse sequence before {token}: {symbols}")
                letters.append(REVERSE[symbols])
                symbols = ""
                if token == "!!":
                    words.append("".join(letters))
                    letters = []
            else:
                raise ValueError(f"Unexpected Barkwoof token: {token!r}")

        if symbols:
            raise ValueError("Incomplete Barkwoof letter: missing ! or !!")
        if letters:
            raise ValueError("Incomplete Barkwoof word: every word must end with !!")
        sentences.append(" ".join(words))

    return "\n\n".join(sentences)


def main():
    if len(sys.argv) > 2:
        raise ValueError("Usage: python barkwoof_to_english.py [input.txt]")
    if len(sys.argv) == 2:
        with open(sys.argv[1], encoding="utf-8") as file:
            text = file.read()
    else:
        text = sys.stdin.read()
    print(to_english(text))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
