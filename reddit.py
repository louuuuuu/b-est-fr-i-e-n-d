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


class Mycog():
    def __init__(self, bot):
        self.bot = bot
#MEME
    @commands.command(pass_context=True)
    async def meme(self, ctx):
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        embed=discord.Embed(url=submission.url, color=0xe5103a)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

#WHOLESOME
    @commands.command(pass_context=True)
    async def wholesome(self, ctx):
        wholesomememes_submissions = reddit.subreddit('wholesomememes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(1, post_to_pick):
            submission = next(x for x in wholesomememes_submissions if not x.stickied)
        embed=discord.Embed(url=submission.url, color=0xe5103a)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

#BREAD
    @commands.command(pass_context=True)
    async def bread(self, ctx):
        BreadStapledToTrees_submissions = reddit.subreddit('BreadStapledToTrees').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in BreadStapledToTrees_submissions if not x.stickied)
        embed=discord.Embed(url=submission.url, color=0xe5103a)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

#ME IN REAL LIFE
    @commands.command(pass_context=True)
    async def meirl(self, ctx):
        me_irl_submissions = reddit.subreddit('me_irl').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in me_irl_submissions if not x.stickied)
        embed=discord.Embed(url=submission.url, color=0xe5103a)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)

#SHITPOST
    @commands.command(pass_context=True)
    async def shitpost(self, ctx):
        shitposting_submissions = reddit.subreddit('shitposting').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in shitposting_submissions if not x.stickied)
        embed=discord.Embed(url= submission.url, color=0xe5103a)
        embed.set_image(url=submission.url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Mycog(bot))

