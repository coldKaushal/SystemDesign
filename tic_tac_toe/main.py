from Player import Player
from Board import Board
if __name__ == "__main__":
    print("Starting the game")
    print("Enter the name of player 1")
    player_name = input()
    print("Picked value for player 1 is X")
    player1 = Player(player_name, 1)
    print("Enter the name of player 2")
    player_name = input()
    print("Picked value for player 2 in O")
    player2 = Player(player_name, -1)

    print("Enter the board size")
    board_size = int(input())
    Board = Board(board_size)
    print("Player 1 to start the game")
    move = 1
    while True:
        print(f"Player {1 if move==1 else 2} to enter the move. Move must be between 1 and {Board.board_size}")
        value = player1.player_value if move==1 else player2.player_value
        while True:
            x = int(input())
            y = int(input())
            if Board.fill_board(x, y, value):
                break
            print("Invalid Move, Retry..")
        if Board.check_for_game_completion():
            print(f"Player {player1.player_name if move==1 else player2.player_name} wins the game")
            Board.print_final_board()
            break
        if Board.check_board_filled():
            print("Draw!")
            Board.print_final_board()
            break
        move = -1 * move

