import discord
import requests
import os
from discord.ext import commands

# class CustomHelp(commands.HelpCommand):

#     def __init__(self):
#         super().__init__()


#     async def send_bot_help(self, mapping):
#         help = ''
#         for cog in mapping:
#             help += f'**{cog.qualified_name}:**\n'
#             for command in cog.get_commands()


#     async def send_cog_help(self, cog):
#         return await super().send_cog_help(cog)


#     async def send_group_help(self, group):
#         return await super().send_group_help(group)


#     async def send_command_help(self, command):
#         return await super().send_command_help(command)


bot = commands.Bot(command_prefix='.')

#load all cogs
for cog in os.listdir('./cogs'):
    if cog.endswith('.py'):
        bot.load_extension(f'cogs.{cog[:-3]}')

bot.run(os.environ['BOT_TOKEN'])