# Generated by Django 4.1 on 2022-11-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_alter_player_country_alter_player_game_player_id_and_more'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='faceit_account',
            field=models.OneToOneField(help_text='Linked faceit account', null=True, on_delete=django.db.models.deletion.CASCADE, to='players.player'),
        ),
    ]