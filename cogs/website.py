# Developers: Stashito, Thinkr3
# Feature: Returns random website
# Parameter: command "website"
# Last Worked On: 07/06/2020

import random
import discord
import asyncio
import discord.ext
from discord.ext import commands

class Website(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def website(self, ctx): #if someone writes 'carnal, website'
        lines = []
        with open("urls.txt") as f:
            lines = [line.strip() for line in f]

        await ctx.send(str(random.choice(lines)))

def setup(client):
    client.add_cog(Website(client))