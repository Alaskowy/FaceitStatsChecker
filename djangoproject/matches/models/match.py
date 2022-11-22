from matches.models.team import Team
from django.db import models

class Match(models.Model):
    match_id = models.CharField(max_length=255, unique=True, help_text="FaceIT Match ID")
    map = models.CharField(max_length=255, help_text="Map on which the game was played")
    winner = models.CharField(max_length=255, help_text="Winner of the match")
    score = models.CharField(max_length=255, help_text="Score of the match")
    rounds = models.CharField(max_length=255, help_text="Amount of rounds in a match")
    region = models.CharField(max_length=255, help_text="Region of the match")
    teams = models.ManyToManyField(Team, help_text="List of teams in a match")
    leavers = models.ManyToManyField('players.Player', help_text="List of leavers in a match")
    epoch = models.DateTimeField(help_text="Epoch of match ending")

    def __str__(self):
        return self.match_id




