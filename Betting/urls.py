from django.urls import path
from . import pViews
from . import gViews

urlpatterns = [
    path('create-league/', pViews.CreateLeague.as_view(), name='create-league'),
    path('update-player-info/', pViews.UpdateNflPlayers.as_view(), name='update-player-info'),
    path('update-all-projections', pViews.UpdatePlayerProjections.as_view()),
    path('update-league-projections', pViews.UpdateLeagueProjections.as_view()),
    path('update-league-rosters', pViews.UpdateLeagueRosters.as_view()),
    path('update-league-state', pViews.UpdateNflState.as_view()),
    path('update-league-matchups', pViews.UpdateLeagueMatchups.as_view()),
    path('attatch-team-to-user', pViews.AttachedTeamToBettor.as_view()),
    path('place-bet', pViews.PlaceBet.as_view()),
    path('get-all-leagues', gViews.GetBettors.as_view())
]