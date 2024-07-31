from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('games/', views.GameList.as_view(), name='game-list'),
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
]
