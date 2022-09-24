from django.urls import path
from .views import *

urlpatterns = [
    path('create-betting-league', CreateBettingLeague.as_view()),
    path('attach-team-to-user', AttachedTeamToBettor.as_view()),
    path('update-betting-matchups', CreateMatchupBets.as_view()),
    path('place-bet-matchup', PlaceMatchupBet.as_view()),
    path('get-matchups', GetMathcupBets.as_view()),
    path('get-all-leagues', GetAllLeagues.as_view()),
    path('get-league-bet-history', GetAllBetsForSingleLeague.as_view()),
    path('request-to-join-league', GetBettingLeagueTeams.as_view()),
    path('request-to-join-team', RequestToJoinLeague.as_view()),
]