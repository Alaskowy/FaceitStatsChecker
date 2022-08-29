from django.db import models
# Create your models here.


class Player(models.Model):
    country = models.CharField(max_length=100)
    nickname = models.CharField(max_length=40)
    game_player_id = models.CharField(max_length=255)

    def __str__(self):
        return self.nickname

