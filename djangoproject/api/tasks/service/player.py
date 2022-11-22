import requests
import os
from players.models.player import Player
from players.models.stats import PlayerStats
from matches.models import Match
from typing import Union
token = os.getenv("TOKEN")


class PlayerService:

    @staticmethod
    def update_player_matches(players_to_update: Union[str, list[str]], match: 'Match') -> None:
        if isinstance(players_to_update, str):
            player_to_update = Player.objects.get(game_player_id=players_to_update)
            player_to_update.matches.add(match)
            player_to_update.save()
        else:
            for player_id in players_to_update:
                player_to_update = Player.objects.get(game_player_id=player_id)
                player_to_update.matches.add(match)
                player_to_update.save()


    @staticmethod
    def get_player_info_based_on_player_id(player_id: str) -> dict:
        """
        Returning player information.
        """
        request = requests.get(f"https://open.faceit.com/data/v4/players/{player_id}",
                               headers={"Authorization": f"Bearer {token}"})
        return request.json()

    @staticmethod
    def create_player(data: dict) -> None:
        """
        Creating player object based on given data from API.
        """
        player_id = data['player_id']
        nickname = data['nickname']
        country = data['country']
        if not Player.objects.filter(nickname=nickname).exists():
            Player.objects.create(nickname=nickname, country=country, game_player_id=player_id)
        # TODO LOGGING

    @staticmethod
    def get_teams_players(data: dict):
        return data['rounds'][0]['teams'][0]['players'] + data['rounds'][0]['teams'][1]['players']

    @staticmethod
    def create_single_player_stats(player_id: str, player_stats: dict, match: 'Match'):
        if not PlayerStats.objects.filter(match=match, player_id=player_id).exists():
            instance = PlayerStats.objects.create(
                match=match,
                triples=player_stats['Triple Kills'],
                assists=player_stats['Assists'],
                kdratio=player_stats['K/D Ratio'],
                deaths=player_stats['Deaths'],
                aces=player_stats['Penta Kills'],
                hspercentage=player_stats['Headshots %'],
                hscount=player_stats['Headshots'],
                quadras=player_stats['Quadro Kills'],
                kills=player_stats['Kills'],
                krratio=player_stats['K/R Ratio'],
                mvps=player_stats['MVPs'],
                player_id=player_id
            )
            return instance




    @staticmethod
    def create_player_stats(match_info: dict, match: 'Match') -> None:
        """
        Creating player stats object based on given data from API.
        """
        players = PlayerService.get_teams_players(match_info)
        for player in players:
            stats = PlayerService.create_single_player_stats(player_id=player['player_id'],
                                                             player_stats=player['player_stats'],
                                                             match=match)
            #Player.objects.filter(player_id__in=[player['player_id'] for player in players])
            obj = Player.objects.get(game_player_id=player['player_id'])
            obj.stats.add(stats)
            obj.save()
