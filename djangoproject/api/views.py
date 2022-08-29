import json
from pprint import pprint
from players.models import Player
from matches.models import Match
from matches.team_model import Team
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
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
    matches = Match.objects.all()
    if not Player.objects.filter(nickname=nickname).exists():
        instance = Player.objects.create(nickname=nickname, country=country, game_player_id=player_id)

def create_team_based_on_match_data(data: str):
    team_1_id = data['rounds'][0]['teams'][0]['team_id']
    team_2_id = data['rounds'][0]['teams'][1]['team_id']
    team_1_players = []
    team_2_players = []
    for player in data['rounds'][0]['teams'][0]['players']:
        team_1_players.append(player["player_id"])
    for player in data['rounds'][0]['teams'][1]['players']:
        team_2_players.append(player["player_id"])
    team = Team(team_id=team_1_id)
    team_1 = Team(team_id=team_2_id)
    team.save()
    team_1.save()
    players = Player.objects.filter(game_player_id__in=team_1_players)
    players_1 = Player.objects.filter(game_player_id__in=team_2_players)
    for player in players:
        team.players.add(player)
    for player in players_1:
        team_1.players.add(player)
    team.save()
    team_1.save()


def get_match_info_based_on_match_id(match_id: str):
    request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}/stats", headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"})
    if request.status_code == 200:
        return request.json()

def create_match(data):
    match_id = data['rounds'][0]['match_id']
    map_played = data['rounds'][0]['round_stats']['Map']
    winner = data['rounds'][0]['round_stats']['Winner']
    score = data['rounds'][0]['round_stats']['Score']
    rounds = data['rounds'][0]['round_stats']['Rounds']
    region = data['rounds'][0]['round_stats']['Region']
    create_team_based_on_match_data(data)
    #if not Match.objects.filter(match_id=match_id).exists():
    #    Match.objects.create(match_id=match_id, map=map_played, winner=winner, score=score, rounds=rounds, region=region, team_1=team_1, team_2=team_2)

class PlayersAPIView(View):
    def get(self, request):
        request = requests.get("https://open.faceit.com/data/v4/players", headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"},
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
                               headers={"Authorization": "Bearer 64cad1ea-124c-432e-896d-f9e14e313cb5"},
                               params={"game": game, "from": '1652973165', "limit": '1'})
        result = request.json()
        match_id = result['items'][0]['match_id']
        print(match_id)
        players = download_players_id(match_id)
        for player in players:
            info_about_player = get_player_info_based_on_player_id(player)
            create_player(info_about_player)
        match = get_match_info_based_on_match_id(match_id)
        create_match(match)

        return HttpResponse(result)





