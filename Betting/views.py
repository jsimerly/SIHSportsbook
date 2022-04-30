from os import stat
from time import sleep
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .sleeperEndpoint import SleeperEndpoint
from .fprosEndpoint import FprosEndpoint

# Create your views here.
class CreateLeague(APIView, SleeperEndpoint):
    serializer_class = LeagueSerializer

    def post(self, request, format='json'):
        #Data directly sent in the request
        leagueId = request.data['sleeperId']
        owner = request.data['owner']
        token = request.data['csrfmiddlewaretoken']
        
        leagueJson = self.getLeague(leagueId) #sends get request to sleeper API

        if leagueJson is None:
            return Response('League Not Found', status=status.HTTP_404_NOT_FOUND)

        data = {}
        #request data for league Info
        data['sleeperId'] = leagueId
        data['owner'] = owner
        data['csrfmiddlewaretoken'] = token

        #sleeper response settings
        data['name'] = leagueJson['name']
        data['status'] = leagueJson['status']
        data['leagueSize'] = leagueJson['total_rosters']
        data['playoffSize'] = leagueJson['settings']['playoff_teams']
        data['ppr'] = leagueJson['scoring_settings']['rec']
        data['tePremium'] = leagueJson['scoring_settings']['bonus_rec_te']

        #sleeper response roster
        data['nQB'] = (leagueJson['roster_positions']).count('QB')
        data['nRB'] = (leagueJson['roster_positions']).count('RB')
        data['nWR'] = (leagueJson['roster_positions']).count('WR')
        data['nTE'] = (leagueJson['roster_positions']).count('TE')
        data['nDST'] = (leagueJson['roster_positions']).count('DEF')
        data['nK'] = (leagueJson['roster_positions']).count('K')
        data['nFlexWrRbTe'] = (leagueJson['roster_positions']).count('FLEX')
        data['nFlexWrRb'] = (leagueJson['roster_positions']).count('') #unknown values
        data['nFlexWrTe'] = (leagueJson['roster_positions']).count('') #
        data['nSuperFlex'] = (leagueJson['roster_positions']).count('SUPER_FLEX')

        leagueSerializer = self.serializer_class(data=data)  #assigning new data to the serializer     

        if leagueSerializer.is_valid():
            newLeague = leagueSerializer.save() #Creating a new League Object in our db
            print(newLeague)
        else:
            return Response(leagueSerializer.errors, status=status.HTTP_201_CREATED)

        #sends GET request to sleeper for rosters and users in the league
        rosterJson = self.getRosters(leagueId)
        userJson = self.getLeagueUsers(leagueId)
    
        nameDict = {}
        for user in userJson:
            nameDict[user['user_id']] = {}
            try: #if someone hasn't name there team, no 'team_name' exist
                nameDict[user['user_id']]['funName'] = user['metadata']['team_name']
            except: #instead we'll name them their display name
                nameDict[user['user_id']]['funName'] = user['display_name']
            nameDict[user['user_id']]['display_name'] = user['display_name']

        #iterate through the rosters
        for team in rosterJson:
            #create serialize data
            rosterData = {} 
            ownerId = team['owner_id']

            rosterData['sleeperId'] = ownerId
            rosterData['sleeperName'] = nameDict[ownerId]['display_name']
            rosterData['funName'] = nameDict[ownerId]['funName']
            rosterData['rosterId'] = team['roster_id']

            rosterData['wins'] = team['settings']['wins']
            rosterData['losses'] = team['settings']['losses']
            rosterData['ties'] = team['settings']['ties']
            rosterData['fpts'] = team['settings']['fpts']

            rosterData['league'] = newLeague.sleeperId

            fantasyTeamSerializer = FantasyTeamSerializer(data=rosterData)

            if fantasyTeamSerializer.is_valid():
                #create new FantasyTeam
                newTeam = fantasyTeamSerializer.save()
                print(newTeam)

                #Iterate through the team's json to get their players
                for playerId in team['players']:
                    try:
                        #find player and add to team
                        player = Player.objects.get(pk=playerId)
                        newTeam.players.add(player)
                    except:
                        #this error will mean you need to POST to UpdateNflPlayers below
                        print('ERROR - missing player ID: {}'.format(playerId))
                newTeam.save()

            else:
                return Response(fantasyTeamSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(leagueSerializer.data, status=status.HTTP_201_CREATED)


## NEED TO ADD PERMISSIONED TO HIT THIS REQUEST
class UpdateNflPlayers(APIView, SleeperEndpoint):
    def post(self, request, format='json'):
        #request sent to sleepers API for players
        playersJson = self.getPlayers()

        #iterate through the all Players
        for playerId in playersJson:
            if playerId is not None:
                playerInfo = playersJson[playerId]

                #check if this player object already exists and create player instance
                try:
                    player = Player.objects(id=playerId)
                except Exception as e:
                    player = Player(id=playerId)

                #special logic for Defence/Special Teams
                if playerInfo['position'] == 'DEF': 
                    try:
                        player.name = playerId
                    except Exception as e:
                        print(f'DEF NAME ERROR: {playerId}')
                        print(e)
                    
                    try:
                        player.pos = playerInfo['position']
                    except Exception as e:
                        print('DEF POS ERROR: {}'.format(playerInfo['position']))
                        print(e)
                
                #standard player info
                else:
                    try:
                        player.name = playerInfo['full_name']
                    except Exception as e:
                        print('PLAYER NAME ERROR {}'.format(playerInfo['full_name']))
                        print(e)

                    try:
                        player.age = playerInfo['age']
                    except Exception as e:
                        print('PLAYER AGE ERRROR: {}'.format(playerInfo['age']))
                        print(e)

                    try:
                        player.pos = playerInfo['fantasy_positions'][0]
                    except Exception as e:
                         print('PLAYER POS ERROR: {}'.format(playerInfo['position']))
                         print(e)

                    #check if player is eligable for multiple positions
                    if playerInfo['fantasy_positions'] is not None:
                        if len(playerInfo['fantasy_positions']) > 1:
                            try:
                                player.pos2 = playerInfo['fantasy_positions'][1]
                            except Exception as e:
                                print('PLAYER POS2 ERROR: {}'.format(playerInfo['position']))
                                print(e)

                    try:
                        player.nflTeam = playerInfo['team']
                    except Exception as e:
                        print('PLAYER TEAM ERROR: {}'.format(playerInfo['team']))
                        print(e)

            print(f'Current Player: {player.name}')
            player.save()
        return Response('Player Update Completed', status=status.HTTP_200_OK)

class UpdatePlayerProjections(APIView, FprosEndpoint):
    def put(self, request, format='json'):
        #update QBs stats
        qbData = self.getPosStats(self.QB)
        qbJson = self.stripQbStats(qbData)

        #if this is too slow use this: https://stackoverflow.com/questions/41744096/efficient-way-to-update-multiple-fields-of-django-model-object
        for qb in qbJson:
            qbInfo = qbJson[qb]
            try:
                Player.objects.filter(pk=qb).update(
                    projPassingYds = qbInfo['passYds'],
                    projPassingTds = qbInfo['passTds'],
                    projInts = qbInfo['ints'],
                    projRushingYds = qbInfo['rushYds'],
                    projRushingTds = qbInfo['rushTds'],
                    projFumbles = qbInfo['fls'],
                )
            except Exception as e:
                print(str(qb) + '|' + str(e))
        
    
        return Response(status=status.HTTP_200_OK)
                
                
