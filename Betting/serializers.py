from rest_framework import serializers

from Fantasy.models import FantasyTeam, FantasyLeague, Player, Matchup
from Betting.models import MatchupBets


class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = (
            'sleeperId', 'sleeperName', 'funName', 'rosterId',
            'wins', 'losses', 'ties', 'fpts',
            'league',
        )

        def create(self, validated_data):
            return FantasyTeam(validated_data)

class FantasyTeamOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = (
            'sleeperName',
        )

class MatchupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matchup
        fields = '__all__'

class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchupBets
        fields = (
            'bettor', 'betType', 'betAmount', 'teamToWin', 'matchup'
        )

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id', 'name', 'pos', 'pos2', 'nflTeam', 'age', 'currentProj'
        )

    def create(self, validated_data):
        return Player(validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id'. instance.id)
        instance.name = validated_data.get('id'. instance.name)
        instance.pos = validated_data.get('id'. instance.pos)
        instance.pos2 = validated_data.get('id'. instance.pos2)
        instance.nflTeam = validated_data.get('id'. instance.nflTeam)
        instance.age = validated_data.get('id'. instance.age)
        instance.save()