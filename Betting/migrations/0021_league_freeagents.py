# Generated by Django 4.0 on 2022-05-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0020_player_estproj'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='freeAgents',
            field=models.ManyToManyField(to='Betting.Player'),
        ),
    ]