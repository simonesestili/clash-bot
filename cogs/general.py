import discord
from discord.ext import commands
from cogs.SQL import postgresql

class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    #COMMAND
    @commands.command()
    async def unlink(self, ctx):
        if not postgresql.select_player_id(ctx.author.id):
            await ctx.send('**You currently have no clash of clans account linked.**')    
        else:   
            postgresql.unlink_user(ctx.author.id)
            await ctx.send('**Successfully unlinked your account.**')  
        


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'**Pong! {round(1000 * ctx.bot.latency)}ms**')


    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=50):
        await ctx.channel.purge(limit=amount+1)



def setup(bot):
    bot.add_cog(General(bot))