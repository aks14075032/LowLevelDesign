class PlayerManager:
    def __init__(self):
        # Can store player moves which will help in undo
        self.player_moves = {}
        self.players_list = {}

    def add_player(self, player, player_id):
        self.players_list[player_id] = player

    def get_player(self, player_id):
        return self.players_list[player_id]

    def get_all_players(self):
        return self.players_list.values()

