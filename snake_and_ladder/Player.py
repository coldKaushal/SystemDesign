class Player:

    def __init__(self, player_name, player_id):
        self.player_name = player_name
        self.player_id = player_id
        self.player_position = 1

    def update_player_position(self, new_player_position):
        self.player_position = new_player_position
