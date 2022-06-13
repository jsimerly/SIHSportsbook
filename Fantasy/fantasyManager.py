from django.apps import apps

if apps.ready: 
    print('ready')
    from decimal import Decimal
    import time
    from django.db.models import Q
    
    from .models import Player

    def update_target_team_roster(team_json, team_obj):
        players = []
        print(team_json)
        for player_id in team_json:
            player_obj = Player.objects.get(sleeper_id=player_id)
            players.append(player_obj)

        team_obj.players.add(*players)
        return players

    def create_unique_ranked_proj_map(league_settings, player_qset):
        proj_map = {}
        for player in player_qset:
            if player.pos == Player.DST:
                proj_map[player] = player.def_total
            elif player.pos == Player.K:
                proj_map[player] = player.k_total
            else:
                proj = 0

                proj += player.proj.pass_yds * league_settings.pass_yard
                proj += player.proj.pass_tds * league_settings.pass_tds
                proj += player.proj.pass_ints * league_settings.pass_ints
                
                proj += player.proj.rush_yds * league_settings.rush_yds
                proj += player.proj.rush_tds * league_settings.rush_tds

                proj += player.proj.rec_yds * league_settings.rec_yds

                if player.pos == Player.RB:
                    proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_rb)
                elif player.pos == Player.WR:
                    proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_wr)
                elif player.pos == Player.TE:
                    proj += player.proj.rec_rec * (league_settings.ppr + league_settings.rec_prem_te)
                else:
                    proj += player.proj.rec_rec * league_settings.ppr

                proj -= player.proj.fumbles * league_settings.fumble_lost

                proj_map[player] = round(proj, 3)
                

        proj_map = sorted(proj_map.items(), key=lambda x: x[1], reverse=True)
        return proj_map

    def get_top_free_agent(pos, free_agents):
        if pos is not None:
            if pos == 'flex':
                free_agents = free_agents.filter(Q(pos=Player.RB) | Q(pos=Player.WR) | Q(pos=Player.TE))
            else:
                free_agents = free_agents.filter(pos=pos)

        top_free_agent = free_agents.order_by('proj_total')[0]
        return {top_free_agent: top_free_agent.proj_total}

    def get_best_players(ranked_players_map, n, free_agents_list, pos=None, free_agent_function=get_top_free_agent):
        best_players = []
        for _ in range(n):
            if not ranked_players_map:
                top_free_agent = free_agent_function(pos, free_agents_list) #if you create new free agent functions, create **kwargs
            else:
                top_player = ranked_players_map[0]
                if top_player[1] <= Decimal(5):
                    top_free_agent = free_agent_function(pos, free_agents_list)
                    best_players.append(top_free_agent)
                else:
                    ranked_players_map.pop(0)
                    best_players.append(top_player)


    def update_target_team_proj(team_obj, league):
        team_proj = Decimal(0)

        players_qset = team_obj.players.all()

        qb_qset = players_qset.filter(pos__contains=[Player.QB])
        rb_qset = players_qset.filter(pos__contains=[Player.RB])
        wr_qset = players_qset.filter(pos__contains=[Player.WR])
        te_qset = players_qset.filter(pos__contains=[Player.TE])
        k_qset = players_qset.filter(pos__contains=[Player.K])
        dst_qset = players_qset.filter(pos__contains=[Player.DST])

        ranked_qbs = create_unique_ranked_proj_map(qb_qset, league.scoring)
        ranked_rbs = create_unique_ranked_proj_map(rb_qset,league.scoring)
        ranked_wrs = create_unique_ranked_proj_map(wr_qset, league.scoring)
        ranked_tes = create_unique_ranked_proj_map(te_qset, league.scoring)
        ranked_ks = create_unique_ranked_proj_map(k_qset, league.scoring)
        ranked_dsts = create_unique_ranked_proj_map(dst_qset, league.scoring)

        starters = []

        starters.extend(get_best_players(ranked_qbs, league.settings.nQB, league.free_agents, Player.QB))
        starters.extend(get_best_players(ranked_rbs, league.settings.nRB, league.free_agents, Player.RB))
        starters.extend(get_best_players(ranked_wrs, league.settings.nWR, league.free_agents, Player.WR))
        starters.extend(get_best_players(ranked_tes, league.settings.nTE, league.free_agents, Player.TE))
        starters.extend(get_best_players(ranked_ks, league.settings.nK, league.free_agents, Player.K))
        starters.extend(get_best_players(ranked_dsts, league.settings.nDST, league.free_agents, Player.DST))

        flex_map = ranked_rbs + ranked_wrs + ranked_tes
        ranked_flex = sorted(flex_map.items(), key=lambda x: x[1], reverse=True)
        starters.extend(get_best_players(ranked_flex, league.settings.n_flex_wr_rb_te))
        #do this for wr/rb and wr/te

        super_flex_map = flex_map + ranked_qbs
        ranked_super_flex = sorted(super_flex_map.items(), key=lambda x: x[1], reverse=True)
        starters.extend(get_best_players(ranked_super_flex, league.settings.n_super_flex))

        for player in starters:
            team_proj += player[1]

        team_obj.save()
        return team_proj

    def update_league_all_rosters(team_qset, roster_data_from_sleeper):
        t0 = time.time()

        non_fa = []

        for team_json in roster_data_from_sleeper:
            team_obj = team_qset.get(roster_id = team_json['roster_id'])
            team_obj.players.clear()

            players = update_target_team_roster(team_json, team_obj)
            non_fa.append(players)

        t1 = time.time()
        print(f'fantasy manager: update all rosters - runtime: {str(t1-t0)}')
        return non_fa

    def update_league_all_proj(league):
        t0 = time.time()
        team_qset = league.FantasyTeams.all()

        for team in team_qset:
            update_target_team_proj(team, league)

        t1 = time.time()
        print(f'fantasy manager: update all proj - runtime: {str(t1-t0)}')
    

    
    

    