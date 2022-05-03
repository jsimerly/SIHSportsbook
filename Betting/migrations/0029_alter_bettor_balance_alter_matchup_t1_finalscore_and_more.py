# Generated by Django 4.0 on 2022-05-03 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0028_remove_bettor_fantasyteams_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bettor',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='t1_finalScore',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='matchup',
            name='t2_finalScore',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True),
        ),
    ]