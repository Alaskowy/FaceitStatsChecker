import requests
import os
from matches.models import Match
from .team import TeamService
from datetime import datetime, timezone
token = os.getenv("TOKEN")


class MatchService:
    @staticmethod
    def get_match_info_based_on_match_id(match_id: str) -> dict:
        """
        Returning match information.
        """
        request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}/stats",
                               headers={"Authorization": f"Bearer {token}"})
        if request.status_code == 200:
            return request.json()

    @staticmethod
    def create_match(data: dict, epoch: datetime) -> Match:
        """
        Creating match based on data, and return match object.
        """
        match_id = data['rounds'][0]['match_id']
        map_played = data['rounds'][0]['round_stats']['Map']
        winner = data['rounds'][0]['round_stats']['Winner']
        score = data['rounds'][0]['round_stats']['Score']
        rounds = data['rounds'][0]['round_stats']['Rounds']
        region = data['rounds'][0]['round_stats']['Region']
        instance = Match.objects.create(match_id=match_id, map=map_played, winner=winner, score=score,
                                        rounds=rounds, region=region, epoch=epoch)
        team1, team2 = TeamService.create_team_based_on_match_data(data, match_id=match_id)
        instance.teams.add(team1, team2)
        return instance

    @staticmethod
    def get_epoch_time_for_match(match_id: str) -> datetime:
        """
        Getting epoch time for match based on match_id and return datetime object.
        """
        request = requests.get(f"https://open.faceit.com/data/v4/matches/{match_id}",
                               headers={"Authorization": f"Bearer {token}"})
        if request.status_code == 200:
            return datetime.fromtimestamp(request.json()['finished_at'], timezone.utc)
