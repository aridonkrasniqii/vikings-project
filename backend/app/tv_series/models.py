from django.db import models
from .managers import VikingManager, NorsemenManager, NflPlayerManager, NflPlayerStatsManager

# Create your models here.
class VikingBase(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Viking(VikingBase):
    actor_name = models.CharField(max_length=255)
    description = models.TextField()
    objects = VikingManager()    
    
    class Meta:
        db_table = 'vikings'
    
    def __str__(self):
        return self.name
    

class Norseman(VikingBase):
    actor_name = models.CharField(max_length=255)
    description = models.TextField()

    objects = NorsemenManager()
    
    class Meta:
        db_table = 'norsemans'
    
    def __str__(self):
        return self.name
from django.db import models

class NFLPlayer(models.Model):
    number = models.IntegerField()
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    experience = models.IntegerField()  # Years in the NFL
    college = models.CharField(max_length=255)

    class Meta:
        db_table = 'nflplayers'

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

    class Meta:
        db_table = 'nflplayerstats'

    def __str__(self):
        return f"{self.player.name} - {self.season}"
