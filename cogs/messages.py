# Developers: Stashito, Thinkr3
# Feature: Counts total messages in the discord channel
# Parameter: None
# Last Worked On: 07/06/2020

import discord
from discord.ext import commands
from sys import stdout

class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.LIMIT = 100000
        self.isCounting = False

    @commands.command(pass_context=True)
    async def messages(self, ctx):
        if not self.isCounting:
            self.isCounting = True
            user_count = {}
            count = 0
            async for message in ctx.channel.history(limit=self.LIMIT):
                if message.author.name not in user_count:
                    user_count[message.author.name] = 0
                user_count[message.author.name] += 1
                count += 1
                stdout.write("\r Parsed through messages: " + str(count))
                stdout.flush()
            stdout.write("\n")


            user_count = {k: v for k, v in sorted(user_count.items(), key=lambda item: item[1])}
            results = "========== Messages per User ==========\n"
            for i, j in user_count.items():
                results += i + ": " + str(j) + "\n"
            await ctx.send(results)
            self.isCounting = False

        else:
            await ctx.send("Already processing messages")
            return

def setup(client):
    client.add_cog(Messages(client))
