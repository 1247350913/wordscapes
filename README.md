# Wordscapes Solver

A lightweight command-line Python tool that helps solve **Wordscapes** puzzles by generating valid words from the puzzle letters and any known letter positions.

Designed to be fast, simple, cross-platform, and dependency-free.

---

## Features

* Find words of a specific length
* Support known letter positions
* Use `_` as a placeholder for unknown letters
* Works on Windows, macOS, and Linux
* Automatically loads the best available dictionary source
* Downloads and caches a fallback dictionary when needed
* No external Python packages required
* Repeat search mode built in
* Quick exit available at any prompt
* Minimal single-file project

---

## How It Works

The script:

1. Loads a dictionary from the best available source:

   * Local Unix dictionary (`/usr/share/dict/words`)
   * Local cached dictionary (`words_cache.txt`)
   * Online fallback dictionary (downloaded once)
2. Filters words by:

   * Required word length
   * Available puzzle letters
   * Known letter positions
3. Displays all matching results in alphabetical order
4. Lets you run another search without restarting

---

## Requirements

* Python 3.6+
* Terminal / Command Prompt / PowerShell

No additional libraries or setup required.

---

## Installation

### Clone the Repository

```bash
git clone <repo-url>
cd wordscapes
```

Or download the ZIP file and extract it.

---

## Project Structure

```text
wordscapes/
├── find_words.py
├── README.md
└── words_cache.txt   (created automatically if needed)
```

---

## Running the Solver

### Windows (PowerShell)

```powershell
python .\\find_words.py
```

or

```powershell
py .\\find_words.py
```

### macOS / Linux

```bash
python3 find_words.py
```

If your system uses `python`:

```bash
python find_words.py
```

---

## Usage

When prompted, enter:

### 1. Puzzle Letters

All letters currently available in the puzzle.

Example:

```text
apple
```

### 2. Desired Word Length

The number of letters in the answer.

Example:

```text
5
```

### 3. Known Letters Pattern

Use known letters in their exact positions. Use `_` for unknown letters.

Example:

```text
a__le
```

Meaning:

* First letter is `a`
* Fourth letter is `l`
* Fifth letter is `e`

---

## Example Session

```text
=== Wordscapes Solver ===

Enter puzzle letters: apple
Enter desired word length: 5
Enter known letters pattern (use _ for unknowns): a__le

Results (1):
apple

Enter another word? (y/n):
```

---

## Matching Rules

A word must satisfy all of the following:

* Correct length
* Uses only the provided puzzle letters
* Matches all known fixed letters
* Uses repeated letters only when enough copies exist
* Contains alphabetic characters only

---

## Dictionary Sources

The program checks sources in this order:

1. System dictionary
   `/usr/share/dict/words`

2. Cached local dictionary
   `words_cache.txt`

3. Online fallback dictionary
   Automatically downloaded and saved for future runs

This makes the tool portable while avoiding repeated downloads.

---

## Exit Options

You can exit the program at any prompt by entering:

```text
q
```

You can also use:

* `Ctrl + C`
* `Ctrl + D` (EOF on supported systems)

---

## Troubleshooting

### Pattern Length Error

If you see:

```text
Error: Pattern length must match word length.
```

Your pattern must contain exactly the same number of characters as the selected word length.

Example:

* Length = `5`
* Pattern = `a__le`

### Invalid Letters

If you see:

```text
Error: Puzzle letters must contain letters only.
```

Remove spaces, numbers, or symbols.

### No Results Found

Possible reasons:

* Incorrect known letter positions
* Missing letters
* Chosen length incorrect
* No matching word exists in the loaded dictionary

### Python Not Found

Check installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Technical Notes

* Words are converted to lowercase
* Non-alphabetic entries are ignored
* Results are sorted alphabetically
* Dictionary downloads are cached locally
* Special characters in input are safely escaped

---

## Why This Project Exists

A fast, no-frills helper for when you are stuck in Wordscapes and want immediate answers without ads, websites, accounts, or unnecessary complexity.

---

## License

Use freely for personal and educ
