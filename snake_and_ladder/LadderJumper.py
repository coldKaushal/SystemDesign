from Board import Board


class LadderJumper:
    def __init__(self, ladder_start, ladder_end, board_last_number):
        self.ladder_start = ladder_start
        self.ladder_end = ladder_end
        self.last_number = board_last_number
        self.validate_ladder_jumper()

    def validate_ladder_jumper(self):
        if self.ladder_start <= 0 or self.ladder_end <= 0:
            raise ValueError("Ladder start and end point should be greater than 0")

        if self.ladder_start > self.last_number or self.ladder_end > self.last_number:
            raise ValueError(
                f"Ladder's start and end point should be less than the last number i.e. {self.last_number}")

        if self.ladder_start > self.ladder_end:
            raise ValueError("Ladder's start point should be less or equal to ladder's end point")

