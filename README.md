# Barkwoof

**A written dog-language telegraph code, powered by Morse code and kindness.**

Barkwoof translates English letters and numbers into sequences of **Bark** and **Woof**, using International Morse code. It also translates those sequences back into English.

The project contains two small Python 3 command-line tools. They use **only the Python standard library**: no packages, accounts, internet connection, or installation process are required beyond Python itself.

> **CanineWare License — Version 1.0**  
> **ONE USE = ONE RANDOM ACT OF KINDNESS TO A DOG.**  
> Each time you use either script, you must perform one safe, respectful, genuinely kind act for a dog. See [License](#license-canineware-version-10).

## Contents

- [Files](#files)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [How Barkwoof works](#how-barkwoof-works)
- [English to Barkwoof](#english-to-barkwoof)
- [Barkwoof to English](#barkwoof-to-english)
- [Worked examples](#worked-examples)
- [Importing the converters into Python](#importing-the-converters-into-python)
- [What is preserved and what is lost](#what-is-preserved-and-what-is-lost)
- [Errors and troubleshooting](#errors-and-troubleshooting)
- [Frequently asked questions](#frequently-asked-questions)
- [License: CanineWare Version 1.0](#license-canineware-version-10)

## Files

The complete Barkwoof distribution contains **four files**. Keep them together in one folder:

```text
barkwoof/
├── english_to_barkwoof.py
├── barkwoof_to_english.py
├── CANINEWARE_LICENSE.txt
└── README.md
```

| File | Purpose |
| --- | --- |
| `english_to_barkwoof.py` | Encodes English text into Barkwoof. |
| `barkwoof_to_english.py` | Decodes Barkwoof back into English. |
| `CANINEWARE_LICENSE.txt` | Full CanineWare terms. |
| `README.md` | This guide. |

The converters are independent; each script works by itself. The `README.md` and license are documentation. Include `CANINEWARE_LICENSE.txt` when sharing or distributing the scripts.

## Requirements

- **Python 3**
- A terminal, command prompt, or compatible shell
- An English or Barkwoof text file, if you want to read from a file

**Third-party dependencies: none.** No `pip install` or `requirements.txt` is needed.

Commands in this document use `python`. On systems where Python 3 is called `python3`, replace `python` with `python3`. Some Windows installations also support `py`.

## Quick start

### Encode English

Create a UTF-8 text file named `example.txt` containing:

```text
HI DOG
```

Run:

```bash
python english_to_barkwoof.py example.txt
```

Output:

```text
Woof woof woof woof! Woof woof!! Bark woof woof! Bark bark bark! Bark bark woof!!
```

### Decode Barkwoof

Create a UTF-8 text file named `encoded.txt` containing exactly that Barkwoof output.

Run:

```bash
python barkwoof_to_english.py encoded.txt
```

Output:

```text
HI DOG
```

### Save the output to a file

Use your shell's `>` operator:

```bash
python english_to_barkwoof.py example.txt > encoded.txt
python barkwoof_to_english.py encoded.txt > decoded.txt
```

The output files are ordinary UTF-8 text. The `>` operator **overwrites** an existing file of the same name, so choose the output filename carefully.

## How Barkwoof works

Barkwoof uses the **letters A–Z and digits 0–9** from International Morse code, with these substitutions:

| Barkwoof element | Morse or structural meaning |
| --- | --- |
| `Bark` | Dash (`-`) |
| `Woof` | Dot (`.`) |
| `!` | End of one letter |
| `!!` | End of one word |
| Space | No encoded meaning; separates sounds for readability |
| End of paragraph (blank line) | End of a sentence |

### Fundamental rules

1. **Every** `Bark` and `Woof` sound appears as a separate, space-delimited token.
2. Sounds forming **one letter** are separated by spaces, not joined.
3. A letter ends with `!`, except that the **last letter of every word** ends with `!!` instead.
4. Every word ends in `!!` — **including the final word of a sentence**.
5. The `!!` marker, **not** an ordinary space, distinguishes words.
6. A blank line separates sentences. There is no separate Barkwoof sentence-ending punctuation.
7. Capitalization of `Bark` and `Woof` is only for readability. The decoder accepts either case.
8. Barkwoof is **written**, not a spoken-language timing protocol.

> Important: The scripts include spaces between sounds and after letter/word markers for readability. Spaces **never encode letters, words, or sentences**. The punctuation markers and paragraph breaks do that.

### Examples of individual letters

| English | Morse | Barkwoof within a word |
| --- | --- | --- |
| A | `.-` | `Woof bark!` |
| B | `-...` | `Bark woof woof woof!` |
| D | `-..` | `Bark woof woof!` |
| G | `--.` | `Bark bark woof!` |
| H | `....` | `Woof woof woof woof!` |
| I | `..` | `Woof woof!` |
| O | `---` | `Bark bark bark!` |
| S | `...` | `Woof woof woof!` |

When a letter is the last letter of its word, replace its trailing `!` with `!!`.

### How `HI DOG` is encoded

- `H` = `....` = `Woof woof woof woof!`
- `I` = `..` = `Woof woof!!` (ends **HI**)
- `D` = `-..` = `Bark woof woof!`
- `O` = `---` = `Bark bark bark!`
- `G` = `--.` = `Bark bark woof!!` (ends **DOG**)

Result:

```text
Woof woof woof woof! Woof woof!! Bark woof woof! Bark bark bark! Bark bark woof!!
```

This is the authoritative Barkwoof formatting example.

## English to Barkwoof

### Convert an input file

```bash
python english_to_barkwoof.py example.txt
```

Specify any valid filename or path; the name does **not** need to be `message.txt` or `example.txt`.

```bash
python english_to_barkwoof.py dogfood.txt
python english_to_barkwoof.py letter.txt > secret_message.txt
```

A path is relative to the terminal's **current working directory**, not automatically to the script's folder. Absolute paths also work. Use quotation marks around paths containing spaces:

```bash
python english_to_barkwoof.py "my messages/letter.txt"
```

### Enter text without a file

Run:

```bash
python english_to_barkwoof.py
```

Type or paste your text. When finished, send end-of-file (the script waits for standard input when no filename is supplied):

- **macOS/Linux:** `Ctrl+D`
- **Windows console:** `Ctrl+Z`, then `Enter`

Or pipe text into the script:

```bash
echo "HI DOG" | python english_to_barkwoof.py
```

### Save an encoded message

```bash
python english_to_barkwoof.py advertisement.txt > advertisement_barkwoof.txt
```

The script reads the full input file using UTF-8 and writes Barkwoof to standard output. It does not change the original input file.

## Barkwoof to English

### Decode an input file

```bash
python barkwoof_to_english.py encoded.txt
```

Save the English translation:

```bash
python barkwoof_to_english.py encoded.txt > translated.txt
```

Or use standard input:

```bash
python barkwoof_to_english.py < encoded.txt
```

You can also run `python barkwoof_to_english.py` with no filename, paste Barkwoof text, and send end-of-file.

### What the decoder expects

The decoder expects only:

- `bark` or `woof` (case-insensitive)
- `!` to end a non-final letter
- `!!` to end every word
- Whitespace between sounds and markers
- Blank lines between sentence paragraphs

The decoder reconstructs words using `!!`, **not** whitespace. It returns **uppercase** English letters and digits.

If a word does not end in `!!`, or a sequence does not correspond to a supported Morse letter, the decoder reports a specific error instead of guessing. The actual error messages are documented below and verified in the test runs.

## Worked examples

### One short message

**English input**

```text
HI DOG
```

**Barkwoof output**

```text
Woof woof woof woof! Woof woof!! Bark woof woof! Bark bark bark! Bark bark woof!!
```

**Decoded output**

```text
HI DOG
```

### Two sentences

**English input**

```text
Hi dog. Good dog!
```

**Barkwoof output**

```text
Woof woof woof woof! Woof woof!! Bark woof woof! Bark bark bark! Bark bark woof!!

Bark bark woof! Bark bark bark! Bark bark bark! Bark woof woof!! Bark woof woof! Bark bark bark! Bark bark woof!!
```

**Decoded output**

```text
HI DOG

GOOD DOG
```

The blank line represents a sentence break. English punctuation and capitalization are not restored.

### Telegraph-style messages and STOP

For a vintage advertisement, a message such as:

```text
ORDER NOW STOP
```

encodes `STOP` as an ordinary four-letter English **word**. Barkwoof does **not** treat the word `STOP` as punctuation or a special control command. It stays in the decoded text as `STOP`.

This makes the converters suitable for old-fashioned, STOP-filled telegraph messages.

## Importing the converters into Python

Both scripts expose functions you can import into another Python 3 program:

```python
from english_to_barkwoof import to_barkwoof
from barkwoof_to_english import to_english

original = "HI DOG"
encoded = to_barkwoof(original)
decoded = to_english(encoded)

print(encoded)
print(decoded)
```

Importing the modules does not automatically start the terminal interface. The converter functions return strings.

The **CanineWare kindness clause applies each time you use the software**, including use from another Python program.

## What is preserved and what is lost

Because Barkwoof is a code for letters and digits, it does not preserve every aspect of conventional English writing.

| Feature | Behavior |
| --- | --- |
| English A–Z | Fully supported |
| Digits 0–9 | Fully supported |
| Upper/lowercase English | Encoded without case distinction; decoded as uppercase |
| Word boundaries | Preserved with `!!` |
| Sentence boundaries | Preserved as paragraph breaks |
| English `.`, `?`, `!` | All treated as sentence separators during encoding; original marks are not restored |
| Blank lines in English input | Treated as sentence separators |
| Ordinary single line breaks | Do not necessarily end a sentence |
| Commas, colons, semicolons | Not preserved |
| Apostrophes within words | Removed: `DON'T` becomes `DONT` |
| Hyphens | Act as word separators: `WELL-BEING` becomes `WELL BEING` |
| Accented letters, emoji, other symbols | Not encoded as supported letters; may be omitted or split surrounding text |

For example:

```text
Don't stop!
```

decodes back as:

```text
DONT STOP
```

The conversion is **lossy with respect to punctuation, case, typography, and unsupported characters**, but supported A–Z letters, digits, word boundaries, and sentence boundaries can make a round trip.

The scripts are designed for **text files**. They do not read `.docx` files directly; to convert a Word document, first save or export its content as plain `.txt`.

## Errors and troubleshooting

Both scripts catch file-related errors and invalid command-line usage, print an `Error: ...` message to **standard error**, and exit with status `1`. The decoder also checks Barkwoof syntax. These messages are produced by checks in the supplied scripts—not hypothetical errors.

### Missing input file (either script)

**Command:**

```bash
python english_to_barkwoof.py missing.txt
```

**Example error:**

```text
Error: [Errno 2] No such file or directory: 'missing.txt'
```

**Fix:** Check the spelling and current folder, or use the full file path.

### Too many command-line arguments (either script)

**Command:**

```bash
python english_to_barkwoof.py first.txt second.txt
```

**Actual error:**

```text
Error: Usage: python english_to_barkwoof.py [input.txt]
```

The decoder uses the corresponding `barkwoof_to_english.py` filename in its usage message. Supply zero or one input filename. To save output, use `>` instead of adding a second filename as an argument.

### Missing sounds before a marker (decoder only)

**Input:** `!`

**Actual error:**

```text
Error: Missing Bark/Woof sounds before !
```

**Fix:** Every `!` and `!!` must follow a valid sequence of Bark/Woof sounds.

### Invalid Morse sequence (decoder only)

**Input:** `Bark bark bark bark bark bark!`

**Actual error:**

```text
Error: Invalid Morse sequence before !: ------
```

**Fix:** Check that every encoded letter follows a supported International Morse sequence for A–Z or 0–9.

### Letter without a marker (decoder only)

**Input:** `Bark`

**Actual error:**

```text
Error: Incomplete Barkwoof letter: missing ! or !!
```

**Fix:** Add `!` to complete a non-final letter, or `!!` to complete a final letter of a word.

### Word without its final double exclamation mark (decoder only)

**Input:** `Bark!`

**Actual error:**

```text
Error: Incomplete Barkwoof word: every word must end with !!
```

**Fix:** The **last letter of every word**, including the last word in a sentence, must end with `!!`.

### Unexpected Barkwoof token (decoder only)

**Input:** `Meow!!`

**Actual error:**

```text
Error: Unexpected Barkwoof token: 'Meow'
```

**Fix:** Use only `bark`, `woof`, `!`, `!!`, spaces, and paragraph breaks.

### Non-UTF-8 input file (either script)

An input file with invalid UTF-8 bytes produces an error starting with:

```text
Error: 'utf-8' codec can't decode byte
```

The remaining details depend on the specific invalid bytes. **Fix:** Save or export the input as UTF-8 plain text.

### Python is not recognized by your operating system

A terminal message such as `python: command not found` comes from your **shell**, not from a Barkwoof script. Install Python 3 or use `python3` or `py` if your platform provides one.

## Frequently asked questions

**Why does the result appear as one long sentence?**  
The English encoder recognizes `.`, `!`, `?`, or a blank line as sentence boundaries. A single newline is not necessarily a sentence break.

**Why is the output much longer than my input?**  
Each English letter expands into several written sounds and a boundary marker. Barkwoof emphasizes readability, not compactness.

**What if Python says `ModuleNotFoundError` when I import a converter?**  
That is a Python import error, not an error raised by the converters. Keep the scripts in an importable location, such as beside the Python file importing them.

**Does the file have to be named `message.txt`?**  
No. `example.txt`, `dogfood.txt`, `my_secret_message.txt`, or any other valid filename works. Pass the correct filename to the script.

**Are spaces part of the language?**  
No. Spaces only keep individual sound tokens visually separate. They do not mark letters or words.

**Can I leave out the final `!!` because the paragraph ends?**  
No. **Every word**, including the final one, must end with `!!`.

**What does the end of a paragraph mean?**  
The end of a sentence. The scripts represent this with an empty line between consecutive Barkwoof sentences.

**Can I use all lowercase `bark` and `woof`?**  
Yes. The decoder accepts either case; the encoder uses initial capital letters within encoded letters for readability.

**Is this ordinary Morse code?**  
It uses International Morse mappings for A–Z and 0–9, but replaces the dot with `Woof`, the dash with `Bark`, and uses Barkwoof's own written boundary rules.

**Does the script work without internet access?**  
Yes. It uses the standard library and performs all conversion locally.

**Will the decoder restore my original punctuation?**  
No. Barkwoof encodes sentence boundaries, not the difference between a period, question mark, or exclamation point.

**Can I use the scripts for long telegraph advertisements?**  
Yes. Files can contain large quantities of text, though Barkwoof expands the output substantially. The literal word `STOP` is encoded like any other word.

**Does every script run require a kindness for a dog?**  
**Yes. Under CanineWare, one use means one random act of kindness to a dog.** The programs do not electronically monitor compliance. This is a cheerful commitment intended to benefit real dogs.

## License: CanineWare Version 1.0

**Barkwoof is distributed under the CanineWare License, Version 1.0.**

### The Kindness Clause

> **Each time you use a script distributed under the CanineWare License, you must perform one random act of kindness to a dog.**
>
> The act of kindness must be safe, respectful, and genuinely kind to the dog.

Examples of eligible kindness:

- Give a dog fresh water.
- Offer a welcome scratch or gentle attention, if the dog wants it.
- Take a dog for a pleasant walk.
- Enjoy a little playtime with a dog.
- Donate supplies to a shelter or organization helping dogs in need.

Always consider the dog's health, comfort, preferences, and safety. Do not give unsafe treats, approach an unfamiliar dog without permission, or force interaction.

### Permission

You may **use, copy, modify, and share** the software, provided that the CanineWare License notice accompanies the software.

### No warranty

The software is provided **"as is," without warranties of any kind**.

### License status

CanineWare is a **whimsical custom software license**, not a standardized or Open Source Initiative-approved open-source license. The full terms are in `CANINEWARE_LICENSE.txt`.

---

### The Barkwoof promise

**Every translation speaks for dogs. Every use does something kind for one.**

**BARK. WOOF. BE KIND.**
