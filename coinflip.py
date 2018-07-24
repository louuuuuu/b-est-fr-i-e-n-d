import discord
from discord.ext import commands
import random 
class coinflip():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coinflip(self, ctx):
        if random.randint(0, 1): await ctx.send('Heads 🤕')
        else: await ctx.send('Tails 🐒')

def setup(bot):
    bot.add_cog(coinflip(bot))
