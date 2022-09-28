from pickle import NEWFALSE
from .sleeperEndpoint import *  
from .serializers import * 

from django.db import DatabaseError, transaction

def create_league(league_id, owner):
    existing_league = FantasyLeague.objects.get(sleeper_id=league_id)
    if existing_league.exists():
        print('EXISTS')
        return {'data': existing_league, 'status':'exists'}
 
    league_json = get_league(league_id)

    if league_json is None:
        return 'error: League Not Found'

    try:
        new_league = FantasyLeague(
            sleeper_id = league_id,
            owner = owner,
            name = league_json['name'],
            status = league_json['status']
        )

        new_league.save()
    except Exception as e:
        print(e)
        return {'status' : 'error', 'data' : e}

    try:
        new_league_settings = LeagueSettings(
            league = new_league,
            league_size = league_json['total_rosters'], 
            playoff_size = league_json['settings']['playoff_teams'],

            nQB = (league_json['roster_positions']).count('QB'),
            nRB = (league_json['roster_positions']).count('RB'),
            nWR = (league_json['roster_positions']).count('WR'),
            nTE = (league_json['roster_positions']).count('TE'),
            nDST = (league_json['roster_positions']).count('DEF'),
            nK = (league_json['roster_positions']).count('K'),

            n_flex_wr_rb_te = (league_json['roster_positions']).count('FLEX'),
            n_flex_wr_rb = (league_json['roster_positions']).count(''), #unknown values
            n_flex_wr_te = (league_json['roster_positions']).count(''), #
            n_super_flex = (league_json['roster_positions']).count('SUPER_FLEX'),
            n_bench = (league_json['roster_positions']).count('BN'),
        )

        new_league_settings.save()

    except Exception as e:
        new_league.delete()
        print(e)
        return {'status' : 'error', 'data' : e}

    #Scoring Settings
    try:
        league_json['scoring_settings']['league_id'] = new_league.id


        new_scoring_settings = ScoringSettings(**league_json['scoring_settings'])
            
        new_scoring_settings.save()
    except Exception as e:
        print(e)
        new_league_settings.delete()
        new_league.delete()
        return {'status' : 'error', 'data' : e}
    
    try:
        user_json = get_league_users(league_id)
    except:
        new_scoring_settings.delete()
        new_league_settings.delete()
        new_league.delete()

        return {'status' : 'error', 'data' : e}

    name_map = {}
    for user in user_json:
        name_map[user['user_id']] = {}
        try:
            name_map[user['user_id']]['fun_name'] = user['metadata']['team_name']
        except:
            name_map[user['user_id']]['fun_name'] = user['display_name']
        name_map[user['user_id']]['display_name'] = user['display_name']

    roster_json = get_rosters(league_id)

    new_fantasy_teams = []

    for team in roster_json:
        try:
            roster_data = {}
            roster_data['league'] = new_league.id
            owner_id = team['owner_id']
            roster_data['owner_id'] = owner_id
            roster_data['roster_id'] = team['roster_id']

            roster_data['sleeper_name'] = name_map[owner_id]['display_name']
            roster_data['fun_name'] = name_map[owner_id]['fun_name']

            roster_data['wins'] = team['settings']['wins']
            roster_data['losses'] = team['settings']['losses']
            roster_data['ties'] = team['settings']['ties']
            roster_data['fpts'] = team['settings']['fpts']
        except:
            new_scoring_settings.delete()
            new_league_settings.delete()
            new_league.delete()


        try:
            new_fantasy_team = FantasyTeam(**roster_data)
            new_fantasy_team.save()
            new_fantasy_teams.append(new_fantasy_team)
        except Exception as e:
            for team in new_fantasy_teams:
                team.delete()
                new_scoring_settings.delete()
                new_league_settings.delete()
                new_league.delete()

            return {'status':'error', 'data' : e}

    new_league.save()
    new_league_settings.save()
    new_scoring_settings.save()

    for new_team in new_fantasy_teams:
        try:
            new_team.update_roster(team['players'])
        except Exception as e:
            for created_team in new_fantasy_team:
                created_team.delete()

            return {'status':'error', 'data' : e}

    #update league
    
    return {'data': new_league, 'status':'created'}
    
