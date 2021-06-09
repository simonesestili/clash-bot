import os
import requests
import discord
from discord.ext import commands
import psycopg2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import json
import urllib.request
from cogs.img import edit
from cogs.SQL import postgresql

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
        edit.fill_img(response.json())
        await ctx.send('**Your current profile.**', file=discord.File(f'cogs/img/out/{tag}.png'))


def setup(bot):
    bot.add_cog(Profile(bot))

