# Tic Tac Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print("-" * 5)


# Function to check for a win
def check_win(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return any(condition == [mark, mark, mark] for condition in win_conditions)


# Function to check for a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)


# Function to get player input
def get_player_input(player, board):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1, 2, 3): ")) - 1
            col = int(input(f"Player {player}, enter the column (1, 2, 3): ")) - 1
            if row in range(3) and col in range(3):
                if board[row][col] == " ":
                    return row, col
                else:
                    print("This position is already taken. Try again.")
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers between 1 and 3.")


# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row, col = get_player_input(current_player, board)

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()