# Generated by Django 4.0 on 2022-05-03 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0026_nflstate_lastplayerupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='bettor',
            name='betsLeft',
            field=models.IntegerField(default=2),
        ),
    ]
