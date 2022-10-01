import requests
import re
from bs4 import BeautifulSoup
import time
import random
import decimal

def get_soup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')
    return soup

def clean_data(data):
    try: 
        decimal.Decimal(data)
        return(data)
    except:
        return 0

def strip_player(url):
    soup = get_soup(url)
    player_rows = soup.find('tbody').findAll('tr', {'class': re.compile('^player-*')})
    
    all_players = []
    for row in player_rows:
        player_dict = {}
        player_name = row.find('a', {'class' : 'playerName'}).text
        player_stats = row.findAll('span', {'class':'playerStat'})
        player_proj = row.find('span', {'class':'playerWeekProjectedPts'})

        player_dict['name'] = player_name
        player_dict['pass_yds'] = clean_data(player_stats[0].text)
        player_dict['pass_tds'] = clean_data(player_stats[1].text)
        player_dict['pass_ints'] = clean_data(player_stats[2].text)
        player_dict['rush_yds'] = clean_data(player_stats[3].text)
        player_dict['rush_tds'] = clean_data(player_stats[4].text)
        player_dict['rec'] = clean_data(player_stats[5].text)
        player_dict['rec_yds'] = clean_data(player_stats[6].text)
        player_dict['rec_tds'] = clean_data(player_stats[7].text)
        player_dict['return_td'] = clean_data(player_stats[8].text)
        player_dict['fum_td'] = clean_data(player_stats[9].text)
        player_dict['2pt_conv'] = clean_data(player_stats[10].text)
        player_dict['fum'] = clean_data(player_stats[11].text)
        player_dict['fp_est'] = clean_data(player_proj.text)
        

        all_players.append(player_dict)
    return all_players

def strip_k(url):
    soup = get_soup(url)
    player_rows = soup.find('tbody').findAll('tr', {'class': re.compile('^player-*')})
    
    all_players = []
    for row in player_rows:
        player_dict = {}
        player_name = row.find('a', {'class' : 'playerName'}).text
        player_stats = row.findAll('span', {'class':'playerStat'})
        player_proj = row.find('span', {'class':'playerWeekProjectedPts'})
        
        try:
            player_dict['name'] = player_name
            player_dict['fgm'] = clean_data(player_stats[0].text)
            player_dict['fgm_0_19'] = clean_data(player_stats[1].text)
            player_dict['fgm_20_29'] = clean_data(player_stats[2].text)
            player_dict['fgm_30_39'] = clean_data(player_stats[3].text)
            player_dict['fgm_40_49'] = clean_data(player_stats[4].text)
            player_dict['fgm_50p'] = clean_data(player_stats[5].text)
            player_dict['fp_est'] = clean_data(player_proj.text)
        except Exception as e:
            print(e)
            continue

        all_players.append(player_dict)
    return all_players

def strip_def(url):
    soup = get_soup(url)
    player_rows = soup.find('tbody').findAll('tr', {'class': re.compile('^player-*')})
    
    all_players = []
    for row in player_rows:
        player_dict = {}
        player_name = row.find('a', {'class' : 'playerName'}).text
        player_stats = row.findAll('span', {'class':'playerStat'})
        player_proj = row.find('span', {'class':'playerWeekProjectedPts'})

        try:
            player_dict['name'] = player_name
            player_dict['sack'] = clean_data(player_stats[0].text)
            player_dict['def_int'] = clean_data(player_stats[1].text)
            player_dict['fum_rec'] = clean_data(player_stats[2].text)
            player_dict['safe'] = clean_data(player_stats[3].text)
            player_dict['def_td'] = clean_data(player_stats[4].text)
            player_dict['def_2pt'] = clean_data(player_stats[5].text)
            player_dict['def_td'] = clean_data(player_stats[6].text)
            player_dict['pts_allow'] = clean_data(player_stats[7].text)
            player_dict['fp_est'] = clean_data(player_proj.text)
        except Exception as e:
            print(e)
            continue

        all_players.append(player_dict)
    return all_players

pos_dict = {
    'qb' : {'pos_str' : '1', 'pages_needed' : 2 , 'strip' : strip_player},
    'rb' : {'pos_str' : '2', 'pages_needed' : 3 , 'strip' : strip_player},
    'wr' : {'pos_str' : '3', 'pages_needed' : 5 , 'strip' : strip_player},
    'te' : {'pos_str' : '4', 'pages_needed' : 2 , 'strip' : strip_player},
    'k'  : {'pos_str' : '7', 'pages_needed' : 2 , 'strip' : strip_k},
    'def': {'pos_str' : '8', 'pages_needed' : 2 , 'strip' : strip_def},
}

def fetch_player_data(pos, season, week):
    offset = 1
    pos_num = pos_dict[pos]['pos_str']
    all_player_data = []
    strip_func = pos_dict[pos]['strip']

    t0 = time.time()
    for _ in range(pos_dict[pos]['pages_needed']):
        
        url = f'https://fantasy.nfl.com/research/projections?offset={offset}&position={pos_num}&statCategory=projectedStats&statSeason={season}&statType=weekProjectedStats&statWeek={week}'
        player_data = strip_func(url)
        all_player_data= all_player_data + player_data
        
        offset += 25
        time.sleep(random.randint(0, 3))
    
    t1 = time.time()
    print(f'Strip {pos} Run Time: {str(t1-t0)}')
    return all_player_data
