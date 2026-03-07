# Tic Tac Toe Game

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in wins)

def is_draw():
    return " " not in board

def play():
    print("=" * 30)
    print("   TIC TAC TOE GAME")
    print("=" * 30)
    print("Positions are numbered 1-9:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

    current_player = "X"

    while True:
        print_board()
        try:
            move = int(input(f"\nPlayer {current_player}, enter position (1-9): ")) - 1
        except ValueError:
            print("Invalid input! Enter a number between 1 and 9.")
            continue

        if move < 0 or move > 8:
            print("Position must be between 1 and 9!")
            continue

        if board[move] != " ":
            print("That position is already taken!")
            continue

        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"\nPlayer {current_player} wins! Congratulations!")
            break

        if is_draw():
            print_board()
            print("\nIt's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play()
    