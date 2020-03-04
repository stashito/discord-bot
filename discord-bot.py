import random
import discord
from discord.ext.commands import Bot
import asyncio
from discord.voice_client import VoiceClient
# import pynacl


BOT_PREFIX = ("carnal, ")
TOKEN = "TOKEN"

bot = Bot(command_prefix=BOT_PREFIX)

@bot.event
async def on_ready(): #what happens when it opens
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def website(ctx): #if someone writes 'carnal, website'
    lines = []
    with open("urls.txt") as f:
        lines = [line.strip() for line in f]

    await ctx.send(str(random.choice(lines)))


@bot.command(pass_context=True)
async def count(ctx, arg):
    await ctx.send(arg)


censored = {'nigger':'good samaritan',
            'Hitler':'fopdoogle',
            'dick':'doodle',
            'cock':'doodle',
            'penis':'doodle',
            'anus':'doodle',
            'mother fucker':'dad',
            'pendejo':'squiggle',
            'fuck':'tarnation',
            'nigga':'good samaritan',
            'gay' : 'happy',
            'damn' : 'gee golly',
            'lesbian' : 'gardyloo',
            'son of a bitch' : 'Jesus',
            'vagina' : 'rose',
            'basterd':'child out of wedlock',
            'ass' : 'pillion',
            'whore' : 'harlot',
            'bitch' : 'snap crackle pop',
            'shit' : 'flummery',
            'go to hell' : 'Prithee transport thyself to tarnation',
            'phuck':'balderdash',
            'joe':'joe mama'}


@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    bad = False
    new_sentence = " "
    for word, replacement in censored.items():
        if word in message.content:
            new_sentence = message.content.replace(word, replacement)
            bad = True

    if bad:
        await message.channel.send(message.author.mention + ": " + new_sentence)
        await message.delete(delay=None)
        bad = False

    #keep this at the end
    await bot.process_commands(message)


follow = None

@bot.command(pass_context=True)
async def follow(ctx, arg):
    global follow

    user_mapping = {}

    for guild in bot.guilds:
            for member in guild.members:
                user_mapping[member] = member.mention

    for key, value in user_mapping.items():
        if str(value) == arg.replace('!', ''):
            follow = key
    print("The follow command Works")


@bot.command(pass_context=True)
async def come(ctx):
    #initiliazles the the channel that the user is in.
    #Original Code: ctx.author.voice.channel
    channel = follow.voice.channel
    #joins to the user "Follow".
    await channel.connect()

#async def followUser():
    #voiceChannel = discord.follow.
    #await voiceChannel.join();


    #Works only when dictionary api is downloaded
#    if message.content.startswith('carnal, define '):
#        msg = ""
#        words = message.content.split('\n')
#        for i in words:
#            msg.join(dictionary.define(i))
#        message.channel.send(msg)



# main
# bot.bg_task = loop.create_task(followUser())

bot.run(TOKEN)
