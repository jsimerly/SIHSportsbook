import requests
import json


def json_fetch(https):
    j = requests.get(https)
    j = json.loads(j.text)
    return j

#uses GET request using sleeperId to get league info
def get_league(league_id):
    url = f'https://api.sleeper.app/v1/league/{league_id}'
    return json_fetch(url)
    

#GET request to get rosters based on league_id
def get_rosters(league_id):
    url = f'https://api.sleeper.app/v1/league/{league_id}/rosters'
    return json_fetch(url)

#GET request to get users in league
def get_league_users(league_id):
    url = f'https://api.sleeper.app/v1/league/{league_id}/users'
    return json_fetch(url)

#get all NFL players
def get_players():
    url = 'https://api.sleeper.app/v1/players/nfl'
    return json_fetch(url)

#get the state of the NFL
def get_nfl_state():
    url = 'https://api.sleeper.app/v1/state/nfl'
    return json_fetch(url)

#get matchups for specific week
def get_matchup_for_league(league_id, week=None):
    if week is None:
        week = 15 #NflState.objects.get(pk=1).week
    url = f'https://api.sleeper.app/v1/league/{league_id}/matchups/{str(week)}'
    return json_fetch(url)

