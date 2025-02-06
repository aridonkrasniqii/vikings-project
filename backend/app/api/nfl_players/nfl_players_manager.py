from abc import ABC

from api.base.managers import BaseManager

class NflPlayerManager(BaseManager):

    def get_paginated_nfl_players(self, request, view):
        return self.get_paginated_models(request, view)

    def get_nfl_player_by_id(self, player_id):
        return self.get_model_by_id(player_id)

    def create_nfl_player(self, data):
        return self.create_model(**data)

    def update_nfl_player(self, nfl_player_id, data):
        return self.update_model(nfl_player_id, data)

    def delete_nfl_player(self, nfl_player):
        return self.delete_model(nfl_player)

class NflPlayerStatsManager(BaseManager, ABC):
    def get_stats_by_player(self, player_id):
        return self.filter(player_id=player_id)

    def create_nfl_player_stats(self, player, stats):
        return self.create_model(player=player, **stats)

    def update_nfl_player_stats(self, stats_id, stats_data):
        return self.update_model(stats_id, stats_data)

    def delete_nfl_player_stats(self, stats):
        return self.delete_model(stats)
