from rest_framework import status

from tv_series.custom_response import CustomResponse
from .models import Viking, NFLPlayer, Norseman, NflPlayerStats


class VikingService:
    def __init__(self):
        pass

    def get_all(self):
        vikings = Viking.objects.all()
        return CustomResponse(vikings, status.HTTP_200_OK)

    def get_by_id(self, viking_id):
        viking = Viking.objects.get_viking_by_id(viking_id)
        if viking:
            return CustomResponse(viking, status.HTTP_200_OK)
        return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

    def create(self, data):
        name = data.get('name')
        description = data.get('description')
        photo = data.get('photo')
        actor_name = data.get('actor_name')

        if not all([name, description, photo, actor_name]):
            return CustomResponse(None, status.HTTP_400_BAD_REQUEST, "Bad request, Missing fields")

        created_viking = Viking.objects.create_viking(name, description, photo, actor_name)
        return CustomResponse(created_viking, status.HTTP_201_CREATED)

    def update(self, viking_id, data):
        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

        name = data.get('name', viking.name)
        description = data.get('description', viking.description)
        photo = data.get('photo', viking.photo)
        actor_name = data.get('actor_name', viking.actor_name)

        updated_viking = Viking.objects.update_viking(viking, name, description, photo, actor_name)
        return CustomResponse(updated_viking, status.HTTP_200_OK)

    def delete(self, viking_id):
        viking = Viking.objects.get_viking_by_id(viking_id)
        if not viking:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Viking not found")

        Viking.objects.delete_viking(viking)
        return CustomResponse(None, status.HTTP_204_NO_CONTENT)

class NorsemanService:
    def __init__(self):
        pass

    def get_all(self):
        norseman = Norseman.objects.all()
        return CustomResponse(norseman, status.HTTP_200_OK)

    def get_by_id(self, norseman_id):
        norseman = Norseman.objects.get_norseman_by_id(norseman_id)
        if norseman:
            return CustomResponse(norseman, status.HTTP_200_OK)
        return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Norseman not found")

    def create(self, data):
        name = data.get('name')
        description = data.get('description')
        photo = data.get('photo')
        actor_name = data.get('actor_name')

        if not all([name, description, photo, actor_name]):
            return CustomResponse(None, status.HTTP_400_BAD_REQUEST, "Bad request. Missing fields.")

        new_norseman = Norseman.objects.create_norseman(name, description, photo, actor_name)
        return CustomResponse(new_norseman, status.HTTP_201_CREATED)

    def update(self, norseman_id, data):
        norseman = Norseman.objects.get_norseman_by_id(norseman_id)
        if not norseman:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Norseman not found")

        name = data.get('name', norseman.name)
        description = data.get('description', norseman.description)
        photo = data.get('photo', norseman.photo)
        actor_name = data.get('actor_name', norseman.actor_name)

        updated_norseman = Norseman.objects.update_norseman(norseman, name, description, photo, actor_name)
        return CustomResponse(updated_norseman, status.HTTP_200_OK)

    def delete(self, norseman_id):
        norseman = Norseman.objects.get_norseman_by_id(norseman_id)
        if not norseman:
            return CustomResponse(None, status.HTTP_404_NOT_FOUND, "Norseman not found")

        Norseman.objects.delete_norseman(norseman)
        return CustomResponse(None, status.HTTP_204_NO_CONTENT)


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
