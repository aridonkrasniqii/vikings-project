from django.contrib import admin

# Register your models here.

from django.contrib import admin

from tv_series.nfl_players.nfl_players_model import NFLPlayer
from tv_series.norsemans.norsemen_models import Norseman
from tv_series.vikings.vikings_model import Viking

admin.site.register(Viking)
admin.site.register(Norseman)
admin.site.register(NFLPlayer)

# (Optional) Add Django Admin & API for Viewing Scraped Data