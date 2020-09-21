#Python3
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot 
from config import *
from discord.utils import get
from random import randint


client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def hello (ctx):
    author = ctx.message.author.mention
    
    messages = [
        "You're kind of sus",
        f"How do you jump into the vent like {ctx.message.author.mention}",
        f"I saw {ctx.message.author.mention} running away from the body",
        f"Vote {ctx.message.author.mention}",
        f"Don't come to electric next round...",
        f"{author} was acting sus so I killed him",
        f"_Ihsaan starts chasing you..._",
        f"Self report, vote {author}",
        f"If it isnt {author} vote me out next round",
        f"who killed {author}",
        ]

    rnd_value = randint(0,len(messages) - 1)
    await ctx.send(messages[rnd_value])

@client.command()
async def play (ctx,arg):
    author = ctx.message.author.mention
    await ctx.send(f'@everyone \n {author} has initiated a game, get ready! \nCode: {arg}')
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command()
async def start (ctx):
    await ctx.send(f'SHHHHH...and do your tasks')
    voice_chat = ctx.author.voice.channel
    for member in voice_chat.members:
        await member.edit(mute = True)

@client.command()
async def discuss (ctx):
    await ctx.send (f'aight, discuss')
    voice_chat = ctx.author.voice.channel
    for member in voice_chat.members:
        await member.edit(mute = False)

@client.command()
async def leave(ctx):
    await ctx.send("_Bot was ejected ..._")
    time.sleep(2)
    await ctx.send("_2 imposters remain_")
    await ctx.voice_client.disconnect()

@client.event
async def on_voice_state_update(member,before, after):
    if member == client.user:
        return
    else:

        if before.channel is None and after.channel is not None:
            role = get(member.guild.roles, name="Among us ~ Crew")
            await member.add_roles(role)
            await member.guild.system_channel.send(f"{member.mention} has joined the station")
        if before.channel is not None and after.channel is None:
            role = get(member.guild.roles, name="Among us ~ Crew")
            await member.remove_roles(role)
            await member.guild.system_channel.send(f"{member.mention} has been ejected")
    


client.run(Token)
