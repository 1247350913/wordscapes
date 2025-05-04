import itertools

# Load dictionary (Linux/Mac). For Windows, use a custom word list
with open("/usr/share/dict/words", "r") as file:
    valid_words = set(word.strip().lower() for word in file if len(word.strip()) >= 3)

def find_words(letters):
    letters = letters.lower()
    found = set()

    for i in range(3, len(letters)+1):
        for combo in itertools.permutations(letters, i):
            word = ''.join(combo)
            if word in valid_words:
                found.add(word)
    return sorted(found)

# Example use
if __name__ == "__main__":
    user_input = input("Enter your letters: ")
    results = find_words(user_input)
    for word in results:
        print(word)
