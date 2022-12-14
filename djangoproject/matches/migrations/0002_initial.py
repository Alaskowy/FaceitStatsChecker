# Generated by Django 4.1 on 2022-09-19 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('matches', '0001_initial'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='players.player'),
        ),
        migrations.AddField(
            model_name='playerstats',
            name='match_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='matches.match'),
        ),
        migrations.AddField(
            model_name='match',
            name='leavers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player'),
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(to='matches.team'),
        ),
    ]
