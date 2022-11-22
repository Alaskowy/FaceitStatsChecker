from django.contrib import admin

from .models.player import Player
from .models.stats import PlayerStats

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'nickname', 'game_player_id')
    search_fields = ('nickname', )
    list_filter = ('country', )

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerStats)