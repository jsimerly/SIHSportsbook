from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from decimal import Decimal
from Fantasy.fprosEndpoint import strip_stats
from Fantasy.models import NflState, PlayerCurrentStats, PlayerProjections
from django.db.models import Q

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
                player_objs_create.append(player)
                player_proj_create.append(PlayerProjections(player=player))
                player_stats_create.append(PlayerCurrentStats(player=player))
            else:
                player_objs_update.append(player)

        if len(player_objs_update) != 0:
            print('{} player(s) updated'.format(len(player_objs_update)))
            Player.objects.bulk_update(player_objs_update, ['pos', 'nfl_team', 'sleeper_id', 'age'])

        if player_objs_create:
            print('{} player(s) created'.format(len(player_objs_create)))
            Player.objects.bulk_create(player_objs_create)
            PlayerProjections.objects.bulk_create(player_proj_create)
            PlayerCurrentStats.objects.bulk_create(player_stats_create)
            

        return Response(status=status.HTTP_200_OK)

class FindSleeperLeagues(APIView):
    def post(self, request, format='json'):
        league_id = request.data['sleeper_id']

        fantasy_league_obj = FantasyLeague.objects.filter(sleeper_id=league_id).first()
        betting_leagues = []

        if fantasy_league_obj:
            league_name = fantasy_league_obj.name
            betting_league_objs = fantasy_league_obj.betting_league.all()
            print(betting_league_objs)
            
            if betting_league_objs:
                for betting_league_obj in betting_league_objs:
                    betting_league = {
                        'league_name': betting_league_obj.league_name,
                        'league_id' : betting_league_obj.id
                    }
                    betting_leagues.append(betting_league)
            
        else:
            league_json = get_league(league_id)
            league_name = league_json['name']

        json = {
                'league_name' : league_name,
                'betting_leagues' : betting_leagues,
            }
                
        return Response(json, status=status.HTTP_200_OK)

class CreateLeague(APIView):
    serializer_class = LeagueSleeperIdSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, format='json'):
        league_id = request.data['sleeper_id']
        owner = request.user.id

        if FantasyLeague.objects.filter(sleeper_id=league_id).exists():
            json = {
                'league_status' : 'exists'
            }
            return Response(json, status=status.HTTP_200_OK)

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
                return Response(fantasy_team_serailizer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(league_serializer.data, status=status.HTTP_201_CREATED)

class UpdatePlayerProjections(APIView):
    def put(self, request, format='json'):
        
        def qb_player_update(qb_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)

            player_proj.pass_yds = qb_info['passYds']
            player_proj.pass_tds = qb_info['passTds']
            player_proj.pass_ints = qb_info['ints']
            player_proj.rush_yds = qb_info['rushYds']
            player_proj.rush_tds = qb_info['rushTds']
            player_proj.fumbles = qb_info['fls']
            player_proj.fp_est = qb_info['fp']

            player.proj_total = qb_info['fp']

            player.save()
            player_proj.save()

        def rb_player_update(rb_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)

            player_proj.rush_yds = rb_info['rushYds']
            player_proj.rush_tds = rb_info['rushTds']
            player_proj.rec_rec = rb_info['rec']
            player_proj.rec_yds = rb_info['recYds']
            player_proj.rec_tds = rb_info['recTds']
            player_proj.fumbles = rb_info['fls']
            player_proj.fp_est = rb_info['fp']

            player.proj_total = rb_info['fp']

            player.save()
            player_proj.save()

        def wr_player_update(wr_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)

            player_proj.rec_rec = wr_info['rec']
            player_proj.rec_yds = wr_info['recYds']
            player_proj.rec_tds = wr_info['recTds']
            player_proj.rush_yds = wr_info['rushYds']
            player_proj.rush_tds = wr_info['rushTds']
            player_proj.fumbles = wr_info['fls']
            player_proj.fp_est = wr_info['fp']
            player.proj_total = wr_info['fp']

            player.save()
            player_proj.save()
            
        def te_player_update(te_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)

            player_proj.rec_rec = te_info['rec']
            player_proj.rec_yds = te_info['recYds']
            player_proj.rec_tds = te_info['recTds']
            player_proj.fumbles = te_info['fls']
            player_proj.fp_est = te_info['fp']
            player.proj_total = te_info['fp']

            player.save()
            player_proj.save()
            
        def k_player_update(k_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)
            
            player_proj.fg = k_info['fg']
            player_proj.xpt = k_info['xpt']
            player_proj.k_total = k_info['fpts']
            player_proj.fp_est = k_info['fpts']
            player.proj_total = k_info['fpts']

            player.save()
            player_proj.save()

        def dst_player_update(dst_info, sleeper_id):
            player = Player.objects.get(sleeper_id=sleeper_id)
            try:
                player_proj = player.proj
            except Exception as e:
                print(e)
                player_proj = PlayerProjections(player=player)

            player_proj.def_sack = dst_info['sacks']
            player_proj.def_int = dst_info['ints']
            player_proj.def_fum_rec = dst_info['fr']
            player_proj.def_forced_fum = dst_info['ff']
            player_proj.def_td = dst_info['tds']
            player_proj.def_saftey = dst_info['saftey']
            player_proj.def_pa = dst_info['pa']
            player_proj.def_yds_against = dst_info['ydsAgn']
            player_proj.def_total = dst_info['fpts']
            player_proj.fp_est = dst_info['fpts']
            player.proj_total = dst_info['fpts']

            player.save()
            player_proj.save()

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
                try:
                    update_func(player_info, player)
                except Exception as e:
                    print(player_info)
                    print(str(player) + '  | Player Update Error | ' + str(e))

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
            roster_data = get_rosters(sleeper_id)
            league.update_all_rosters(roster_data)

            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateNflState(APIView):
    def put(self, request, format='json'):
        nfl_state_json = get_nfl_state()

        try:
            NflState.objects.filter(pk=1).update_or_create(
                week = nfl_state_json['leg'],
                display_week = nfl_state_json['display_week'],
                season = nfl_state_json['league_season'],
                non_reg_week = nfl_state_json['week']
            )

            return Response ('Updated', status=status.HTTP_200_OK)
        except:
            return Response('error: Internal Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateFantasyLeagueMatchups(APIView):
    serializer_class = LeagueSleeperIdSerializer

    def put(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            sleeper_id = serializer.data.get('sleeper_id')
            league = FantasyLeague.objects.get(sleeper_id=sleeper_id)
            teams = league.FantasyTeams.all()

            matchups_json = get_matchup_for_league(sleeper_id)

            matchups = {}
            for matchup_json in matchups_json:
                matchup_id = matchup_json['matchup_id']
                roster_id = matchup_json['roster_id']
                
                if matchup_id in matchups:
                    matchups[matchup_id].append(roster_id)
                else:
                    matchups[matchup_id] = [roster_id]

            nfl_state = NflState.objects.get(pk=1)

            week = nfl_state.week
            season = nfl_state.season
            
            for matchup_id, values in matchups.items():
                team1_obj = teams.get(roster_id=values[0])
                team2_obj = teams.get(roster_id=values[1])

                matchup = Matchup.objects.filter(
                        Q(week=week) | 
                        Q(season=season) |
                        Q(team1=team1_obj) | 
                        Q(team2=team2_obj) 
                    )

                matchup.update_or_create(
                    week = week,
                    season = season,
                    matchup_id = matchup_id,
                    league = league,
                    team1 = team1_obj,
                    team2 = team2_obj
                )
            
            return Response(serializer.data, status=status.HTTP_200_OK)
  
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        


        
