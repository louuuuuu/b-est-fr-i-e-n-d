import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import random
import sys
import re
import requests
import json
import urllib
from bs4 import BeautifulSoup
import requests
from discord.voice_client import VoiceClient
import praw 


Bot = commands.Bot(command_prefix="%")


Bot.remove_command("help")
Bot.load_extension('help')
Bot.load_extension('8ball')
Bot.load_extension('avatar')
Bot.load_extension('maths')
Bot.load_extension('roleplay')
Bot.load_extension('dice')
Bot.load_extension('yomumma')
Bot.load_extension('coinflip')
Bot.load_extension('mod')
Bot.load_extension('search')
Bot.load_extension('reddit')
Bot.load_extension('rps')
Bot.load_extension('money')
Bot.load_extension('emote')
Bot.load_extension('code')
Bot.load_extension('music')
Bot.load_extension('marry')

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     user_agent='bestfriend')







@Bot.event
async def on_ready():
    print ("m##################################################################")
    print ("Starting up")
    print ("BOT IS ONLINE")
    print ("m##################################################################")
    game = discord.Game("%help for commands!")
    await Bot.change_presence(status=discord.Status.do_not_disturb, activity=game)



@Bot.command(pass_contex=True)
async def server(ctx):
    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="__**Best friend Server Invite**__", color=0xe5103a)
    embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
    embed.add_field(name="_*With permissions*_", value="[Link To My Server](https://discord.gg/MdS8QMg)")
    await ctx.send(embed=embed)

@Bot.command(pass_context=True)
async def bot(ctx):
    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="__**Invite Best Friend **__", color=0xe5103a)
    embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
    embed.add_field(name="_*With permissions*_", value="[Invite Link](https://discordapp.com/oauth2/authorize?client_id=447857064233009153&scope=bot&permissions=8)")
    embed.add_field(name="_*With no permissions*_", value="[Invite Link](https://discordapp.com/oauth2/authorize?client_id=447857064233009153&scope=bot&permissions=0)")
    await ctx.send(embed=embed)


@Bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="__**PING TIME**__", color=0xe5103a)
    embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
    embed.add_field(name="_*Ping*_", value=Bot.latency)
    await ctx.send(embed=embed)


Bot.run(str(""))

