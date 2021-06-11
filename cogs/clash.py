import discord, json
from discord.ext import commands


class Clash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def townhall(self, ctx, level):
        with open('cogs/clash_data.json', 'r') as f:
            data = json.load(f)
        
        if level not in data["buildings"]['townHall']: 
            return

        embed = discord.Embed(title=f'__Town Hall {level}__', url='https://clashofclans.fandom.com/wiki/Town_Hall')
        embed.set_image(url=data["buildings"]["townHall"][level])

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Clash(bot))