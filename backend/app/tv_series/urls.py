from django.urls import path

from tv_series.nfl_players.nfl_players_view import NFLPlayerListView, NFLPlayerDetailView, NFLPlayerScrapeView
from tv_series.norsemans.norsemen_view import NorsemanListView, NorsemanDetailView, NorsemanScrapeView
from tv_series.vikings.vikings_view import VikingsListView, VikingsDetailView, VikingsScrapeView

urlpatterns = [
    path('vikings/', VikingsListView.as_view(), name='viking_list'),  # List all Vikings
    path('viking/<int:pk>/', VikingsDetailView.as_view(), name='viking_detail'),
    path('viking/scrape/', VikingsScrapeView.as_view(), name='viking_scrape'),

    path('norsemen/', NorsemanListView.as_view(), name='norseman_list'),
    path('norseman/<int:pk>/', NorsemanDetailView.as_view(), name='norseman_detail'),
    path('norsemen/scrape/', NorsemanScrapeView.as_view(), name='norseman_scrape'),

    path('nflplayers/', NFLPlayerListView.as_view(), name='nfl__player_list'),
    path('nflplayer/<int:pk>/', NFLPlayerDetailView.as_view(), name='nfl_player_detail'),
    path('nflplayers/scrape/', NFLPlayerScrapeView.as_view(), name='nfl_player_scrape'),
]





