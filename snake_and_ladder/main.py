from Player import Player
from Board import Board
from Dice import Dice
from SnakeJumper import SnakeJumper
from LadderJumper import LadderJumper
from GameBoard import GameBoard

if __name__ == '__main__':
    print("Initialising 2 players for demo")
    list_of_players = []
    for i in range(1, 3):
        print(f"Enter the name of the player {i}")
        player_name = input()
        player = Player(player_name, i)
        list_of_players.append(player)

    print("Initialising the board size")
    print("Enter the board size")
    board_size = int(input())
    board = Board(board_size)

    print(f"Board initialised, the game will start at 1 till {board_size*board_size}")

    print("initialising the Dice")
    print("Enter the max dice number. The number must be greater than 0")

    dice_number = int(input())
    dice = Dice(dice_number)

    print(f"Initialising snakes, for demo adding 3 snakes")
    snakes = []
    for _ in range(3):
        print("Enter the snake start and end point, start point must be greater or equal to end point")
        snake_start = int(input())
        snake_end = int(input())
        snake_jumper = SnakeJumper(snake_start, snake_end, board_size)
        snakes.append(snake_jumper)

    print(f"Initialising ladder, for demo adding 3 ladders")
    ladders = []
    for _ in range(3):
        print("Enter the ladder start and end point, start point must be less than end point")
        ladder_start = int(input())
        ladder_end = int(input())
        ladder_jumper = LadderJumper(ladder_start, ladder_end, board_size)

    print("Initialised snakes and ladders")
    print("Game starts")
    gameBoard = GameBoard(list_of_players, board, snakes, ladders, dice)
    gameBoard.play_game()
