from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from .utils import get_user_data
from players.models import Player

@receiver(post_save, sender=Account)
def fetch_data(sender, instance, created, **kwargs):
    if created:
        nickname = instance.nickname
        user = Account.objects.get(email=instance.email)
        user_data = get_user_data(nickname)
        player = Player.objects.create(nickname=nickname, country=user_data['country'],
                                       game_player_id=user_data['player_id'])
        user.faceit_account = player
        user.save()

