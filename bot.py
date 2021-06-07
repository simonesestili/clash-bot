import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=';')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong!')


def token():
    with open('bot_token.txt', 'r') as file:
        token = file.readline().strip()
    return token


bot.run(token())