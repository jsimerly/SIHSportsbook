from django.db import models
from django.contrib.auth import get_user_model

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

    #Betting Related
    currentProj = models.DecimalField(decimal_places=3, max_digits=8, null=True)

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

    ppr = models.DecimalField(decimal_places=3, max_digits=8, )
    tePremium = models.DecimalField(decimal_places=3, max_digits=8, )

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

class FantasyTeam(models.Model):
    #Identity
    sleeperId = models.CharField(max_length=64, null=False, primary_key=True)
    rosterId = models.IntegerField(null=True)

    sleeperName = models.CharField(null=True, max_length=50)
    funName = models.CharField(null=True, max_length=30)

    userAccount = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    #Current Week
    currentProj = models.FloatField(null=True)
    currentMathcupId = models.IntegerField(null=True)

    #Season
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    fpts = models.IntegerField(default=0)

    #Betting Season
    spreadWin = models.IntegerField(default=0)
    spreadLoss = models.IntegerField(default=0)

    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(League, on_delete=models.PROTECT, default=0, null=False)

    
    #Functions
    def saveCurrentProj(self, proj):
        self.currentProj = round(proj, 3)
        self.save()



