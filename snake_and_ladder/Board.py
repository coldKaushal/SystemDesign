class Board:
    def __init__(self, board_size):
        self.board_size = board_size
        self.check_board_size()

    def check_board_size(self):
        if self.board_size <= 0:
            raise ValueError("Board Size should be greater than 0")

    def get_first_number(self):
        return 0

    def get_last_number(self):
        return int(self.board_size * self.board_size)