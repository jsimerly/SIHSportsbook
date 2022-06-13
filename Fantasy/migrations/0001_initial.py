# Generated by Django 4.0 on 2022-06-06 21:37

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Account', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FantasyLeague',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sleeper_id', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=256, null=True)),
                ('status', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='FantasyTeam',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner_id', models.CharField(max_length=64)),
                ('roster_id', models.IntegerField(null=True)),
                ('sleeper_name', models.CharField(max_length=50, null=True)),
                ('fun_name', models.CharField(max_length=30, null=True)),
                ('week_start_proj', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('current_proj', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('current_point_total', models.DecimalField(decimal_places=3, max_digits=7, null=True)),
                ('current_mathcup_id', models.IntegerField(null=True)),
                ('wins', models.IntegerField(default=0)),
                ('losses', models.IntegerField(default=0)),
                ('ties', models.IntegerField(default=0)),
                ('fpts', models.IntegerField(default=0)),
                ('spreadWin', models.IntegerField(default=0)),
                ('spreadLoss', models.IntegerField(default=0)),
                ('league', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='FantasyTeams', to='Fantasy.fantasyleague')),
            ],
        ),
        migrations.CreateModel(
            name='NflState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('display_week', models.IntegerField()),
                ('season', models.IntegerField()),
                ('non_reg_week', models.IntegerField()),
                ('last_player_update', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('sleeper_id', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=80)),
                ('pos', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[('QB', 'Quarterback'), ('RB', 'Runningback'), ('WR', 'Wide Reciever'), ('TE', 'Tight End'), ('K', 'Kicker'), ('DEF', 'Defense and Special Teams')], max_length=20, null=True), blank=True, default=list, null=True, size=None)),
                ('nfl_team', models.CharField(choices=[('BUF', 'Buffalo Bills'), ('MIA', 'Miami Dolphins'), ('NE', 'New England Patriots'), ('NYJ', 'New York Jets'), ('BAL', 'Baltimore Ravens'), ('CIN', 'Cincinnati Bengals'), ('CLE', 'Cleveland Browns'), ('PIT', 'Pittsburgh Steelers'), ('HOU', 'Houston Texans'), ('IND', 'Indianapolis Colts'), ('JAX', 'Jacksonville Jaguars'), ('TEN', 'Tennessee Titans'), ('DEN', 'Denver Broncos'), ('KC', 'Kansas City Chiefs'), ('LV', 'Las Vegas Raiders'), ('LAC', 'Los Angeles Chargers'), ('DAL', 'Dallas Cowboys'), ('NYG', 'New York Giants'), ('PHI', 'Philadelphia Eagles'), ('WAS', 'Washington Commanders'), ('CHI', 'Chicago Bears'), ('DET', 'Detriot Lions'), ('GB', 'Green Bay Packers'), ('MIN', 'Minnesota Vikings'), ('ATL', 'Atlanta Falcons'), ('CAR', 'Carolina Panthers'), ('NO', 'New Orleans Saints'), ('TB', 'Tamba Bay Buccaneers'), ('ARI', 'Arizona Cardinals'), ('LAR', 'Los Angeles Rams'), ('SF', 'San Francisco 49ers'), ('SEA', 'Seattle Seahawks'), (None, 'Free Agent')], max_length=64, null=True)),
                ('age', models.IntegerField(null=True)),
                ('proj_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('current_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='ScoringSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_yds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pass_tds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pass_ints', models.DecimalField(decimal_places=3, max_digits=6)),
                ('pass_2pts', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rush_yds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rush_tds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rush_2pts', models.DecimalField(decimal_places=3, max_digits=6)),
                ('ppr', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_yds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_tds', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_2pts', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_prem_rb', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_prem_wr', models.DecimalField(decimal_places=3, max_digits=6)),
                ('rec_prem_te', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fumble', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fumble_lost', models.DecimalField(decimal_places=3, max_digits=6)),
                ('xp_miss', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_miss', models.DecimalField(decimal_places=3, max_digits=6)),
                ('xp_made', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_0_19', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_20_29', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_30_39', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_40_49', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fg_50_plus', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_td', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_sack', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_int', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_fum_rec', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_saftey', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_forced_fum', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_blocked_kick', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_0', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_6', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_13', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_27', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_34', models.DecimalField(decimal_places=3, max_digits=6)),
                ('def_pa_35_plus', models.DecimalField(decimal_places=3, max_digits=6)),
                ('league', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='scoring', to='Fantasy.fantasyleague')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerProjections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_ints', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rush_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rush_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_rec', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('fumbles', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('fg', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('xpt', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('k_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_sack', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_int', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_fum_rec', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_forced_fum', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_td', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_saftey', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_pa', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_yds_against', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proj', to='Fantasy.player')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerCurrentStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('pass_ints', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rush_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rush_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_rec', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_yds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('rec_tds', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('fumbles', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('fg', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('xpt', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('k_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_sack', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_int', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_fum_rec', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_forced_fum', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_td', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_saftey', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_pa', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_yds_against', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('def_total', models.DecimalField(decimal_places=3, default=0, max_digits=8)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current', to='Fantasy.player')),
            ],
        ),
        migrations.CreateModel(
            name='Matchup',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('matchup_id', models.IntegerField()),
                ('week', models.IntegerField()),
                ('season', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('league', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Fantasy.fantasyleague')),
                ('team1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matchup_away', to='Fantasy.fantasyteam')),
                ('team2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='matchup_home', to='Fantasy.fantasyteam')),
            ],
        ),
        migrations.CreateModel(
            name='LeagueSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('league_size', models.IntegerField(choices=[(4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32)], default=12)),
                ('playoff_size', models.IntegerField(choices=[(0, 0), (2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20)], default=6)),
                ('nQB', models.IntegerField(default=1)),
                ('nRB', models.IntegerField(default=2)),
                ('nWR', models.IntegerField(default=2)),
                ('nTE', models.IntegerField(default=1)),
                ('nK', models.IntegerField(default=1)),
                ('nDST', models.IntegerField(default=1)),
                ('n_flex_wr_rb_te', models.IntegerField(default=1)),
                ('n_flex_wr_rb', models.IntegerField(default=None)),
                ('n_flex_wr_te', models.IntegerField(default=None)),
                ('n_super_flex', models.IntegerField(default=1)),
                ('n_bench', models.IntegerField(default=7)),
                ('league', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='Fantasy.fantasyleague')),
            ],
        ),
        migrations.AddField(
            model_name='fantasyteam',
            name='players',
            field=models.ManyToManyField(to='Fantasy.Player'),
        ),
        migrations.AddField(
            model_name='fantasyleague',
            name='free_agents',
            field=models.ManyToManyField(to='Fantasy.Player'),
        ),
        migrations.AddField(
            model_name='fantasyleague',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owner', to='Account.user'),
        ),
    ]