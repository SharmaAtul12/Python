# Rock Paper Scissors - Best of N Rounds
# Play against the computer with score tracking and statistics

import random

CHOICES = ["rock", "paper", "scissors"]

ASCII_ART = {
    "rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """,
}

stats = {"wins": 0, "losses": 0, "draws": 0, "rounds": 0}
move_history = {"rock": 0, "paper": 0, "scissors": 0}


def determine_winner(player, computer):
    if player == computer:
        return "draw"
    winning_moves = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if winning_moves[player] == computer:
        return "win"
    return "lose"


def get_computer_choice():
    return random.choice(CHOICES)


def display_choices(player, computer):
    print("\nYou chose:")
    print(ASCII_ART[player])
    print("Computer chose:")
    print(ASCII_ART[computer])


def play_round():
    print("\nChoose your move:")
    print("  1. Rock")
    print("  2. Paper")
    print("  3. Scissors")

    while True:
        choice = input("Enter 1/2/3: ").strip()
        if choice in ("1", "2", "3"):
            player = CHOICES[int(choice) - 1]
            break
        print("Invalid input! Enter 1, 2, or 3.")

    computer = get_computer_choice()
    display_choices(player, computer)

    result = determine_winner(player, computer)
    stats["rounds"] += 1
    move_history[player] += 1

    if result == "win":
        stats["wins"] += 1
        print("You WIN this round!")
    elif result == "lose":
        stats["losses"] += 1
        print("You LOSE this round!")
    else:
        stats["draws"] += 1
        print("It's a DRAW!")

    return result


def play_best_of_n():
    try:
        n = int(input("\nBest of how many rounds? (odd number): "))
        if n <= 0 or n % 2 == 0:
            print("Please enter a positive odd number!")
            return
    except ValueError:
        print("Invalid number!")
        return

    wins_needed = (n // 2) + 1
    player_wins = 0
    computer_wins = 0
    round_num = 0

    print(f"\n--- Best of {n} ---")
    print(f"First to {wins_needed} wins!\n")

    while player_wins < wins_needed and computer_wins < wins_needed:
        round_num += 1
        print(f"=== Round {round_num} ===")
        print(f"Score: You {player_wins} - {computer_wins} Computer")

        result = play_round()
        if result == "win":
            player_wins += 1
        elif result == "lose":
            computer_wins += 1

    print("\n" + "=" * 40)
    if player_wins > computer_wins:
        print(f"  YOU WIN the series {player_wins}-{computer_wins}!")
    else:
        print(f"  COMPUTER WINS the series {computer_wins}-{player_wins}!")
    print("=" * 40)


def show_stats():
    total = stats["rounds"]
    if total == 0:
        print("\nNo games played yet!")
        return

    win_rate = (stats["wins"] / total) * 100

    print("\n" + "=" * 35)
    print("       YOUR STATISTICS")
    print("=" * 35)
    print(f"  Total Rounds:  {total}")
    print(f"  Wins:          {stats['wins']}")
    print(f"  Losses:        {stats['losses']}")
    print(f"  Draws:         {stats['draws']}")
    print(f"  Win Rate:      {win_rate:.1f}%")

    print("\n  Move Usage:")
    for move in CHOICES:
        count = move_history[move]
        pct = (count / total) * 100 if total > 0 else 0
        bar = "█" * int(pct // 5)
        print(f"    {move.capitalize():<10} {count:>3} ({pct:.0f}%) {bar}")


def main():
    print("=" * 40)
    print("    ROCK  PAPER  SCISSORS")
    print("=" * 40)

    while True:
        print("\n1. Quick Play (single round)")
        print("2. Best of N")
        print("3. View Stats")
        print("4. Reset Stats")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            play_round()
        elif choice == "2":
            play_best_of_n()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            for key in stats:
                stats[key] = 0
            for key in move_history:
                move_history[key] = 0
            print("Stats reset!")
        elif choice == "5":
            show_stats()
            print("\nThanks for playing!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
