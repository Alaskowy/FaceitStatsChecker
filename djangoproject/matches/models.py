from .team_model import Team
from django.db import models

class Match(models.Model):
    match_id = models.CharField(max_length=255, unique=True)
    map = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    rounds = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    teams = models.ManyToManyField(Team)
    leavers = models.ManyToManyField('players.Player', null=True)

    def __str__(self):
        return self.match_id



