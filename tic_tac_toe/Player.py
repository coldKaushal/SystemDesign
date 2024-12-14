
class Player:
    def __init__(self, player_name, player_value):
        self.check_valid_player_value(player_value)
        self.player_name = player_name
        self.player_value = player_value
    
    def check_valid_player_value(self, player_value):
        if player_value <= 0:
            raise ValueError("Player value must be greater than 0")
    