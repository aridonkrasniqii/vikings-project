from abc import ABC

from tv_series.base.managers import BaseManager

class NflPlayerManager(BaseManager):
    def get_all(self):
        return self.get_all_models()

    def get_by_id(self, player_id):
        return self.get_model_by_id(player_id)

    def create(self, nfl_player):
        return self.create_model(**nfl_player)

    def update(self, nfl_player):
        return self.update_model(nfl_player)

    def delete(self, nfl_player):
        return self.delete_model(nfl_player)

class NflPlayerStatsManager(BaseManager, ABC):
    def get_stats_by_player(self, player_id):
        return self.filter(player_id=player_id)

    def create(self, stats):
        return self.create_model(stats)

    def update(self, stats):
        return self.update_model(stats)

    def delete(self, stats):
        return self.delete_model(stats)
