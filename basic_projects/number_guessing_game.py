# Number Guessing Game

import random

def play():
    print("=" * 35)
    print("   NUMBER GUESSING GAME")
    print("=" * 35)

    print("\nChoose difficulty:")
    print("1. Easy   (1-50,   10 attempts)")
    print("2. Medium (1-100,  7 attempts)")
    print("3. Hard   (1-500,  10 attempts)")

    while True:
        try:
            choice = int(input("\nEnter choice (1/2/3): "))
            if choice in (1, 2, 3):
                break
        except ValueError:
            pass
        print("Please enter 1, 2, or 3.")

    if choice == 1:
        max_num, max_attempts = 50, 10
    elif choice == 2:
        max_num, max_attempts = 100, 7
    else:
        max_num, max_attempts = 500, 10

    secret = random.randint(1, max_num)
    attempts = 0
    score = 100

    print(f"\nI'm thinking of a number between 1 and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == secret:
            print(f"\nYou guessed it in {attempts} attempt(s)!")
            print(f"Score: {max(score, 10)} points")
            break
        elif guess < secret:
            print("Too low! Go higher.")
        else:
            print("Too high! Go lower.")

        score -= (100 // max_attempts)
    else:
        print(f"\nOut of attempts! The number was {secret}.")
        print("Score: 0 points")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == "y":
        play()

if __name__ == "__main__":
    play()
