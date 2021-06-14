import discord, json
from discord.ext import commands
from cogs.utils import util

class Buildings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('cogs/clash_data.json', 'r') as f: 
            self.data = json.load(f)

    
    @commands.command()
    async def townhall(self, ctx, level):
        name = 'townHall'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Town_Hall', level))


    @commands.command()
    async def cannon(self, ctx, level):
        name = 'cannon'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Cannon/Home_Village', level))


    @commands.command()
    async def archertower(self, ctx, level):
        name = 'archerTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Archer_Tower', level))


    @commands.command()
    async def mortar(self, ctx, level):
        name = 'mortar'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Mortar', level))


    @commands.command()
    async def airdefense(self, ctx, level):
        name = 'airDefense'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Air_Defense', level))

    
    @commands.command()
    async def wizardtower(self, ctx, level):
        name = 'wizardTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wizard_Tower', level))

    
    @commands.command()
    async def airsweeper(self, ctx, level):
        name = 'airSweeper'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Air_Sweeper', level))

    
    @commands.command()
    async def hiddentesla(self, ctx, level):
        name = 'hiddenTesla'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Hidden_Tesla/Home_Village', level))

    
    @commands.command()
    async def bombtower(self, ctx, level):
        name = 'bombTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Bomb_Tower', level))

    
    @commands.command()
    async def xbow(self, ctx, level):
        name = 'xBow'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/X-Bow', level))

    
    @commands.command()
    async def infernotower(self, ctx, level):
        name = 'infernoTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Inferno_Tower', level))

    
    @commands.command()
    async def eagleartillery(self, ctx, level):
        name = 'eagleArtillery'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Eagle_Artillery', level))

    
    @commands.command()
    async def scattershot(self, ctx, level):
        name = 'scattershot'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Scattershot', level))

    
    @commands.command()
    async def wall(self, ctx, level):
        name = 'wall'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['defenses'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Walls/Home_Village', level))

    
    @commands.command()
    async def goldmine(self, ctx, level):
        name = 'goldMine'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Gold_Mine/Home_Village', level))

    
    @commands.command()
    async def goldstorage(self, ctx, level):
        name = 'goldStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Gold_Storage/Home_Village', level))

    
    @commands.command()
    async def elixircollector(self, ctx, level):
        name = 'elixirCollector'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Elixir_Collector/Home_Village', level))

    
    @commands.command()
    async def elixirstorage(self, ctx, level):
        name = 'elixirStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Elixir_Storage/Home_Village', level))

    
    @commands.command()
    async def darkelixirdrill(self, ctx, level):
        name = 'darkElixirDrill'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill', level))

    
    @commands.command()
    async def darkelixirstorage(self, ctx, level):
        name = 'darkElixirStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Elixir_Storage', level))

    
    @commands.command()
    async def clancastle(self, ctx, level):
        name = 'clanCastle'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['resources'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Clan_Castle', level))

    
    @commands.command()
    async def armycamp(self, ctx, level):
        name = 'armyCamp'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Army_Camp/Home_Village', level))

    
    @commands.command()
    async def barracks(self, ctx, level):
        name = 'barracks'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Barracks', level))

    
    @commands.command()
    async def darkbarracks(self, ctx, level):
        name = 'darkBarracks'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Barracks', level))

    
    @commands.command()
    async def laboratory(self, ctx, level):
        name = 'laboratory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Laboratory', level))

    
    @commands.command()
    async def spellfactory(self, ctx, level):
        name = 'spellFactory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Spell_Factory', level))

    
    @commands.command()
    async def darkspellfactory(self, ctx, level):
        name = 'darkSpellFactory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Spell_Factory', level))

    
    @commands.command()
    async def workshop(self, ctx, level):
        name = 'workshop'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Workshop', level))

    
    @commands.command()
    async def pethouse(self, ctx, level):
        name = 'petHouse'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['buildings']['army'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Pet_House', level))


def setup(bot):
    bot.add_cog(Buildings(bot))
