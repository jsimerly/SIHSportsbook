from email.policy import default
from pickle import FALSE
from secrets import choice
from statistics import mode
from telnetlib import DET
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
    QB = 1
    RB = 2
    WR = 3
    TE = 4
    K = 5
    DST = 6

    POS_CHOICES = (
        (QB, 'Quarterback'),
        (RB, 'Runningback'),
        (WR, 'Wide Reciever'),
        (TE, 'Tight End'),
        (K, 'Kicker'),
        (DST, 'Defense and Special Teams')
    )

    BUF = 1
    MIA = 2
    NE = 3
    NYJ = 4

    BAL = 5
    CIN = 6
    CLE = 7
    PIT = 8

    HOU = 9
    IND = 10
    JAX = 11
    TEN = 12

    DEN = 13
    KC = 14
    LV = 15
    LAC = 16

    DAL = 17
    NYG = 18
    PHI = 19
    WAS = 20

    CHI = 21
    DET = 22
    GB = 23
    MIN = 24

    ATL = 25
    CAR = 26
    NO = 27
    TB = 28

    ARI = 29
    LAR = 30
    SF = 31
    SEA = 32

    FREE= 0

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
    pos = models.IntegerField(null=False, choices=POS_CHOICES)
    pos2 = models.IntegerField(null=True, choices=POS_CHOICES)

    nflTeam = models.IntegerField(null=True, choices=NFL_TEAM_CHOICES)
    age = models.IntegerField(null=True)

    #Betting
    currentProj = models.FloatField(null=True)

    #Functions
    def saveCurrentProj(self, proj):
        self.currentProj = round(proj, 3)
        self.save()

class League(models.Model):
    #Identity
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=FALSE, related_name='owner')
    sleeperId = models.IntegerField(null=False)
    name = models.CharField(null=True, max_length=256)

    #State
    status = models.IntegerField()

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

    STD = 0
    HALF = 1
    FULL = 2

    PPR_CHOICE = (
        (STD, 0),
        (HALF, 0.5),
        (FULL, 1),
    )
    TE_PREM_CHOICE = (
        (STD, 0),
        (HALF, 0.5),
        (FULL, 1),
    )
    ppr = models.IntegerField(default=FULL, choices=PPR_CHOICE)
    tePremium = models.IntegerField(default=STD, choices=TE_PREM_CHOICE)

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
    sleeperId = models.CharField(max_length=12, null=False, primary_key=True)
    sleeperName = models.CharField(null=False, max_length=50)
    funName = models.CharField(null=False, max_length=30)
    matchupId = models.IntegerField(null=True)

    userAccount = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    #Current Week
    currentProj = models.FloatField()
    currentMathcupId = models.IntegerField()

    #Season
    win = models.IntegerField(default=0)
    loss = models.IntegerField(default=0)
    tie = models.IntegerField(default=0)

    #Betting Season
    spreadWin = models.IntegerField(default=0)
    spreadLoss = models.IntegerField(default=0)

    #Team
    players = models.ManyToManyField(Player)
    league = models.ForeignKey(League, on_delete=models.PROTECT, default=0)

    
    #Functions
    def saveCurrentProj(self, proj):
        self.currentProj = round(proj, 3)
        self.save()



