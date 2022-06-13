from django.urls import path
from .views import *

urlpatterns = [
    path('create-league/', CreateLeague.as_view(), name='create-league'),
    path('update-nfl-players', UpdateNflPlayers.as_view(), name='update-nfl-players'),

    path('update-player-projections', UpdatePlayerProjections.as_view(), name='update-player-projections'),
    path('update-league-projections', UpdateLeagueProjections.as_view(), name='update-league-projections'),
    path('update-league-rosters', UpdateLeagueRosters.as_view(), name='update-league-rosters'),
    path('update-nfl-state', UpdateNflState.as_view(), name='update-nfl-state'),
    path('update-league-matchups', UpdateFantasyLeagueMatchups.as_view(), name='update-league-matchups')
]