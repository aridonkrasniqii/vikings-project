from django.db import transaction

from tv_series.base.validators import BaseValidator

from rest_framework import status
from tv_series.base.models.entity_response import EntityResponse
from tv_series.base.services import BaseService
from .nfl_players_model import NFLPlayer, NflPlayerStats
from .nfl_players_validator import NFLPlayerValidator, NflPlayerStatsValidator
from ..base.serializers import NFLPlayerSerializer, PaginatedNFLPlayerSerializer


class NFLPlayerService(BaseService):

    NFL_PLAYER_CREATED = 'NFL player created'
    NFL_PLAYER_UPDATED = 'NFL player updated'
    NFL_PLAYER_DELETED = 'NFL player deleted'
    NFL_PLAYER_NOT_FOUND = 'NFL player not found'
    NFL_PLAYER_BAD_REQUEST = 'Bad request. Missing fields.'

    def __init__(self):
        super().__init__(NFLPlayerSerializer, PaginatedNFLPlayerSerializer)

    def get_all(self, request, view):
        return self.paginated_response(NFLPlayer.objects.get_paginated_nfl_players(request, view))

    def get_by_id(self, nfl_player_id):
        validation_response = self._validate_id(nfl_player_id)
        if validation_response:
            return validation_response

        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if nfl_player:
            return self.response(nfl_player, status.HTTP_200_OK)
        return self.response(None, status.HTTP_404_NOT_FOUND, self.NFL_PLAYER_NOT_FOUND)

    def create(self, data):
        self._validate_data(data)

        stats_data = data.pop('stats', [])

        with transaction.atomic():
            created_nfl_player = NFLPlayer.objects.create_nfl_player(data)
            for stat in stats_data:
                NflPlayerStats.objects.create_nfl_player_stats(created_nfl_player, stat)

        return self.response(created_nfl_player, status.HTTP_201_CREATED, self.NFL_PLAYER_CREATED)

    def update(self, nfl_player_id, data):
        validation_response = self._validate_id(nfl_player_id)
        if validation_response:
            return validation_response

        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if not nfl_player:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.NFL_PLAYER_NOT_FOUND)

        validation_response = self._validate_data(data)
        if validation_response:
            return validation_response

        stats_data = data.pop('stats', [])

        with transaction.atomic():
            updated_nfl_player = NFLPlayer.objects.update_nfl_player(nfl_player_id, data)
            for stat in stats_data:
                NflPlayerStats.objects.update_nfl_player_stats(stat['id'], stat)

        return self.response(updated_nfl_player, status.HTTP_200_OK, self.NFL_PLAYER_UPDATED)

    def delete(self, nfl_player_id):
        self._validate_id(nfl_player_id)

        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if not nfl_player:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.NFL_PLAYER_NOT_FOUND)

        NFLPlayer.objects.delete_nfl_player(nfl_player)
        return self.response(nfl_player, status.HTTP_200_OK, self.NFL_PLAYER_DELETED)

    def _validate_id(self, nfl_player_id):
        is_valid_id, error_message = BaseValidator.validate_id(nfl_player_id)
        if not is_valid_id:
            return EntityResponse(None, status.HTTP_400_BAD_REQUEST, error_message)
        return None

    def _validate_data(self, data):
        name = data.get('name')
        photo = data.get('photo')
        number = data.get('number')
        position = data.get('position')
        age = data.get('age')
        experience = data.get('experience')
        college = data.get('college')

        validator = NFLPlayerValidator(name, photo, number, position, age, experience, college)
        is_valid, error_message = validator.validate()

        if not is_valid:
            return self.response(None, status.HTTP_400_BAD_REQUEST, error_message)

        stats_data = data.get('stats', [])
        for stat in stats_data:
            stat_validator = NflPlayerStatsValidator(
                season=stat.get('season'),
                team=stat.get('team'),
                games_played=stat.get('games_played'),
                receptions=stat.get('receptions'),
                receiving_yards=stat.get('receiving_yards'),
                receiving_touchdowns=stat.get('receiving_touchdowns'),
                longest_reception=stat.get('longest_reception')
            )
            is_valid, error_message = stat_validator.validate()
            if not is_valid:
                return self.response(None, status.HTTP_400_BAD_REQUEST, error_message)

        return




