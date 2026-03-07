# Hangman Game
# Guess the hidden word letter by letter before running out of attempts

import random

WORDS = {
    "animals": ["elephant", "giraffe", "penguin", "dolphin", "cheetah", "octopus"],
    "fruits": ["mango", "banana", "strawberry", "pineapple", "blueberry", "watermelon"],
    "countries": ["brazil", "australia", "germany", "japan", "canada", "egypt"],
    "programming": ["python", "variable", "function", "boolean", "string", "dictionary"],
}

HANGMAN_STAGES = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
]


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_hint(word, guessed_letters):
    unrevealed = [letter for letter in word if letter not in guessed_letters]
    if unrevealed:
        return random.choice(unrevealed)
    return None


def play_round():
    print("\nChoose a category:")
    categories = list(WORDS.keys())
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat.capitalize()}")

    while True:
        try:
            cat_choice = int(input("Enter choice: "))
            if 1 <= cat_choice <= len(categories):
                break
            print("Invalid choice!")
        except ValueError:
            print("Enter a number!")

    category = categories[cat_choice - 1]
    word = random.choice(WORDS[category])
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_STAGES) - 1
    hints_left = 1
    score = 100

    print(f"\nCategory: {category.capitalize()}")
    print(f"The word has {len(word)} letters. You get {max_wrong} wrong guesses and {hints_left} hint.\n")

    while wrong_guesses < max_wrong:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        if hints_left > 0:
            print(f"(Type 'hint' to use your hint)")

        guess = input("\nGuess a letter: ").lower().strip()

        if guess == "hint" and hints_left > 0:
            hint_letter = get_hint(word, guessed_letters)
            if hint_letter:
                print(f"Hint: The word contains '{hint_letter}'")
                guessed_letters.add(hint_letter)
                hints_left -= 1
                score -= 20
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Correct! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            score -= 15
            print(f"Wrong! '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"\nCongratulations! You guessed the word: '{word}'")
            score = max(score, 10)
            print(f"Score: {score} points")
            return score

    # Player lost
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"\nGame Over! The word was: '{word}'")
    return 0


def main():
    print("=" * 40)
    print("       HANGMAN GAME")
    print("=" * 40)

    total_score = 0
    rounds = 0

    while True:
        score = play_round()
        total_score += score
        rounds += 1

        print(f"\n--- Total Score: {total_score} ({rounds} round{'s' if rounds != 1 else ''}) ---")

        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again != "y":
            print(f"\nFinal Score: {total_score} in {rounds} round{'s' if rounds != 1 else ''}.")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
