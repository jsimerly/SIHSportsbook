from textwrap import indent
from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index),
    path('test/', index),
    path('login/', index),
    path('register/',index),
    path('new-league/', index),
    path('league/', index)
]