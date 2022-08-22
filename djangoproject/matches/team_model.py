from players.models import Player

from django.db import models
class Team(models.Model):
    team_id = models.CharField(max_length=255, unique=True)
    overtime_score = models.CharField(max_length=255)
    second_half_score = models.CharField(max_length=255)
    first_half_score = models.CharField(max_length=255)
    final_score = models.CharField(max_length=255)
    # player_one = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player1')
    # player_two = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player2')
    # player_three = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player3')
    # player_four = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player4')
    # player_five = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='player5')
    players = models.ForeignKey(Player, on_delete=models.CASCADE)