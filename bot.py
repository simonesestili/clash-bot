import discord
import json
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix=';')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


def token():
    with open('config.json', 'r') as f:
        return json.load(f)['token']


bot.run(token())