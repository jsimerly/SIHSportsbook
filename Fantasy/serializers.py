from rest_framework import serializers

from Fantasy.models import FantasyTeam, FantasyLeague, Player, Matchup, LeagueSettings, ScoringSettings

class LeagueCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyLeague
        fields = (
            'sleeper_id', 'owner', 'name', 'status'
        )

        def create(self, validated_data):
            return FantasyLeague(validated_data)

class LeagueSettingSerialzier(serializers.ModelSerializer):
    class Meta:
        model = LeagueSettings
        fields = (
            'league', 'league_size', 'playoff_size',
            'nQB', 'nRB', 'nWR', 'nTE', 'nK', 'nDST',
            'n_flex_wr_rb_te', 'n_flex_wr_rb', 'n_flex_wr_te',
            'n_super_flex', 'n_bench'
        )

class ScoringSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoringSettings
        fields = (
            'league',
            'pass_yds', 'pass_tds', 'pass_ints', 'pass_2pts',
            'rush_tds', 'rush_yds', 'rush_2pts', 
            'ppr', 'rec_yds', 'rec_tds', 'rec_2pts',
            'rec_prem_rb', 'rec_prem_te', 
            'fumble', 'fumble_lost',
            'xp_miss', 'fg_miss', 'xp_made', 'fg_0_19', 'fg_20_29', 'fg_30_39', 'fg_40_49', 'fg_50_plus',
            'def_td', 'def_sack', 'def_int', 'def_int', 'def_fum_rec', 'def_saftey', 'def_forced_fum','def_blocked_kick',
            'def_pa_0', 'def_pa_6', 'def_pa_13', 'def_pa_27', 'def_pa_34', 'def_pa_35_plus'
        )

class LeagueSleeperIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyLeague
        fields = ('sleeper_id',)
        extra_kwargs = {
            'sleeper_id' : {
                'read_only': False,
                'validators' : [],
            },
        }

class FantasyTeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = (
            'league', 'owner_id', 'roster_id', 'sleeper_name', 'fun_name',
            'wins', 'losses', 'ties', 'fpts'
        )