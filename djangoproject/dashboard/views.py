from django.views.generic import TemplateView
import plotly.graph_objs as go
from django.views import View
from players.models import PlayerStats, Player


def get_last_matches(player_id):
    # TODO 5/10 ostatnich meczy
    player = Player.objects.get(game_player_id=player_id).matches.all().values()[:5]
    return player


class DashboardViewSet(TemplateView):
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
