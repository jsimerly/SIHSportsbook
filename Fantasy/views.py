from os import stat
from turtle import pos
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
import decimal
from Fantasy.fprosEndpoint import strip_stats
from Fantasy.models import NflState, PlayerCurrentStats, PlayerProjections

from .sleeperEndpoint import * 
from .serializers import * 

# Create your views here.
class UpdateNflPlayers(APIView):
    # permission_classes = [IsAdminUser]

    #This acts as both a POST and PUT
    def post(self, request, format='json'):
        players_json = get_players()

        player_objs_update = []

        player_objs_create = []
        player_proj_create = []
        player_stats_create = []

        for player_id in players_json:
            new_player = False
            if player_id is not None:
                player_info = players_json[player_id]

                try: 
                    player = Player.objects.get(sleeper_id=player_id)
                    print('New Player')
                except Exception as e:
                    player = Player(sleeper_id=player_id)
                    new_player = True
                    print(e)

                #special logic for Defenses
                if player_info['position'] == 'DEF':
                    try:
                        player.name = player_id
                        player.pos = [player_info['position']]
                    except Exception as e:
                        print(f'DEF ERROR: {player_id}')
                        print(e)

                else:
                    #try to trouble shoot this
                    player.name = player_info['full_name']
                    player.age = player_info['age']
                    player.pos = player_info['fantasy_positions']
                    player.nfl_team = player_info['team']

            if new_player:
                print(f'Player Created: {player.name} - {player.pos} - {player.sleeper_id}')
                player_objs_create.append(player)
                player_proj_create.append(PlayerProjections(player=player))
                player_stats_create.append(PlayerCurrentStats(player=player))
            else:
                print(f'Player Updated: {player.name} - {player.pos} - {player.sleeper_id}')
                player_objs_update.append(player)
                player_proj_create.append(PlayerProjections(player=player))
                player_stats_create.append(PlayerCurrentStats(player=player))

        if len(player_objs_update) != 0:
            print('{} player(s) updated'.format(len(player_objs_update)))
            Player.objects.bulk_update(player_objs_update, ['pos', 'nfl_team', 'sleeper_id', 'age'])

        if player_objs_create:
            print('{} player(s) created'.format(len(player_objs_create)))
            Player.objects.bulk_create(player_objs_create)
            PlayerProjections.objects.bulk_create(player_proj_create)
            PlayerCurrentStats.objects.bulk_create(player_stats_create)
            

        return Response(status=status.HTTP_200_OK)

class CreateLeague(APIView):
    serializer_class = LeagueSleeperIdSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        league_id = request.data['sleeper_id']
        owner = request.user.id
        # token = request.data['csrfmiddlewaretoken']

        league_json = get_league(league_id)

        if league_json is None:
            return Response('error: League Not Found', status=status.HTTP_404_NOT_FOUND)
        
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
            return Response(league_serializer.errors, status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            return Response(league_settings_serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            return Response(scoring_settings_serializer.errors)

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
                return Response(fantasy_team_serailizer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(league_serializer.data, status=status.HTTP_201_CREATED)

class UpdatePlayerProjections(APIView):
    def put(self, request, format='json'):
        def qb_player_update(qb_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    pass_yds = qb_info['passYds'],
                    pass_tds = qb_info['passTds'],
                    pass_ints = qb_info['ints'],
                    rush_yds = qb_info['rushYds'],
                    rush_tds = qb_info['rushTds'],
                    fumbles = qb_info['fls'],
                    fp_est = qb_info['fp']
                )
        def rb_player_update(rb_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    rush_yds = rb_info['rushYds'],
                    rush_tds = rb_info['rushTds'],
                    rec_rec = rb_info['rec'],
                    rec_yd = rb_info['recYds'],
                    rec_tds = rb_info['recTds'],
                    fumbles = rb_info['fls'],
                    fp_est = rb_info['fp']
                )

        def wr_player_update(wr_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    rec_rec = wr_info['rec'],
                    rec_yds = wr_info['recYds'],
                    rec_tds = wr_info['recTds'],
                    rush_yds = wr_info['rushYds'],
                    rush_tds = wr_info['rushTds'],
                    fumbles = wr_info['fls'],
                    fp_est = wr_info['fp']
                )
        def te_player_update(te_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    rec_rec = te_info['rec'],
                    rec_yds = te_info['recYds'],
                    rec_tds = te_info['recTds'],
                    fumbles = te_info['fls'],
                    fp_est = te_info['fp']
                )
        def k_player_update(k_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    fg = k_info['fg'],
                    xpt = k_info['xpt'],
                    k_total = k_info['fpts'],
                    fp_est = k_info['fpts'],
                )
        def dst_player_update(dst_info, sleeper_id):
            Player.objects.get(sleeper_id=sleeper_id).proj.update_or_create(
                    def_sack = dst_info['sacks'],
                    def_int = dst_info['ints'],
                    def_fum_rec = dst_info['fr'],
                    def_forced_fum = dst_info['ff'],
                    def_td = dst_info['tds'],
                    def_saftey = dst_info['saftey'],
                    def_pa = dst_info['pa'],
                    def_yds_against = dst_info['ydsAgn'],
                    def_total = dst_info['fpts'],
                    fp_est = dst_info['fpts'],
                )

        def update_player_proj(pos):
            func_map = {
                'qb' : qb_player_update,
                'rb' : rb_player_update,
                'wr' : wr_player_update,
                'te' : te_player_update,
                'k' : k_player_update,
                'dst' : dst_player_update,
            }

            update_func = func_map[pos]
            pos_data = strip_stats(pos)

            for player in pos_data:
                player_info = pos_data[player]
                # try:
                update_func(player_info, player)
                # except Exception as e:
                #     print(str(player) + '  | Player Update Error | ' + str(e))

        update_player_proj('qb')
        update_player_proj('rb')
        update_player_proj('wr')
        update_player_proj('te')
        update_player_proj('k')
        update_player_proj('dst')

        return Response(status=status.HTTP_200_OK)

class UpdateLeagueProjections(APIView):
    serializer_class = LeagueSleeperIdSerializer

    def put(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            sleeper_id = serializer.data.get('sleeper_id')

            league = FantasyLeague.objects.get(sleeper_id=sleeper_id)
            league.update_all_proj()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateLeagueRosters(APIView):
    serializer_class = LeagueSleeperIdSerializer

    def put(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            sleeper_id = serializer.data.get('sleeper_id')

            league = FantasyLeague.objects.get(sleeper_id=sleeper_id)
            league.update_all_rosters()

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateNflState(APIView):
    def put(self, request, format='json'):
        nfl_state_json = get_nfl_state()

        try:

            NflState.objects.filter(pk=1).update(
                week = nfl_state_json['leg'],
                display_week = nfl_state_json['display_week'],
                season = nfl_state_json['league_season'],
                non_reg_week = nfl_state_json['week']
            )

            return Response ('Updated', status=status.HTTP_200_OK)
        except:
            return Response('error: Internal Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#
class UpdateFantasyLeagueMatchups(APIView):
    serializer_class = LeagueSleeperIdSerializer

    def put(self, request, format='json'):
        pass
        
