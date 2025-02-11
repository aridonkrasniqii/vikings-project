from asgiref.sync import sync_to_async
from django.db import transaction

from rest_framework import status
from api.base.services import BaseService
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
        self._validate_id(nfl_player_id)

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

    @sync_to_async
    def update_or_create(self, data):
        validation_response = self._validate_data(data)
        if validation_response:
            raise ValueError(f"Invalid data: {validation_response}")

        stats_data = data.pop('stats', [])

        with transaction.atomic():
            nfl_player = self._update_or_create_player(data)
            self._update_or_create_player_stats(nfl_player, stats_data)

        return self._generate_response(nfl_player)

    def _update_or_create_player(self, data):
        nfl_player, created = NFLPlayer.objects.update_or_create(
            name=data.get('name'),
            defaults={
                'number': data.get('number'),
                'position': data.get('position'),
                'age': data.get('age'),
                'experience': data.get('experience'),
                'college': data.get('college'),
            }
        )
        return nfl_player

    def _update_or_create_player_stats(self, nfl_player, stats_data):
        for stat in stats_data:
            NflPlayerStats.objects.update_or_create(
                player=nfl_player,
                season=stat.get('season'),
                defaults={
                    'team': stat.get('team'),
                    'games_played': stat.get('games_played'),
                    'receptions': stat.get('receptions'),
                    'receiving_yards': stat.get('receiving_yards'),
                    'receiving_touchdowns': stat.get('receiving_touchdowns'),
                    'longest_reception': stat.get('longest_reception'),
                }
            )

    def _generate_response(self, nfl_player):
        status_code = status.HTTP_200_OK
        message = self.NFL_PLAYER_UPDATED if hasattr(nfl_player, 'id') else self.NFL_PLAYER_CREATED
        return self.response(nfl_player, status_code, message)

    def update(self, nfl_player_id, data):
        self._validate_id(nfl_player_id)

        nfl_player = NFLPlayer.objects.get_nfl_player_by_id(nfl_player_id)
        if not nfl_player:
            return self.response(None, status.HTTP_404_NOT_FOUND, self.NFL_PLAYER_NOT_FOUND)

        self._validate_data(data)

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

        return None




