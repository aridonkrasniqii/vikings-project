from django.db import models

from api.base.models.base_models import VikingBase
from api.nfl_players.nfl_players_manager import NflPlayerManager, NflPlayerStatsManager


class NFLPlayer(VikingBase):
    number = models.IntegerField(null=True)
    position = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    experience = models.IntegerField(null=True)
    college = models.CharField(max_length=255, null=True)

    objects = NflPlayerManager()

    class Meta:
        db_table = 'nflplayers'
        app_label = 'api'

    def __str__(self):
        return self.name


class NflPlayerStats(models.Model):
    player = models.ForeignKey(NFLPlayer, related_name='stats', on_delete=models.CASCADE)
    season = models.IntegerField()
    team = models.CharField(max_length=255)
    games_played = models.FloatField(default=0)
    receptions = models.FloatField(default=0)
    receiving_yards = models.FloatField(default=0)
    receiving_touchdowns = models.FloatField(default=0)
    longest_reception = models.FloatField(default=0)

    objects = NflPlayerStatsManager()

    class Meta:
        db_table = 'nflplayerstats'

    def __str__(self):
        return f"{self.player.name} - {self.season}"
