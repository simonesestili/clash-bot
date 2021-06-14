import os
import requests
import discord
from discord.ext import commands
import psycopg2
from cogs.SQL import postgresql
from cogs.utils import util

os.environ['http_proxy'] = os.environ.get('FIXIE_URL', '')
os.environ['https_proxy'] = os.environ.get('FIXIE_URL', '')

headers = {
    'Accept': 'application/json',
    'authorization': 'Bearer ' + os.environ['COC_TOKEN']
}

class Clan(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def format_donations(self, num):
        return ' ' * (6 - len(num)) + num

    @commands.command()
    async def clan(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]
        if not tag:
            tag = postgresql.select_player_id(ctx.author.id)
            if not tag:
                await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid clan tag following the clan command.**')
                return
            response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag[0]}', headers=headers)
            tag = response.json()['clan']['tag'][1:]        
        
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers)

        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid clan tag following the clan command.**')
            return

        with open('txt/clan.txt', 'r') as f:
            text = f.read()

        clan = response.json()
        
        type_ = clan['type'].capitalize()
        if type_ == 'Inviteonly': type_ = 'Invite Only'
        if type_ == 'Anyonecanjoin': type_ = 'Anyone Can Join'
        
        freq = clan['warFrequency'].capitalize()
        if clan['warFrequency'].capitalize() == 'Twiceaweek': freq = 'Twice a Week'
        elif clan['warFrequency'].capitalize() == 'Onceaweek': freq = 'Once a Week'
        elif clan['warFrequency'].capitalize() == 'Notset': freq = 'Not Set'

        profile_embed = discord.Embed(title=f'**{clan["name"]}{clan["tag"]}**', description=text.format(
            th=util.get_th(clan['requiredTownhallLevel']),
            tag=clan['tag'][1:],
            desc=clan['description'],
            lvl=clan['clanLevel'],
            cwl=clan['warLeague']['name'],
            clan_pts=clan['clanPoints'],
            versus_pts=clan['clanVersusPoints'],
            location=clan['location']['name'],
            lang='Not Set' if 'chatLanguage' not in clan else clan['chatLanguage']['name'],
            type=type_,
            clan_required_trophies=clan['requiredTrophies'],
            versus_required_trophies=clan['requiredVersusTrophies'],
            req_th=clan['requiredTownhallLevel'],
            war_wins=clan['warWins'],
            war_losses='War Log Private' if 'warLosses' not in clan else clan['warLosses'],
            war_ties='War Log Private' if 'warTies' not in clan else clan['warTies'],
            war_frequency=freq 
            ))
        await ctx.send(embed=profile_embed)


    @commands.command()
    async def stats(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]
        if not tag:
            tag = postgresql.select_player_id(ctx.author.id)
            if not tag:
                await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the stats command.**')
                return
            tag = postgresql.select_player_id(ctx.author.id)[0]
            response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
            tag = response.json()['clan']['tag'][1:]        
        
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers)

        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the stats command.**')
            return

        with open('txt/stats.txt', 'r') as f:
            text = f.read()

        name = response.json()['name']
        tag = response.json()['tag']
        members = response.json()['memberList']
        num_members = response.json()['members']
        th_avg = trophy_avg = vs_trophy_avg = exp_avg = dono_avg = 0

        for member in members:
            th_avg = th_avg + util.th_by_tag(member['tag'][1:])
            trophy_avg = trophy_avg + member['trophies']
            vs_trophy_avg = trophy_avg + member['versusTrophies']
            exp_avg = exp_avg + member['expLevel']
            dono_avg = dono_avg + member['donations']

        th_avg = th_avg / num_members
        trophy_avg = trophy_avg / num_members
        vs_trophy_avg = vs_trophy_avg / num_members
        exp_avg = exp_avg / num_members
        dono_avg = dono_avg / num_members

        profile_embed = discord.Embed(title=f'**{name}{tag}**', description=text.format(
            th=util.get_th(round(th_avg)),
            th_avg=round(th_avg),
            trophy_avg=round(trophy_avg),
            vs_trophy_avg=round(vs_trophy_avg),
            exp_avg=round(exp_avg),
            dono_avg=round(dono_avg)
            ))

        await ctx.send(embed=profile_embed)


    @commands.command()
    async def donations(self, ctx, tag=''):
        tag = tag.upper()
        if tag.startswith('#'): tag = tag[1:]
        if not tag:
            tag = postgresql.select_player_id(ctx.author.id)
            if not tag:
                await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the stats command.**')
                return
            tag = postgresql.select_player_id(ctx.author.id)[0]
            response = requests.get(f'https://api.clashofclans.com/v1/players/%23{tag}', headers=headers)
            tag = response.json()['clan']['tag'][1:]        
        
        response = requests.get(f'https://api.clashofclans.com/v1/clans/%23{tag}', headers=headers)

        if response.status_code != 200:
            await ctx.send('**Please link a valid player tag with the \'link\' command or enter a valid tag following the stats command.**')
            return

        members = sorted(response.json()['memberList'], key=lambda member: member['donations'], reverse=True)

        table = ' #    DON    REC  NAME '
        num = 1
        for member in members:
            disp_num = str(num) if num > 9 else ' ' + str(num)
            table += f"\n{disp_num} {self.format_donations(str(member['donations']))} {self.format_donations(str(member['donationsReceived']))}  {member['name']}"
            num = num + 1
        
        embed = discord.Embed(title=f'**{response.json()["name"]}{response.json()["tag"]}**', description='```'+table+'```')
        await ctx.send(embed=embed)
            

def setup(bot):
    bot.add_cog(Clan(bot))