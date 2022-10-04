from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=255)
    matches = models.ForeignKey("matches.Match", on_delete=models.CASCADE, null=True)
    players = models.ManyToManyField("players.Player")

    def __str__(self):
        return self.team_id
