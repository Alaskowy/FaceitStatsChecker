from django.db import models

# Create your models here

class PlayerStats(models.Model):
    match = models.ForeignKey("matches.Match", on_delete=models.CASCADE)
    triples = models.PositiveSmallIntegerField()
    assists = models.PositiveSmallIntegerField()
    kdratio = models.FloatField(max_length=5)
    deaths = models.PositiveSmallIntegerField()
    aces = models.PositiveSmallIntegerField()
    hspercentage = models.PositiveSmallIntegerField()
    hscount = models.PositiveSmallIntegerField()
    quadras = models.PositiveSmallIntegerField()
    kills = models.SmallIntegerField()
    krratio = models.FloatField(max_length=5)
    mvps = models.PositiveSmallIntegerField()
    player_id = models.CharField(max_length=100)

    def __str__(self):
        return str(self.match)

class Player(models.Model):
    country = models.CharField(max_length=100)
    nickname = models.CharField(max_length=40)
    game_player_id = models.CharField(max_length=255)
    matches = models.ManyToManyField("matches.Match")
    stats = models.ManyToManyField(PlayerStats, null=True)

    def __str__(self):
        return self.nickname

