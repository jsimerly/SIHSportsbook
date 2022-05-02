from re import M
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Max
import decimal
import time

User = get_user_model()

# Create your models here. 
class NflState(models.Model):
    week = models.IntegerField()
    displayWeek = models.IntegerField()
    season = models.IntegerField()

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
    ### NEED AN UPDATE ROSTERS METHOD BEFORE FINISHING PROJECTIONS


    #Identity
    sleeperId = models.IntegerField(primary_key=True, null=False)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=False, related_name='owner')
    name = models.CharField(null=True, max_length=256)

    #State
    status = models.CharField(max_length=60)
    freeAgents = models.ManyToManyField(Player)

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

    def _mapPlayerProj(self, playerQset):
            projMap = {}

            for player in playerQset:
                if player.pos == Player.DST:
                    projMap[player] = player.projDtotal
                elif player.pos == Player.K:
                    projMap[player] = player.projKtotal
                else:
                    proj = 0

                    proj += player.projPassingYds * self.pp_passing_yard
                    proj += player.projPassingTds * self.pp_Passing_td
                    proj += player.projInts * self.pp_passing_int

                    proj += player.projRushingYds * self.pp_rushing_yard
                    proj += player.projRushingTds * self.pp_rushing_td
                    proj += player.projFumbles * self.pp_rushing_2pt

                    proj += player.projRec * self.ppr
                    proj += player.projRecYds * self.pp_rec_yard
                    proj += player.projRecTds * self.pp_rec_td

                    projMap[player] = round(proj, 3)
                    
            projMap = sorted(projMap.items(), key=lambda x: x[1], reverse=True)
            return projMap

    def _getTopFreeAgent(self, pos):
        leagueFreeAgents = self.FantasyTeams.all()
        print(leagueFreeAgents)


    def _getTopPlayers(self, set, n, pos):
        playerList = []
        for _ in range(n):
            try:
                top = set[0][0]
                set.pop(0)
                if top.estProj != 0:
                    playerList.append(top)
                else:
                    topFA = self._getTopFreeAgent(pos)
                    playerList.append(topFA)
            except Exception as e:
                print(e)
                topFA = self._getTopFreeAgent(pos)
                playerList.append(topFA)

        return playerList

    def updateTeamProjections(self):
        t0 = time.time()
        teams = self.FantasyTeams.all()

        for team in teams:
            currentProj = decimal.Decimal(0)

            teamQbs = team.players.filter(pos=Player.QB)
            teamRbs = team.players.filter(pos=Player.RB)
            teamWrs = team.players.filter(pos=Player.WR)
            teamTes = team.players.filter(pos=Player.TE)
            teamKs = team.players.filter(pos=Player.K)
            teamDst = team.players.filter(pos=Player.DST)

            teamQBs2 = team.players.filter(pos2=Player.QB)
            teamRbs2 = team.players.filter(pos2=Player.RB)
            teamWrs2 = team.players.filter(pos2=Player.WR)
            teamTes2 = team.players.filter(pos2=Player.TE)

            qbs = self._mapPlayerProj(teamQbs)
            rbs = self._mapPlayerProj(teamRbs)
            wrs = self._mapPlayerProj(teamWrs)
            tes = self._mapPlayerProj(teamTes)
            k = self._mapPlayerProj(teamKs)
            dst = self._mapPlayerProj(teamDst)

            starters = []

            starters.extend(self._getTopPlayers(qbs, self.nQB, Player.QB))
            starters.extend(self._getTopPlayers(rbs, self.nRB, Player.RB))
            starters.extend(self._getTopPlayers(wrs, self.nWR, Player.WR))
            starters.extend(self._getTopPlayers(tes, self.nTE, Player.TE))
            starters.extend(self._getTopPlayers(k, self.nK, Player.K))
            starters.extend(self._getTopPlayers(dst, self.nDST, Player.DST))
                    
            print(team.funName)
            print(starters)
            print(currentProj)


        t1 = time.time()
        runtime = t1-t0
        print(f'Runtime for updateTeamProjections: {runtime}')

class FantasyTeam(models.Model):
    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(League, on_delete=models.PROTECT, default=0, null=False, related_name='FantasyTeams')

    #Identity
    sleeperId = models.CharField(max_length=64, null=False, primary_key=True)
    rosterId = models.IntegerField(null=True)

    sleeperName = models.CharField(null=True, max_length=50)
    funName = models.CharField(null=True, max_length=30)

    userAccount = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

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
    
    



