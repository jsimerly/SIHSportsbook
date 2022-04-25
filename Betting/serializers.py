from rest_framework import serializers
from .models import League

class CreateLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model=League
        fields = (
            'sleeperId', 'owner', 'name', 
            'leagueSize', 'playoffSize', 'ppr', 'tePremium', 
            'nQB', 'nRB', 'nWR', 'nTE', 'nK', 'nDST',
            'nFlexWrRbTe', 'nFlexWrRb', 'nSuperFlex',
            )
