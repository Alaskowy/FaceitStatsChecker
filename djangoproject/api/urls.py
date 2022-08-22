from django.urls import path

from .views import PlayersAPIView, PlayersGamesHistory

urlpatterns = [
    path("players/", PlayersAPIView.as_view(), name='players'),
    path("matches/", PlayersGamesHistory.as_view(), name='matches'),
]