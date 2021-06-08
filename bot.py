import discord
import requests
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

#load all cogs
for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f'cogs.{cog[:-3]}')

bot.run(os.environ['BOT_TOKEN'])