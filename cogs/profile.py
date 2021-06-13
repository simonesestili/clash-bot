import os
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

    
    #EVENTS
    pass

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

    
    # @commands.command()
    # async def units(self, ctx, tag=''):
    #     if tag.startswith('#'): tag = tag[1:]
    #     if not tag:
    #         tag = postgresql.select_player_id(ctx.author.id)[0]
        
    #     response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        
    #     if response.status_code != 200:
    #         await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the profile command.**')
    #         return

    #     with open('txt/units.txt', 'r') as f:
    #         text = f.read()

    #     profile = response.json()
    #     hero_lvls = util.get_heroes(profile['heroes'])
    #     profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description='')
    #     profile_embed.add_field(name='**Troops**', value=text.format(
            

    #     ))
    #     await ctx.send(embed=profile_embed)
        


def setup(bot):
    bot.add_cog(Profile(bot))

