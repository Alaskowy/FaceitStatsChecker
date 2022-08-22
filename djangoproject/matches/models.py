from .team_model import Team
from django.db import models
# Create your models here.

class Match(models.Model):
    match_id = models.CharField(max_length=255)
    map = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    rounds = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    team_1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_2")



class PlayerStats(models.Model):
    match_id = models.OneToOneField(Match, on_delete=models.CASCADE)


