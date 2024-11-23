# tic_tac_toe_game/main.py

from tic_tac_toe_game.game import print_board, check_winner, check_draw, player_move

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize empty board
    current_player = 'X'  # Player X starts first

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
