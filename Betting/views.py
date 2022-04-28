from os import stat
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .sleeperEndpoint import SleeperEndpoint

# Create your views here.
class CreateLeague(APIView, SleeperEndpoint):
    serializer_class = LeagueSerializer

    def post(self, request, format='json'):
        #Data directly sent in the request
        sleeperId = request.data['sleeperId']
        owner = request.data['owner']
        token = request.data['csrfmiddlewaretoken']
        
        leagueJson = self.getLeague(sleeperId) #sends get request to sleeper API

        if leagueJson is None:
            return Response('League Not Found', status=status.HTTP_404_NOT_FOUND)

        data = {}
        #request data
        data['sleeperId'] = sleeperId
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

        serializer = self.serializer_class(data=data)  #assigning new data to the serializer     

        if serializer.is_valid():
            league = serializer.save() #Creating a new League Object in our db

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

                    
                
                
