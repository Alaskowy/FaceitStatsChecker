from django.contrib import admin
from django.urls import path, include
from .views import DashboardViewSet, MatchDetailView


urlpatterns = [
    path(r"", DashboardViewSet.as_view()),
    ##path(r"^matches/(?P<match_id>[0-9]+", view.as_view())
]