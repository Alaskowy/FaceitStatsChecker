# Generated by Django 4.1 on 2022-08-22 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_remove_team_player_five_remove_team_player_four_and_more'),
        ('players', '0003_remove_player_match_player_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='matches.team'),
        ),
    ]
