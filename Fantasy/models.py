from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q
from django.contrib.postgres.fields import ArrayField
from django.db import models
import decimal
import time
import numpy as np

from django.db import models

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
    sleeper_id = models.CharField(max_length=6)
    name = models.CharField(null=False, max_length=80)

    #About
    pos = ArrayField(
        models.CharField(max_length=20, blank=True, choices=POS_CHOICES),
        default=list,
        blank=True
        )
    nfl_team = models.CharField(
        null=True, 
        max_length=64,
        choices=NFL_TEAM_CHOICES
        )

    age = models.IntegerField(null=True)

class PlayerProjections(models.Model):
    player = models.ForeignKey(
        Player, 
        on_delete=models.CASCADE,
        related_name='proj'
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

class FantasyLeague(models.Model):
    #Identity
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    sleeper_id = models.IntegerField(null=False)

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

    #used to update all of the rosters in a league
    def updateRosters(self,rosterData):
        t0 = time.time()

        #get all teams in League instance
        teamObjs = self.FantasyTeams.all()
        nonFAs = [] #used to keep track of players that are on a team

        #loop through the rosterData obtained from sleeper
        for teamJson in rosterData:
            teamObj = teamObjs.get(rosterId = teamJson['roster_id']) #get FantasyTeam object assocaited with rosterId on sleeper
            teamObj.players.clear() #clear all teams players-fantasyTeam relationships before we add new ones

            #loop through all players from sleepers Json response and find their associate objects
            players = [] 
            for playerId in teamJson['players']:
                playerObj = Player.objects.get(pk=playerId)
                players.append(playerObj)
                nonFAs.append(playerObj)

            #add the many to many relationship back
            teamObj.players.add(*players)

        #set all players to FA then remove the players who are not taken
        self.freeAgents.set(Player.objects.all()) #this takes .5sec to make quicker might need to record changes rather than reupdate all Players
        self.freeAgents.remove(*nonFAs)

        t1 = time.time()
        print(f'models.League.updateRosters runtime: {str(t1-t0)}')

    #playerQset finds a teams players at a specific position
    def _mapPlayerProj(self, playerQset): 
            projMap = {}
            #loop through player set to parse data and calculate a score based on the league settings
            for player in playerQset:
                #not currently doing calculations for def scoring differencess
                if player.pos == Player.DST:
                    projMap[player] = player.projDtotal
                #not currently doing calcs for k
                elif player.pos == Player.K:
                    projMap[player] = player.projKtotal
                else:
                    proj = 0
                    #passing calculations
                    proj += player.projPassingYds * self.pp_passing_yard
                    proj += player.projPassingTds * self.pp_Passing_td
                    proj += player.projInts * self.pp_passing_int
                    #rushing calculations
                    proj += player.projRushingYds * self.pp_rushing_yard
                    proj += player.projRushingTds * self.pp_rushing_td
                    proj += player.projFumbles * self.pp_rushing_2pt
                    #rec calculations
                    proj += player.projRec * self.ppr
                    proj += player.projRecYds * self.pp_rec_yard
                    proj += player.projRecTds * self.pp_rec_td

                    #round and store in a dict {PlayerObject : calcultedProjection}
                    projMap[player] = round(proj, 3)
                    
            #sort the dict so that we can grab the [0] item in the array as the highest scorer
            projMap = sorted(projMap.items(), key=lambda x: x[1], reverse=True)
            return projMap

    #used to find the best free agent avaliable if a team doesn't meet the treshhold requirements
    def _getTopFreeAgent(self, pos):
        #This will just grab the best overall player
        if pos is None:
            freeAgents = self.freeAgents.all()
        elif pos == 'flex':
            #Grab a all freeAgents who are either RB, WR, OR TE
            freeAgents = self.freeAgents.filter(Q(pos=Player.RB) | Q(pos=Player.WR) | Q(pos=Player.TE))
        else:
            freeAgents = self.freeAgents.filter(pos=pos)
        #get to top freeAgent, save their proj, and return a tuple
        topFreeAgent = freeAgents.order_by('-estProj')[0]
        topFreeAgentTup = (topFreeAgent, topFreeAgent.estProj)
        return topFreeAgentTup

    #returns the player with the highest projection or finds the best Free Agent if they have no players to start
    def _getTopPlayers(self, qSet, n, pos=None):
        playerList = []
        #n is the number of this position that they start, this runs that many times
        for _ in range(n):
            try:
                #find highest scoring player
                topPlayer = qSet[0]
                #if player is projected no point get a free agent
                if topPlayer[1] == decimal.Decimal(0):
                    topFa = self._getTopFreeAgent(pos=pos)
                    playerList.append(topFa)
                else:
                    #remove player from list so they're not reused in team projections
                    qSet.pop(0)
                    playerList.append(topPlayer)
            #most likely error thrown is an empty list 'index out of range', this happens because don't have anyone at the positions
            except Exception as e:
                topFa = self._getTopFreeAgent(pos=pos)
                playerList.append(topFa)

        #return list of tuples (PlayerObj, Projection)
        return playerList

    #called to update all teams projections 
    def updateTeamProjections(self):
        t0 = time.time()
        teams = self.FantasyTeams.all()

        #run through all of the teams to make updates
        for team in teams:
            print(team.funName)
            currentProj = decimal.Decimal(0) #use Decimal so the type are the same
            #get all of the player on the team
            teamQbs = team.players.filter(pos=Player.QB)
            teamRbs = team.players.filter(pos=Player.RB)
            teamWrs = team.players.filter(pos=Player.WR)
            teamTes = team.players.filter(pos=Player.TE)
            teamKs = team.players.filter(pos=Player.K)
            teamDst = team.players.filter(pos=Player.DST)
            #get players that can play multiple positions. This is not currently in use
            teamQBs2 = team.players.filter(pos2=Player.QB)
            teamRbs2 = team.players.filter(pos2=Player.RB)
            teamWrs2 = team.players.filter(pos2=Player.WR)
            teamTes2 = team.players.filter(pos2=Player.TE)
            #get all of the players projections
            qbs = self._mapPlayerProj(teamQbs)
            rbs = self._mapPlayerProj(teamRbs)
            wrs = self._mapPlayerProj(teamWrs)
            tes = self._mapPlayerProj(teamTes)
            k = self._mapPlayerProj(teamKs)
            dst = self._mapPlayerProj(teamDst)

            starters = []
            #find all of the players who would be in a starting line up
            #Standard Slots
            starters.extend(self._getTopPlayers(qbs, self.nQB, Player.QB))
            starters.extend(self._getTopPlayers(rbs, self.nRB, Player.RB))
            starters.extend(self._getTopPlayers(wrs, self.nWR, Player.WR))
            starters.extend(self._getTopPlayers(tes, self.nTE, Player.TE))
            starters.extend(self._getTopPlayers(k, self.nK, Player.K))
            starters.extend(self._getTopPlayers(dst, self.nDST, Player.DST))
            #Flex and misc
            flex = rbs + wrs + tes
            starters.extend(self._getTopPlayers(flex, self.nFlexWrRbTe, pos='flex'))
            #Super Flex
            superFlex = flex + qbs
            starters.extend(self._getTopPlayers(superFlex, self.nSuperFlex,))

            #update the proj based on assumed starting lineup
            for playerTup in starters:
                currentProj += playerTup[1]

            #set teams currentProj
            team.currentProj = currentProj
            print(currentProj)
            team.save()
          
        t1 = time.time()
        runtime = t1-t0
        print(f'models.League.updateTeamProjections runtime: {runtime}')

class LeagueSettings(models.Model):
    league = models.ForeignKey(
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
    playoff_oize = models.IntegerField(default=6, choices=PLAYOFF_SIZE_CHOICE)

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

class ScoringSettings(models.Model):
    league_settings = models.ForeignKey(
        LeagueSettings, 
        on_delete=models.CASCADE,
        related_name='scoring'
        )

    passing_yard = models.DecimalField(decimal_places=3, max_digits=6,)
    passing_td = models.DecimalField(decimal_places=3, max_digits=6,)
    passing_int = models.DecimalField(decimal_places=3, max_digits=6,)
    passing_2pt = models.DecimalField(decimal_places=3, max_digits=6,)
    
    rushing_yard = models.DecimalField(decimal_places=3, max_digits=6,)
    rushing_td = models.DecimalField(decimal_places=3, max_digits=6,)
    rushing_2pt = models.DecimalField(decimal_places=3, max_digits=6,)

    ppr = models.DecimalField(decimal_places=3, max_digits=6,) 
    rec_yard = models.DecimalField(decimal_places=3, max_digits=6,)
    rec_td = models.DecimalField(decimal_places=3, max_digits=6,)
    rec_2pt = models.DecimalField(decimal_places=3, max_digits=6,)

    rec_prem_rb = models.DecimalField(decimal_places=3, max_digits=6,)
    rec_prem_wr = models.DecimalField(decimal_places=3, max_digits=6,)
    rec_prem_te = models.DecimalField(decimal_places=3, max_digits=6,)

    fumble = models.DecimalField(decimal_places=3, max_digits=6,)
    fumble_lost = models.DecimalField(decimal_places=3, max_digits=6,)

    fg_0_19 = models.DecimalField(decimal_places=3, max_digits=6,)
    fg_20_29 = models.DecimalField(decimal_places=3, max_digits=6,)
    fg_30_39 = models.DecimalField(decimal_places=3, max_digits=6,)
    fg_40_49 = models.DecimalField(decimal_places=3, max_digits=6,)
    fg_50_plus = models.DecimalField(decimal_places=3, max_digits=6,)

    def_td = models.DecimalField(decimal_places=3, max_digits=6,)
    def_sack = models.DecimalField(decimal_places=3, max_digits=6,)
    def_int = models.DecimalField(decimal_places=3, max_digits=6,)
    def_fum_rec = models.DecimalField(decimal_places=3, max_digits=6,)
    def_saftey = models.DecimalField(decimal_places=3, max_digits=6,)
    def_forced_fum = models.DecimalField(decimal_places=3, max_digits=6,)
    def_blocked_kick = models.DecimalField(decimal_places=3, max_digits=6,)

    def_pa_0 = models.DecimalField(decimal_places=3, max_digits=6,)
    def_pa_6 = models.DecimalField(decimal_places=3, max_digits=6,)
    def_pa_13 = models.DecimalField(decimal_places=3, max_digits=6,)
    def_pa_27 = models.DecimalField(decimal_places=3, max_digits=6,)
    def_pa_34 = models.DecimalField(decimal_places=3, max_digits=6,)
    def_pa_35_plus = models.DecimalField(decimal_places=3, max_digits=6,)

class FantasyTeam(models.Model):
    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(FantasyLeague, on_delete=models.PROTECT, default=0, null=False, related_name='FantasyTeams')

    #Identity
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    ownerId = models.CharField(max_length=64, null=False)
    rosterId = models.IntegerField(null=True)

    sleeperName = models.CharField(null=True, max_length=50)
    funName = models.CharField(null=True, max_length=30)

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
    
    over_under = models.DecimalField(decimal_places=3, max_digits=7)

    t1_SP = models.DecimalField(decimal_places=3, max_digits=8)
    t2_SP = models.DecimalField(decimal_places=3, max_digits=8)

    t1_ML = models.DecimalField(decimal_places=3, max_digits=8)
    t2_ML = models.DecimalField(decimal_places=3, max_digits=8)

    vig = models.DecimalField(decimal_places=4, max_digits=7)
    standardLine = models.DecimalField(decimal_places=4, max_digits=7)

    payoutDate = models.DateTimeField(null=True)

    def setLines(self):
        MAX_SPREAD = .40
        vig = self.vig
        #over under
        self.over_under = abs(self.t1_projection + self.t2_projection)
        #spread
        self.t1_SP = -(self.t1_projection - self.t2_projection)
        self.t2_SP = -(self.t2_projection - self.t1_projection)
        #money line
        spread = abs(self.t1_SP)
        percentSpread = (1/1.75)*np.log(spread*.0175+1)

        if percentSpread > MAX_SPREAD:
            percentSpread = MAX_SPREAD

        favOdds = .5 + percentSpread
        undOdds = 1 - percentSpread
        favOdds += vig/2
        undOdds += vig/2

        favML = (-1*favOdds/(1-favOdds)*100)
        if undOdds < .5:
            undML = ((1-undOdds)/undOdds)*100
        else:
            undML = (-1*undOdds/(1-undOdds)*100)

        if self.t1_projection > self.t2_projection:
            self.t1_ML = favML
            self.t2_ML = undML
        elif self.t2_projection > self.t1_projection:
            self.t2_ML = favML
            self.t1_ML = undML
        else:
            self.t1_ML = -(100+vig/2)
            self.t2_ML = -(100+vig/2)

        self.save()