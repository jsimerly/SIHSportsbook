from rest_framework import serializers

from Fantasy.models import FantasyTeam, FantasyLeague, Player, Matchup
from Betting.models import BettingLeague, MatchupBets


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
