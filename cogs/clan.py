import os
import requests
import discord
from discord.ext import commands
import psycopg2
from cogs.SQL import postgresql
from cogs.utils import util

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer ' + os.environ['COC_TOKEN']
}

class Clan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['linkclan', 'LINKC', 'LINKCLAN'])
    async def linkc(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'):
            tag = tag[1:]
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers)
        if response.status_code != 200:
            await ctx.send('Plese enter a valid player tag!')
            return

        name = response.json()['name']
        postgresql.insert_clan(ctx.author.id, tag)
        await ctx.send(f'**Successfully linked to __{name}__.**')


    @commands.command()
    async def linkedc(self, ctx):
        tag = postgresql.select_clan_id(ctx.author.id)[0]
        if tag == None:
            await ctx.send('**You currently have no clash of clans clan linked.**')
            return
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers).json()
        name, tag = response['name'], response['tag']
        await ctx.send(f'**You are currently linked to __{name}{tag}__**')


    @commands.command()
    async def clan(self, ctx):
        tag = postgresql.select_player_id(ctx.author.id)[0]
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers)

        if response.status_code != 200:
            await ctx.send('Plese link a valid clan tag with the \'linkc\' command.')
            return

        with open('txt/clan.txt', 'r') as f:
            text = f.read()

        clan = response.json()
        profile_embed = discord.Embed(title=f'**{clan["name"]}{clan["tag"]}**', description=text.format(
            tag=clan['tag'][1:],

            ))
        await ctx.send(embed=profile_embed)

def setup(bot):
    bot.add_cog(Clan(bot))