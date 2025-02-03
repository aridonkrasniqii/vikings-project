from tv_series.base.managers import BaseManager

class NflPlayerManager(BaseManager):
    def get_all_nfl_players(self):
        return self.get_all()

    def get_nfl_player_by_id(self, player_id):
        return self.get_by_id(player_id)

    def create_nfl_player(self, nfl_player):
        return self.create_model(nfl_player)

    def update_nfl_player(self, nfl_player):
        return self.update_model(nfl_player)

    def delete_nfl_player(self, nfl_player):
        return self.delete_model(nfl_player)

class NflPlayerStatsManager(BaseManager):
    def get_stats_by_player(self, player_id):
        return self.filter(nflplayer_id=player_id)

    def create_stats(self, stats):
        return self.create_model(stats)

    def update_stats(self, stats):
        return self.update_model(stats)

    def delete_stats(self, stats):
        return self.delete_model(stats)
