from django.apps import AppConfig
from django.db.models.signals import post_save

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from .models import Account
        from .signals import fetch_data
        post_save.connect(fetch_data, sender=Account)