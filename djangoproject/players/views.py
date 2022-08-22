# Create your views here.
from .models import Player

import json

from django.shortcuts import render
import requests
from django.views import View
from django.http import HttpResponse

# Create your views here.


class PlayersView(View):
    def get(self, request):
        data = Player.objects.all().last()
        print(data['country'])
        print(data['nickname'])
        return HttpResponse(json.dumps(request.json()))