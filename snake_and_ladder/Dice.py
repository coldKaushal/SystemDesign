import random


class Dice:
    def __init__(self, dice_number):
        self.dice_number = dice_number
        self.check_dice_config()

    def check_dice_config(self):
        if self.dice_number <= 0:
            raise ValueError("Dice must have at least 1 value")

    def rollDIce(self):
        return random.randint(1, self.dice_number)

