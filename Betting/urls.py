from django.urls import path
from . import views

urlpatterns = [
    path('create-league/', views.CreateLeague.as_view(), name='create-league'),
    path('update-player-info/', views.UpdateNflPlayers.as_view(), name='update-player-info'),
    path('update-all-projections', views.UpdatePlayerProjections.as_view()),
    path('update-league-projections', views.UpdateLeagueProjections.as_view()),
    path('update-league-rosters', views.UpdateLeagueRosters.as_view()),
    path('update-league-state', views.UpdateNflState.as_view())
]