from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Game, PlayerProfile
from rest_framework import generics
from .serializers import UserSerializer, GameSerializer, ProfileSerializer

from rest_framework.permissions import IsAuthenticated  # Import the IsAuthenticated permission

# Create your views here.
class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class GameList(generics.ListAPIView):

    queryset = Game.objects.all()
    serializer_class = GameSerializer

class ProfileList(generics.ListAPIView):

    queryset = PlayerProfile.objects.all()
    serializer_class = ProfileSerializer

