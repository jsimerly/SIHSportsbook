from rest_framework import serializers

from Fantasy.models import FantasyTeam, FantasyLeague, Player, Matchup
from Betting.models import BettingLeague, MatchupBets, Bettor


class BettingLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BettingLeague
        fields = (
            'fantasy_league', 'bookie',
        )

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchupBets
        fields = (
            'bettor', 'betType', 'betAmount', 'teamToWin', 'matchup'
        )

class BettorSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Bettor
        fields = (
            'user', 'team', 'league'
        )