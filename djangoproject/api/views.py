import json
from typing import Union
from pprint import pprint
from players.models import Player
from matches.models import Match
from matches.team_model import Team
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import os
import requests
from django.views import View
from django.http import HttpResponse
from .tasks.service import MatchService, TeamService, PlayerService
SECOND_MATCH = "1-7a4ed8f2-f4c2-40e3-a995-3a3ee5f24d37"
token = os.getenv("TOKEN")


class PlayersAPIView(View):
    def get(self, request):
        request = requests.get("https://open.faceit.com/data/v4/players", headers={"Authorization": f"Bearer {token}"},
                               params={"nickname": "Alask"})
        result = request.json()
        player_id = result['player_id']
        if not Player.objects.filter(nickname=result['nickname']).exists():
            Player.objects.create(nickname=result['nickname'], country=result['country'], game_player_id=player_id)
        return HttpResponse(json.dumps(result))


class PlayersGamesHistory(View):
    def get(self, request):
        nickname = "Alask"
        game = "csgo"
        try:
            player = Player.objects.get(nickname=nickname)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)
        request = requests.get(f"https://open.faceit.com/data/v4/players/808291d9-7d38-4a56-b26e-70581040db41/history",
                               headers={"Authorization": f"Bearer {token}"},
                               params={"game": game, "from": '1652973165', "limit": '1'})
        result = request.json()
        match_id = result['items'][0]['match_id']
        match_id = SECOND_MATCH
        players = TeamService.download_teams_with_players(match_id)
        for player in players:
            info_about_player = PlayerService.get_player_info_based_on_player_id(player)
            PlayerService.create_player(info_about_player)
        match = MatchService.get_match_info_based_on_match_id(match_id)
        matchstats = MatchService.create_match(match)
        PlayerService.create_player_stats(match=matchstats, data=match)

        return HttpResponse(result)





