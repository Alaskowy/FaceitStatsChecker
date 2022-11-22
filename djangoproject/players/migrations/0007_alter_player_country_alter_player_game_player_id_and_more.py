# Generated by Django 4.1 on 2022-11-14 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0007_match_epoch_alter_match_leavers_alter_match_map_and_more'),
        ('players', '0006_alter_player_stats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='country',
            field=models.CharField(help_text="Player's country", max_length=100),
        ),
        migrations.AlterField(
            model_name='player',
            name='game_player_id',
            field=models.CharField(help_text="Player's FaceIT ID", max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='matches',
            field=models.ManyToManyField(help_text="Player's matches", to='matches.match'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(help_text="Player's nickname", max_length=40),
        ),
        migrations.AlterField(
            model_name='player',
            name='stats',
            field=models.ManyToManyField(help_text="Player's statistics", to='players.playerstats'),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='aces',
            field=models.PositiveSmallIntegerField(help_text="Player's aces in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='assists',
            field=models.PositiveSmallIntegerField(help_text="Player's assists in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='deaths',
            field=models.PositiveSmallIntegerField(help_text="Player's deaths in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='hscount',
            field=models.PositiveSmallIntegerField(help_text="Player's headshots in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='hspercentage',
            field=models.PositiveSmallIntegerField(help_text="Player's HS% in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='kdratio',
            field=models.FloatField(help_text="Player's K/D Ratio in match", max_length=5),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='kills',
            field=models.SmallIntegerField(help_text="Player's kills in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='krratio',
            field=models.FloatField(help_text="Player's K/R Ratio in match", max_length=5),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='match',
            field=models.ForeignKey(help_text='Related match', on_delete=django.db.models.deletion.CASCADE, to='matches.match'),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='mvps',
            field=models.PositiveSmallIntegerField(help_text="Player's MVP's in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='player_id',
            field=models.CharField(help_text="Player's FaceIT ID", max_length=100),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='quadras',
            field=models.PositiveSmallIntegerField(help_text="Player's quadra kills in match"),
        ),
        migrations.AlterField(
            model_name='playerstats',
            name='triples',
            field=models.PositiveSmallIntegerField(help_text="Player's triple kills in match"),
        ),
    ]