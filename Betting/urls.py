from django.urls import path
from .views import *

urlpatterns = [
    path('attatch-team-to-user', AttachedTeamToBettor.as_view()),
    path('place-bet', PlaceBet.as_view()),
    # path('get-all-leagues', GetBettors.as_view())
]