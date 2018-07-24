from discord.ext import commands
import random 
class dice():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def roll(self, ctx):
        x = random.randint(1,6)
        if x ==1:
            await ctx.send("🎲1" + ' ' +ctx.message.author.mention)
        elif x ==2:
            await ctx.send("🎲2" + ' '+ctx.message.author.mention)
        elif x ==3:
            await ctx.send("🎲3" + ' '+ctx.message.author.mention)
        elif x ==4:
            await ctx.send("🎲4" + ' '+ctx.message.author.mention)
        elif x ==5:
            await ctx.send("🎲5" + ' '+ctx.message.author.mention)
        elif x ==6:
            await ctx.send("🎲6" + ' ' +ctx.message.author.mention)

def setup(bot):
    bot.add_cog(dice(bot))
