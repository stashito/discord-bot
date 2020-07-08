# Developers: Stashito, Thinkr3
# Feature: Narrates when a user joins a channel
# Parameter: ???
# Last Worked On: 08/06/2020

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

class Narrate(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def narrate(self, poop):
        pass

    
    @commands.command()
    async def join(self, ctx):
        await author.voice.channel.connect()





def setup(client):
    client.add_cog(Narrate(client))