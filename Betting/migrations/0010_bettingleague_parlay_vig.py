# Generated by Django 4.0 on 2022-07-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Betting', '0009_placedparlay_payout_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bettingleague',
            name='parlay_vig',
            field=models.DecimalField(decimal_places=4, default=0.01, max_digits=7),
        ),
    ]