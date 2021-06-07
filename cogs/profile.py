import os
import discord
from discord.ext import commands


class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    #EVENTS


    #COMMANDS
    @commands.command()
    async def link(self, ctx, tag=''):
        pass



def setup(bot):
    bot.add_cog(Profile(bot))

