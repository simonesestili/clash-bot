import discord, json
from discord.ext import commands
from cogs.utils import util

class Troops(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open('cogs/clash_data.json', 'r') as f: 
            self.data = json.load(f)


    @commands.command()
    async def barbarian(self, ctx, level='1'):
        name = 'barbarian'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Barbarian', level))


    @commands.command()
    async def archer(self, ctx, level='1'):
        name = 'archer'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Archer', level))


    @commands.command()
    async def giant(self, ctx, level='1'):
        name = 'giant'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Giant', level))


    @commands.command()
    async def goblin(self, ctx, level='1'):
        name = 'goblin'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Goblin', level))


    @commands.command()
    async def wallbreaker(self, ctx, level='1'):
        name = 'wallBreaker'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wall_Breaker', level))


    @commands.command()
    async def balloon(self, ctx, level='1'):
        name = 'balloon'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Balloon', level))


    @commands.command()
    async def wizard(self, ctx, level='1'):
        name = 'wizard'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wizard', level))


    @commands.command()
    async def healer(self, ctx, level='1'):
        name = 'healer'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Healer', level))


    @commands.command()
    async def dragon(self, ctx, level='1'):
        name = 'dragon'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dragon', level))


    @commands.command()
    async def pekka(self, ctx, level='1'):
        name = 'pekka'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/P.E.K.K.A', level))


    @commands.command()
    async def babydragon(self, ctx, level='1'):
        name = 'babyDragon'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Baby_Dragon/Home_Village', level))


    @commands.command()
    async def miner(self, ctx, level='1'):
        name = 'miner'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Miner', level))


    @commands.command()
    async def electrodragon(self, ctx, level='1'):
        name = 'electroDragon'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Electro_Dragon', level))


    @commands.command()
    async def yeti(self, ctx, level='1'):
        name = 'yeti'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Yeti', level))


    @commands.command()
    async def dragonrider(self, ctx, level='1'):
        name = 'dragonRider'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Dragon_Rider', level))


    @commands.command()
    async def minion(self, ctx, level='1'):
        name = 'minion'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Minion', level))


    @commands.command()
    async def hogrider(self, ctx, level='1'):
        name = 'hogRider'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Hog_Rider', level))

        
    @commands.command()
    async def valkyrie(self, ctx, level='1'):
        name = 'valkyrie'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Valkyrie', level))

        
    @commands.command()
    async def golem(self, ctx, level='1'):
        name = 'golem'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Golem', level))

        
    @commands.command()
    async def witch(self, ctx, level='1'):
        name = 'witch'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Witch', level))

        
    @commands.command()
    async def lavahound(self, ctx, level='1'):
        name = 'lavaHound'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Lava_Hound', level))

        
    @commands.command()
    async def bowler(self, ctx, level='1'):
        name = 'bowler'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Bowler', level))


    @commands.command()
    async def icegolem(self, ctx, level='1'):
        name = 'iceGolem'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Ice_Golem', level))


    @commands.command()
    async def headhunter(self, ctx, level='1'):
        name = 'headhunter'
        if level not in self.data['home']['troops'][name]: await ctx.send(f'**Please enter a valid level for** `{util.title(name)}`')

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


    @commands.command()
    async def rocketballoon(self, ctx):
        name = 'rocketBalloon'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name], util.title(name), 'https://clashofclans.fandom.com/wiki/Rocket_Balloon'))


    @commands.command()
    async def unicorn(self, ctx):
        name = 'unicorn'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name]['img'], util.title(name), 'https://clashofclans.fandom.com/wiki/Unicorn'))


    @commands.command()
    async def lassi(self, ctx):
        name = 'lassi'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name]['img'], util.title(name), 'https://clashofclans.fandom.com/wiki/L.A.S.S.I'))


    @commands.command()
    async def mightyyak(self, ctx):
        name = 'mightyYak'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name]['img'], util.title(name), 'https://clashofclans.fandom.com/wiki/Mighty_Yak'))


    @commands.command()
    async def electroowl(self, ctx):
        name = 'electroOwl'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name]['img'], util.title(name), 'https://clashofclans.fandom.com/wiki/Electro_Owl'))


    @commands.command()
    async def wallwrecker(self, ctx, level='1'):
        name = 'wallWrecker'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Wall_Wrecker', level))


    @commands.command()
    async def battleblimp(self, ctx, level='1'):
        name = 'battleBlimp'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Battle_Blimp', level))


    @commands.command()
    async def stoneslammer(self, ctx, level='1'):
        name = 'stoneSlammer'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Stone_Slammer', level))


    @commands.command()
    async def siegebarracks(self, ctx, level='1'):
        name = 'siegeBarracks'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Siege_Barracks', level))


    @commands.command()
    async def loglauncher(self, ctx, level='1'):
        name = 'logLauncher'

        await ctx.send(embed=util.embed(self.data['home']['troops'][name][level], util.title(name), 'https://clashofclans.fandom.com/wiki/Log_Launcher', level))


def setup(bot):
    bot.add_cog(Troops(bot))