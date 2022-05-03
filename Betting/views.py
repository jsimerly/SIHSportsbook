import time
from django import http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from Betting.models import NflState

from .serializers import *
from .sleeperEndpoint import SleeperEndpoint
from .fprosEndpoint import FprosEndpoint

# Create your views here.
class CreateLeague(APIView, SleeperEndpoint):
    serializer_class = LeagueSerializer

    def post(self, request, format='json'):
        t0 = time.time()
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
            
        t1 = time.time()
        runTime = t1-t0
        print('Create League Run Time: ' + str(runTime))
        return Response(leagueSerializer.data, status=status.HTTP_201_CREATED)

## NEED TO ADD PERMISSION TO HIT THIS REQUEST
class UpdateNflPlayers(APIView, SleeperEndpoint):
    def post(self, request, format='json'):
        t0 = time.time()
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

        state = NflState.objects.get(pk=1)
        state.updateLastPlayerDateTime()

        t1 = time.time()
        print(f'views.UpdateNflPlayers runtime: {str(t1-t0)}')
        return Response('Player Update Completed', status=status.HTTP_200_OK)

class UpdatePlayerProjections(APIView, FprosEndpoint):
    def put(self, request, format='json'):
        t0t = time.time()

        #if this is too slow remake using this this: https://stackoverflow.com/questions/41744096/efficient-way-to-update-multiple-fields-of-django-model-object
        def qbPlayerUpdate(self, qbInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projPassingYds = qbInfo['passYds'],
                    projPassingTds = qbInfo['passTds'],
                    projInts = qbInfo['ints'],
                    projRushingYds = qbInfo['rushYds'],
                    projRushingTds = qbInfo['rushTds'],
                    projFumbles = qbInfo['fls'],
                    estProj = qbInfo['fp']
                )
        def rbPlayerUpdate(self, rbInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projRushingYds = rbInfo['rushYds'],
                    projRushingTds = rbInfo['rushTds'],
                    projRec = rbInfo['rec'],
                    projRecYds = rbInfo['recYds'],
                    projRecTds = rbInfo['recTds'],
                    projFumbles = rbInfo['fls'],
                    estProj = rbInfo['fp']
                )

        def wrPlayerUpdate(self, wrInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projRec = wrInfo['rec'],
                    projRecYds = wrInfo['recYds'],
                    projRecTds = wrInfo['recTds'],
                    projRushingYds = wrInfo['rushYds'],
                    projRushingTds = wrInfo['rushTds'],
                    projFumbles = wrInfo['fls'],
                    estProj = wrInfo['fp']
                )
        def tePlayerUpdate(self, teInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projRec = teInfo['rec'],
                    projRecYds = teInfo['recYds'],
                    projRecTds = teInfo['recTds'],
                    projFumbles = teInfo['fls'],
                    estProj = teInfo['fp']
                )
        def kPlayerUpdate(self, kInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projFg = kInfo['fg'],
                    projXpt = kInfo['xpt'],
                    projKtotal = kInfo['fpts'],
                    estProj = kInfo['fpts'],
                )
        def dstPlayerUpdate(self, dstInfo, pk):
            Player.objects.filter(pk=pk).update(
                    projSacks = dstInfo['sacks'],
                    projDInts = dstInfo['ints'],
                    projFumbleRec = dstInfo['fr'],
                    projForcedFum = dstInfo['ff'],
                    projDTds = dstInfo['tds'],
                    projSaftey = dstInfo['saftey'],
                    projPA = dstInfo['pa'],
                    projYdsAgn = dstInfo['ydsAgn'],
                    projDtotal = dstInfo['fpts'],
                    estProj = dstInfo['fpts'],
                )

        def updatePlayerPosProj(self, posJson, posUpdater):
            for player in posJson:
                playerInfo = posJson[player]
                try:
                    posUpdater(self, playerInfo, player)
                except Exception as e:
                    print(str(player) + 'Player Update Error |' + str(e))

        t0 = time.time()
        qbData = self.getPosStats(self.QB)
        qbJson = self.stripQbStats(qbData)
        rbData = self.getPosStats(self.RB)
        rbJson = self.stripRbStats(rbData)
        wrData = self.getPosStats(self.WR)
        wrJson = self.stripWrStats(wrData)
        teData = self.getPosStats(self.TE)
        teJson = self.stripTeStats(teData)
        kData = self.getPosStats(self.K)
        kJson = self.stripKStats(kData)
        dstData = self.getPosStats(self.DST)
        dstJson = self.stripDstStats(dstData)
        t1 = time.time()
        print(f'stripping all stats time {str(t1-t0)}')

        t0 = time.time()
        updatePlayerPosProj(self, qbJson, qbPlayerUpdate)
        updatePlayerPosProj(self, rbJson, rbPlayerUpdate)
        updatePlayerPosProj(self, wrJson, wrPlayerUpdate)
        updatePlayerPosProj(self, teJson, tePlayerUpdate)
        updatePlayerPosProj(self, kJson, kPlayerUpdate)
        updatePlayerPosProj(self, dstJson, dstPlayerUpdate)
        t1 = time.time()
        print(f'Player Proj Update runtime: {str(t1-t0)}')

        t1t = time.time()
        runTime = t1t-t0t
        print('Update Run Time: ' + str(runTime))

        return Response(status=status.HTTP_200_OK)
                
class UpdateLeagueProjections(APIView):
    serializer_class = LeagueOnlySerializer

    def put(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)
       
        if serializer.is_valid():
            pk = serializer.data.get('sleeperId')

            #Find league and update their projections
            league = League.objects.get(pk=pk)
            league.updateTeamProjections()
        
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateLeagueRosters(APIView, SleeperEndpoint):
    serializer_class = LeagueOnlySerializer

    def put(self, request, format='json'):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            pk = serializer.data.get('sleeperId')
            #get updated rosters from sleeper
            leagueRosterData = self.getRosters(pk)
    
            #find league and update rosters
            league = League.objects.get(pk=pk)
            league.updateRosters(leagueRosterData)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateNflState(APIView, SleeperEndpoint):
    def put(self, request, format='json'):
        nflStateJson = self.getNflState()
        NflState.objects.filter(pk=1).update(
            week=nflStateJson['leg'],
            displayWeek=nflStateJson['display_week'],
            season=nflStateJson['league_season'],
            non_reg_week=nflStateJson['week']
        )
        return Response('Updated', status=status.HTTP_200_OK)

class UpdateLeagueMatchups(APIView):
    def put(self, request, format='json'):
        return Response(status=status.HTTP_200_OK)