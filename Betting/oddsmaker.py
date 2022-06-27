import numpy as np
import decimal

class Oddsmaker:
    @staticmethod
    def create_over_under(team1, team2, vig):
        over = team1.current_proj + team2.current_proj
        under = team2.current_proj + team1.current_proj

        total_odds = 1+vig
        over_odds = total_odds/2
        under_odds = total_odds/2

        o_u_dict = {
            'values' : {
                'over' : over,
                'under' : under
            },
            'odds' : {
                'over' : over_odds,
                'under' : under_odds,
            }
        }
        return o_u_dict

    @staticmethod
    def create_moneylines(team1, team2, vig):
        point_spread = team1.current_proj - team2.current_proj
        abs_spread = float(abs(point_spread))

        prob_spread = (1/1.75)*np.log((abs_spread*.0175)+1)

        total_odds = float(1+vig)

        if point_spread > 0:
            team1_implied_odds = total_odds/2 + prob_spread
            team2_implied_odds = total_odds/2 - prob_spread
        elif point_spread < 0:
            team1_implied_odds = total_odds/2 - prob_spread
            team2_implied_odds = total_odds/2 + prob_spread
        else:
            team1_implied_odds = total_odds/2
            team2_implied_odds = total_odds/2

        team1_implied_odds = round(decimal.Decimal(team1_implied_odds), 3)
        team2_implied_odds = round(decimal.Decimal(team2_implied_odds), 3)

        ml_dict = {
            'values' : {
                'team1' : team1_implied_odds,
                'team2' : team2_implied_odds,
            },
            'odds' : {
                'team1' : team1_implied_odds,
                'team2' : team2_implied_odds,
            }
        }
        return ml_dict

    @staticmethod
    def create_spreads(team1, team2, vig):
        spread = abs(team1.current_proj - team2.current_proj)

        total_odds = 1+vig

        spread_dict = {
            'values' : {
                'team1' : spread,
                'team2' : spread,
            },
            'odds' : {
                'team1' : total_odds/2,
                'team2' : total_odds/2,
            }
        }
        return spread_dict
