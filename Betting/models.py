from turtle import undo
import django
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.db.models import Q
import decimal
import time
import numpy as np

from django.db import models

User = get_user_model()

# Create your models here. 
class NflState(models.Model):
    week = models.IntegerField()
    displayWeek = models.IntegerField()
    season = models.IntegerField()
    non_reg_week = models.IntegerField()
    lastPlayerUpdate = models.DateTimeField(null=True)

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
        (BUF, 'Buffalo Bills'),
        (MIA, 'Miami Dolphins'),
        (NE, 'New England Patriots'),
        (NYJ, 'New York Jets'),

        (BAL, 'Baltimore Ravens'),
        (CIN, 'Cincinnati Bengals'),
        (CLE, 'Cleveland Browns'),
        (PIT, 'Pittsburgh Steelers'),

        (HOU, 'Houston Texans'),
        (IND, 'Indianapolis Colts'),
        (JAX, 'Jacksonville Jaguars'),
        (TEN, 'Tennessee Titans'),

        (DEN, 'Denver Broncos'),
        (KC, 'Kansas City Chiefs'),
        (LV, 'Las Vegas Raiders'),
        (LAC, 'Los Angeles Chargers'),

        (DAL, 'Dallas Cowboys'),
        (NYG, 'New York Giants'),
        (PHI, 'Philadelphia Eagles'),
        (WAS, 'Washington Commanders'),

        (CHI, 'Chicago Bears'),
        (DET, 'Detriot Lions'),
        (GB, 'Green Bay Packers'),
        (MIN, 'Minnesota Vikings'),

        (ATL, 'Atlanta Falcons'),
        (CAR, 'Carolina Panthers'),
        (NO, 'New Orleans Saints'),
        (TB, 'Tamba Bay Buccaneers'),

        (ARI, 'Arizona Cardinals'),
        (LAR, 'Los Angeles Rams'),
        (SF, 'San Francisco 49ers'),
        (SEA, 'Seattle Seahawks'),

        (FREE, 'Free Agent'),
    )
    #Identity
    id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(null=False, max_length=80)

    #About
    pos = models.CharField(null=True, max_length=5, choices=POS_CHOICES)
    pos2 = models.CharField(null=True, max_length=5, choices=POS_CHOICES)

    nflTeam = models.CharField(null=True, max_length=64,choices=NFL_TEAM_CHOICES)
    age = models.IntegerField(null=True)

    estProj = models.DecimalField(decimal_places=3, max_digits=9, default=0)

    #Betting Related
    projPassingYds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projPassingTds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projInts = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    
    projRushingYds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projRushingTds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projFumbles = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    projRec = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projRecYds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projRecTds = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    projFg = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projXpt = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projKtotal = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    
    projSacks = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projDInts = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projFumbleRec = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projForcedFum = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projDTds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projSaftey = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projPA = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projYdsAgn = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    projDtotal = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    currentPassingYds = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentPassingTds = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentInts = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    
    currentRushingYds = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentRushingTds = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentFumbles = models.DecimalField(decimal_places=3, max_digits=8, null=True)

    currentRec = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentRecYds = models.DecimalField(decimal_places=3, max_digits=8, null=True)
    currentRecTds = models.DecimalField(decimal_places=3, max_digits=8, null=True)

    currentSacks = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentDInts = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentFumbleRec = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentForcedFum = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentDTds = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentSaftey = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentPA = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentYdsAgn = models.DecimalField(decimal_places=2, max_digits=8, default=0)
    currentDtotal = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    #Functions
    def saveCurrentProj(self, proj):
        self.currentProj = round(proj, 3)
        self.save()

class League(models.Model):
    #Identity
    sleeperId = models.IntegerField(primary_key=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name='owner')
    name = models.CharField(null=True, max_length=256)

    #State
    status = models.CharField(max_length=60)
    freeAgents = models.ManyToManyField(Player)
    standardVig = models.DecimalField(decimal_places=4, max_digits=7, default=0.075)

    #League Settings
    LEAGUE_SIZE_CHOICE = (
        (6,6),
        (8,8),
        (10,10),
        (12,12),
        (14,14),
        (16,16),
        (18,18),
        (20,20)
    )
    leagueSize = models.IntegerField(default=12, choices=LEAGUE_SIZE_CHOICE)

    PLAYOFF_SIZE_CHOICE = (
        (0,0),
        (2,2),
        (4,4),
        (6,6),
        (8,8),
        (10,10),
        (12,12),
        (14,14),
        (16,16),
        (18,18),
        (20,20),
    )
    playoffSize = models.IntegerField(default=4, choices=PLAYOFF_SIZE_CHOICE)

    #scoring settings
    pp_passing_yard = decimal.Decimal(.04) #can expand here later to be more league specific
    pp_Passing_td = 4
    pp_passing_int = -1
    pp_passing_2pt = 2

    pp_rushing_yard = decimal.Decimal(.1)
    pp_rushing_td = 6
    pp_rushing_2pt = 2
    
    ppr = models.DecimalField(decimal_places=3, max_digits=8, default=1)
    pp_rec_yard = decimal.Decimal(.1)
    pp_rec_td = 6
    pp_rec_2pt = 2

    rbPremium = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    wrPremium = models.DecimalField(decimal_places=3, max_digits=8, default=0)
    tePremium = models.DecimalField(decimal_places=3, max_digits=8, default=0)

    pp_fumble = -1
    pp_fumbleLost = -2

    pp_fg_0_19 = 3
    pp_fg_20_29 = 3
    pp_fg_30_39 = 3
    pp_fg_40_49= 4
    pp_fg_50_ = 5
    pp_pat_made = 1
    pp_pat_miss = -1

    pp_def_td = 6
    pp_def_sack = 1
    pp_def_int = 2
    pp_def_fumRec = 2
    pp_def_saftey = 2
    pp_def_forceFubme = 1
    pp_def_blockedKick = 2
    pp_pa_0 = 10
    pp_pa_6 = 7
    pp_pa_13 = 4
    pp_pa_20 = 1
    pp_pa_27 = 0
    pp_pa_34 = -1
    pp_pa_35_ = -4

    #Startable Roster
    nQB = models.IntegerField(default=1)
    nRB = models.IntegerField(default=2)
    nWR = models.IntegerField(default=2)
    nTE = models.IntegerField(default=1)
    nK = models.IntegerField(default=1)
    nDST = models.IntegerField(default=1)

    nFlexWrRbTe = models.IntegerField(default=1)
    nFlexWrRb = models.IntegerField(default=None)
    nFlexWrTe = models.IntegerField(default=None)
    nSuperFlex = models.IntegerField(default=1)

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

class Bettor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    betsLeft = models.IntegerField(default=2)

class FantasyTeam(models.Model):
    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(League, on_delete=models.PROTECT, default=0, null=False, related_name='FantasyTeam')

    #Identity
    sleeperId = models.CharField(max_length=64, null=False, primary_key=True)
    rosterId = models.IntegerField(null=True)

    sleeperName = models.CharField(null=True, max_length=50)
    funName = models.CharField(null=True, max_length=30)

    bettor = models.ForeignKey(Bettor, on_delete=models.PROTECT, null=True)

    #Current Week
    currentProj = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    currentMathcupId = models.IntegerField(null=True)

    #Season
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    fpts = models.IntegerField(default=0)

    #Betting Season
    spreadWin = models.IntegerField(default=0)
    spreadLoss = models.IntegerField(default=0)
    
class Matchup(models.Model):
    matchupId = models.IntegerField()
    week = models.IntegerField()
    season = models.IntegerField()

    team1 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='matchupTeam1')
    team2 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='matchupTeam2')

    t1_projection = models.DecimalField(decimal_places=3, max_digits=6)
    t2_projection = models.DecimalField(decimal_places=3, max_digits=6)

    t1_finalScore = models.DecimalField(decimal_places=3, max_digits=6, null=True, blank=True)
    t2_finalScore = models.DecimalField(decimal_places=3, max_digits=6, null=True, blank=True)

    over_under = models.DecimalField(decimal_places=3, max_digits=8)

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

class Bets(models.Model):
    bettor = models.ForeignKey(Bettor, on_delete=models.CASCADE)
    BET_STATUS_CHOCIES = (
        ('O', 'Open'),
        ('W', 'Won'),
        ('L', 'Lost'),
        ('R', 'Refunded'),
        ('C', 'Cashed Out')
    )
    betStatus = models.CharField(choices=BET_STATUS_CHOCIES, max_length=64)

    BET_TYPE_CHOICES = (
        ('ML', 'Moneyline'),
        ('OU', 'Over Under'),
        ('SP', 'Spread'),
    )
    betType = models.CharField(choices=BET_TYPE_CHOICES, max_length=64)
    betAmount = models.DecimalField(decimal_places=2, max_digits=10,)
    vig = models.DecimalField(decimal_places=4, max_digits=7)

    teamToWin = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='teamToWin')
    matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)




    



