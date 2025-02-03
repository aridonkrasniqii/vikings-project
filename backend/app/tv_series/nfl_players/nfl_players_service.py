from rest_framework import status

from tv_series.base.models.custom_response import CustomResponse
from .nfl_players_model import NFLPlayer, NflPlayerStats

class NFLPlayerService:
    def __init__(self):
        pass

    def get_all(self):
        nfl_players = NFLPlayer.objects.all()
        return CustomResponse(nfl_players, status.HTTP_200_OK)

    def get_by_id(self, nfl_player_id):
        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if nfl_player:
            return CustomResponse(nfl_player, status.HTTP_200_OK)
        return CustomResponse(None, status.HTTP_404_NOT_FOUND, "NFL player not found")

    def create(self, data):
        name = data.get('name')
        photo = data.get('photo')
        position = data.get('position')
        stats = data.get('stats')

        if not all([name, photo, position]):
            return CustomResponse(None, status.HTTP_400_BAD_REQUEST, "Bad request. Missing fields.")

        new_nfl_player = NFLPlayer.objects.create_nfl_player(name, photo, position, stats)
        return CustomResponse(new_nfl_player, status.HTTP_201_CREATED)

    def update(self, nfl_player_id, data):
        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if not nfl_player:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "NFL player not found")

        name = data.get('name', nfl_player.name)
        photo = data.get('photo', nfl_player.photo)
        position = data.get('position', nfl_player.position)
        stats = data.get('stats', nfl_player.stats)

        updated_nfl_player = NFLPlayer.objects.update_nfl_player(nfl_player, name, photo, position, stats)
        return CustomResponse(updated_nfl_player, status.HTTP_200_OK)

    def delete(self, nfl_player_id):
        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if not nfl_player:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "NFL player not found")

        NFLPlayer.objects.delete_nfl_player(nfl_player)
        return CustomResponse(None, status.HTTP_204_NO_CONTENT)

class NflPlayerStatsService:
    def __init__(self):
        pass

    def create(self, data):
        touchdowns = data.get('touchdowns', 0)
        yards = data.get('yards', 0)
        interceptions = data.get('interceptions', 0)
        sacks = data.get('sacks', 0)
        fumbles = data.get('fumbles', 0)

        new_stats = NflPlayerStats.objects.create_stats(touchdowns, yards, interceptions, sacks, fumbles)
        return CustomResponse(new_stats, status.HTTP_201_CREATED)

    def update(self, stats_id, data):
        stats = NflPlayerStats.objects.get(id=stats_id)
        if not stats:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Stats not found")

        updated_stats = NflPlayerStats.objects.update_stats(stats, **data)
        return CustomResponse(updated_stats, status.HTTP_200_OK)

    def delete(self, stats_id):
        stats = NflPlayerStats.objects.get(id=stats_id)
        if not stats:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Stats not found")

        NflPlayerStats.objects.delete_stats(stats)
        return CustomResponse(None, status.HTTP_204_NO_CONTENT)
