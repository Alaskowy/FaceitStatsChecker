from django.db import models
from .stats import PlayerStats

class Player(models.Model):
    country = models.CharField(max_length=100, help_text="Player's country")
    nickname = models.CharField(max_length=40, help_text="Player's nickname")
    game_player_id = models.CharField(max_length=255, help_text="Player's FaceIT ID")
    matches = models.ManyToManyField("matches.Match", help_text="Player's matches")
    stats = models.ManyToManyField(PlayerStats, help_text="Player's statistics")

    def __str__(self):
        return self.nickname