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
        context = super(DashboardViewSet, self).get_context_data(**kwargs)
        queryset = PlayerStats.objects.all().filter(player_id='808291d9-7d38-4a56-b26e-70581040db41')

        y = [ele.kdratio for ele in queryset]
        x = [str(ele.match) for ele in queryset]
        figure = go.Figure([go.Scatter(x=x, y=y)])
        figure.update_layout(autosize=True, width=1550, height=220)

        last_matches = list(get_last_matches('808291d9-7d38-4a56-b26e-70581040db41'))
        stats = []
        context['last_matches'] = last_matches
        context['graph'] = figure.to_html()
        return context



