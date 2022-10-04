import requests
import os
from matches.models import Match
from .team import TeamService
token = os.getenv("TOKEN")


class MatchService:
    @staticmethod
    def get_match_info_based_on_match_id(match_id: str) -> str:
        """
        Returning match information.
        """
        request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}/stats",
                               headers={"Authorization": f"Bearer {token}"})
        if request.status_code == 200:
            return request.json()

    @staticmethod
    def create_match(data: dict) -> Match:
        """
        Creating match based on data, and return match object.
        """
        match_id = data['rounds'][0]['match_id']
        map_played = data['rounds'][0]['round_stats']['Map']
        winner = data['rounds'][0]['round_stats']['Winner']
        score = data['rounds'][0]['round_stats']['Score']
        rounds = data['rounds'][0]['round_stats']['Rounds']
        region = data['rounds'][0]['round_stats']['Region']
        if not Match.objects.filter(match_id=match_id).exists():
            match_pk = match_id
            instance = Match.objects.create(match_id=match_id, map=map_played, winner=winner, score=score,
                                            rounds=rounds, region=region)
            team1, team2 = TeamService.create_team_based_on_match_data(data, match_id=match_pk)
            instance.teams.add(team1, team2)
            return instance
