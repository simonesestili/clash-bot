import discord, json
from discord.ext import commands
from cogs.utils import util

class Spells(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('cogs/clash_data.json', 'r') as f: 
            self.data = json.load(f)

    @commands.command()
    async def lightning(self, ctx):
        name = 'lightning'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Lightning_Spell'))


    @commands.command()
    async def healing(self, ctx):
        name = 'healing'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Healing_Spell'))


    @commands.command()
    async def rage(self, ctx):
        name = 'rage'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Rage_Spell'))


    @commands.command()
    async def jump(self, ctx):
        name = 'jump'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Jump_Spell'))


    @commands.command()
    async def freeze(self, ctx):
        name = 'freeze'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Freeze_Spell'))


    @commands.command()
    async def clone(self, ctx):
        name = 'clone'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Clone_Spell'))


    @commands.command()
    async def invisibility(self, ctx):
        name = 'invisibility'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Invisibility_Spell'))


    @commands.command()
    async def poison(self, ctx):
        name = 'poison'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Poison_Spell'))


    @commands.command()
    async def earthquake(self, ctx):
        name = 'earthquake'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Earthquake_Spell'))


    @commands.command()
    async def haste(self, ctx):
        name = 'haste'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Haste_Spell'))


    @commands.command()
    async def skeleton(self, ctx):
        name = 'skeleton'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Skeleton_Spell'))


    @commands.command()
    async def bat(self, ctx):
        name = 'bat'

        await ctx.send(embed=util.embed(self.data['home']['spells'][name]["img"], util.title(name), 'https://clashofclans.fandom.com/wiki/Bat_Spell'))

    
def setup(bot):
    bot.add_cog(Spells(bot))