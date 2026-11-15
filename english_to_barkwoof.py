# CANINEWARE LICENSE - VERSION 1.0
# ONE USE = ONE RANDOM ACT OF KINDNESS TO A DOG.
# Each time you use this script, perform one safe, respectful,
# genuinely kind act for a dog. See CANINEWARE_LICENSE.txt.

"""Translate English text into the written Barkwoof code. Python 3; no dependencies."""

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


def to_barkwoof(text):
    """Encode A-Z and 0-9; ! ends letters, !! ends every word.

    English .!? or a blank line end a sentence (a Barkwoof paragraph).
    Other punctuation is not encoded.
    """
    text = re.sub(r"(?<=[A-Za-z])['’](?=[A-Za-z])", "", text).upper()
    sentences = re.split(r"[.!?]+|\n\s*\n", text)
    output = []

    for sentence in sentences:
        words = re.findall(r"[A-Z0-9]+", sentence)
        encoded_words = []
        for word in words:
            letters = []
            for char in word:
                sounds = ["Bark" if symbol == "-" else "Woof" for symbol in MORSE[char]]
                sounds[1:] = [sound.lower() for sound in sounds[1:]]
                letters.append(" ".join(sounds))
            encoded_words.append("! ".join(letters) + "!!")
        if encoded_words:
            output.append(" ".join(encoded_words))

    return "\n\n".join(output)


def main():
    if len(sys.argv) > 2:
        raise ValueError("Usage: python english_to_barkwoof.py [input.txt]")
    if len(sys.argv) == 2:
        with open(sys.argv[1], encoding="utf-8") as file:
            text = file.read()
    else:
        text = sys.stdin.read()
    print(to_barkwoof(text))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
