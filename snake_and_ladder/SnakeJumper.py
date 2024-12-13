from Board import Board


class SnakeJumper:
    def __init__(self, snake_start, snake_end, board_last_number):
        self.snake_end = snake_end
        self.last_number = board_last_number
        self.validate_snake_jumper()

    def validate_snake_jumper(self):
        if self.snake_start <= 0 or self.snake_end <= 0:
            raise ValueError("Snake's start and end point should be greater than 0")

        if self.snake_start > self.last_number or self.snake_end > self.snake_end:
            raise ValueError(f"Snake's start and end point should be less than the last number of board which is {self.last_number}")

        if self.snake_start < self.snake_end:
            raise ValueError("Snake's start point should be greater or equal to snake's end point")