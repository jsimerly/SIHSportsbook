# Generated by Django 4.0 on 2022-04-30 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0012_remove_player_currentproj_player_currentfumbles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='projFumbles',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='player',
            name='projInts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='player',
            name='projPassingTds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='player',
            name='projPassingYds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='player',
            name='projRushingTds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AlterField(
            model_name='player',
            name='projRushingYds',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
