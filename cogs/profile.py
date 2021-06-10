import os
import requests
import discord
from discord.ext import commands
import psycopg2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from cogs.SQL import postgresql
from cogs.utils import util

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
    async def linkp(self, ctx, tag=''):
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
    async def unlink(self, ctx):
        postgresql.unlink_user(ctx.author.id)
        await ctx.send('**Successfully unlinked your account.**')


    @commands.command()
    async def linked(self, ctx):
        tag = postgresql.select_id(ctx.author.id)[0]
        if tag == None:
            await ctx.send('**You currently have no clash of clans profile linked.**')
            return
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers).json()
        name, tag = response['name'], response['tag']
        await ctx.send(f'**You are currently linked to __{name}{tag}__**')



    @commands.command()
    async def profile(self, ctx):
        tag = postgresql.select_id(ctx.author.id)[0]
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        
        if response.status_code != 200:
            await ctx.send('Plese link a valid player tag with the \'linkp\' command.')
            return

        with open('txt/profile.txt', 'r') as f:
            text = f.read()
        profile = response.json()
        heroes = util.get_heroes(profile['heroes'])
        profile_embed = discord.Embed(title=f'**{profile["name"]}{profile["tag"]}**', description=text.format(
            lvl=profile['expLevel'], 
            th_emoji=util.get_th(profile['townHallLevel']), 
            th_lvl=profile['townHallLevel'], 
            trophy_emoji=util.get_trophy(profile),
            trophies=profile['trophies'],
            best_trophy_emoji=util.get_trophy(profile),
            best_trophies=profile['bestTrophies'],
            clan_name=profile['clan']['name'],
            role=profile['role'].capitalize(),
            stars=profile['warStars'],
            barb_lvl=heroes[0],
            queen_lvl=heroes[1],
            grand_lvl=heroes[2],
            royal_lvl=heroes[3],
            troops_donated=profile['donations'],
            troops_received=profile['donationsReceived'],
            attacks_won=profile['attackWins'],
            defense_wins=profile['defenseWins']
            ))
        await ctx.send(embed=profile_embed)

    
        


def setup(bot):
    bot.add_cog(Profile(bot))

