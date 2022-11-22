from players.models import Player
from matches.models import Match
from matches.team_model import Team
from typing import Union
import requests
import os
token = os.getenv("TOKEN")


class TeamService:
    @staticmethod
    def create_teams(players: dict[str, list[str]]) -> tuple[list[str], list[str]]:
        """
        Returning lists of players in teams
        """
        team_1_players = []
        team_2_players = []
        for player_1, player_2 in zip(players['faction1'], players['faction2']):
            team_1_players.append(player_1)
            team_2_players.append(player_2)
        return team_1_players, team_2_players

    @staticmethod
    def download_teams_with_players(match_id: str, teams_flag=False) -> Union[list[str], dict[str, list[str]]]:
        """
        Returning list of player id in current match_id with breakdown of teams.
        """
        request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}",
                               headers={"Authorization": f"Bearer {token}"}, )
        result = request.json()
        teams = ['faction1', 'faction2']
        if teams_flag:
            list_of_players = {}
            for team in teams:
                roster = result['teams'][team]['roster']
                team_of_players = [player['player_id'] for player in roster]
                list_of_players[team] = team_of_players
        else:
            list_of_players = []
            for team in teams:
                roster = result['teams'][team]['roster']
                team_of_players = [player['player_id'] for player in roster]
                list_of_players.extend(team_of_players)
        return list_of_players

    @staticmethod
    def create_team_based_on_match_data(data: dict[Any], match_id) -> tuple['Team', ...]:
        """
         Returning Team objects based on data.
        """
        teams = {}
        team_1 = [player['player_id'] for player in data['rounds'][0]['teams'][0]['players']]
        team_2 = [player['player_id'] for player in data['rounds'][0]['teams'][1]['players']]
        teams.update({'faction1': team_1, 'faction_2': team_2})
        team_1_id = data['rounds'][0]['teams'][0]['team_id']
        team_2_id = data['rounds'][0]['teams'][1]['team_id']
        if len(team_1) + len(team_2) == 10:
            team_1_players, team_2_players = TeamService.create_teams(teams)
        else:
            players = TeamService.download_teams_with_players(match_id, teams_flag=True)
            team_1_players, team_2_players = TeamService.create_teams(players)
            leavers = set(team_1_players + team_2_players) - set(team_1 + team_2)
            if leavers:
                match = Match.objects.get(match_id=match_id)
                for leaver in leavers:
                    obj = Player.objects.get(game_player_id=leaver)
                    match.leavers.add(obj)
                match.save()

        match = Match.objects.get(match_id=match_id)
        team = Team.objects.create(team_id=team_1_id, matches=match)
        team_1 = Team.objects.create(team_id=team_2_id, matches=match)
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
        return team, team_1
