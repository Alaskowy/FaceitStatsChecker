# Generated by Django 4.1 on 2022-10-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_alter_playerstats_aces_alter_playerstats_assists_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstats',
            name='player_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='stats',
            field=models.ManyToManyField(null=True, to='players.playerstats'),
        ),
    ]