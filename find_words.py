import re
import sys
import urllib.request
from pathlib import Path

CACHE_FILE = Path(__file__).with_name("words_cache.txt")

DICTIONARY_URLS = [
    "https://gist.githubusercontent.com/gonzalezjo/24c64dc8d6ec8dba316b72cceef55811/raw",
    "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt",
]

LOCAL_DICTIONARY_PATHS = [
    Path("/usr/share/dict/words"),
    Path("/usr/dict/words"),
]

EXIT_WORDS = {"q"}

def normalize_words(lines):
    return {
        word.strip().lower()
        for word in lines
        if word.strip().isalpha()
    }

def load_words_from_file(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        return normalize_words(file)

def download_words(url):
    with urllib.request.urlopen(url, timeout=20) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        text = response.read().decode(charset, errors="ignore")
    return normalize_words(text.splitlines())

def load_words():
    for path in LOCAL_DICTIONARY_PATHS:
        if path.exists():
            words = load_words_from_file(path)
            if words:
                print(f"\nLoaded dictionary from system path: {path}")
                return words

    if CACHE_FILE.exists():
        words = load_words_from_file(CACHE_FILE)
        if words:
            print(f"\nLoaded dictionary from cache: {CACHE_FILE}")
            return words

    for url in DICTIONARY_URLS:
        try:
            print(f"\nDownloading dictionary from: {url}")
            words = download_words(url)
            if words:
                CACHE_FILE.write_text("\n".join(sorted(words)), encoding="utf-8")
                print(f"Saved dictionary cache to: {CACHE_FILE}")
                return words
        except Exception as exc:
            print(f"Warning: Failed to download from {url}: {exc}")

    raise RuntimeError("Could not load any dictionary.")

WORDS = load_words()

def prompt_text(message):
    try:
        value = input(message).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        sys.exit(0)

    if value.lower() in EXIT_WORDS:
        print()
        sys.exit(0)

    return value

def matches(word, known_pattern, available_letters):
    if len(word) != len(known_pattern):
        return False

    used = list(available_letters)

    for i, char in enumerate(known_pattern):
        if char == "_":
            if word[i] not in used:
                return False
            used.remove(word[i])
        else:
            if word[i] != char:
                return False

    return True

def prompt_int(message):
    while True:
        value = prompt_text(message)

        try:
            number = int(value)
            if number <= 0:
                print("Error: Please enter a number greater than 0.")
                continue
            return number
        except ValueError:
            print("Error: Please enter a valid integer.")

def prompt_yes_no(message):
    while True:
        value = prompt_text(message).lower()

        if value in ("y", "yes"):
            return True

        if value in ("n", "no"):
            return False

        print("Please enter y or n.")

def run_solver():
    letters = prompt_text("Enter puzzle letters: ").lower()
    word_length = prompt_int("Enter desired word length: ")
    known = prompt_text("Enter known letters pattern (use _ for unknowns): ").lower()

    if not letters.isalpha():
        print("Error: Puzzle letters must contain letters only.")
        return

    if len(known) != word_length:
        print("Error: Pattern length must match word length.")
        return

    if not all(c.isalpha() or c == "_" for c in known):
        print("Error: Pattern may contain only letters and underscores.")
        return

    pattern = re.compile(f"^[{re.escape(letters)}]{{{word_length}}}$")

    results = sorted(
        word for word in WORDS
        if pattern.match(word) and matches(word, known, letters)
    )

    print(f"\nResults ({len(results)}):")
    for word in results:
        print(word)

def main():
    print("\n=== Wordscapes Solver ===\n")

    while True:
        run_solver()

        again = prompt_yes_no("\nEnter another word? (y/n): ")
        if not again:
            print()
            break

if __name__ == "__main__":
    main()
