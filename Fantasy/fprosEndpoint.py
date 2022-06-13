import requests
from bs4 import BeautifulSoup
import time

from .FP_TO_ID import *

#Turn HTML response into BS4 soup object for easy parsing
def get_soup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup

def get_week_string(week):
    if week is None:
        return ''
    return f'?week={week}'

#strip all of the stats out of the tables from FantasyPros
def strip_qb_stats(rows):
    t0 = time.time()
    qbs = {}

    #iterate through each row of the table
    for row in rows[2:]:
        info = {}

        #get the name of the player
        name = row.find('a', class_='player-name').text
        #Attempt to map their name to Primary Key
        try:
            pk = FP_TO_ID['qb'][name]
        #Skip this player if they're not found in the dict 
        except Exception as e:
            print(name + "FP_TO_ID Error | " + str(e)) #this usually means FP spells a players name different from sleeper
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
        info['fp'] = statCols[9].text

        qbs[pk] = info
    
    t1 = time.time()
    print(f'stripQbState Run Time: {str(t1-t0)}')
    return qbs

def strip_rb_stats(rows):
    t0 = time.time()
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
        info['fp'] = statCols[7].text

        rbs[pk] = info

    t1 = time.time()
    print(f'stripRbState Run Time: {str(t1-t0)}')
    return rbs

def strip_wr_stats(rows):
    t0 = time.time()
    wrs = {}

    for row in rows[2:]:
        info = {}

        name = row.find('a', class_='player-name').text
        try:
            pk = FP_TO_ID['wr'][name]
        except Exception as e:
            print(name + ' FP_TO_ID Error | ' + str(e))
            continue

        statCols = row.findAll('td', class_='center')
        info['name'] = name
        info['rec'] = statCols[0].text
        info['recYds'] = statCols[1].text
        info['recTds'] = statCols[2].text
        info['rushYds'] = statCols[4].text
        info['rushTds'] = statCols[5].text
        info['fls'] = statCols[6].text
        info['fp'] = statCols[7].text

        wrs[pk] = info
    
    t1 = time.time()
    print(f'stripWrState Run Time: {str(t1-t0)}')
    return wrs

def strip_te_stats(rows):
    t0 = time.time()
    tes = {}

    for row in rows[2:]:
        info = {}

        name = row.find('a', class_='player-name').text
        try:
            pk = FP_TO_ID['te'][name]
        except Exception as e:
            print(name + ' FP_TO_ID Error | ' + str(e))
            continue

        statCols = row.findAll('td', class_='center')
        info['name'] = name
        info['rec'] = statCols[0].text
        info['recYds'] = statCols[1].text
        info['recTds'] = statCols[2].text
        info['fls'] = statCols[3].text
        info['fp'] = statCols[4].text

        tes[pk] = info

    t1 = time.time()
    print(f'stripTeState Run Time: {str(t1-t0)}')
    return tes

def strip_k_stats(rows):
    t0 = time.time()
    ks = {}

    for row in rows[2:]:
        info = {}

        name = row.find('a', class_='player-name').text
        try:
            pk = FP_TO_ID['k'][name]
        except Exception as e:
            print(name + ' FP_TO_ID Error | ' + str(e))
            continue

        statCols = row.findAll('td', class_='center')
        info['name'] = name
        info['fg'] = statCols[0].text
        info['xpt'] = statCols[2].text
        info['fpts'] = statCols[3].text

        ks[pk] = info

    t1 = time.time()
    print(f'stripKState Run Time: {str(t1-t0)}')
    return ks

def strip_dst_stats(rows):
    t0 = time.time()
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

        dst[pk] = info

    t1 = time.time()
    print(f'stripDstState Run Time: {str(t1-t0)}')
    return dst

#pre setting these as they are on FantasyPros URL
QB = 'qb'
RB = 'rb'
WR = 'wr'
TE = 'te'
K = 'k'
DST = 'dst'

#Gets the out of Fantasy Pros page
def get_pos_stats(pos_key, week):
    pos_fp_map = {
        'qb' : 'qb',
        'rb' : 'rb',
        'wr' : 'wr',
        'te' : 'te',
        'k' : 'k',
        'dst' : 'dst'
    }
    fp_pos_str = pos_fp_map[pos_key]
    #used if you're trying to get past weeks data
    week_str = get_week_string(week)

    url = f'https://www.fantasypros.com/nfl/projections/{fp_pos_str}.php{week_str}'

    #BS4 parsing
    soup = get_soup(url)
    table = soup.find('table', id='data')
    rows = table.findAll('tr')
    return rows

def strip_stats(pos, week=None):
    fp_data = get_pos_stats(pos, week)
    
    func_map = {
        'qb' : strip_qb_stats,
        'rb' : strip_rb_stats,
        'wr' : strip_wr_stats,
        'te' : strip_te_stats,
        'k' : strip_k_stats,
        'dst' : strip_dst_stats
    }

    strip_func = func_map[pos]
    return strip_func(fp_data)
        
