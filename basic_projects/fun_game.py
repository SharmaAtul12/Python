import random

def number_guessing_game():
    print("=" * 40)
    print("   🎯 NUMBER GUESSING GAME 🎯")
    print("=" * 40)

    high_score = float("inf")

    while True:
        secret = random.randint(1, 100)
        attempts = 0
        print("\nI'm thinking of a number between 1 and 100.")
        print("Can you guess it?\n")

        while True:
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Please enter a valid number!")
                continue

            attempts += 1

            if guess < secret:
                print("📈 Too low! Try higher.")
            elif guess > secret:
                print("📉 Too high! Try lower.")
            else:
                print(f"\n🎉 Correct! You guessed it in {attempts} attempt(s)!")
                if attempts < high_score:
                    high_score = attempts
                    print(f"🏆 New high score: {high_score} attempt(s)!")
                else:
                    print(f"⭐ High score: {high_score} attempt(s)")
                break

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != "y":
            print("\nThanks for playing! Goodbye! 👋")
            break


if __name__ == "__main__":
    number_guessing_game()
