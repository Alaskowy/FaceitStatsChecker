from django.contrib import admin
from django.urls import path, include
from .views import DashboardViewSet, MatchDetailView


urlpatterns = [
    path(r"", DashboardViewSet.as_view(), name='dashboard'),
    path(r"matches/<str:match_id>", MatchDetailView.as_view(), name='match-detail')
]