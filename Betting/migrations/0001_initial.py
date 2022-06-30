# Generated by Django 4.0 on 2022-06-30 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Fantasy', '0001_initial'),
        ('Account', '0003_alter_user_is_email_verified'),
    ]

    operations = [
        migrations.CreateModel(
            name='BettingLeague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('std_vig', models.DecimalField(decimal_places=4, default=0.0476, max_digits=7)),
                ('weekly_allowance', models.DecimalField(decimal_places=2, default=10, max_digits=10)),
                ('weekly_n_bets', models.IntegerField(default=10)),
                ('bet_on_self', models.BooleanField(default=True)),
                ('bet_on_opponent', models.BooleanField(default=False)),
                ('bookie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.user')),
                ('fantasy_league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betting_league', to='Fantasy.fantasyleague')),
            ],
        ),
        migrations.CreateModel(
            name='Bettor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('allowance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bets_left', models.IntegerField(default=10)),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bettor', to='Betting.bettingleague')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Fantasy.fantasyteam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.user')),
            ],
        ),
        migrations.CreateModel(
            name='MatchupBets',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('ml_team1', models.DecimalField(decimal_places=3, max_digits=9)),
                ('ml_team2', models.DecimalField(decimal_places=3, max_digits=9)),
                ('ml_edited', models.BooleanField(default=False)),
                ('over', models.DecimalField(decimal_places=3, max_digits=9)),
                ('over_odds', models.DecimalField(decimal_places=3, max_digits=9)),
                ('under', models.DecimalField(decimal_places=3, max_digits=9)),
                ('under_odds', models.DecimalField(decimal_places=3, max_digits=9)),
                ('o_u_edited', models.BooleanField(default=False)),
                ('spread_team1', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team1_odds', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team2', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team2_odds', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_edited', models.BooleanField(default=False)),
                ('payout_date', models.DateTimeField(default=datetime.datetime(2022, 7, 5, 7, 0, tzinfo=utc))),
                ('betting_league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matchups', to='Betting.bettingleague')),
                ('fantasy_matchup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='betting_matchups', to='Fantasy.matchup')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bet_matchup_away', to='Fantasy.fantasyteam')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bet_matchup_home', to='Fantasy.fantasyteam')),
            ],
        ),
        migrations.CreateModel(
            name='PlacedParlay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('betStatus', models.CharField(choices=[('O', 'Open'), ('W', 'Won'), ('L', 'Lost'), ('R', 'Refunded'), ('C', 'Cashed Out')], max_length=64)),
                ('line', models.DecimalField(decimal_places=4, max_digits=7)),
                ('payoutDate', models.DateTimeField()),
                ('bettor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Betting.bettor')),
            ],
        ),
        migrations.CreateModel(
            name='PlacedMatchupBet',
            fields=[
                ('betStatus', models.CharField(choices=[('O', 'Open'), ('W', 'Won'), ('L', 'Lost'), ('R', 'Refunded'), ('C', 'Cashed Out')], default='O', max_length=64)),
                ('line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('bet_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payout_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_placed', models.DateTimeField()),
                ('payout_date', models.DateTimeField()),
                ('id_placed', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bet_type', models.CharField(choices=[('O', 'Over'), ('U', 'Under'), ('MF', 'Favorite'), ('MD', 'Underdog'), ('SF', 'Favorite Spread'), ('SD', 'Underdog Spread')], max_length=20)),
                ('bet_value', models.DecimalField(decimal_places=3, max_digits=9)),
                ('bettor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Betting.bettor')),
                ('mathcup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Betting.matchupbets')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
