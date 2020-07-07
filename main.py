# Developers: Stashito, Thinkr3, Dondischj
# Feature: What happens when it opens
# Last Worked On: 07/06/2020

import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = "carnal, ")

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

client.run('Njc3Njg5Nzk0OTY0NDg4MTky.XwO6Hw.9A5U5uYwkQ9bmVSW-8XmdhxbJdM')
