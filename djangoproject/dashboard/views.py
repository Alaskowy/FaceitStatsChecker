from django.contrib.auth.models import AnonymousUser
from django.views.generic import TemplateView
import plotly.graph_objs as go
from django.views import View
from players.models import PlayerStats, Player
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from matches.models import Match, Team


def get_last_matches(player_id):
    # TODO Last 5/10 matches
    player = Player.objects.get(game_player_id=player_id).matches.all().values()[:5]
    return player


def get_players_stats_in_match(team1, team2, match_id):
    match_pk = Match.objects.get(match_id=match_id).id
    team_1 = Team.objects.get(team_id=team1, matches=match_pk).players.all().values()
    team_2 = Team.objects.get(team_id=team2, matches=match_pk).players.all().values()
    team_1_ids = [player['game_player_id'] for player in team_1]
    team_2_ids = [player['game_player_id'] for player in team_2]
    team_1_stats = PlayerStats.objects.filter(match=match_pk, player_id__in=team_1_ids)
    team_2_stats = PlayerStats.objects.filter(match=match_pk, player_id__in=team_2_ids)

    return team_1_stats, team_2_stats


def get_players_nicknames_connected_to_stats(team1, team2):
    t1 = {}
    t2 = {}
    for player_1, player_2 in zip(team1, team2):
        t1[player_1] = Player.objects.get(game_player_id=player_1.player_id).nickname
        t2[player_2] = Player.objects.get(game_player_id=player_2.player_id).nickname

    t1 = sorted(t1.items(), key=lambda x: x[0].kills, reverse=True)
    t2 = sorted(t2.items(), key=lambda x: x[0].kills, reverse=True)
    return t1, t2

class DashboardViewSet(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        if not isinstance(user, AnonymousUser):
            context = super(DashboardViewSet, self).get_context_data(**kwargs)
            queryset = PlayerStats.objects.all().filter(player_id=user.faceit_account.game_player_id)
            y = [ele.kdratio for ele in queryset]
            x = [str(ele.match) for ele in queryset]
            figure = go.Figure([go.Scatter(x=x, y=y)])
            figure.update_layout(autosize=True, width=1550, height=220)

            last_matches = list(get_last_matches(user.faceit_account.game_player_id))
            stats = []
            context['last_matches'] = last_matches
            context['graph'] = figure.to_html()
            return context


class MatchDetailView(LoginRequiredMixin, TemplateView):
    template_name = 'match_detail.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        match_id = kwargs.get('match_id')
        context = super(MatchDetailView, self).get_context_data(**kwargs)
        match = Match.objects.get(match_id=match_id)
        player_stats = PlayerStats.objects.get(player_id=user.faceit_account.game_player_id, match_id=match.pk)
        team1, team2 = get_players_stats_in_match(match.teams.first(), match.teams.last(), match_id)
        t1, t2 = get_players_nicknames_connected_to_stats(team1, team2)
        context['t1'] = t1
        context['t2'] = t2
        context['match_stats'] = match
        context['player_stats'] = player_stats
        return context
