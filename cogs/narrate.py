# Developers: Stashito, Thinkr3
# Feature: Narrates when a user joins a channel (WIP)
# Parameter: "join" and "leave"
# Last Worked On: 08/09/2020

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

class Narrate(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.channel = None
        self.current_memberlist = []
        self.new_memberlist = []
    
    @commands.Cog.listener()
    async def narrate(self, ctx):
        pass

    @commands.command()
    async def leave(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect()
        self.current_memberlist = []

    @commands.command()
    async def join(self, ctx):
        await ctx.author.voice.channel.connect()
        self.channel = ctx.author.voice.channel
        self.current_memberlist = self.channel.members
        print(self.current_memberlist)

    @commands.command()
    async def compare(self, ctx):
        self.new_memberlist = self.channel.members
        if len(self.current_memberlist) != len(self.new_memberlist):
            if len(self.current_memberlist) > len(self.new_memberlist):
                print(list(set(self.current_memberlist) - set(self.new_memberlist)))
                #say(list(set(self.current_memberlist) - set(self.new_memberlist)))
            elif len(self.current_memberlist) < len(self.new_memberlist):
                print(list(set(self.new_memberlist) - set(self.current_memberlist)))
                #say(self, ctx, list(set(self.new_memberlist) - set(self.current_memberlist)))
            self.current_memberlist = self.channel.members
        
    @commands.command()
    async def say(self, ctx, param):
        guild = ctx.guild
        voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
        audio_source = discord.FFmpegPCMAudio('msg.mp3')
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

def setup(client):
    client.add_cog(Narrate(client))