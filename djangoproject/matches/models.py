from .team_model import Team
from django.db import models
# Create your models here.

class Match(models.Model):
    match_id = models.CharField(max_length=255, unique=True)
    map = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)
    score = models.CharField(max_length=255)
    rounds = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    team_1 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_1")
    team_2 = models.OneToOneField(Team, on_delete=models.CASCADE, related_name="team_2")

    def __str__(self):
        return self.match_id



