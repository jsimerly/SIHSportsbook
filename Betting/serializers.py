from rest_framework import serializers

from Fantasy.models import FantasyTeam, FantasyLeague, Player, Matchup
from Betting.models import BettingLeague, MatchupBets, Bettor


class CreateBettingLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingLeague
        fields = (
            'fantasy_league', 'bookie',
        )

class FindBettingLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingLeague
        fields = (
            'pk',
        )

class BettorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Bettor
        fields = (
            'user', 'team', 'league'
        )

class MatchupBetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchupBets
        fields = (
            'fantasy_matchup', 'team1', 'team2', 
            'ml_team1', 'ml_team2',
            'over', 'over_odds', 'under', 'under_odds',
            'spread_team1', 'spread_team1_odds', 'spread_team2', 'spread_team2_odds'
        )

class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = ('fun_name', 'sleeper_name', 'id')