# tic_tac_toe_game/game.py

def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, symbol):
    """Check if the current player has won."""
    for i in range(3):
        if all([cell == symbol for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == symbol for j in range(3)]):  # Check column
            return True

    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False

def check_draw(board):
    """Check if the game is a draw."""
    return all([cell != ' ' for row in board for cell in row])

def player_move(board, symbol):
    """Allow a player to make a move."""
    while True:
        try:
            move = int(input(f"Player {symbol}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                board[row][col] = symbol
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")
