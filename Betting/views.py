from django.utils import timezone
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
        all_bettors = league.bettor.all()

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

class PlaceMatchupBet(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        #get bet info from front end
        data = request.data
        betting_data=data['bets']
        parlay_wager = decimal.Decimal(data['parlay_wager'])
        parlay_status = data['parlay'] and len(betting_data) > 1

        if parlay_status:
            parlay_map = {
                'placed_bets' : [],
                'odds' : [],
                'payout_date' : [],
            }

        for bet_info in betting_data:
           
            bettor_id = bet_info['bettorId']
            bettor = Bettor.objects.get(id=bettor_id)
             
            if bettor.user == request.user:
                matchup_id = bet_info['matchupId']

                matchup_bet = MatchupBets.objects.get(id=matchup_id)
                
                bet_amount = bet_info['betAmount']

                time_placed = timezone.now()

                #Matchup Related
                bet_type = bet_info['betType']
    
                payout_date = matchup_bet.payout_date
                
                bet_type_map = {
                    'spread_team1' : ('S1', matchup_bet.spread_team1_odds, matchup_bet.spread_team1),
                    'spread_team2' : ('S2', matchup_bet.spread_team2_odds, matchup_bet.spread_team2),
                    'ml_team1' : ('M1', matchup_bet.ml_team1, 1),
                    'ml_team2' : ('M2', matchup_bet.ml_team2, 2),
                    'over' : ('O', matchup_bet.over_odds, matchup_bet.over),
                    'under' : ('U', matchup_bet.under_odds, matchup_bet.under),
                }
            
                bet_type, odds, bet_value = bet_type_map[bet_type]
                line = Oddsmaker.implied_odds_to_american(odds)
                payout_amount = Oddsmaker.calculate_payout_from_american(bet_amount, line)

                if parlay_status:
                    payout_amount = 0

                bet = PlacedBet.objects.create(
                    subtype= 'FFM',
                    line = line,
                    bet_amount = bet_amount,
                    payout_amount = payout_amount,
                    payout_date = payout_date,
                    time_placed = time_placed,
                    bet_type = bet_type,
                    bet_value = bet_value,
                    bettor = bettor,
                    matchup_bet = matchup_bet,
                    parlayed = parlay_status,
                )

                if parlay_status:
                    parlay_map['placed_bets'].append(bet)
                    parlay_map['odds'].append(odds)
                    parlay_map['payout_date'].append(payout_date)

        if parlay_status:
            if parlay_wager > 0:
                payout_date = max(parlay_map['payout_date']) + datetime.timedelta(hours=6)
                parlay_vig = matchup_bet.betting_league.parlay_vig
                line = Oddsmaker.calculate_parlay_line(parlay_map['odds'], parlay_vig)
                payout_amount = Oddsmaker.calculate_payout_from_american(parlay_wager, line)

                parlayBet = PlacedParlay.objects.create(
                    bettor=bettor,
                    wager = parlay_wager,
                    payout_date = payout_date,
                    line = line,
                    payout_amount = payout_amount,
                )

                parlayBet.placed_bets.add(*parlay_map['placed_bets'])
            

            # bettorObj.betsLeft -= 1
            # bettorObj.balance -= decimal.Decimal(betAmount)
            bettor.save()

        return Response({'data':'data1'},status=status.HTTP_200_OK)

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
                    'team' : bettor.team.fun_name,
                    'bettor_id' : bettor.id,
                    'parlay_vig' : bettor.league.parlay_vig
                } 
                json.append(leagueInfo)

            return Response(json, status=status.HTTP_200_OK)
       
        return Response({'error': "not logged in"}, status=status.HTTP_204_NO_CONTENT)

class GetAllBetsForSingleLeague(APIView):
    lookup_url_kwarg = 'bettor-id'

    def getBetInfo(self, bet_obj, parlayed=False):
        if bet_obj.subtype == 'FFM':
            matchup = MatchupBets.objects.get(id=bet_obj.matchup_bet_id)
            subtype_info = {
                'team1' : matchup.team1.fun_name,
                'team2' : matchup.team2.fun_name,
            }                    
        
        bet_info = {
            'parlayed' : parlayed,
            'subtype_info' : subtype_info,
            'type' : bet_obj.subtype,
            'wager' : bet_obj.bet_amount,
            'payout_amount' : bet_obj.payout_amount,
            'payout_date' : bet_obj.payout_date,
            'status' : bet_obj.bet_status,
            'bet_type' : bet_obj.bet_type,
            'bet_value' : bet_obj.bet_value,
            'line' : bet_obj.line, 
        }

        return bet_info

    def get(self, request, format='json'):
        if request.user.is_authenticated:
            bettor_id = request.GET.get(self.lookup_url_kwarg)
            bet_qset = PlacedBet.objects.filter(Q(bettor_id=bettor_id) & Q(parlayed=False))
            parlayed_qset = PlacedParlay.objects.filter(bettor_id=bettor_id)

            
            json = {
                'open' : [],
                'closed' : [],
            }
            for bet_obj in bet_qset:
 
                bet_info = self.getBetInfo(bet_obj)

                if bet_info['status'] == 'O':
                    json['open'].append(bet_info)
                else:
                    json['closed'].append(bet_info)


            for bet_obj in parlayed_qset:
                print(bet_obj)
                parlay_info = {
                    'parlayed' : True,
                    'wager': bet_obj.wager,
                    'to_win': bet_obj.payout_amount,
                    'payout_date' : bet_obj.payout_date,
                    'status' : bet_obj.bet_status,
                    'bets' : [],
                }
            
                attached_bets = bet_obj.placed_bets.all()

                for bet_obj in attached_bets:
                    bet_info = self.getBetInfo(bet_obj, parlayed=True)
                    parlay_info['bets'].append(bet_info)

                if parlay_info['status'] == 'O':
                    json['open'].append(parlay_info)
                else:
                    json['closed'].append(parlay_info)

            return Response(json)
        return Response('NA')

         
           

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