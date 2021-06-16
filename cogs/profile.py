import os
import requests
import discord
from discord.ext import commands
import psycopg2
from cogs.SQL import postgresql
from cogs.utils import util
import json

os.environ['http_proxy'] = os.environ.get('FIXIE_URL', '')
os.environ['https_proxy'] = os.environ.get('FIXIE_URL', '')

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer ' + os.environ['COC_TOKEN']
}

class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    def get_troops(self, troops):
        troop_dict = {'Barbarian':'-', 'Archer':'-', 'Giant':'-', 'Goblin':'-', 'Wall Breaker':'-', 'Balloon':'-', 'Wizard':'-', 'Healer':'-', 'Dragon':'-', 'P.E.K.K.A':'-', 'Baby Dragon':'-', 'Miner':'-', 'Electro Dragon':'-', 'Yeti':'-', 'Dragon Rider':'-', 'Minion':'-', 'Hog Rider':'-', 'Valkyrie':'-', 'Golem':'-', 'Witch':'-', 'Lava Hound':'-', 'Bowler':'-', 'Ice Golem':'-', 'Headhunter':'-', 'Wall Wrecker':'-', 'Battle Blimp':'-', 'Stone Slammer':'-', 'Siege Barracks':'-', 'Log Launcher':'-', 'Unicorn':'-', 'L.A.S.S.I':'-', 'Mighty Yak':'-', 'Electro Owl':'-'}
        for troop in troops:
            if troop['name'] in troop_dict and troop['village'] == 'home':
                troop_dict[troop['name']] = str(troop['level'])
        return troop_dict


    def get_spells(self, spells):
        spell_dict = {'Lightning Spell':'-', 'Healing Spell':'-', 'Rage Spell':'-', 'Jump Spell':'-', 'Freeze Spell':'-', 'Clone Spell':'-', 'Invisibility Spell':'-', 'Poison Spell':'-', 'Earthquake Spell':'-', 'Haste Spell':'-', 'Skeleton Spell':'-', 'Bat Spell':'-'}
        for spell in spells:
            if spell['name'] in spell_dict:
                spell_dict[spell['name']] = str(spell['level'])
        return spell_dict
 

    #COMMANDS
    @commands.command(help='Links Discord account to specified Clash of Clans profile.\n`.link <tag>`')
    async def link(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'):
            tag = tag[1:]
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        if response.status_code != 200:
            await ctx.send('Plese enter a valid player tag!')
            return

        name = response.json()['name']
        postgresql.insert_player(ctx.author.id, tag)
        await ctx.send(f'**Successfully linked to __{name}__.**')


    @commands.command()
    async def linked(self, ctx):
        if postgresql.select_player_id(ctx.author.id):
            tag = postgresql.select_player_id(ctx.author.id)[0]
        else:
            tag = None
        if tag == None:
            await ctx.send('**You currently have no clash of clans profile linked.**')
            return
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers).json()
        name, tag = response['name'], response['tag']
        await ctx.send(f'**You are currently linked to __{name}{tag}__**')



    @commands.command(aliases=['PROFILE'])
    async def profile(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]    
        tag = postgresql.select_player_id(ctx.author.id) if not tag else tag
        if not tag:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid player tag following the profile command.**')
            return

        
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag[0]}', headers=headers)
        
        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid player tag following the profile command.**')
            return

        with open('txt/profile.txt', 'r') as f:
            text = f.read()

        profile = response.json()
        hero_lvls = util.get_heroes(profile['heroes'])
        profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description=text.format(
            lvl=profile['expLevel'], 
            th_emoji=util.get_th(profile['townHallLevel']), 
            th_lvl=profile['townHallLevel'], 
            trophy_emoji=util.get_trophy(profile),
            trophies=profile['trophies'],
            best_trophy_emoji=util.best_trophy(profile['bestTrophies']),
            best_trophies=profile['bestTrophies'],
            clan_name=profile['clan']['name'],
            role=profile['role'].capitalize(),
            stars=profile['warStars'],
            barb_lvl=hero_lvls[0],
            queen_lvl=hero_lvls[1],
            grand_lvl=hero_lvls[2],
            royal_lvl=hero_lvls[3],
            troops_donated=profile['donations'],
            troops_received=profile['donationsReceived'],
            attacks_won=profile['attackWins'],
            defenses_won=profile['defenseWins'],
            tag=profile['tag'][1:]
            ))
        await ctx.send(embed=profile_embed)
        
    
    @commands.command(aliases=['BUILDER'])
    async def builder(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]    
        tag = postgresql.select_player_id(ctx.author.id) if not tag else tag    
        if not tag:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid player tag following the builder command.**')
            return

        
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag[0]}', headers=headers)
        
        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid player tag following the builder command.**')
            return

        with open('txt/builder_profile.txt', 'r') as f:
            text = f.read()
        profile = response.json()

        profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description=text.format(
            lvl=profile['expLevel'], 
            bh_lvl=profile['builderHallLevel'],
            bh_trophies=profile['versusTrophies'],
            best_bh_trophies=profile['bestVersusTrophies'],
            builder_emoji=util.builder_emoji(profile['builderHallLevel']),
            bm_lvl=util.battle_machine(profile),
            builder_wins=profile['versusBattleWins'],
            tag=profile['tag']
            ))
        await ctx.send(embed=profile_embed)

    
    @commands.command()
    async def units(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]
        if not tag:
            tag = postgresql.select_player_id(ctx.author.id)[0]
        
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        
        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the profile command.**')
            return

        with open('txt/units.txt', 'r') as f:
            text = f.read()

        with open('cogs/clash_data.json', 'r') as f:
            data = json.load(f)
        profile = response.json()
        th_lvl=profile['townHallLevel']
        troops = self.get_troops(profile['troops'])
        spells = self.get_spells(profile['spells'])
        max_troops = data['home']['troops']
        max_spells = data['home']['spells']
        profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description=text.format(
            e1=troops['Barbarian'], em1=max_troops['barbarian']['max'][th_lvl-1],
            e2=troops['Archer'], em2=max_troops['archer']['max'][th_lvl-1],
            e3=troops['Giant'], em3=max_troops['giant']['max'][th_lvl-1],
            e4=troops['Goblin'], em4=max_troops['goblin']['max'][th_lvl-1],
            e5=troops['Wall Breaker'], em5=max_troops['wallBreaker']['max'][th_lvl-1],
            e6=troops['Balloon'], em6=max_troops['balloon']['max'][th_lvl-1],
            e7=troops['Wizard'], em7=max_troops['wizard']['max'][th_lvl-1],
            e8=troops['Healer'], em8=max_troops['healer']['max'][th_lvl-1],
            e9=troops['Dragon'], em9=max_troops['dragon']['max'][th_lvl-1],
            e10=troops['P.E.K.K.A'], em10=max_troops['pekka']['max'][th_lvl-1],
            e11=troops['Baby Dragon'], em11=max_troops['babyDragon']['max'][th_lvl-1],
            e12=troops['Miner'], em12=max_troops['miner']['max'][th_lvl-1],
            e13=troops['Electro Dragon'], em13=max_troops['electroDragon']['max'][th_lvl-1],
            e14=troops['Yeti'], em14=max_troops['yeti']['max'][th_lvl-1],
            e15=troops['Dragon Rider'],  em15=max_troops['dragonRider']['max'][th_lvl-1],
            d1=troops['Minion'], dm1=max_troops['minion']['max'][th_lvl-1],
            d2=troops['Hog Rider'], dm2=max_troops['hogRider']['max'][th_lvl-1],
            d3=troops['Valkyrie'], dm3=max_troops['valkyrie']['max'][th_lvl-1],
            d4=troops['Golem'], dm4=max_troops['golem']['max'][th_lvl-1],
            d5=troops['Witch'], dm5=max_troops['witch']['max'][th_lvl-1],
            d6=troops['Lava Hound'], dm6=max_troops['lavaHound']['max'][th_lvl-1],
            d7=troops['Bowler'], dm7=max_troops['bowler']['max'][th_lvl-1],
            d8=troops['Ice Golem'], dm8=max_troops['iceGolem']['max'][th_lvl-1],
            d9=troops['Headhunter'], dm9=max_troops['headhunter']['max'][th_lvl-1],
            p1=troops['Unicorn'], pm1=max_troops['unicorn']['max'][th_lvl-1],
            p2=troops['L.A.S.S.I'], pm2=max_troops['lassi']['max'][th_lvl-1],
            p3=troops['Mighty Yak'], pm3=max_troops['mightyYak']['max'][th_lvl-1],
            p4=troops['Electro Owl'], pm4=max_troops['electroOwl']['max'][th_lvl-1],
            es1=spells['Lightning Spell'], esm1=max_spells['lightning']['max'][th_lvl-1],
            es2=spells['Healing Spell'], esm2=max_spells['healing']['max'][th_lvl-1],
            es3=spells['Rage Spell'], esm3=max_spells['rage']['max'][th_lvl-1],
            es4=spells['Jump Spell'], esm4=max_spells['jump']['max'][th_lvl-1],
            es5=spells['Freeze Spell'], esm5=max_spells['freeze']['max'][th_lvl-1],
            es6=spells['Clone Spell'], esm6=max_spells['clone']['max'][th_lvl-1],
            es7=spells['Invisibility Spell'], esm7=max_spells['invisibility']['max'][th_lvl-1],
            ds1=spells['Poison Spell'], dsm1=max_spells['poison']['max'][th_lvl-1],
            ds2=spells['Earthquake Spell'], dsm2=max_spells['earthquake']['max'][th_lvl-1],
            ds3=spells['Haste Spell'], dsm3=max_spells['haste']['max'][th_lvl-1],
            ds4=spells['Skeleton Spell'], dsm4=max_spells['skeleton']['max'][th_lvl-1],
            ds5=spells['Bat Spell'], dsm5=max_spells['bat']['max'][th_lvl-1],
            m1=troops['Wall Wrecker'], mm1=max_troops['wallWrecker']['max'][th_lvl-1],
            m2=troops['Battle Blimp'], mm2=max_troops['battleBlimp']['max'][th_lvl-1],
            m3=troops['Stone Slammer'], mm3=max_troops['stoneSlammer']['max'][th_lvl-1],
            m4=troops['Siege Barracks'], mm4=max_troops['siegeBarracks']['max'][th_lvl-1],
            m5=troops['Log Launcher'], mm5=max_troops['logLauncher']['max'][th_lvl-1]
        ))
        await ctx.send(embed=profile_embed)
        


def setup(bot):
    bot.add_cog(Profile(bot))

