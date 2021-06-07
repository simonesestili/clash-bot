import discord
import json
import requests
import os
from discord.ext import commands

bot = commands.Bot(command_prefix=';')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


bot.run(os.environ['BOT_TOKEN'])