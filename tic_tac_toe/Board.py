
class Board:

    def __init__(self, board_size):
        self.check_valid_board_size(board_size)
        self.board_size = board_size
        self.board = [ [0 for _ in range(board_size)] for _ in range(board_size) ]

    def check_valid_board_size(self, board_size):
        if board_size <= 0:
            raise ValueError("Board Size must be greater than 0")
        

    def check_valid_move(self, x, y):
        if x<0 or y<0 or x >= self.board_size or y >= self.board_size:
            print("The cell values must be in the board range")
            return False

        if self.board[x][y]!=0:
            print("Board Value already occupied")
            return False
        
        return True
    
    def fill_board(self, fill_x, fill_y, value):
        x = fill_x - 1
        y = fill_y - 1

        if not self.check_valid_move(x, y):
            return False

        self.board[x][y] = value
        return True
    
    def check_game_completion_for_rows(self):
        for row in self.board:
            if row[0]==0:
                continue
            check = True
            for y in row:
                if y!=row[0]:
                    check = False
                    break
            if check:
                return True
        return False


    def check_game_completion_for_columns(self):
        for i in range(self.board_size):
            col_value = self.board[0][i]
            if col_value==0:
                continue
            check = True
            for j in range(self.board_size):
                if self.board[j][i]!=col_value:
                    check = False
                    break
            if check:
                return True
        
        return False

    def check_game_completion_for_diagonal(self):
        top_left_val = self.board[0][0]
        if top_left_val==0:
            return False
        check = True
        for i in range(self.board_size):
            if self.board[i][i]!=top_left_val:
                check = False
                break
        
        if check:
            return True
        
        top_right_val = self.board[:-1][0]
        if top_right_val==0:
            return False
        
        for i in range(self.board_size):
            if self.board[i][self.board_size-1-i]!=top_right_val:
                return False
        return True
    
    def check_for_game_completion(self):
        if self.check_game_completion_for_columns() or self.check_game_completion_for_rows() or self.check_game_completion_for_diagonal():
            return True
        
        return False
    
    def check_board_filled(self):
        for row in self.board:
            for val in row:
                if val==0:
                    return False
        
        return True
    
    def print_final_board(self):
        print(self.board)