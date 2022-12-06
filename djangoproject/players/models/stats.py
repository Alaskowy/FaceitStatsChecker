from django.db import models


class PlayerStats(models.Model):
    match = models.ForeignKey("matches.Match", on_delete=models.CASCADE, help_text="Related match",)
    triples = models.PositiveSmallIntegerField(help_text="Player's triple kills in match",)
    assists = models.PositiveSmallIntegerField(help_text="Player's assists in match",)
    kdratio = models.FloatField(max_length=5, help_text="Player's K/D Ratio in match",)
    deaths = models.PositiveSmallIntegerField(help_text="Player's deaths in match",)
    aces = models.PositiveSmallIntegerField(help_text="Player's aces in match",)
    hspercentage = models.PositiveSmallIntegerField(help_text="Player's HS% in match",)
    hscount = models.PositiveSmallIntegerField(help_text="Player's headshots in match",)
    quadras = models.PositiveSmallIntegerField(help_text="Player's quadra kills in match",)
    kills = models.SmallIntegerField(help_text="Player's kills in match",)
    krratio = models.FloatField(max_length=5, help_text="Player's K/R Ratio in match",)
    mvps = models.PositiveSmallIntegerField(help_text="Player's MVP's in match",)
    player_id = models.CharField(max_length=100, help_text="Player's FaceIT ID",)

    def __str__(self):
        return str(self.player_id)
