# Developers: Stashito, Thinkr3
# Feautures: Nothing this is shit
# Developing Feautures: Follow, count
# Depricated Feautures: Speak, translate, synonymize, antonymize
# Last Worked On: 09/03/2020

import random, discord, asyncio
from discord.ext.commands import Bot
from discord.ext import tasks
# from PyDictionary import PyDictionary
from discord.voice_client import VoiceClient
from sys import stdout



# dictionary=PyDictionary()

BOT_PREFIX = ("carnal, ")
TOKEN = "Njc3Njg5Nzk0OTY0NDg4MTky.XwO6Hw.9A5U5uYwkQ9bmVSW-8XmdhxbJdM"

bot = Bot(command_prefix=BOT_PREFIX)

@commands.Cog.listener()
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


censored = {'Hitler':'fopdoodle',
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

censor = True
@bot.command(pass_context=True)
async def toggle(ctx, arg):
    global censor
    if arg == "censorship":
        censor = not censor
    await ctx.send("Censorship is now: " + str(censor))


@bot.command(pass_context=True)
async def define(ctx, arg):
    for i in dictionary.meaning(arg):
        print(i)
    await ctx.send(dictionary.meaning(arg))

LIMIT = 1000000
isCounting = False


@bot.command(pass_context=True)
async def count(ctx, arg):
    oldest = ""
    user_count = {}
    count = 0
    last_message = ""
    global isCounting
    if isCounting:
        await ctx.send("Already processing messages")
        return
    await ctx.send("Processing messages...")
    isCounting = True
    await ctx.send("Parsed through 0 messages!")

    progress_bar = ctx.channel.last_message
    async for message in ctx.channel.history(limit=LIMIT):
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
    isCounting = False
    # await ctx.send(oldest)

@bot.command(pass_context=True)
async def messages(ctx):
    user_count = {}
    count = 0
    async for message in ctx.channel.history(limit=LIMIT):
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




@bot.event
async def on_message(message):
    global censor
    if message.author.id == bot.user.id:
        return

    if censor:
        bad = False
        new_sentence = message.content
        for phrase in new_sentence.split(" "):
            for word, replacement in censored.items():
                if word in new_sentence and ("carnal, " not in new_sentence) and (not (message.id == bot.user.id)):
                    new_sentence = new_sentence.replace(word, replacement)
                    bad = True

        if bad:
            await message.channel.send(message.author.mention + ": " + new_sentence)
            await message.delete(delay=None)
            bad = False

        # Google API not working anymore, its a paid service now. $1 USD per 50,000 characters translated.
    # if speaking:
    #     words = message.content.split(" ")
    #     print(words)
    #     for i in words:
    #         print(i)
    #         await message.channel.send(dictionary.translate(i, language))
    #keep this at the end
    await bot.process_commands(message)




# follow = None
# isFollowing = False
#
# @bot.command(pass_context=True)
# async def follow(ctx, arg):
#     global follow
#     user_mapping = {}
#
#     #makes a 2d arrays that assigns mention to userID.
#     for guild in bot.guilds:
#             for member in guild.members:
#                 user_mapping[member] = member.mention
#
#     for key, value in user_mapping.items():
#         if str(value) == arg.replace('!', ''):
#             follow = key
#             come.start()
#             print("happened")
#     print("The follow command Works")
#
#  @bot.command(pass_context=True)
#  async def stop(ctx, arg):
#      if arg == "following":
#          isFollowing = False
#
#
# @tasks.loop(seconds=5.0)
# async def come():
#     print(True)
#     print(follow.voice.channel)
#     #joins to the user "Follow".
#     await follow.voice.channel.connect()
#
# async def followUser():
#     voiceChannel = discord.follow.
#     await voiceChannel.join();
#
#
#

bot.run(TOKEN)
