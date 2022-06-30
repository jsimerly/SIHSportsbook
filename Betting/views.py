from multiprocessing.dummy import active_children
from turtle import st
from numpy import mat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import decimal

from Betting.models import *
from Fantasy.models import *

from .oddsmaker import Oddsmaker
from .serializers import *

class CreateBettingLeague(APIView):
    serializer_class = CreateBettingLeagueSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format='josn'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            league = FantasyLeague.objects.get(id=serializer.data.get('fantasy_league'))
            bookie = request.user

            BettingLeague.objects.create(
                fantasy_league = league,
                bookie = bookie
            )

            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttachedTeamToBettor(APIView):
    #add permissions to only be able to do this as a Betting League Owner
    def post(self, request, format='json'):
        betting_league = request.data['betting_league_id']
        teams_info = request.data['teams_info']

        league = BettingLeague.objects.get(pk=betting_league)
        print(league)
        all_bettors = league.bettor.all()
        print(all_bettors)

        for team_info in teams_info:
            team_id = FantasyTeam.objects.get(id=team_info['id'])
            bettor_qset = all_bettors.filter(
                Q(league=league) | 
                Q(team=team_id)
            )
            
            try:
                user = User.objects.get(email=team_info['user_email'])

              
                if len(bettor_qset) == 0:
                    Bettor.objects.create(
                        user = user,
                        league = league,
                        team = team_id,
                    )
                else:
                    bettor = bettor_qset.first()
                    bettor.user = user
                    bettor.save()
            except Exception as e:
                print(e)
                return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)

class CreateMatchupBets(APIView):
    def post(self, request, format='json'):
        
        league_id = request.data.get('id')
        betting_league = BettingLeague.objects.get(id=league_id)
        fantasty_league_matchups = betting_league.fantasy_league.matchup_set.filter(active=True)

        vig = betting_league.std_vig

        for matchup in fantasty_league_matchups:
            ou_dict = Oddsmaker.create_over_under(matchup.team1, matchup.team2, vig)
            ml_dict = Oddsmaker.create_moneylines(matchup.team1, matchup.team2, vig)
            spread_dict = Oddsmaker.create_spreads(matchup.team1, matchup.team2, vig)

            matchup_bet =  MatchupBets.objects.filter(fantasy_matchup=matchup)
            
            if not matchup_bet:
                MatchupBets.objects.create(
                    team1 = matchup.team1,
                    team2 = matchup.team2,

                    betting_league = betting_league,
                    fantasy_matchup = matchup,

                    ml_team1 = ml_dict['odds']['team1'],
                    ml_team2 = ml_dict['odds']['team2'],

                    over = ou_dict['values']['over'],
                    over_odds = ou_dict['odds']['over'],
                    under = ou_dict['values']['under'],
                    under_odds = ou_dict['odds']['under'],

                    spread_team1 = spread_dict['values']['team1'],
                    spread_team1_odds =  spread_dict['odds']['team1'],
                    spread_team2 = spread_dict['values']['team2'],
                    spread_team2_odds = spread_dict['odds']['team2'],
                )  
            else:
                matchup_bet.update(
                    team1 = matchup.team1,
                    team2 = matchup.team2,

                    ml_team1 = ml_dict['odds']['team1'],
                    ml_team2 = ml_dict['odds']['team2'],

                    over = ou_dict['values']['over'],
                    over_odds = ou_dict['odds']['over'],
                    under = ou_dict['values']['under'],
                    under_odds = ou_dict['odds']['under'],

                    spread_team1 = spread_dict['values']['team1'],
                    spread_team1_odds =  spread_dict['odds']['team1'],
                    spread_team2 = spread_dict['values']['team2'],
                    spread_team2_odds = spread_dict['odds']['team2'],
                )          

        return Response(status=status.HTTP_200_OK)

class GetMathcupBets(APIView):
    serializer_class = MatchupBets
    lookup_url_kwarg = 'league-id'

    def get(self, request, format='json'):
        league_id = request.GET.get(self.lookup_url_kwarg)

        if league_id != None:
            betting_league = BettingLeague.objects.filter(id=league_id).first()
            if betting_league:
                matchup_bets = betting_league.matchups.filter(active=True)

                json = []
                i=0
                for matchup_bet in matchup_bets:
                    i+= 1
                    matchup_info = { 
                        "id" : i,
                        "matchupId" : matchup_bet.id,
                        "payoutDate" : matchup_bet.payout_date,
                        "data" : {
                            "team1" : matchup_bet.team1.fun_name,
                            "team2" : matchup_bet.team2.fun_name,

                            "ml_team1" : matchup_bet.ml_team1,
                            "ml_team2" : matchup_bet.ml_team2,

                            "over" : matchup_bet.over,
                            "over_odds" : matchup_bet.over_odds,
                            "under" : matchup_bet.under,
                            "under_odds" : matchup_bet.under_odds,

                            "spread_team1" : matchup_bet.spread_team1,
                            "spread_team2" : matchup_bet.spread_team2,
                            "spread_team1_odds" : matchup_bet.spread_team1_odds,
                            "spread_team2_odds" : matchup_bet.spread_team2_odds,
                        }
                    }

                    json.append(matchup_info)
            return Response(json, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class PlaceBet(APIView):
#     serializer_class = BetSerializer
#     permission_classes = [IsAuthenticated]

#     def post(self, request, format='json'):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             #get bet info from front end
#             bettorId = serializer.data.get('bettor')
#             matchupId = serializer.data.get('matchup')
#             teamToWinId = serializer.data.get('teamToWin')
#             betAmount = serializer.data.get('betAmount')

#             #get objects needed for bet model
#             teamToWinObj = FantasyTeam.objects.get(pk=teamToWinId)
#             matchupObj = Matchup.objects.get(pk=matchupId)
#             bettorObj = Bettor.objects.get(pk=bettorId)

#             fantasyTeam = bettorObj.fantasyteam_set.first()
#             league = fantasyTeam.league
            
#             vig = league.standardVig
#             betStatus = 'O'

#             MatchupBets.objects.create(
#                 bettor=bettorObj,
#                 betStatus=betStatus,
#                 betType=serializer.data.get('betType'),
#                 betAmount=betAmount,
#                 vig=vig,
#                 teamToWin=teamToWinObj,
#                 matchup=matchupObj,
#             )

#             bettorObj.betsLeft -= 1
#             bettorObj.balance -= decimal.Decimal(betAmount)
#             bettorObj.save()

#             return Response(status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetBettors(APIView):
    def get(self, request, format='json'):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            bettors_qset = user.bettor_set.all()

          
            json = []
            for bettor in bettors_qset:
                leagueInfo = {
                    'league_id' : bettor.league.id,
                    'league_name' : bettor.league.fantasy_league.name,
                    'team' : bettor.team.fun_name
                } 
                json.append(leagueInfo)

            
            
            return Response(json, status=status.HTTP_200_OK)
        else:
            return Response({'error': "not logged in"}, status=status.HTTP_204_NO_CONTENT)

# class GetBetHistory(APIView):
#     def get(self, request, format='json'):
#         print(request)
#         if request.user.is_authenticated:
#             user = User.objects.get(id=request.user.id)
#             return Response(user, status=status.HTTP_200_OK)


# class GetLeagueInfo(APIView):
#     serializer_class = LeagueOnlySerializer
#     lookup_url_kwarg = 'league'

#     def get(self, request, format='json'):
#         leagueId = request.GET.get(self.lookup_url_kwarg)
#         if leagueId != None:
#             pass