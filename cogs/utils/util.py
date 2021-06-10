import requests
import os 

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer ' + os.environ['COC_TOKEN']
}

def get_th(th_lvl):
    if th_lvl == 14: return ':TownHall14:852342970501693470'
    if th_lvl == 13: return ':TownHall13:852342970274545666'
    if th_lvl == 12: return ':TownHall12:852342970555564032'
    if th_lvl == 11: return ':TownHall11:852342970459881482'
    if th_lvl == 10: return ':TownHall10:852342970552156182'
    if th_lvl == 9: return ':TownHall9:852342970115686401'
    if th_lvl == 8: return ':TownHall8:852342970334052364'
    if th_lvl == 7: return ':TownHall7:852342970505363466'
    if th_lvl == 6: return ':TownHall6:852342970673135626'
    if th_lvl == 5: return ':TownHall5:852342970447167488'
    if th_lvl == 4: return ':TownHall4:852342970417283082'
    if th_lvl == 3: return ':TownHall3:852342970472726578'
    if th_lvl == 2: return ':TownHall2:852342970291060816'
    else: return ':TownHall1:852342970597244968'


def get_trophy(profile):
    name = profile['league']['name']
    if name == None: return ':UnrankedLeague:852342970451886080'
    elif name[0:3] == 'Leg': return ':LegendLeague:852342969804914709'
    elif name[0:3] == 'Tit': return ':TitanLeague:852342970149371915'
    elif name[0:3] == 'Cha': return ':ChampionLeague:852342970317537360'
    elif name[0:3] == 'Mas': return ':MasterLeague:852342970295517244'
    elif name[0:3] == 'Cry': return ':CrystalLeague:852342970384384040'
    elif name[0:3] == 'Gol': return ':GoldLeague:852342970119356460'
    elif name[0:3] == 'Sil': return ':SilverLeague:852342970522140742'
    else: return ':BronzeLeague:852342970472202270'


def best_trophy(trophies):
    if trophies >= 5000: return ':LegendLeague:852342969804914709'
    elif trophies >= 4100: return ':TitanLeague:852342970149371915'
    elif trophies >= 3200: return ':ChampionLeague:852342970317537360'
    elif trophies >= 2600: return ':MasterLeague:852342970295517244'
    elif trophies >= 2000: return ':CrystalLeague:852342970384384040'
    elif trophies >= 1400: return ':GoldLeague:852342970119356460'
    elif trophies >= 800: return ':SilverLeague:852342970522140742'
    elif trophies >= 400: return ':LegendLeague:852342969804914709'
    else: return ':BronzeLeague:852342970472202270'


def builder_emoji(bh_lvl):
    if bh_lvl == 9: return ':BuilderHall9:852397167934046269'
    elif bh_lvl == 8: return ':BuilderHall8:852397167942828072'
    elif bh_lvl == 7: return ':BuilderHall7:852397167904817192'
    elif bh_lvl == 6: return ':BuilderHall6:852397167993290772'
    elif bh_lvl == 5: return ':BuilderHall5:852397167933915146'
    elif bh_lvl == 4: return ':BuilderHall4:852397167959212062'
    elif bh_lvl == 3: return ':BuilderHall3:852397168002334740'
    elif bh_lvl == 2: return ':BuilderHall2:852397167951609926'
    else: return ':BuilderHall1:852397167909666896'


def get_heroes(heroes):
    lvls = [0,0,0,0]
    for hero in heroes:
        hero_name = hero['name']

        if hero_name[0:3] == 'Bar':
            lvls[0] = hero['level']
        elif hero_name[0:2] == 'Ar':
            lvls[1] = hero['level']
        elif hero_name[0:2] == 'Gr':
            lvls[2] = hero['level']
        elif hero_name[0:2] == 'Ro':
            lvls[3] = hero['level']
    return lvls


def battle_machine(profile):
    heroes = profile['heroes']
    for hero in heroes:
        if hero['name'] == 'Battle Machine':
            return hero['level']
    return 0


def th_by_tag(tag):
    response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
    if response.status_code != 200:
        return None
    return response.json()['townHallLevel']