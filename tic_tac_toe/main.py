from typing import List
from Player import Player

from Board import Board
if __name__ == "__main__":
    print("Starting the game")
    print("Enter number of players")
    num_of_players = int(input())
    list_of_players: List[Player] = []
    for i in range(num_of_players):
        print(f"Enter name and player value for player {i}. Value must be greater than 0")
        name_of_player = input()
        value_of_player = int(input())
        player = Player(name_of_player, value_of_player)
        list_of_players.append(player)

    print("Enter the board size")
    board_size = int(input())
    Board = Board(board_size)
    print("Player 1 to start the game")
    current_player = 0
    while True:
        print(f"Enter the move {list_of_players[current_player].player_name}")
        value = list_of_players[i].player_value
        while True:
            x = int(input())
            y = int(input())
            if Board.fill_board(x, y, value):
                break
            print("Invalid Move, Retry..")
        if Board.check_for_game_completion():
            print(f"{list_of_players[i].player_name} wins the game!")
            Board.print_final_board()
            break
        if Board.check_board_filled():
            print("Draw!")
            Board.print_final_board()
            break
        current_player += 1
        current_player = current_player%num_of_players

