# Generated by Django 4.1 on 2022-10-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0005_delete_playerstats'),
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('triples', models.PositiveSmallIntegerField(max_length=2)),
                ('assists', models.PositiveSmallIntegerField(max_length=3)),
                ('kdratio', models.FloatField(max_length=5)),
                ('deaths', models.PositiveSmallIntegerField(max_length=3)),
                ('aces', models.PositiveSmallIntegerField(max_length=2)),
                ('hspercentage', models.PositiveSmallIntegerField(max_length=3)),
                ('hscount', models.PositiveSmallIntegerField(max_length=3)),
                ('quadras', models.PositiveSmallIntegerField(max_length=2)),
                ('kills', models.SmallIntegerField(max_length=3)),
                ('krratio', models.FloatField(max_length=5)),
                ('mvps', models.PositiveSmallIntegerField(max_length=2)),
                ('match', models.ManyToManyField(to='matches.match')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='stats',
            field=models.ManyToManyField(to='players.playerstats'),
        ),
    ]
