import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import random
from translate import Translator
import sys
import re
import requests
import json
import urllib
from bs4 import BeautifulSoup
import requests
from discord.voice_client import VoiceClient
import praw 


reddit = praw.Reddit(client_id='bKnxwGmOfT-BLw',
                     client_secret='Fqa9mtajYKME3deHZxoJZfmRRhA',
                     user_agent='bestfriend')

class search():
    def __init__(self, bot):
        self.bot = bot
#YOUTUBE
    @commands.command(pass_context=True)
    async def yt(self, ctx, *args):
        url = "https://www.youtube.com/results?search_query=" + \
                urllib.parse.quote(" ".join(args).lower())
        for vid in BeautifulSoup(urllib.request.urlopen(url).read(), \
            "html5lib").findAll(attrs={'class': 'yt-uix-tile-link'}, \
                limit = 1):
            if "user" not in vid["href"] and "googleads" not in vid["href"]:
                await ctx.channel.purge(limit=1)
                await ctx.send('https://www.youtube.com' + vid['href'])
                break

#GOOGLE
    @commands.command(pass_context=True)
    async def google(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await ctx.send('https://encrypted.google.com/search?hl=en&q={}'.format(" ".join(args).replace(' ', '+')))


#WIKI
    @commands.command(pass_context=True)
    async def wiki(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await ctx.send('https://en.wikipedia.org/wiki/{}'.format(" ".join(args).replace(' ', '_')))


        
#STEAM
    @commands.command(pass_context=True)
    async def steam(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await ctx.send('https://steamcommunity.com/id/{}'.format(" ".join(args).replace(' ', '+')))


#CAT
    @commands.command(pass_context=True)
    async def cat(self, ctx):
        await ctx.channel.purge(limit=1)
        for i in range (0,5):
            try:
                r = requests.get("https://aws.random.cat/meow")
                r = str(r.content)
                r = r.replace("b'","")
                r = r.replace("'","")
                r = r.replace("\\","")
                url = json.loads(r)["file"]
                await ctx.send(url)
                break
            except:
                pass

#DOG
    @commands.command(pass_context=True)
    async def dog(self, ctx):
        r = requests.get("https://random.dog/woof")
        r = str(r.content)
        r = r.replace("b'","")
        r = r.replace("'","")
        await ctx.channel.purge(limit=1)
        await ctx.send("https://random.dog/" + r)


#SOUNDCLOUD
    @commands.command(pass_context=True)
    async def soundcloud(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await ctx.send('https://soundcloud.com/search?q={}'.format(" ".join(args).replace(' ', '+')))




#URBAN DICTIONARY
    @commands.command(pass_context=True)
    async def urban(self, ctx, *args):
        await ctx.channel.purge(limit=1)
        await self.bot.say('{}'.format("https://www.urbandictionary.com/define.php?term={}".format(" ".join(args).replace(' ', '+'))))



def setup(bot):
    bot.add_cog(search(bot))

