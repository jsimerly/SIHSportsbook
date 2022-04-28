# Generated by Django 4.0 on 2022-04-26 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '0002_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='NflState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('displayWeek', models.IntegerField()),
                ('season', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80)),
                ('pos', models.IntegerField(choices=[(1, 'Quarterback'), (2, 'Runningback'), (3, 'Wide Reciever'), (4, 'Tight End'), (5, 'Kicker'), (6, 'Defense and Special Teams')])),
                ('pos2', models.IntegerField(choices=[(1, 'Quarterback'), (2, 'Runningback'), (3, 'Wide Reciever'), (4, 'Tight End'), (5, 'Kicker'), (6, 'Defense and Special Teams')], null=True)),
                ('nflTeam', models.IntegerField(choices=[(1, 'Buffalo Bills'), (2, 'Miami Dolphins'), (3, 'New England Patriots'), (4, 'New York Jets'), (5, 'Baltimore Ravens'), (6, 'Cincinnati Bengals'), (7, 'Cleveland Browns'), (8, 'Pittsburgh Steelers'), (9, 'Houston Texans'), (10, 'Indianapolis Colts'), (11, 'Jacksonville Jaguars'), (12, 'Tennessee Titans'), (13, 'Denver Broncos'), (14, 'Kansas City Chiefs'), (15, 'Las Vegas Raiders'), (16, 'Los Angeles Chargers'), (17, 'Dallas Cowboys'), (18, 'New York Giants'), (19, 'Philadelphia Eagles'), (20, 'Washington Commanders'), (21, 'Chicago Bears'), (22, 'Detriot Lions'), (23, 'Green Bay Packers'), (24, 'Minnesota Vikings'), (25, 'Atlanta Falcons'), (26, 'Carolina Panthers'), (27, 'New Orleans Saints'), (28, 'Tamba Bay Buccaneers'), (29, 'Arizona Cardinals'), (30, 'Los Angeles Rams'), (31, 'San Francisco 49ers'), (32, 'Seattle Seahawks'), (0, 'Free Agent')], null=True)),
                ('age', models.IntegerField(null=True)),
                ('currentProj', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('sleeperId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, null=True)),
                ('status', models.IntegerField()),
                ('leagueSize', models.IntegerField(choices=[(6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)], default=12)),
                ('playoffSize', models.IntegerField(choices=[(0, 0), (2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)], default=4)),
                ('ppr', models.IntegerField(choices=[(0, 0), (1, 0.5), (2, 1)], default=2)),
                ('tePremium', models.IntegerField(choices=[(0, 0), (1, 0.5), (2, 1)], default=0)),
                ('nQB', models.IntegerField(default=1)),
                ('nRB', models.IntegerField(default=2)),
                ('nWR', models.IntegerField(default=2)),
                ('nTE', models.IntegerField(default=1)),
                ('nK', models.IntegerField(default=1)),
                ('nDST', models.IntegerField(default=1)),
                ('nFlexWrRbTe', models.IntegerField(default=1)),
                ('nFlexWrRb', models.IntegerField(default=None)),
                ('nFlexWrTe', models.IntegerField(default=None)),
                ('nSuperFlex', models.IntegerField(default=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='Account.user')),
            ],
        ),
        migrations.CreateModel(
            name='FantasyTeam',
            fields=[
                ('sleeperId', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('sleeperName', models.CharField(max_length=50)),
                ('funName', models.CharField(max_length=30)),
                ('matchupId', models.IntegerField(null=True)),
                ('currentProj', models.FloatField()),
                ('currentMathcupId', models.IntegerField()),
                ('win', models.IntegerField(default=0)),
                ('loss', models.IntegerField(default=0)),
                ('tie', models.IntegerField(default=0)),
                ('spreadWin', models.IntegerField(default=0)),
                ('spreadLoss', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='Betting.league')),
                ('players', models.ManyToManyField(to='Betting.Player')),
                ('userAccount', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Account.user')),
            ],
        ),
    ]
