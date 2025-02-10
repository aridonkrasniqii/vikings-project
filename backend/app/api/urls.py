from django.urls import path

from api.nfl_players.nfl_players_view import NFLPlayerListView, NFLPlayerDetailView
from api.norsemans.norsemen_view import NorsemanListView, NorsemanDetailView
from api.vikings.vikings_view import VikingsListView, VikingsDetailView
urlpatterns = [
    path('vikings/', VikingsListView.as_view(), name='viking_list'),
    path('vikings/<int:pk>/', VikingsDetailView.as_view(), name='viking_detail'),

    path('norsemen/', NorsemanListView.as_view(), name='norseman_list'),
    path('norsemen/<int:pk>/', NorsemanDetailView.as_view(), name='norseman_detail'),

    path('nflplayers/', NFLPlayerListView.as_view(), name='nfl__player_list'),
    path('nflplayers/<int:pk>/', NFLPlayerDetailView.as_view(), name='nfl_player_detail')
]





