# Developers: Stashito, Thinkr3
# Feature: Censors certain blasphemous words into their PG variant
# Parameter: None
# Toggle Parameter: toggle censorship (flips between true and false)
# Last Worked On: 08/07/2020

import discord
from discord.ext import commands

class Censor(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.censor = True
        self.censored = {'Hitler':'fopdoodle',
            'dick':'doodle',
            'cock':'doodle',
            'penis':'doodle',
            'ween':'doodle',
            'anus':'doodle',
            'mother fucker':'dad',
            'pendejo':'squiggle',
            'fuck':'tarnation',
            'faggot':'happy',
            'murder':'compliment',
            'black man':'good samaritan',
            'cotton':'flowers',
            'nigga':'good samaritan',
            'nigger':'good samaritan',
            'gay' : 'happy',
            'damn' : 'gee golly',
            'lesbian' : 'gardyloo',
            'son of a bitch' : 'Jesus',
            'vagina' : 'rose',
            'bastard':'child out of wedlock',
            'ass' : 'pillion',
            'whore' : 'harlot',
            'bitch' : 'snap crackle pop',
            'shit' : 'flummery',
            'go to hell' : 'Prithee transport thyself to tarnation',
            'phuck':'balderdash',
            'joe':'jerome mama',
            'nino minecraft': 'nigger',
            'trap':'man',
            'traps':'men',
            'stinky':'yummy',
            'post':'square',
            'ugly':'cute',
            'cancer':'healthy',
            'peyton':'geyton',
            'ez':'that was really hard',
            'rodrigo':'simp',
            'milk':'kefir',
            'dumpling':'pierogi',
            'retard':'smart',
            'jerk':'cut',
            'not funny':'funny',
            'instagram':'pornhub'}


    @commands.command()
    async def toggle(self, ctx, arg):
        if arg == "censorship":
            self.censor = not self.censor
        await ctx.send("Censorship is now: " + str(censor))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.client.user.id:
            return

        if self.censor:
            bad = False
            new_sentence = message.content
            for phrase in new_sentence.split(" "):
                for word, replacement in self.censored.items():
                    if word in new_sentence and ("carnal, " not in new_sentence) and (not (message.id == self.client.user.id)):
                        new_sentence = new_sentence.replace(word, replacement)
                        bad = True

            if bad:
                await message.channel.send(message.author.mention + ": " + new_sentence)
                await message.delete(delay=None)
                bad = False


def setup(client):
    client.add_cog(Censor(client))
