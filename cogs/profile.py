import os
import requests
import discord
from discord.ext import commands
import psycopg2

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
    @commands.command()
    async def link(self, ctx, tag=''):
        if tag.startswith('#'):
            tag = tag[1:]
        response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
        if response.status_code != 200:
            await ctx.send('Plese enter a valid player tag!')
        
        conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASS'], host=os.environ['DB_HOST'])
        with conn:
            with conn.cursor() as cur:
                cur.execute(f'INSERT IGNORE INTO user_tags (discord_id, profile-tag) VALUES (\'{ctx.message.author.id}\', \'{tag}\')')
        conn.close()
        




def setup(bot):
    bot.add_cog(Profile(bot))

