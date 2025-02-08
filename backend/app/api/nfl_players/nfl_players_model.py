from django.db import models

from api.base.models.base_models import VikingBase
from api.nfl_players.nfl_players_manager import NflPlayerManager, NflPlayerStatsManager


class NFLPlayer(VikingBase):
    number = models.IntegerField(null=True)
    position = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)  # Years in the NFL
    college = models.CharField(max_length=255, null=True)

    objects = NflPlayerManager()

    class Meta:
        db_table = 'nflplayers'
        # app_label = "api"

    def __str__(self):
        return self.name


class NflPlayerStats(models.Model):
    player = models.ForeignKey(NFLPlayer, related_name='stats', on_delete=models.CASCADE)
    season = models.IntegerField()  # Season year
    team = models.CharField(max_length=255)  # Team for the season
    games_played = models.IntegerField(default=0)  # Total games played
    receptions = models.IntegerField(default=0)  # Total receptions
    receiving_yards = models.IntegerField(default=0)  # Total receiving yards
    receiving_touchdowns = models.IntegerField(default=0)  # Receiving touchdowns
    longest_reception = models.IntegerField(default=0)  # Longest reception in yards

    objects = NflPlayerStatsManager()

    class Meta:
        db_table = 'nflplayerstats'
        app_label = "api"

    def __str__(self):
        return f"{self.player.name} - {self.season}"
