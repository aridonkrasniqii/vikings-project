from django.urls import path
from .views import VikingView, NorsemanView, NFLPlayerView, NflPlayerStats

urlpatterns = [
    path('vikings/', VikingView.as_view(), name='vikings'),
    path('vikings/<int:pk>/', VikingView.as_view(), name='vikings_by_id'),
    
    path('norsemen/', NorsemanView.as_view(), name='norsemen'),
    path('norsemen/<int:pk>/', NorsemanView.as_view(), name='norsemen_by_id'),
    
    path('nfl-players/', NFLPlayerView.as_view(), name='nfl_players'),
    path('nfl-players/<int:pk>/', NFLPlayerView.as_view(), name='nfl_players_by_id'),
    
    path('nfl-player-stats/', NflPlayerStats.as_view(), name='nfl_player_stats'),
    path('nfl-player-stats/<int:pk>/', NflPlayerStats.as_view(), name='nfl_player_stats_by_id'),
]
