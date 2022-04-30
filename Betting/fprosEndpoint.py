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
            pk = FP_TO_ID['qb'][name]

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
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rushYds'] = statCols[1].text
            stats['rushTds'] = statCols[2].text
            stats['rec'] = statCols[3].text
            stats['recYds'] = statCols[4].text
            stats['recTds'] = statCols[5].text
            stats['fls'] = statCols[6].text

            rbs[name] = stats

        return rbs

    def stripWrStats(self, rows):
        wrs = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rec'] = statCols[0].text
            stats['recYds'] = statCols[1].text
            stats['recTds'] = statCols[2].text
            stats['rushYds'] = statCols[4].text
            stats['rushTds'] = statCols[5].text
            stats['fls'] = statCols[6].text

            wrs[name] = stats

        return wrs

    def stripWrStats(self, rows):
        tes = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rec'] = statCols[0].text
            stats['recYds'] = statCols[1].text
            stats['recTds'] = statCols[2].text
            stats['fls'] = statCols[3].text

            tes[name] = stats

        return tes

    def stripKStats(self, rows):
        ks = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['fg'] = statCols[0].text
            stats['xpt'] = statCols[2].text
            stats['fpts'] = statCols[3].text

            ks[name] = stats

        return ks

    def stripDstStats(self, rows):
        dst = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['sacks'] = statCols[0].text
            stats['ints'] = statCols[1].text
            stats['fr'] = statCols[2].text
            stats['ff'] = statCols[3].text
            stats['tds'] = statCols[4].text
            stats['saftey'] = statCols[5].text
            stats['pa'] = statCols[6].text
            stats['ydsAgn'] = statCols[7].text
            stats['fpts'] = statCols[8].text

            dst[name] = stats

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
    
