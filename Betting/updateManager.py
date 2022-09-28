from .oddsmaker import Oddsmaker
from .models import MatchupBets

def create_matchups_bets(betting_league):
    fantasy_league_matchups = betting_league.fantasy_league.matchup_set.filter(active=True)
    vig = betting_league.std_vig

    for matchup in fantasy_league_matchups:
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