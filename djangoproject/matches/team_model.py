from django.db import models
from players.models import Player

class Team(models.Model):
    team_id = models.CharField(max_length=255)
    players = models.ManyToManyField(Player, default=None)