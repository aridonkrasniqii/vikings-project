from django.db import models
import logging

class VikingManager(models.Manager):
    def get_all_vikings(self):
        return self.all()

    def get_viking_by_id(self, viking_id):
        return self.filter(id=viking_id).first()


    def create_viking(self, viking):
        return self.create(**viking.__dict__)

    def update_viking(self, viking):
        viking.save()
        return viking

    def delete_viking(self, viking):
        viking.delete()

class NorsemenManager(models.Manager):
    def get_all_norsemen(self):
        return self.all()

    def get_norseman_by_id(self, norseman_id):
        return self.filter(id=norseman_id).first()

    def create_norseman(self, norseman):
        return self.create(**norseman.__dict__)

    def update_norseman(self, norseman):
        norseman.save()
        return norseman

    def delete_norseman(self, norseman):
        norseman.delete()

class NflPlayerManager(models.Manager):
    def get_all_nfl_players(self):
        return self.all()

    def get_nfl_player_by_id(self, player_id):
        return self.filter(id=player_id).first()

    def create_nfl_player(self, nfl_player):
        return self.create(**nfl_player.__dict__)

    def update_nfl_player(self, nfl_player):
        nfl_player.save()
        return nfl_player

    def delete_nfl_player(self, nfl_player):
        nfl_player.delete()
        
class NflPlayerStatsManager(models.Manager):
    def get_stats_by_player(self, player_id):
        return self.filter(nflplayer__id=player_id)

    def create_stats(self, stats):
        return self.create(**stats.__dict__)

    def update_stats(self, stats):
        stats.save()
        return stats

    def delete_stats(self, stats):
        stats.delete()