from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('create-user/', views.CreateUser.as_view(), name='create-user'),
    path('authentication/', views.LogIn.as_view(), name='api-token-auth'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('current-user', views.CurrentUser.as_view(), name='current-user'),
    path('activate-user/<uidb64>/<token>', views.activate_uesr.as_view(), name='activate')
]