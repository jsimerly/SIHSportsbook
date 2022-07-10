from pyexpat import model
from secrets import choice
from uuid import uuid4
import datetime
from django.forms import CharField
import pytz

from django.contrib.auth import get_user_model
from django.db import models




from Fantasy.models import FantasyLeague, FantasyTeam, Matchup

User = get_user_model()

# Create your models here.    
class BettingLeague(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)

    fantasy_league = models.ForeignKey(
        FantasyLeague,
        on_delete=models.CASCADE,
        related_name='betting_league',
    )

    std_vig = models.DecimalField(
        decimal_places=4, 
        max_digits=7, 
        default=0.0476
        )

    bookie = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        )

    weekly_allowance = models.DecimalField(decimal_places=2, max_digits=10, default=10)
    weekly_n_bets = models.IntegerField(default=10)

    bet_on_self = models.BooleanField(default=True)
    bet_on_opponent = models.BooleanField(default=False)

class Bettor(models.Model):
    id = models.UUIDField(
        default=uuid4, 
        primary_key=True, 
        unique=True, 
        editable=False
    )

    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    league = models.ForeignKey(
        BettingLeague, 
        on_delete=models.PROTECT,
        related_name="bettor"
    )

    team = models.ForeignKey(
        FantasyTeam, 
        on_delete=models.PROTECT,
    )

    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    allowance = models.DecimalField(decimal_places=2, max_digits=10, default=10)
    bets_left = models.IntegerField(default=2)

class MatchupBets(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    active = models.BooleanField(default=True)
    
    betting_league = models.ForeignKey(BettingLeague, on_delete=models.CASCADE, related_name='matchups')
    fantasy_matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE, related_name='betting_matchups')

    team1 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='bet_matchup_away')
    team2 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='bet_matchup_home')

    ml_team1 = models.DecimalField(decimal_places=3, max_digits=9,)
    ml_team2 = models.DecimalField(decimal_places=3, max_digits=9,)
    ml_edited = models.BooleanField(default=False)

    over = models.DecimalField(decimal_places=3, max_digits=9,)
    over_odds = models.DecimalField(decimal_places=3, max_digits=9,)
    under = models.DecimalField(decimal_places=3, max_digits=9,)
    under_odds= models.DecimalField(decimal_places=3, max_digits=9,)
    o_u_edited = models.BooleanField(default=False)

    spread_team1 = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team1_odds = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team2 = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team2_odds = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_edited = models.BooleanField(default=False)

    def next_tuesday_3AM():
        today = datetime.date.today()
        tuesday = today + datetime.timedelta((1-today.weekday())%7)
        tuesday_at_3_naive = datetime.datetime.combine(tuesday, datetime.time(hour=3))

        timezone = pytz.timezone('US/Eastern')
        tuesday_at_3 = timezone.localize(tuesday_at_3_naive)
        return tuesday_at_3

    payout_date = models.DateTimeField(default=next_tuesday_3AM())

class BasePlacedBet(models.Model):
    BET_STATUS_CHOCIES = (
        ('O', 'Open'),
        ('W', 'Won'),
        ('L', 'Lost'),
        ('R', 'Refunded'),
        ('C', 'Cashed Out')
    )
    betStatus = models.CharField(choices=BET_STATUS_CHOCIES, default= 'O',max_length=64)
    bettor = models.ForeignKey(Bettor, on_delete=models.CASCADE)

    line = models.DecimalField(decimal_places=3, max_digits=9,)

    bet_amount = models.DecimalField(decimal_places=2, max_digits=10,)
    payout_amount = models.DecimalField(decimal_places=2, max_digits=10,)

    time_placed = models.DateTimeField()
    payout_date = models.DateTimeField()

    parlayed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class PlacedBet(BasePlacedBet, models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    matchup_bet = models.ForeignKey(MatchupBets, on_delete=models.PROTECT, null=True)

    SUBTYPE_CHOICES = (
        ('FFM', 'Fantasy Football Matchup'),
    )

    subtype = models.CharField(choices=SUBTYPE_CHOICES, max_length=64)

    BET_TYPE_CHOICES = (
        #matchup options
        ('M_O', 'Over'), ('M_U', 'Under'),
        ('M_M1', 'Moneyline Team1'), ('M_M2', 'Moneyline Team2'),
        ('M_S1', 'Spread Team1'), ('M_S2', 'Spread Team2'),
    )
    bet_type = models.CharField(choices=BET_TYPE_CHOICES, max_length=20)  
    bet_value = models.DecimalField(decimal_places=3, max_digits=9,)        
    
     #Same as Parlay use the link below



# Need to work on parlays use this SO link: https://stackoverflow.com/questions/64026839/in-django-is-it-possible-to-have-a-foreign-key-defined-to-some-superclass-but
class PlacedParlay(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False)
    bettor = models.ForeignKey(Bettor, on_delete=models.CASCADE)

    BET_STATUS_CHOCIES = (
        ('O', 'Open'),
        ('W', 'Won'),
        ('L', 'Lost'),
        ('R', 'Refunded'),
        ('C', 'Cashed Out')
    )
    
    placed_bets = models.ManyToManyField(PlacedBet)
    betStatus = models.CharField(choices=BET_STATUS_CHOCIES, max_length=64, default='O')

    line = models.DecimalField(decimal_places=4, max_digits=7)
    wager = models.DecimalField(decimal_places=2, max_digits=10)
    payout_amount = models.DecimalField(decimal_places=2, max_digits=10,)

    payout_date = models.DateTimeField()






    



