import json
from pprint import pprint
from players.models import Player
from matches.models import Match
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
import simplejson
import requests
from django.views import View
from django.http import HttpResponse

# Create your views here.

def download_players_id(match_id: str) -> list:
    request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}", headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"},)
    result = request.json()
    teams = ['faction1', 'faction2']
    list_of_players = []
    for team in teams:
        roster = result['teams'][team]['roster']
        team_of_players = [player['player_id'] for player in roster]
        list_of_players.extend(team_of_players)
    return list_of_players

def get_player_info_based_on_player_id(player_id: str):
    request = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}", headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"})
    return request.json()

def create_player(data):
    player_id = data['player_id']
    nickname = data['nickname']
    country = data['country']
    match = Match.objects.all()
    match.team_1.objects.all().filter()
    pprint(data)

class PlayersAPIView(View):
    def get(self, request):
        request = requests.get("https://open.faceit.com/data/v4/players", headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"},
                               params={"nickname": "Alask"})
        result = request.json()
        # game_player_id = result['games']['csgo']['game_player_id']
        if not Player.objects.filter(nickname=result['nickname']).exists():
            Player.objects.create(nickname=result['nickname'], country=result['country'], game_player_id=game_player_id)
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
                               headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"},
                               params={"game": game, "from": '1652973165', "limit": '1'})
        result = request.json()
        match_id = result['items'][0]['match_id']
        print(match_id)
        players = download_players_id(match_id)
        info_about_player = get_player_info_based_on_player_id(players[0])
        create_player(info_about_player)
        return HttpResponse(simplejson.dumps(result))





