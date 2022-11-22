from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=255, help_text="Team's FaceIT ID")
    matches = models.ForeignKey("matches.Match", on_delete=models.CASCADE, null=True, help_text="List of matches for a team")
    players = models.ManyToManyField("players.Player", help_text="List of players in a team")

    def __str__(self):
        return self.team_id
