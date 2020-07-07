# Developers: Stashito, Thinkr3
# Feature: Literally returns "test" if .test
# Parameter: test
# Last Worked On: 08/06/2020

import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test(self, ctx):
        await ctx.send('test')

def setup(client):
    client.add_cog(Test(client))

