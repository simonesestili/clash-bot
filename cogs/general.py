import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    #EVENTS
    @commands.Cog.listener(hidden=True)
    async def on_ready():
        print('READY')


def setup(bot):
    bot.add_got(General(bot))