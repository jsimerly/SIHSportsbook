from django.forms import JSONField
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
        data = self.jsonFetch(url)
        return data
