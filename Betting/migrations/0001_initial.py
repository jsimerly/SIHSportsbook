# Generated by Django 4.0 on 2022-06-13 17:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '__first__'),
        ('Fantasy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BettingLeague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('std_vig', models.DecimalField(decimal_places=4, default=0.05, max_digits=7)),
                ('weekly_allowance', models.DecimalField(decimal_places=2, max_digits=10)),
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
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Betting.bettingleague')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Fantasy.fantasyteam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Account.user')),
            ],
        ),
        migrations.CreateModel(
            name='PlacedBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betStatus', models.CharField(choices=[('O', 'Open'), ('W', 'Won'), ('L', 'Lost'), ('R', 'Refunded'), ('C', 'Cashed Out')], max_length=64)),
                ('line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('bet_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payout_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time_placed', models.DateTimeField()),
                ('payout_date', models.DateTimeField()),
                ('bettor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Betting.bettor')),
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
            name='MatchupBets',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ml_team1', models.DecimalField(decimal_places=3, max_digits=9)),
                ('ml_team2', models.DecimalField(decimal_places=3, max_digits=9)),
                ('over', models.DecimalField(decimal_places=3, max_digits=9)),
                ('over_line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('under', models.DecimalField(decimal_places=3, max_digits=9)),
                ('under_line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team1', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team1_line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team2', models.DecimalField(decimal_places=3, max_digits=9)),
                ('spread_team2_line', models.DecimalField(decimal_places=3, max_digits=9)),
                ('fantasy_matchup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Fantasy.matchup')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bet_matchup_away', to='Fantasy.fantasyteam')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bet_matchup_home', to='Fantasy.fantasyteam')),
            ],
        ),
        migrations.CreateModel(
            name='PlacedMatchupBet',
            fields=[
                ('placedbet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Betting.placedbet')),
                ('id_placed', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('bet_type', models.CharField(choices=[('O', 'Over'), ('U', 'Under'), ('MF', 'Favorite'), ('MD', 'Underdog'), ('SF', 'Favorite Spread'), ('SD', 'Underdog Spread')], max_length=20)),
                ('bet_value', models.DecimalField(decimal_places=3, max_digits=9)),
                ('mathcup', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Betting.matchupbets')),
            ],
            bases=('Betting.placedbet',),
        ),
    ]
