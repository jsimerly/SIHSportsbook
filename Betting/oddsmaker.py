import numpy as np
import decimal

class Oddsmaker:
    @staticmethod
    def create_over_under(team1, team2, vig):
        over = team1.current_proj + team2.current_proj
        under = team2.current_proj + team1.current_proj

        over_rounded = decimal.Decimal(.5 * round(float(over)/.5))
        under_rounded = decimal.Decimal(.5 * round((float(under)/.5)))


        total_odds = 1+vig
        over_odds = total_odds/2
        under_odds = total_odds/2

        o_u_dict = {
            'values' : {
                'over' : over_rounded,
                'under' : under_rounded
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
        team1_spread = team1.current_proj - team2.current_proj

        total_odds = 1+vig

        spread_dict = {
            'values' : {
                'team1' : round(team1_spread, 1),
                'team2' : round(-team1_spread, 1)
            },
            'odds' : {
                'team1' : total_odds/2,
                'team2' : total_odds/2,
            }
        }
        return spread_dict
        

    @staticmethod
    def implied_odds_to_american(odds):
        odds = float(odds)
        if odds < .5:
            american_odds = ((1-odds)/(odds))*100
            american_odds = round(decimal.Decimal(american_odds),0)
            return american_odds
        else:
            american_odds = -100*((odds)/(1-odds))
            american_odds = round(decimal.Decimal(american_odds),0)
            return american_odds


    @staticmethod
    def calculate_payout_from_american(bet, line):
        line = float(line)
        bet = float(bet)
        if line > 0:
            payout = line/100 * bet

        payout = 100/(-1*line) * bet

        payout = round(decimal.Decimal(payout),2)
        return payout

    @staticmethod
    def calculate_parlay_line(input_odds):
        final_odds = 1
        for prob in input_odds:
            final_odds *= prob

        odds = float(final_odds)
        if odds < .5:
            american_odds = ((1-odds)/(odds))*100
            american_odds = round(decimal.Decimal(american_odds),0)
            return american_odds
        else:
            american_odds = -100*((odds)/(1-odds))
            american_odds = round(decimal.Decimal(american_odds),0)
            return american_odds
