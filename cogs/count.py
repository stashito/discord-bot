# Developers: Stashito, Thinkr3
# Feature: Checks how many times a user has said a certain words 
# Parameter: String (word)
# Last Worked On: 08/06/2020

import discord
from discord.ext import commands
from sys import stdout

class Count(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.LIMIT = 1000000
        self.isCounting = False


    @commands.command(pass_context=True)
    async def count(self, ctx, arg):
        oldest = ""
        user_count = {}
        count = 0
        last_message = ""
        self.isCounting
        if self.isCounting:
            await ctx.send("Already processing messages")
            return
        await ctx.send("Processing messages...")
        self.isCounting = True
        await ctx.send("Parsed through 0 messages!")

        progress_bar = ctx.channel.last_message
        async for message in ctx.channel.history(limit=self.LIMIT):
            if count % 1000 == 0:
                await progress_bar.edit(content="Parsed through " + str(count) + " messages!")


            if str(arg) in message.content:
                if message.author.name not in user_count:
                    user_count[message.author.name] = 0
                user_count[message.author.name] += message.content.count(str(arg))
                oldest = message.created_at
            count += 1
            stdout.write("\r Parsed through messages: " + str(count))
            stdout.flush()
        stdout.write("\n")

        user_count = {k: v for k, v in sorted(user_count.items(), key=lambda item: item[1])}
        results = "========== " + arg + " ==========\n"
        for i, j in user_count.items():
            results += i + ": " + str(j) + "\n"
        await ctx.send(results)
        self.isCounting = False
        # await ctx.send(oldest)

def setup(client):
    client.add_cog(Count(client))
