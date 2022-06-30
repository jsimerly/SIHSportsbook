from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q
from django.contrib.postgres.fields import ArrayField
from django.db import models
from decimal import Decimal
import time


User = get_user_model()

class NflState(models.Model):
    week = models.IntegerField()
    display_week = models.IntegerField()
    season = models.IntegerField()
    non_reg_week = models.IntegerField()
    last_player_update = models.DateTimeField(null=True)

    def updateLastPlayerDateTime(self):
        self.lastPlayerUpdate = timezone.now()
        self.save()

    def __str__(self):
        return f'Nfl State week: {self.week}'

class Player(models.Model):
    #Static
    QB = 'QB'
    RB = 'RB'
    WR = 'WR'
    TE = 'TE'
    K = 'K'
    DST = 'DEF'
    
    OL = 'OL'
    DL = 'DL'
    DT = 'DT'
    LB = 'LB'
    P = 'P'
    DB = 'DB'

    POS_CHOICES = (
        (QB, 'Quarterback'),
        (RB, 'Runningback'),
        (WR, 'Wide Reciever'),
        (TE, 'Tight End'),
        (K, 'Kicker'),
        (DST, 'Defense and Special Teams')
    )

    BUF = 'BUF'
    MIA = 'MIA'
    NE = 'NE'
    NYJ = 'NYJ'

    BAL = 'BAL'
    CIN = 'CIN'
    CLE = 'CLE'
    PIT = 'PIT'

    HOU = 'HOU'
    IND = 'IND'
    JAX = 'JAX'
    TEN = 'TEN'

    DEN = 'DEN'
    KC = 'KC'
    LV = 'LV'
    LAC = 'LAC'

    DAL = 'DAL'
    NYG = 'NYG'
    PHI = 'PHI'
    WAS = 'WAS'

    CHI = 'CHI'
    DET = 'DET'
    GB = 'GB'
    MIN = 'MIN'

    ATL = 'ATL'
    CAR = 'CAR'
    NO = 'NO'
    TB = 'TB'

    ARI = 'ARI'
    LAR = 'LAR'
    SF = 'SF'
    SEA = 'SEA'

    FREE = None

    NFL_TEAM_CHOICES = (
        (BUF, 'Buffalo Bills'),(MIA, 'Miami Dolphins'),(NE, 'New England Patriots'),(NYJ, 'New York Jets'),
        (BAL, 'Baltimore Ravens'),(CIN, 'Cincinnati Bengals'), (CLE, 'Cleveland Browns'),(PIT, 'Pittsburgh Steelers'),
        (HOU, 'Houston Texans'),(IND, 'Indianapolis Colts'),(JAX, 'Jacksonville Jaguars'),(TEN, 'Tennessee Titans'),
        (DEN, 'Denver Broncos'),(KC, 'Kansas City Chiefs'),(LV, 'Las Vegas Raiders'),(LAC, 'Los Angeles Chargers'),

        (DAL, 'Dallas Cowboys'),(NYG, 'New York Giants'),(PHI, 'Philadelphia Eagles'),(WAS, 'Washington Commanders'),
        (CHI, 'Chicago Bears'),(DET, 'Detriot Lions'),(GB, 'Green Bay Packers'),(MIN, 'Minnesota Vikings'),
        (ATL, 'Atlanta Falcons'),(CAR, 'Carolina Panthers'),(NO, 'New Orleans Saints'),(TB, 'Tamba Bay Buccaneers'),
        (ARI, 'Arizona Cardinals'),(LAR, 'Los Angeles Rams'),(SF, 'San Francisco 49ers'),(SEA, 'Seattle Seahawks'),

        (FREE, 'Free Agent'),
    )
    #Identity
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    sleeper_id = models.CharField(max_length=6, unique=True)
    name = models.CharField(null=False, max_length=80)

    #About
    pos = ArrayField(
        models.CharField(
            max_length=20, 
            blank=True, 
            choices=POS_CHOICES, 
            null=True),
        default=list,
        blank=True,
        null=True
        )
    nfl_team = models.CharField(
        null=True, 
        max_length=64,
        choices=NFL_TEAM_CHOICES
        )

    age = models.IntegerField(null=True)

    proj_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    current_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    def __str__(self):
        return f'Player Obj: {self.name} - {self.sleeper_id}'

class PlayerProjections(models.Model):
    player = models.OneToOneField(
        Player, 
        on_delete=models.CASCADE,
        related_name='proj',
        unique=True
        )

    total = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    fp_est = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    pass_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    pass_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    pass_ints = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    rush_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rush_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    rec_rec = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rec_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rec_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    fumbles = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    fg = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    xpt = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    k_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    def_sack = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_int = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_fum_rec = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_forced_fum = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_td = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_saftey = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_pa = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_yds_against = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    def __str__(self):
        return f'Player Proj Obj: {self.player}' 

class PlayerCurrentStats(models.Model):
    player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE,
        related_name='current'
        )

    total = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    pass_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    pass_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    pass_ints = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    rush_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rush_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    rec_rec = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rec_yds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    rec_tds = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    fumbles = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    fg = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    xpt = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    k_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    
    def_sack = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_int = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_fum_rec = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_forced_fum = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_td = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_saftey = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_pa = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_yds_against = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    def_total = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    def __str__(self):
        return f'Player Current Stats Obj: {self.player}'

def update_target_team_roster(team_json, team_obj):
    players = []
    print(team_json)
    for player_id in team_json:
        print(player_id)
        player_obj = Player.objects.get(sleeper_id=player_id)
        players.append(player_obj)

    team_obj.players.add(*players)
    return players

def create_unique_ranked_proj_map(player_qset, league_settings):
    proj_map = {}

    for player in player_qset:
        if Player.DST in player.pos:
            proj_map[player] = player.def_total
        elif Player.K in player.pos:
            proj_map[player] = player.k_total
        else:
            proj = 0

            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                continue

            proj += player.proj.pass_yds * league_settings.pass_yds
            proj += player.proj.pass_tds * league_settings.pass_tds
            proj += player.proj.pass_ints * league_settings.pass_ints
            
            proj += player.proj.rush_yds * league_settings.rush_yds
            proj += player.proj.rush_tds * league_settings.rush_tds

            proj += player.proj.rec_yds * league_settings.rec_yds

            if Player.RB in player.pos:
                proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_rb)
            elif Player.WR in player.pos:
                proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_wr)
            elif Player.TE in player.pos:
                proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_te)
            else:
                proj += player.proj.rec_rec * league_settings.ppr

            proj -= player.proj.fumbles * league_settings.fumble_lost

            proj_map[player] = round(proj, 3)
            
    proj_map = sorted(proj_map.items(), key=lambda x: x[1], reverse=True)
    return proj_map

def get_top_free_agent(pos, free_agents):
    if pos is not None:
        if pos == 'flex':
            free_agents = free_agents.filter(Q(pos__contains=[Player.RB]) | Q(pos__contains=[Player.WR]) | Q(pos__contains=[Player.TE]))
        else:
            free_agents = free_agents.filter(pos__contains=[pos])
            ## Go update leagues Free Agents

    top_free_agent = free_agents.order_by('proj_total')[0]
    return (top_free_agent, top_free_agent.proj_total)

def get_best_players(ranked_players_map, n, free_agents_list, pos=None, free_agent_function=get_top_free_agent):
    best_players = []
    for _ in range(n):
        if not ranked_players_map:
            top_free_agent = free_agent_function(pos, free_agents_list) #if you create new free agent functions, create **kwargs
        else:
            top_player = ranked_players_map[0]
            if top_player[1] <= Decimal(5):
                top_free_agent = free_agent_function(pos, free_agents_list)
                best_players.append(top_free_agent)
            else:
                ranked_players_map.pop(0)
                best_players.append(top_player)

    return best_players

def update_target_team_proj(team_obj, league):
    team_proj = Decimal(0)
    
    players_qset = team_obj.players.all()

    qb_qset = players_qset.filter(pos__contains=[Player.QB])
    rb_qset = players_qset.filter(pos__contains=[Player.RB])
    wr_qset = players_qset.filter(pos__contains=[Player.WR])
    te_qset = players_qset.filter(pos__contains=[Player.TE])
    k_qset = players_qset.filter(pos__contains=[Player.K])
    dst_qset = players_qset.filter(pos__contains=[Player.DST])

    ranked_qbs = create_unique_ranked_proj_map(qb_qset, league.scoring)
    ranked_rbs = create_unique_ranked_proj_map(rb_qset,league.scoring)
    ranked_wrs = create_unique_ranked_proj_map(wr_qset, league.scoring)
    ranked_tes = create_unique_ranked_proj_map(te_qset, league.scoring)
    ranked_ks = create_unique_ranked_proj_map(k_qset, league.scoring)
    ranked_dsts = create_unique_ranked_proj_map(dst_qset, league.scoring)

    starters = []

    starters.extend(get_best_players(ranked_qbs, league.settings.nQB, league.free_agents, Player.QB))
    starters.extend(get_best_players(ranked_rbs, league.settings.nRB, league.free_agents, Player.RB))
    starters.extend(get_best_players(ranked_wrs, league.settings.nWR, league.free_agents, Player.WR))
    starters.extend(get_best_players(ranked_tes, league.settings.nTE, league.free_agents, Player.TE))
    starters.extend(get_best_players(ranked_ks, league.settings.nK, league.free_agents, Player.K))
    starters.extend(get_best_players(ranked_dsts, league.settings.nDST, league.free_agents, Player.DST))

    flex_map = ranked_rbs + ranked_wrs + ranked_tes

    ranked_flex = sorted(flex_map, key=lambda x: x[1], reverse=True)
    starters.extend(get_best_players(ranked_flex, league.settings.n_flex_wr_rb_te, league.free_agents))
    #do this for wr/rb and wr/te

    super_flex_map = flex_map + ranked_qbs
    ranked_super_flex = sorted(super_flex_map, key=lambda x: x[1], reverse=True)
    starters.extend(get_best_players(ranked_super_flex, league.settings.n_super_flex, league.free_agents))

    for player in starters:
        team_proj += player[1]

    team_obj.current_proj = team_proj
    team_obj.save()
    return team_proj

def update_league_all_rosters(team_qset, roster_data_from_sleeper):
    t0 = time.time()

    non_fa_ids = []

    for team_json in roster_data_from_sleeper:
        team_obj = team_qset.get(roster_id = team_json['roster_id'])
        team_obj.players.clear()

        players = update_target_team_roster(team_json['players'], team_obj)
        for player in players:
            non_fa_ids.append(player.id)

    t1 = time.time()
    print(f'fantasy manager: update all rosters - runtime: {str(t1-t0)}')
    return non_fa_ids

def update_league_all_proj(league):
    t0 = time.time()
    team_qset = league.FantasyTeams.all()

    for team in team_qset:
        update_target_team_proj(team, league)

    t1 = time.time()
    print(f'fantasy manager: update all proj - runtime: {str(t1-t0)}')

class FantasyLeague(models.Model):
    #Identity
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    sleeper_id = models.CharField(max_length=20, null=False, unique=True)

    owner = models.ForeignKey(
        User, 
        on_delete=models.PROTECT, 
        null=False, 
        related_name='owner'
        )

    name = models.CharField(
        null=True, 
        max_length=256
        )

    #State
    status = models.CharField(max_length=60)
    free_agents = models.ManyToManyField(Player)

    def update_all_rosters(self, sleeper_data):
        non_free_agents = update_league_all_rosters(self.FantasyTeams.all(), sleeper_data)
        free_agents = Player.objects.all().exclude(id__in=non_free_agents)
        self.free_agents.set(free_agents)

    def update_all_proj(self):
        update_league_all_proj(self)

    def __str__(self):
        return f'League Obj: {self.name}'

class LeagueSettings(models.Model):
    league = models.OneToOneField(
        FantasyLeague, 
        on_delete=models.CASCADE,
        related_name='settings',
        )

    LEAGUE_SIZE_CHOICE = (
        (4,4), (6,6), (8,8), (10,10), (12,12), (14,14),
        (16,16), (18,18), (20,20), (22,22), (24,24),
        (26,26), (28,28), (30,30), (32,32),
    )
    PLAYOFF_SIZE_CHOICE = (
        (0,0), (2,2), (4,4), (6,6), (8,8), (10,10),
        (12,12), (14,14), (16,16), (18,18), (20,20),
    )
    
    league_size = models.IntegerField(default=12, choices=LEAGUE_SIZE_CHOICE)
    playoff_size = models.IntegerField(default=6, choices=PLAYOFF_SIZE_CHOICE)

    #Startable Roster
    nQB = models.IntegerField(default=1)
    nRB = models.IntegerField(default=2)
    nWR = models.IntegerField(default=2)
    nTE = models.IntegerField(default=1)
    nK = models.IntegerField(default=1)
    nDST = models.IntegerField(default=1)

    n_flex_wr_rb_te = models.IntegerField(default=1)
    n_flex_wr_rb = models.IntegerField(default=None)
    n_flex_wr_te = models.IntegerField(default=None)
    n_super_flex = models.IntegerField(default=1)
    n_bench = models.IntegerField(default=7)

    def __str__(self):
        return f'League Settings Obj: {self.league}'

class ScoringSettings(models.Model):
    league = models.OneToOneField(
        FantasyLeague, 
        on_delete=models.CASCADE,
        related_name='scoring'
        )

    pass_yds = models.DecimalField(decimal_places=3, max_digits=6, default=.04)
    pass_tds = models.DecimalField(decimal_places=3, max_digits=6, default=4)
    pass_ints = models.DecimalField(decimal_places=3, max_digits=6, default=-2)
    pass_2pts = models.DecimalField(decimal_places=3, max_digits=6, default=2)
    
    rush_yds = models.DecimalField(decimal_places=3, max_digits=6, default=.1)
    rush_tds = models.DecimalField(decimal_places=3, max_digits=6, default=6)
    rush_2pts = models.DecimalField(decimal_places=3, max_digits=6, default=2)

    ppr = models.DecimalField(decimal_places=3, max_digits=6, default=0) 
    rec_yds = models.DecimalField(decimal_places=3, max_digits=6, default=.1)
    rec_tds = models.DecimalField(decimal_places=3, max_digits=6, default=6)
    rec_2pts = models.DecimalField(decimal_places=3, max_digits=6, default=2)

    rec_prem_rb = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    rec_prem_wr = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    rec_prem_te = models.DecimalField(decimal_places=3, max_digits=6, default=0)

    fumble = models.DecimalField(decimal_places=3, max_digits=6, default=-1)
    fumble_lost = models.DecimalField(decimal_places=3, max_digits=6, default=-2)

    xp_miss = models.DecimalField(decimal_places=3, max_digits=6, default=-1)
    fg_miss = models.DecimalField(decimal_places=3, max_digits=6, default=-1)
    xp_made = models.DecimalField(decimal_places=3, max_digits=6, default=1)
    fg_0_19 = models.DecimalField(decimal_places=3, max_digits=6, default=3)
    fg_20_29 = models.DecimalField(decimal_places=3, max_digits=6, default=3)
    fg_30_39 = models.DecimalField(decimal_places=3, max_digits=6, default=3)
    fg_40_49 = models.DecimalField(decimal_places=3, max_digits=6, default=4)
    fg_50_plus = models.DecimalField(decimal_places=3, max_digits=6, default=5)

    def_td = models.DecimalField(decimal_places=3, max_digits=6,default=6)
    def_sack = models.DecimalField(decimal_places=3, max_digits=6, default=1)
    def_int = models.DecimalField(decimal_places=3, max_digits=6,default=2)
    def_fum_rec = models.DecimalField(decimal_places=3, max_digits=6, default=2)
    def_saftey = models.DecimalField(decimal_places=3, max_digits=6, default=2)
    def_forced_fum = models.DecimalField(decimal_places=3, max_digits=6, default=1)
    def_blocked_kick = models.DecimalField(decimal_places=3, max_digits=6, default=2)

    def_pa_0 = models.DecimalField(decimal_places=3, max_digits=6, default=10)
    def_pa_6 = models.DecimalField(decimal_places=3, max_digits=6, default=7)
    def_pa_13 = models.DecimalField(decimal_places=3, max_digits=6, default=4)
    def_pa_27 = models.DecimalField(decimal_places=3, max_digits=6, default=1)
    def_pa_34 = models.DecimalField(decimal_places=3, max_digits=6, default=0)
    def_pa_35_plus = models.DecimalField(decimal_places=3, max_digits=6, default=-1)

    def __str__(self):
        return f'League Scoring Obj: {self.league}'

class FantasyTeam(models.Model):
    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(FantasyLeague, on_delete=models.PROTECT, default=0, null=False, related_name='FantasyTeams')

    #Identity
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    owner_id = models.CharField(max_length=64, null=False)
    roster_id = models.IntegerField(null=True)

    sleeper_name = models.CharField(null=True, max_length=50)
    fun_name = models.CharField(null=True, max_length=30)

    #Current Week
    week_start_proj = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    current_proj = models.DecimalField(max_digits=7, decimal_places=3, null=True)

    current_point_total = models.DecimalField(max_digits=7, decimal_places=3, null=True)
    current_mathcup_id = models.IntegerField(null=True)

    #Season
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    fpts = models.IntegerField(default=0)

    #Betting Season
    spreadWin = models.IntegerField(default=0)
    spreadLoss = models.IntegerField(default=0)

    def update_roster(self, roster):
        update_target_team_roster(roster, self)

    def __str__(self):
        return f'Fantasy Team Obj: {self.fun_name}'

class Matchup(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    matchup_id = models.IntegerField()
    week = models.IntegerField()
    season = models.IntegerField()

    active = models.BooleanField(default=True)

    league = models.ForeignKey(
        FantasyLeague, 
        on_delete=models.PROTECT, 
        null=True
        )

    team1 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='matchup_away')
    team2 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='matchup_home')

    def __str__(self):
        return f'Matchup Obj: {self.league} - {self.week}.{self.matchup_id} {self.season}'