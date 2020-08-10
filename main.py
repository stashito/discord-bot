# Developers: Stashito, Thinkr3, Dondischj
# Feature: What happens when it opens
# Last Worked On: 08/06/2020

import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "cl ")

@commands.Cog.listener()
async def on_ready(): #Launch Method
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
with open("token.txt", "r") as f:
    client.run(f.read())
