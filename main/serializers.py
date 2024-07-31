from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Game, PlayerProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['name', 'description', 'image', 'num_players']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = ['user', 'background', 'role']