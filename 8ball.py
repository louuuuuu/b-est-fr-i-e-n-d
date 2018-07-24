import discord
from discord.ext import commands
import asyncio
import random 

class ball():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def ball(self, ctx):
        author = ctx.message.author
        x = random.randint(1,10)
        if x ==1:
            await ctx.send("🎱It will never happen." + ' ' +author.mention)
        elif x ==2:
            await ctx.send("🎱I wouldn't." + ' '+author.mention)
        elif x ==3:
            await ctx.send("🎱I would." + ' '+author.mention)
        elif x ==4:
            await ctx.send("🎱Certainly." + ' '+author.mention)
        elif x ==5:
            await ctx.send("🎱Don't even bother." + ' '+author.mention)
        elif x ==6:
            await ctx.send("🎱Maybe in the future." + ' ' +author.mention)
        elif x ==7:
            await ctx.sendy("🎱Ask again." + ' ' +author.mention)
        elif x ==8:
            await ctx.send("🎱Its you're choice." + ' ' +author.mention)
        elif x ==9:
            await ctx.sendy("🎱Go for it." + ' ' +author.mention)
        elif x ==10:
            await ctx.send("🎱Don't know." + ' ' +author.mention)     


def setup(bot):
    bot.add_cog(ball(bot))
