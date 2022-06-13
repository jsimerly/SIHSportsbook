import time
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import decimal

from Betting.models import *
from Fantasy.models import *

from .serializers import *
# Create your views here.

class AttachedTeamToBettor(APIView):
    serializer_class = FantasyTeamOnlySerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            sleeperName = serializer.data.get('sleeperName')
            teamObj = FantasyTeam.objects.get(sleeperName=sleeperName)
            bettorObj = Bettor.objects.get_or_create(user=request.user)
            teamObj.bettor = bettorObj[0]

            teamObj.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlaceBet(APIView):
    serializer_class = BetSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            #get bet info from front end
            bettorId = serializer.data.get('bettor')
            matchupId = serializer.data.get('matchup')
            teamToWinId = serializer.data.get('teamToWin')
            betAmount = serializer.data.get('betAmount')

            #get objects needed for bet model
            teamToWinObj = FantasyTeam.objects.get(pk=teamToWinId)
            matchupObj = Matchup.objects.get(pk=matchupId)
            bettorObj = Bettor.objects.get(pk=bettorId)

            fantasyTeam = bettorObj.fantasyteam_set.first()
            league = fantasyTeam.league
            
            vig = league.standardVig
            betStatus = 'O'

            MatchupBets.objects.create(
                bettor=bettorObj,
                betStatus=betStatus,
                betType=serializer.data.get('betType'),
                betAmount=betAmount,
                vig=vig,
                teamToWin=teamToWinObj,
                matchup=matchupObj,
            )

            bettorObj.betsLeft -= 1
            bettorObj.balance -= decimal.Decimal(betAmount)
            bettorObj.save()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

