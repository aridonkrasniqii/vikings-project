from django.urls import path

from api.nfl_players.nfl_players_view import NFLPlayerListView, NFLPlayerDetailView, NFLPlayerScrapeView
from api.norsemans.norsemen_view import NorsemanListView, NorsemanDetailView, NorsemanScrapeView
from api.vikings.vikings_view import VikingsListView, VikingsDetailView, VikingsScrapeView

urlpatterns = [
    path('vikings/', VikingsListView.as_view(), name='viking_list'),  # List all Vikings
    path('vikings/<int:pk>/', VikingsDetailView.as_view(), name='viking_detail'),
    path('vikings/scrape/', VikingsScrapeView.as_view(), name='viking_scrape'),

    path('norsemen/', NorsemanListView.as_view(), name='norseman_list'),
    path('norsemen/<int:pk>/', NorsemanDetailView.as_view(), name='norseman_detail'),
    path('norsemen/scrape/', NorsemanScrapeView.as_view(), name='norseman_scrape'),

    path('nflplayers/', NFLPlayerListView.as_view(), name='nfl__player_list'),
    path('nflplayers/<int:pk>/', NFLPlayerDetailView.as_view(), name='nfl_player_detail'),
    path('nflplayers/scrape/', NFLPlayerScrapeView.as_view(), name='nfl_player_scrape'),
]





