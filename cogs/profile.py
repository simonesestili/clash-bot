import os
import requests
import discord
from discord.ext import commands
import psycopg2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
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

        postgresql.insert_player(ctx.author.id, tag)


    @commands.command()
    async def unlink(self, ctx):
        postgresql.unlink_user(ctx.author.id)


    @commands.command()
    async def profile(self, ctx):
        tag = postgresql.select_id(ctx.author.id)[0]
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        if response.status_code != 200:
            await ctx.send('Plese link a valid player tag with the \'linkp\' command.')
            return
        edit.fill_img(response.json())


def setup(bot):
    bot.add_cog(Profile(bot))

