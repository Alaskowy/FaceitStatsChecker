# Generated by Django 4.1 on 2022-08-22 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='player_five',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_four',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_one',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_three',
        ),
        migrations.RemoveField(
            model_name='team',
            name='player_two',
        ),
    ]
