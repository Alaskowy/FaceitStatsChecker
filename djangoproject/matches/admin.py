from django.contrib import admin
from .models import Match
from .models import Team
# Register your models here.

admin.site.register(Match)
admin.site.register(Team)