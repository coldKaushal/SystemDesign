from Player import Player
from Board import Board
from SnakeJumper import SnakeJumper
from LadderJumper import LadderJumper
from typing import List
from Dice import Dice


class GameBoard:
    def __init__(self, players: List[Player], board: Board, snakes: List[SnakeJumper], ladders: List[LadderJumper], dice: Dice):

        self.players = players
        self.board = board
        self.snakes = snakes
        self.ladders = ladders
        self.dice = dice
        self.map_for_snakes = self.create_map_for_snakes()
        self.map_for_ladder = self.create_map_for_ladders()

    def create_map_for_snakes(self):
        map_for_snakes = {}
        for snake in self.snakes:
            map_for_snakes[snake.snake_start] = snake.snake_end

        return map_for_snakes

    def create_map_for_ladders(self):
        map_for_ladder = {}
        for ladder in self.ladders:
            map_for_ladder[ladder.ladder_start] = ladder.ladder_end

        return map_for_ladder

    def play_game(self):
        while self.players:
            current_player = self.players.pop(0)
            print(f"Current Player {current_player.player_name} at position {current_player.player_position}")
            current_dice_roll = self.dice.rollDIce()

            new_move = current_player.player_position + current_dice_roll
            while new_move > self.board.get_last_number():
                current_dice_roll = self.dice.rollDIce()
                new_move = current_player.player_position + current_dice_roll
            print(f"New move is {new_move}")
            if new_move == self.board.get_last_number():
                print(f"Player {current_player.player_name} wins")
                continue

            if new_move in self.snakes:
                current_player.update_player_position(self.snakes[new_move])
                print(f"Player {current_player.player_name} was eaten by snake to {current_player.player_position} position")
                self.players.append(current_player)
                continue

            if new_move in self.ladders:
                current_player.update_player_position(self.ladders[new_move])
                print(f"Player {current_player.player_name} was climbed on a ladder to {current_player.player_position} position")
                self.players.append(current_player)
                continue
            current_player.update_player_position(new_move)
            self.players.append(current_player)

        print("Game Over")



