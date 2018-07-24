import discord
from discord.ext import commands
import asyncio


class music():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def join(self, ctx, *, channel: discord.VoiceChannel=None):
        await ctx.author.voice.channel.connect()
   
def setup(bot):
    bot.add_cog(music(bot))