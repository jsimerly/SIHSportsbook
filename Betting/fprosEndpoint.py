import requests
from bs4 import BeautifulSoup

from .FP_TO_ID import *

class FprosEndpoint():

    #Turn HTML response into BS4 soup object for easy parsing
    def _getSoup(self, url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup

    def _getWeekString(self, week):
        if week is None:
            return ''
        return f'?week={week}'

    #strip all of the stats out of the tables from FantasyPros
    def stripQbStats(self, rows):
        qbs = {}

        #iterate through each row of the table
        for row in rows[2:]:
            info = {}

            #get the name of the player
            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['qb'][name]
            except Exception as e:
                print(name + "FP_TO_ID Error | " + str(e))
                continue

            #parse out all the stats from the row | This could change if the HTML format of the page changes
            statCols = row.findAll('td', class_='center')
            info['name'] = name
            info['passYds'] = statCols[2].text
            info['passTds'] = statCols[3].text
            info['ints'] = statCols[4].text
            info['rushYds'] = statCols[6].text
            info['rushTds'] = statCols[7].text
            info['fls'] = statCols[8].text

            qbs[pk] = info

        return qbs
    
    def stripRbStats(self, rows):
        rbs = {}

        for row in rows[2:]:
            info = {}

            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['rb'][name]
            except Exception as e:
                print(name + 'FP_TO_ID Error | ' + str(e))
                continue

            statCols = row.findAll('td', class_='center')
            info['name'] = name
            info['rushYds'] = statCols[1].text
            info['rushTds'] = statCols[2].text
            info['rec'] = statCols[3].text
            info['recYds'] = statCols[4].text
            info['recTds'] = statCols[5].text
            info['fls'] = statCols[6].text

            rbs[pk] = info

        return rbs

    def stripWrStats(self, rows):
        wrs = {}

        for row in rows[2:]:
            info = {}

            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['wr'][name]
            except Exception as e:
                print(name + 'FP_TO_ID Error | ' + str(e))
                continue

            statCols = row.findAll('td', class_='center')
            info['name'] = name
            info['rec'] = statCols[0].text
            info['recYds'] = statCols[1].text
            info['recTds'] = statCols[2].text
            info['rushYds'] = statCols[4].text
            info['rushTds'] = statCols[5].text
            info['fls'] = statCols[6].text

            wrs[pk] = info

        return wrs

    def stripTeStats(self, rows):
        tes = {}

        for row in rows[2:]:
            info = {}

            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['te'][name]
            except Exception as e:
                print(name + 'FP_TO_ID Error | ' + str(e))
                continue

            statCols = row.findAll('td', class_='center')
            info['name'] = name
            info['rec'] = statCols[0].text
            info['recYds'] = statCols[1].text
            info['recTds'] = statCols[2].text
            info['fls'] = statCols[3].text

            tes[pk] = info

        return tes

    def stripKStats(self, rows):
        ks = {}

        for row in rows[2:]:
            info = {}

            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['k'][name]
            except Exception as e:
                print(name + 'FP_TO_ID Error | ' + str(e))
                continue

            statCols = row.findAll('td', class_='center')
            info['name'] = name
            info['fg'] = statCols[0].text
            info['xpt'] = statCols[2].text
            info['fpts'] = statCols[3].text

            ks[pk] = info

        return ks

    def stripDstStats(self, rows):
        dst = {}

        for row in rows[2:]:
            info = {}

            name = row.find('a', class_='player-name').text
            try:
                pk = FP_TO_ID['dst'][name]
            except Exception as e:
                print(name + ': FP_TO_ID error | ' + str(e))
                continue

            statCols = row.findAll('td', class_='center')
            info['sacks'] = statCols[0].text
            info['ints'] = statCols[1].text
            info['fr'] = statCols[2].text
            info['ff'] = statCols[3].text
            info['tds'] = statCols[4].text
            info['saftey'] = statCols[5].text
            info['pa'] = statCols[6].text
            info['ydsAgn'] = statCols[7].text
            info['fpts'] = statCols[8].text

            dst[name] = info

        return dst

    #pre setting these as they are on FantasyPros URL
    QB = 'qb'
    RB = 'rb'
    WR = 'wr'
    TE = 'te'
    K = 'k'
    DST = 'dst'

    #Gets the out of Fantasy Pros page
    def getPosStats(self, pos, week=None):
        #used if you're trying to get past weeks data
        weekString = self._getWeekString(week)

        url = f'https://www.fantasypros.com/nfl/projections/{pos}.php{weekString}'

        #BS4 parsing
        soup = self._getSoup(url)
        table = soup.find('table', id='data')
        rows = table.findAll('tr')
        return rows
    
