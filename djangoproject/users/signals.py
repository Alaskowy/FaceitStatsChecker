from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from .utils import get_user_data
from players.models import Player
from api.tasks.service import MatchService, TeamService, PlayerService
import os
import requests
from matches.models import Match
token = os.getenv("TOKEN")

def fetch_data_helper(player: 'Player', game='csgo', limit=5):
    request = requests.get(f"https://open.faceit.com/data/v4/players/{player.game_player_id}/history",
                           headers={"Authorization": f"Bearer {token}"},
                           params={"game": game, "from": '1652973165', "limit": limit})
    result = request.json()
    for x in range(limit):
        match_id = result['items'][x]['match_id']
        if Match.objects.filter(match_id=match_id).exists():
            return # TODO something
        players = TeamService.download_teams_with_players(match_id)
        for player in players:
            info_about_player = PlayerService.get_player_info_based_on_player_id(player)
            PlayerService.create_player(info_about_player)
        epoch = MatchService.get_epoch_time_for_match(match_id)
        match_info = MatchService.get_match_info_based_on_match_id(match_id)
        match = MatchService.create_match(match_info, epoch)
        PlayerService.update_player_matches(players, match)
        PlayerService.create_player_stats(match_info, match)


@receiver(post_save, sender=Account)
def fetch_data(sender, instance, created, **kwargs):
    if created:
        nickname = instance.nickname
        user = Account.objects.get(email=instance.email)
        user_data = get_user_data(nickname)
        player = Player.objects.create(nickname=nickname, country=user_data['country'],
                                       game_player_id=user_data['player_id'])
        user.faceit_account = player
        fetch_data_helper(user.faceit_account)
        user.save()

