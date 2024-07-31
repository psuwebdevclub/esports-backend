from django.db import models
from django.contrib.auth.models import User
class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='game_images/')
    num_players = models.IntegerField()

class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.CharField(max_length=500)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username}'s profile for {self.game.name}"