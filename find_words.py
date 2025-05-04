import re

# Load a word list (ensure it's in the same folder or provide full path)
with open("/usr/share/dict/words", "r") as file:
    WORDS = set(word.strip().lower() for word in file if word.strip().isalpha())

def matches(word, known_pattern, available_letters):
    if len(word) != len(known_pattern):
        return False
    used = list(available_letters)
    for i, char in enumerate(known_pattern):
        if char == '_':
            if word[i] not in used:
                return False
            used.remove(word[i])
        else:
            if word[i] != char:
                return False
    return True

def main():
    print("=== Wordscapes Solver ===")
    word_length = int(input("Enter desired word length: ").strip())
    known = input("Enter known letters pattern (use _ for unknowns): ").strip().lower()
    letters = input("Enter available letters: ").strip().lower()

    if len(known) != word_length:
        print("Error: Pattern length must match word length.")
        return

    pattern = re.compile(f"^[{letters}]{{{word_length}}}$")

    results = sorted([
        word for word in WORDS
        if pattern.match(word)
        and matches(word, known, letters)
    ])

    print(f"\nResults ({len(results)}):")
    for word in results:
        print(word)

if __name__ == "__main__":
    main()
