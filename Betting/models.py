from uuid import uuid4
from django.contrib.auth import get_user_model
from django.db import models



from Fantasy.models import FantasyLeague, FantasyTeam, Matchup

User = get_user_model()

# Create your models here.    
class BettingLeague(models.Model):
    id = models.UUIDField(default=lambda: str(uuid4()), primary_key=True, unique=True, editable=False)

    fantasy_league = models.ForeignKey(
        FantasyLeague,
        on_delete=models.CASCADE,
        related_name='betting_league',
    )

    std_vig = models.DecimalField(
        decimal_places=4, 
        max_digits=7, 
        default=0.05
        )

    bookie = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        )

    weekly_allowance = models.DecimalField(decimal_places=2, max_digits=10)
    weekly_n_bets = models.IntegerField(default=10)

    bet_on_self = models.BooleanField(default=True)
    bet_on_opponent = models.BooleanField(default=False)

class Bettor(models.Model):
    id = models.UUIDField(default=lambda: str(uuid4()), primary_key=True, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    league = models.ForeignKey(BettingLeague, on_delete=models.PROTECT,)
    team = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT,)

    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    allowance = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    bets_left = models.IntegerField(default=10)

class MatchupBets(models.Model):
    id = models.UUIDField(default=lambda: str(uuid4()), primary_key=True, unique=True, editable=False)
    fantasy_matchup = models.ForeignKey(Matchup, on_delete=models.PROTECT)

    team1 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='bet_matchup_away')
    team2 = models.ForeignKey(FantasyTeam, on_delete=models.PROTECT, related_name='bet_matchup_home')

    ml_team1 = models.DecimalField(decimal_places=3, max_digits=9,)
    ml_team2 = models.DecimalField(decimal_places=3, max_digits=9,)

    over = models.DecimalField(decimal_places=3, max_digits=9,)
    over_line = models.DecimalField(decimal_places=3, max_digits=9,)
    under = models.DecimalField(decimal_places=3, max_digits=9,)
    under_line= models.DecimalField(decimal_places=3, max_digits=9,)

    spread_team1 = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team1_line = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team2 = models.DecimalField(decimal_places=3, max_digits=9,)
    spread_team2_line = models.DecimalField(decimal_places=3, max_digits=9,)

class PlacedBet(models.Model):
    BET_STATUS_CHOCIES = (
        ('O', 'Open'),
        ('W', 'Won'),
        ('L', 'Lost'),
        ('R', 'Refunded'),
        ('C', 'Cashed Out')
    )
    betStatus = models.CharField(choices=BET_STATUS_CHOCIES, max_length=64)
    bettor = models.ForeignKey(Bettor, on_delete=models.CASCADE)

    line = models.DecimalField(decimal_places=3, max_digits=9,)

    bet_amount = models.DecimalField(decimal_places=2, max_digits=10,)
    payout_amount = models.DecimalField(decimal_places=2, max_digits=10,)

    time_placed = models.DateTimeField()
    payout_date = models.DateTimeField()


class PlacedMatchupBet(PlacedBet):
    id_placed = models.UUIDField(default=lambda: str(uuid4()), primary_key=True, unique=True, editable=False)
    mathcup = models.ForeignKey(MatchupBets, on_delete=models.PROTECT)

    BET_TYPE_CHOICES = (
        ('O', 'Over'), ('U', 'Under'),
        ('MF', 'Favorite'), ('MD', 'Underdog'),
        ('SF', 'Favorite Spread'), ('SD', 'Underdog Spread'),
    )
    bet_type = models.CharField(choices=BET_TYPE_CHOICES, max_length=20)  
    bet_value = models.DecimalField(decimal_places=3, max_digits=9,)        
    
     #Same as Parlay use the link below



# Need to work on parlays use this SO link: https://stackoverflow.com/questions/64026839/in-django-is-it-possible-to-have-a-foreign-key-defined-to-some-superclass-but
class PlacedParlay(models.Model):
    id = models.UUIDField(default=lambda: str(uuid4()), primary_key=True, unique=True, editable=False)
    bettor = models.ForeignKey(Bettor, on_delete=models.CASCADE)

    BET_STATUS_CHOCIES = (
        ('O', 'Open'),
        ('W', 'Won'),
        ('L', 'Lost'),
        ('R', 'Refunded'),
        ('C', 'Cashed Out')
    )

    betStatus = models.CharField(choices=BET_STATUS_CHOCIES, max_length=64)
    line = models.DecimalField(decimal_places=4, max_digits=7)

    payoutDate = models.DateTimeField()






    



