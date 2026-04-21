# Wordscapes Solver

A simple command-line Python tool that helps solve **Wordscapes** puzzles by generating valid words from the available letters, and any known letter positions.

Designed to be lightweight, fast, and dependency-free.

---

## Features

* Finds words of a specific length
* Supports known letter positions
* Use `_` as a wildcard placeholder for unknown letters
* Uses a built-in system English dictionary
* No external Python packages required
* Minimal single-file project

---

## How It Works

The script:

1. Loads a system dictionary of English words
2. Filters words by:
   * Required word length
   * Available letters
   * Known letter positions
3. Displays all matching results in alphabetical order

---

## Requirements

* Python 3.6+
* macOS or Linux recommended
* Terminal / Command Prompt access

### Dictionary File Required

This project uses the standard Unix dictionary file:

```text
/usr/share/dict/words
```

This file is commonly available on:

* macOS
* Linux
* WSL (Windows Subsystem for Linux)

---

## Windows Users

Windows usually does **not** include `/usr/share/dict/words`.

### Option 1 — Use WSL (Recommended)

Install Windows Subsystem for Linux and run the script there.

### Option 2 — Use Your Own Word List

Replace:

```python
with open("/usr/share/dict/words", "r") as file:
```

with a local dictionary file path such as:

```python
with open("words.txt", "r") as file:
```

Then place a word list file in the project folder.

---

## Installation

### Clone the Repository

```bash
git clone <repo-url>
cd wordscapes
```

Or download the ZIP and extract it.

---

## Project Structure

```text
wordscapes/
├── find_words.py
└── README.md
```

---

## Running the Solver

From the project folder:

```bash
python3 find_words.py
```

If your system uses `python` instead:

```bash
python find_words.py
```

---

## Usage

When prompted, enter:

### 1. Desired Word Length

The number of letters in the answer.

Example:

```text
5
```

### 2. Known Letters Pattern

Use known letters in their exact positions. Use `_` for unknown letters.

Example:

```text
a__le
```

Meaning:

* First letter is `a`
* Fourth letter is `l`
* Fifth letter is `e`

### 3. Available Letters

Enter the letters you currently have available.

Example:

```text
apple
```

---

## Example Session

```text
=== Wordscapes Solver ===
Enter desired word length: 5
Enter known letters pattern (use _ for unknowns): a__le
Enter available letters: apple

Results (1):
apple
```

---

## Matching Rules

A word must satisfy all of the following:

* Correct length
* Uses only available letters
* Matches all known fixed letters
* Uses available letters only as many times as provided

---

## Troubleshooting

### Pattern Length Error

If you see:

```text
Error: Pattern length must match word length.
```

Your pattern must contain exactly the same number of characters as the chosen word length.

Example:

* Length = `5`
* Pattern = `a__le`

Valid.

### Python Not Found

Check installation:

```bash
python3 --version
```

### No Results Found

Possible reasons:

* Incorrect known letter positions
* Missing available letters
* Word not present in dictionary
* Chosen length incorrect

---

## Technical Notes

* Words are converted to lowercase
* Non-alphabetic dictionary entries are ignored
* Results are automatically sorted alphabetically

---

## Why This Project Exists

A fast, no-frills helper for when you are stuck in Wordscapes and want immediate answers without ads, websites, or unnecessary complexity.

---

## License

Use freely for personal and educational purposes.
