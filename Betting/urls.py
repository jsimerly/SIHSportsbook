from django.urls import path
from . import views

urlpatterns = [
    path('create-league/', views.CreateLeague.as_view(), name='create-league')
]