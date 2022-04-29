import requests
from bs4 import BeautifulSoup

class FprosEndpoint():
    def _getSoup(self, url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup

    def _getWeekString(week):
        if week is not None:
            return f'?week={week}'
        return ''

    def stripQbStats(rows):
        qbs = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['passYds'] = statCols[2]
            stats['passTds'] = statCols[3]
            stats['ints'] = statCols[4]
            stats['rushYds'] = statCols[6]
            stats['rushTds'] = statCols[7]
            stats['fls'] = statCols[8]

            qbs[name] = stats

        return qbs
    
    def stripRbStats(rows):
        rbs = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rushYds'] = statCols[1]
            stats['rushTds'] = statCols[2]
            stats['rec'] = statCols[3]
            stats['recYds'] = statCols[4]
            stats['recTds'] = statCols[5]
            stats['fls'] = statCols[6]

            rbs[name] = stats

        return rbs

    def stripWrStats(rows):
        wrs = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rec'] = statCols[0]
            stats['recYds'] = statCols[1]
            stats['recTds'] = statCols[2]
            stats['rushYds'] = statCols[4]
            stats['rushTds'] = statCols[5]
            stats['fls'] = statCols[6]

            wrs[name] = stats

        return wrs

    def stripWrStats(rows):
        tes = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['rec'] = statCols[0]
            stats['recYds'] = statCols[1]
            stats['recTds'] = statCols[2]
            stats['fls'] = statCols[3]

            tes[name] = stats

        return tes

    def stripKStats(rows):
        ks = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['fg'] = statCols[0]
            stats['xpt'] = statCols[2]
            stats['fpts'] = statCols[3]

            ks[name] = stats

        return ks

    def stripDstStats(rows):
        dst = {}

        for row in rows[2:]:
            stats = {}

            name = row.find('a', class_='player-name').text

            statCols = row.findAll('td', class_='center')
            stats['sacks'] = statCols[0]
            stats['ints'] = statCols[1]
            stats['fr'] = statCols[2]
            stats['ff'] = statCols[3]
            stats['tds'] = statCols[4]
            stats['saftey'] = statCols[5]
            stats['pa'] = statCols[6]
            stats['ydsAgn'] = statCols[7]
            stats['fpts'] = statCols[8]

            dst[name] = stats

        return dst

    QB = 'qb'
    RB = 'rb'
    WR = 'wr'
    TE = 'te'
    K = 'k'
    DST = 'dst'

    def getPosStats(self, pos, week=None):
        weekString = self._getWeekString(week)
        url = f'https://www.fantasypros.com/nfl/projections/{pos}.php{weekString}'
        soup = self._getSoup(url)
        table = soup.find('table', id='data')
        rows = table.findAll('tr')
        return rows
    
    