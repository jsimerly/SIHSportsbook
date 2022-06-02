from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth import get_user_model


from Betting.serializers import LeagueOnlySerializer, LeagueSerializer

User = get_user_model()

class GetBettors(APIView):
    
    def get(self, request, format='json'):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            bettorsQset = user.bettor_set.all()

            json = []
            for bettor in bettorsQset:
                leagueInfo = {
                    'leagueId' : bettor.league.sleeperId,
                    'leagueName' : bettor.league.name,
                    'team' : bettor.team.funName
                } 
                json.append(leagueInfo)
            
            return Response(json, status=status.HTTP_200_OK)
        else:
            return Response({'error': "not logged in"}, status=status.HTTP_204_NO_CONTENT)

class GetBetHistory(APIView):
    def get(self, request, format='json'):
        print(request)
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            return Response(user, status=status.HTTP_200_OK)


class GetLeagueInfo(APIView):
    serializer_class = LeagueOnlySerializer
    lookup_url_kwarg = 'league'

    def get(self, request, format='json'):
        leagueId = request.GET.get(self.lookup_url_kwarg)
        if leagueId != None:
            pass
        
class GetMatchups(APIView):
    pass

