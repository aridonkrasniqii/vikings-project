
from django.contrib import admin

from api.nfl_players.nfl_players_model import NFLPlayer
from api.norsemans.norsemen_models import Norseman
from api.vikings.vikings_model import Viking

admin.site.register(Viking)
admin.site.register(Norseman)
admin.site.register(NFLPlayer)

# (Optional) Add Django Admin & API for Viewing Scraped Data