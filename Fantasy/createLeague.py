from .sleeperEndpoint import *  
from .serializers import * 

def create_league(league_id, owner):    

    league_json = get_league(league_id)

    if league_json is None:
        return 'error: League Not Found'
    
    #Fantasy League
    league_data = {}
    league_data['sleeper_id'] = league_id
    league_data['owner'] = owner
    league_data['name'] = league_json['name']
    league_data['status'] = league_json['status']
    # data['crsfmiddlewaretoken'] = token 

    league_serializer = LeagueCreateSerializer(data=league_data)

    if league_serializer.is_valid():
        new_league = league_serializer.save()
        print(new_league)
    else:
        return {'status':'error', 'data' : league_serializer.errors}

    #League Settings
    league_settings_data = {}
    league_settings_data['league'] = new_league.id
    league_settings_data['leagueSize'] = league_json['total_rosters']
    league_settings_data['playoffSize'] = league_json['settings']['playoff_teams']

    league_settings_data['nQB'] = (league_json['roster_positions']).count('QB')
    league_settings_data['nRB'] = (league_json['roster_positions']).count('RB')
    league_settings_data['nWR'] = (league_json['roster_positions']).count('WR')
    league_settings_data['nTE'] = (league_json['roster_positions']).count('TE')
    league_settings_data['nDST'] = (league_json['roster_positions']).count('DEF')
    league_settings_data['nK'] = (league_json['roster_positions']).count('K')

    league_settings_data['n_flex_wr_rb_te'] = (league_json['roster_positions']).count('FLEX')
    league_settings_data['n_flex_wr_rb'] = (league_json['roster_positions']).count('') #unknown values
    league_settings_data['n_flex_wr_te'] = (league_json['roster_positions']).count('') #
    league_settings_data['n_super_flex'] = (league_json['roster_positions']).count('SUPER_FLEX')
    league_settings_data['nBench'] = (league_json['roster_positions']).count('BN')

    league_settings_serializer = LeagueSettingSerialzier(data=league_settings_data)
    
    if league_settings_serializer.is_valid():
        league_settings_serializer.save()
    else:

        return {'status':'error', 'data' : league_settings_serializer.errors}

    #Scoring Settings
    league_scoring_settings = {}
    league_scoring_settings['league'] = new_league.id
    league_scoring_settings['pass_yds'] = round(league_json['scoring_settings']['pass_yd'], 3)
    league_scoring_settings['pass_tds'] = round(league_json['scoring_settings']['pass_td'], 3)
    league_scoring_settings['pass_ints'] = round(league_json['scoring_settings']['pass_int'], 3)
    league_scoring_settings['pass_2pts'] = round(league_json['scoring_settings']['pass_2pt'], 3)

    league_scoring_settings['rush_yds'] = round(league_json['scoring_settings']['rush_yd'], 3)
    league_scoring_settings['rush_tds'] = round(league_json['scoring_settings']['rush_td'], 3)
    league_scoring_settings['rush_2pts'] = round(league_json['scoring_settings']['rush_2pt'], 3)

    league_scoring_settings['ppr'] = round(league_json['scoring_settings']['rec'], 3)
    league_scoring_settings['rec_yds'] = round(league_json['scoring_settings']['rec_yd'], 3)
    league_scoring_settings['rec_tds'] = round(league_json['scoring_settings']['rec_td'], 3)
    league_scoring_settings['rec_2pts'] = round(league_json['scoring_settings']['rec_2pt'], 3)

    league_scoring_settings['rec_prem_rb'] = round(league_json['scoring_settings']['bonus_rec_rb'], 3)
    league_scoring_settings['rec_prem_te'] = round(league_json['scoring_settings']['bonus_rec_te'], 3)
    league_scoring_settings['rec_prem_wr'] = round(league_json['scoring_settings']['bonus_rec_wr'], 3)

    league_scoring_settings['fumble'] = round(league_json['scoring_settings']['fum'], 3)
    league_scoring_settings['fumble_lost'] = round(league_json['scoring_settings']['fum_lost'], 3)

    league_scoring_settings['xp_miss'] = round(league_json['scoring_settings']['xpmiss'], 3)
    league_scoring_settings['fg_miss'] = round(league_json['scoring_settings']['fgmiss'], 3)
    league_scoring_settings['xp_made'] = round(league_json['scoring_settings']['xpm'], 3)
    league_scoring_settings['fg_0_19'] = round(league_json['scoring_settings']['fgm_0_19'], 3)
    league_scoring_settings['fg_20_29'] = round(league_json['scoring_settings']['fgm_20_29'], 3)
    league_scoring_settings['fg_30_39'] = round(league_json['scoring_settings']['fgm_30_39'], 3)
    league_scoring_settings['fg_40_49'] = round(league_json['scoring_settings']['fgm_40_49'], 3)
    league_scoring_settings['fg_50_plus'] = round(league_json['scoring_settings']['fgm_50p'], 3)

    league_scoring_settings['def_td'] = round(league_json['scoring_settings']['def_td'], 3)
    league_scoring_settings['def_sack'] = round(league_json['scoring_settings']['sack'], 3)
    league_scoring_settings['def_int'] = round(league_json['scoring_settings']['int'], 3)
    league_scoring_settings['def_fum_rec'] = round(league_json['scoring_settings']['fum_rec'], 3)
    league_scoring_settings['def_saftey'] = round(league_json['scoring_settings']['safe'], 3)
    league_scoring_settings['def_forced_fum'] = round(league_json['scoring_settings']['ff'], 3)
    league_scoring_settings['def_blocked_kick'] = round(league_json['scoring_settings']['blk_kick'], 3)

    league_scoring_settings['def_pa_0'] = round(league_json['scoring_settings']['pts_allow_0'], 3)
    league_scoring_settings['def_pa_6'] = round(league_json['scoring_settings']['pts_allow_1_6'], 3)
    league_scoring_settings['def_pa_13'] = round(league_json['scoring_settings']['pts_allow_7_13'], 3)
    league_scoring_settings['def_pa_27'] = round(league_json['scoring_settings']['pts_allow_21_27'], 3)
    league_scoring_settings['def_pa_34'] = round(league_json['scoring_settings']['pts_allow_28_34'], 3)
    league_scoring_settings['def_pa_35_plus'] = round(league_json['scoring_settings']['pts_allow_35p'], 3)

    scoring_settings_serializer = ScoringSettingsSerializer(data=league_scoring_settings)

    if scoring_settings_serializer.is_valid():
        scoring_settings_serializer.save()
    else:
        return {'status':'error', 'data' : scoring_settings_serializer.errors}

    user_json = get_league_users(league_id)

    name_map = {}
    for user in user_json:
        name_map[user['user_id']] = {}
        try:
            name_map[user['user_id']]['fun_name'] = user['metadata']['team_name']
        except:
            name_map[user['user_id']]['fun_name'] = user['display_name']
        name_map[user['user_id']]['display_name'] = user['display_name']

    roster_json = get_rosters(league_id)

    for team in roster_json:
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

        fantasy_team_serailizer = FantasyTeamCreateSerializer(data=roster_data)

        if fantasy_team_serailizer.is_valid():
            new_fantasy_team = fantasy_team_serailizer.save()
            new_fantasy_team.update_roster(team['players'])

        else:
            return {'status':'error', 'data' : fantasy_team_serailizer.error}

    return {'data': league_serializer.data, 'status':'successful'}