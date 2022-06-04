import requests
import json

class SleeperEndpoint():
    #gets json form a GET request
    def jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    #uses GET request using sleeperId to get league info
    def getLeague(self, leagueId):
        url = f'https://api.sleeper.app/v1/league/{leagueId}'
        return self.jsonFetch(url)
        

    #GET request to get rosters based on leagueId
    def getRosters(self, leagueId):
        url = f'https://api.sleeper.app/v1/league/{leagueId}/rosters'
        return self.jsonFetch(url)

    #GET request to get users in league
    def getLeagueUsers(self,leagueId):
        url = f'https://api.sleeper.app/v1/league/{leagueId}/users'
        return self.jsonFetch(url)

    #get all NFL players
    def getPlayers(self):
        url = 'https://api.sleeper.app/v1/players/nfl'
        return self.jsonFetch(url)

    #get the state of the NFL
    def getNflState(self):
        url = 'https://api.sleeper.app/v1/state/nfl'
        return self.jsonFetch(url)

    #get matchups for specific week
    def getMatchupForLeague(self, leagueId, week=None):
        if week is None:
            week = 15 #NflState.objects.get(pk=1).week
        url = f'https://api.sleeper.app/v1/league/{leagueId}/matchups/{str(week)}'
        return self.jsonFetch(url)

