import discord
from discord.ext import commands

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    #COMMAND
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(1000 * ctx.bot.latency)}ms')


def setup(bot):
    bot.add_cog(General(bot))