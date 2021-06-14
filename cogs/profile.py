import os
from typing import TypedDict
import requests
import discord
from discord.ext import commands
import psycopg2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from cogs.SQL import postgresql
from cogs.utils import util

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
        troop_dict = {'Barbarian':'-', 'Archer':'-', 'Giant':'-', 'Goblin':'-', 'Wall Breaker':'-', 'Balloon':'-', 'Wizard':'-', 'Healer':'-', 'Dragon':'-', 'P.E.K.K.A':'-', 'Baby Dragon':'-', 'Miner':'-', 'Electro Dragon':'-', 'Yeti':'-', 'Minion':'-', 'Hog Rider':'-', 'Valkyrie':'-', 'Golem':'-', 'Witch':'-', 'Lava Hound':'-', 'Bowler':'-', 'Ice Golem':'-', 'Headhunter':'-', 'Wall Wrecker':'-', 'Battle Blimp':'-', 'Stone Slammer':'-', 'Siege Barracks':'-', 'Log Launcher':'-', 'Unicorn':'-', 'L.A.S.S.I':'-', 'Mighty Yak':'-', 'Electro Owl':'-'}
        for troop in troops:
            if troop['name'] in troop_dict:
                troop_dict[troop['name']] = str(troop['level'])
        return troop_dict


    def get_spells(self, spells):
        spell_dict = {'Lightning Spell':'-', 'Healing Spell':'-', 'Rage Spell':'-', 'Jump Spell':'-', 'Freeze Spell':'-', 'Clone Spell':'-', 'Invisibility Spell':'-', 'Poison Spell':'-', 'Earthquake Spell':'-', 'Haste':'-', 'Skeleton Spell':'-', 'Bat Spell':'-'}
        for spell in spells:
            if spell['name'] in spell_dict:
                spell_dict[spell['name']] = str(spell['level'])
        return spell_dict
 

    #COMMANDS
    @commands.command(aliases=['linkprofile', 'LINKP', 'LINKPROFILE'])
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
        if tag.startswith('#'): tag = tag[1:]
        if not tag:
            tag = postgresql.select_player_id(ctx.author.id)[0]
        
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        
        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the profile command.**')
            return

        with open('txt/units.txt', 'r') as f:
            text = f.read()

        profile = response.json()
        troops = self.get_troops(profile['troops'])
        spells = self.get_spells(profile['spells'])
        profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description=text.format(
            e1=troops['Barbarian'], 
            e2=troops['Archer'],
            e3=troops['Giant'],
            e4=troops['Goblin'],
            e5=troops['Wall Breaker'],
            e6=troops['Balloon'],
            e7=troops['Wizard'],
            e8=troops['Healer'],
            e9=troops['Dragon'],
            e10=troops['P.E.K.K.A'],
            e11=troops['Baby Dragon'],
            e12=troops['Miner'],
            e13=troops['Electro Dragon'],
            e14=troops['Yeti'],
            d1=troops['Minion'],
            d2=troops['Hog Rider'],
            d3=troops['Valkyrie'],
            d4=troops['Golem'],
            d5=troops['Witch'],
            d6=troops['Lava Hound'],
            d7=troops['Bowler'],
            d8=troops['Ice Golem'],
            d9=troops['Headhunter'],
            p1=troops['Unicorn'],
            p2=troops['L.A.S.S.I'],
            p3=troops['Mighty Yak'],
            p4=troops['Electro Owl'],
            es1=spells['Lightning Spell'],
            es2=spells['Healing Spell'],
            es3=spells['Rage Spell'],
            es4=spells['Jump Spell'],
            es5=spells['Freeze Spell'],
            es6=spells['Clone Spell'],
            es7=spells['Invisibility Spell'],
            ds1=spells['Poison Spell'],
            ds2=spells['Earthquake Spell'],
            ds3=spells['Haste Spell'],
            ds4=spells['Skeleton Spell'],
            ds5=spells['Bat Spell']            
        ))
        await ctx.send(embed=profile_embed)
        


def setup(bot):
    bot.add_cog(Profile(bot))

