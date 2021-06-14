import discord, json
from discord.ext import commands
from cogs.utils import util

class Troops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('cogs/clash_data.json', 'r') as f: 
            self.data = json.load(f)


    @commands.command()
    async def barbarian(self, ctx, level):
        name = 'barbarian'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Barbarian', level))


    @commands.command()
    async def archer(self, ctx, level):
        name = 'archer'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Archer', level))


    @commands.command()
    async def giant(self, ctx, level):
        name = 'giant'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Giant', level))


    @commands.command()
    async def goblin(self, ctx, level):
        name = 'goblin'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Goblin', level))


    @commands.command()
    async def wallbreaker(self, ctx, level):
        name = 'wallBreaker'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wall_Breaker', level))


    @commands.command()
    async def balloon(self, ctx, level):
        name = 'balloon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Balloon', level))


    @commands.command()
    async def wizard(self, ctx, level):
        name = 'wizard'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wizard', level))


    @commands.command()
    async def healer(self, ctx, level):
        name = 'healer'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Healer', level))


    @commands.command()
    async def dragon(self, ctx, level):
        name = 'dragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dragon', level))


    @commands.command()
    async def pekka(self, ctx, level):
        name = 'pekka'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/P.E.K.K.A', level))


    @commands.command()
    async def babydragon(self, ctx, level):
        name = 'babyDragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Baby_Dragon/Home_Village', level))


    @commands.command()
    async def miner(self, ctx, level):
        name = 'miner'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Miner', level))


    @commands.command()
    async def electrodragon(self, ctx, level):
        name = 'electroDragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Electro_Dragon', level))


    @commands.command()
    async def yeti(self, ctx, level):
        name = 'yeti'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Yeti', level))


    @commands.command()
    async def minion(self, ctx, level):
        name = 'minion'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Minion', level))


    @commands.command()
    async def hogrider(self, ctx, level):
        name = 'hogRider'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Hog_Rider', level))

        
    @commands.command()
    async def valkyrie(self, ctx, level):
        name = 'valkyrie'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Valkyrie', level))

        
    @commands.command()
    async def golem(self, ctx, level):
        name = 'golem'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Golem', level))

        
    @commands.command()
    async def witch(self, ctx, level):
        name = 'witch'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Witch', level))

        
    @commands.command()
    async def lavahound(self, ctx, level):
        name = 'lavaHound'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Lava_Hound', level))

        
    @commands.command()
    async def bowler(self, ctx, level):
        name = 'bowler'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Bowler', level))


    @commands.command()
    async def icegolem(self, ctx, level):
        name = 'iceGolem'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Ice_Golem', level))


    @commands.command()
    async def headhunter(self, ctx, level):
        name = 'headhunter'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Headhunter', level))


    @commands.command()
    async def superbarbarian(self, ctx):
        name = 'superBarbarian'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Barbarian'))


    @commands.command()
    async def superarcher(self, ctx):
        name = 'superArcher'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Archer'))


    @commands.command()
    async def supergiant(self, ctx):
        name = 'superGiant'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Giant'))


    @commands.command()
    async def sneakygoblin(self, ctx):
        name = 'sneakyGoblin'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Sneaky_Goblin'))


    @commands.command()
    async def superwallbreaker(self, ctx):
        name = 'superWallBreaker'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Wall_Breaker'))


    @commands.command()
    async def superwizard(self, ctx):
        name = 'superWizard'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Wizard'))


    @commands.command()
    async def infernodragon(self, ctx):
        name = 'infernoDragon'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Inferno_Dragon'))


    @commands.command()
    async def superminion(self, ctx):
        name = 'superMinion'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Minion'))


    @commands.command()
    async def supervalkyrie(self, ctx):
        name = 'superValkyrie`'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Valkyrie'))


    @commands.command()
    async def superwitch(self, ctx):
        name = 'superWitch'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Super_Witch'))


    @commands.command()
    async def icehound(self, ctx):
        name = 'iceHound'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Ice_Hound'))


def setup(bot):
    bot.add_cog(Troops(bot))