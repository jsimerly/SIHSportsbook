from Fantasy.models import FantasyLeague, Matchup, NflState, Player, PlayerProjections
from .sleeperEndpoint import get_nfl_state, get_rosters, get_matchups_for_league
from .fprosEndpoint import strip_stats
from .projectionsEndpoint import fetch_player_data
from django.db.models import Q
from .FP_TO_ID import *


def update_nfl_state():
    nfl_state_json = get_nfl_state()

    try:
        NflState.objects.filter(pk=1).update(
            week = nfl_state_json['leg'],
            display_week = nfl_state_json['display_week'],
            season = nfl_state_json['league_season'],
            non_reg_week = nfl_state_json['week']
        )
    except:
        pass

def update_league_rosters(sleeper_id):
    league = FantasyLeague.objects.get(sleeper_id=sleeper_id)
    roster_data = get_rosters(sleeper_id)

    league.update_all_rosters(roster_data)

def update_fantasy_league_matchups(sleeper_id):
   
    league = FantasyLeague.objects.get(sleeper_id=sleeper_id)
    teams = league.teams.all()

    nfl_state = NflState.objects.get(pk=1)

    week = nfl_state.week
    season = nfl_state.season
    

    matchups_json = get_matchups_for_league(sleeper_id, week)

    matchups = {}
    for matchup_json in matchups_json:
       
        matchup_id = matchup_json['matchup_id']
        roster_id = matchup_json['roster_id']
        
        if matchup_id in matchups:
            matchups[matchup_id].append(roster_id)
        else:
            matchups[matchup_id] = [roster_id]

    update_nfl_state()
    
    for matchup_id, values in matchups.items():
        team1_obj = teams.get(roster_id=values[0])
        team2_obj = teams.get(roster_id=values[1])      

        matchup = Matchup.objects.filter(
                Q(week=week) & 
                Q(season=season) &
                Q(team1=team1_obj) & 
                Q(team2=team2_obj) 
            )

        matchup.update_or_create(
            week = week,
            season = season,
            matchup_id = matchup_id,
            league = league,
            team1 = team1_obj,
            team2 = team2_obj,
            active=True
        )
    

    old_matchups = Matchup.objects.filter(
        ( ~Q(week=week) | ~Q(season=season) ) 
        & Q(active=True)
    )

    old_matchups.update(active=False)
    for old_matchup in old_matchups:
        old_matchup.betting_matchup.update(active=False)

def update_player_proj(pk, player_data):
    player = Player.objects.get(pk=pk)

    try:
        player_proj = player.proj
    except:
        player_proj = PlayerProjections(player=player)

    player_proj.update(player_data)

def update_pos_group(pos, season, week):
    player_data = fetch_player_data(pos, season,week)

    for player_info in player_data:
        name = player_info.name 
        try:
            pk = FP_TO_ID[pos][name]
        except Exception as e:
            print(name + 'FP_TO_ID Error | ' + str(e))
            continue

        update_player_proj(pk, player_info)



# def update_player_proj(pos):
#     func_map = {
#         'qb' : qb_player_update,
#         'rb' : rb_player_update,
#         'wr' : wr_player_update,
#         'te' : te_player_update,
#         'k' : k_player_update,
#         'dst' : dst_player_update,
#     }

#     update_func = func_map[pos]
#     pos_data = strip_stats(pos)

#     for player in pos_data:
#         player_info = pos_data[player]
#         try:
#             update_func(player_info, player)
#         except Exception as e:
#             print(player_info)
#             print(str(player) + '  | Player Update Error | ' + str(e))



# def qb_player_update(qb_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)

#     player_proj.pass_yds = qb_info['passYds']
#     player_proj.pass_tds = qb_info['passTds']
#     player_proj.pass_ints = qb_info['ints']
#     player_proj.rush_yds = qb_info['rushYds']
#     player_proj.rush_tds = qb_info['rushTds']
#     player_proj.fumbles = qb_info['fls']
#     player_proj.fp_est = qb_info['fp']

#     player.proj_total = qb_info['fp']

#     player.save()
#     player_proj.save()

# def rb_player_update(rb_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)

#     player_proj.rush_yds = rb_info['rushYds']
#     player_proj.rush_tds = rb_info['rushTds']
#     player_proj.rec_rec = rb_info['rec']
#     player_proj.rec_yds = rb_info['recYds']
#     player_proj.rec_tds = rb_info['recTds']
#     player_proj.fumbles = rb_info['fls']
#     player_proj.fp_est = rb_info['fp']

#     player.proj_total = rb_info['fp']

#     player.save()
#     player_proj.save()

# def wr_player_update(wr_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)

#     player_proj.rec_rec = wr_info['rec']
#     player_proj.rec_yds = wr_info['recYds']
#     player_proj.rec_tds = wr_info['recTds']
#     player_proj.rush_yds = wr_info['rushYds']
#     player_proj.rush_tds = wr_info['rushTds']
#     player_proj.fumbles = wr_info['fls']
#     player_proj.fp_est = wr_info['fp']
#     player.proj_total = wr_info['fp']

#     player.save()
#     player_proj.save()
    
# def te_player_update(te_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)

#     player_proj.rec_rec = te_info['rec']
#     player_proj.rec_yds = te_info['recYds']
#     player_proj.rec_tds = te_info['recTds']
#     player_proj.fumbles = te_info['fls']
#     player_proj.fp_est = te_info['fp']
#     player.proj_total = te_info['fp']

#     player.save()
#     player_proj.save()
    
# def k_player_update(k_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)
    
#     player_proj.fg = k_info['fg']
#     player_proj.xpt = k_info['xpt']
#     player_proj.k_total = k_info['fpts']
#     player_proj.fp_est = k_info['fpts']
#     player.proj_total = k_info['fpts']

#     player.save()
#     player_proj.save()

# def dst_player_update(dst_info, sleeper_id):
#     player = Player.objects.get(sleeper_id=sleeper_id)
#     try:
#         player_proj = player.proj
#     except Exception as e:
#         print(e)
#         player_proj = PlayerProjections(player=player)

#     player_proj.def_sack = dst_info['sacks']
#     player_proj.def_int = dst_info['ints']
#     player_proj.def_fum_rec = dst_info['fr']
#     player_proj.def_forced_fum = dst_info['ff']
#     player_proj.def_td = dst_info['tds']
#     player_proj.def_saftey = dst_info['saftey']
#     player_proj.def_pa = dst_info['pa']
#     player_proj.def_yds_against = dst_info['ydsAgn']
#     player_proj.def_total = dst_info['fpts']
#     player_proj.fp_est = dst_info['fpts']
#     player.proj_total = dst_info['fpts']

#     player.save()
#     player_proj.save()

# def update_player_proj(pos):
#     func_map = {
#         'qb' : qb_player_update,
#         'rb' : rb_player_update,
#         'wr' : wr_player_update,
#         'te' : te_player_update,
#         'k' : k_player_update,
#         'dst' : dst_player_update,
#     }

#     update_func = func_map[pos]
#     pos_data = strip_stats(pos)

#     for player in pos_data:
#         player_info = pos_data[player]
#         try:
#             update_func(player_info, player)
#         except Exception as e:
#             print(player_info)
#             print(str(player) + '  | Player Update Error | ' + str(e))

# def update_all_player_proj():
#     update_player_proj('qb')
#     update_player_proj('rb')
#     update_player_proj('wr')
#     update_player_proj('te')
#     update_player_proj('k')
#     update_player_proj('dst')