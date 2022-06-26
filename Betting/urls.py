from django.urls import path
from .views import *

urlpatterns = [
    path('create-betting-league', CreateBettingLeague.as_view()),
    path('attach-team-to-user', AttachedTeamToBettor.as_view()),
    # path('place-bet', PlaceBet.as_view()),
    # path('get-all-leagues', GetBettors.as_view())
]