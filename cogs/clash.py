import discord, json
from discord.ext import commands


class Clash(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        with open('cogs/clash_data.json', 'r') as f: 
            self.data = json.load(f)


    def embed(self, data, name, url, level):
        embed = discord.Embed(title=f'__{name} {level}__', url=url)
        embed.set_image(url=data)
        return embed


    def title(self, text):
        title = ''
        for let in text:
            if let.isupper():
                title += ' '
            title += let
        return title[0].upper() + title[1:]


    @commands.command()
    async def townhall(self, ctx, level):
        name = 'townHall'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Town_Hall', level))


    @commands.command()
    async def cannon(self, ctx, level):
        name = 'cannon'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Cannon/Home_Village', level))


    @commands.command()
    async def archertower(self, ctx, level):
        name = 'archerTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Archer_Tower', level))


    @commands.command()
    async def mortar(self, ctx, level):
        name = 'mortar'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Mortar', level))


    @commands.command()
    async def airdefense(self, ctx, level):
        name = 'airDefense'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Air_Defense', level))

    
    @commands.command()
    async def wizardtower(self, ctx, level):
        name = 'wizardTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Wizard_Tower', level))

    
    @commands.command()
    async def airsweeper(self, ctx, level):
        name = 'airSweeper'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Air_Sweeper', level))

    
    @commands.command()
    async def hiddentesla(self, ctx, level):
        name = 'hiddenTesla'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Hidden_Tesla/Home_Village', level))

    
    @commands.command()
    async def bombtower(self, ctx, level):
        name = 'bombTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Bomb_Tower', level))

    
    @commands.command()
    async def xbow(self, ctx, level):
        name = 'xBow'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/X-Bow', level))

    
    @commands.command()
    async def infernotower(self, ctx, level):
        name = 'infernoTower'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Inferno_Tower', level))

    
    @commands.command()
    async def eagleartillery(self, ctx, level):
        name = 'eagleArtillery'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Eagle_Artillery', level))

    
    @commands.command()
    async def scattershot(self, ctx, level):
        name = 'scattershot'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Scattershot', level))

    
    @commands.command()
    async def wall(self, ctx, level):
        name = 'wall'
        if level not in self.data['home']['buildings']['defenses'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['defenses'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Walls/Home_Village', level))

    
    @commands.command()
    async def goldmine(self, ctx, level):
        name = 'goldMine'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Gold_Mine/Home_Village', level))

    
    @commands.command()
    async def goldstorage(self, ctx, level):
        name = 'goldStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Gold_Storage/Home_Village', level))

    
    @commands.command()
    async def elixircollector(self, ctx, level):
        name = 'elixirCollector'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Elixir_Collector/Home_Village', level))

    
    @commands.command()
    async def elixirstorage(self, ctx, level):
        name = 'elixirStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Elixir_Storage/Home_Village', level))

    
    @commands.command()
    async def darkelixirdrill(self, ctx, level):
        name = 'darkElixirDrill'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Elixir_Drill', level))

    
    @commands.command()
    async def darkelixirstorage(self, ctx, level):
        name = 'darkElixirStorage'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Elixir_Storage', level))

    
    @commands.command()
    async def clancastle(self, ctx, level):
        name = 'clanCastle'
        if level not in self.data['home']['buildings']['resources'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['resources'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Clan_Castle', level))

    
    @commands.command()
    async def armycamp(self, ctx, level):
        name = 'armyCamp'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Army_Camp/Home_Village', level))

    
    @commands.command()
    async def barracks(self, ctx, level):
        name = 'barracks'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Barracks', level))

    
    @commands.command()
    async def darkbarracks(self, ctx, level):
        name = 'darkBarracks'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Barracks', level))

    
    @commands.command()
    async def laboratory(self, ctx, level):
        name = 'laboratory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Laboratory', level))

    
    @commands.command()
    async def spellfactory(self, ctx, level):
        name = 'spellFactory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Spell_Factory', level))

    
    @commands.command()
    async def darkspellfactory(self, ctx, level):
        name = 'darkSpellFactory'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Dark_Spell_Factory', level))

    
    @commands.command()
    async def workshop(self, ctx, level):
        name = 'workshop'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Workshop', level))

    
    @commands.command()
    async def pethouse(self, ctx, level):
        name = 'petHouse'
        if level not in self.data['home']['buildings']['army'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['buildings']['army'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Pet_House', level))


    @commands.command()
    async def barbarian(self, ctx, level):
        name = 'barbarian'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Barbarian', level))


    @commands.command()
    async def archer(self, ctx, level):
        name = 'archer'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Archer', level))


    @commands.command()
    async def giant(self, ctx, level):
        name = 'giant'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Giant', level))


    @commands.command()
    async def goblin(self, ctx, level):
        name = 'goblin'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Goblin', level))


    @commands.command()
    async def wallbreaker(self, ctx, level):
        name = 'wallBreaker'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Wall_Breaker', level))


    @commands.command()
    async def balloon(self, ctx, level):
        name = 'balloon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Balloon', level))


    @commands.command()
    async def wizard(self, ctx, level):
        name = 'wizard'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Wizard', level))


    @commands.command()
    async def healer(self, ctx, level):
        name = 'healer'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Healer', level))


    @commands.command()
    async def dragon(self, ctx, level):
        name = 'dragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Dragon', level))


    @commands.command()
    async def pekka(self, ctx, level):
        name = 'pekka'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/P.E.K.K.A', level))


    @commands.command()
    async def babydragon(self, ctx, level):
        name = 'babyDragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Baby_Dragon/Home_Village', level))


    @commands.command()
    async def miner(self, ctx, level):
        name = 'miner'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Miner', level))


    @commands.command()
    async def electrodragon(self, ctx, level):
        name = 'electroDragon'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Electro_Dragon', level))


    @commands.command()
    async def yeti(self, ctx, level):
        name = 'yeti'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Yeti', level))


    @commands.command()
    async def minion(self, ctx, level):
        name = 'minion'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Minion', level))


    @commands.command()
    async def hogrider(self, ctx, level):
        name = 'hogRider'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Hog_Rider', level))

        
    @commands.command()
    async def valkyrie(self, ctx, level):
        name = 'valkyrie'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Valkyrie', level))

        
    @commands.command()
    async def golem(self, ctx, level):
        name = 'golem'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Golem', level))

        
    @commands.command()
    async def witch(self, ctx, level):
        name = 'witch'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Witch', level))

        
    @commands.command()
    async def lavahound(self, ctx, level):
        name = 'lavaHound'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Lava_Hound', level))

        
    @commands.command()
    async def bowler(self, ctx, level):
        name = 'bowler'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Bowler', level))


    @commands.command()
    async def icegolem(self, ctx, level):
        name = 'iceGolem'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Ice_Golem', level))


    @commands.command()
    async def headhunter(self, ctx, level):
        name = 'headhunter'
        if level not in self.data['home']['troops'][name]: return

        await ctx.send(embed=self.embed(self.data['home']['troops'][name][level], self.title(name), 'https://clashofclans.fandom.com/wiki/Headhunter', level))

        
    


    

    
    

    
    

def setup(bot):
    bot.add_cog(Clash(bot))