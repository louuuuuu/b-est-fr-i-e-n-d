from discord.ext import commands
import random 
class rps():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def paper(self, ctx):
        """rolls paper"""
        x = random.randint(1,3)                                         #paper
        if x ==1:
            await self.bot.say("**✂️scissors.**" + ' '+ '**YOU LOSE**' + ' ' + ctx.message.author.mention) #scissors
        elif x ==2:
            await self.bot.say("**📝paper.**" + ' '+ '**DRAW**' + ' ' + ctx.message.author.mention) #paper
        elif x ==3:
            await self.bot.say("**🗿rock.**" + ' '+ '**YOU WIN**' + ' ' + ctx.message.author.mention) #rock
    #Rock paper scissors 
    @commands.command(pass_context=True)
    async def rock(self, ctx):
        """roles rock"""
        x = random.randint(1,3)
        if x ==1:
            await self.bot.say("**✂️scissors.**" + ' '+ '**YOU WIN**' + ' ' + ctx.message.author.mention) #scissors
        elif x ==2:
            await self.bot.say("**📝paper.**" + ' '+ '**YOU LOSE**' + ' ' + ctx.message.author.mention) #paper
        elif x ==3:
            await self.bot.say("**🗿rock.**" + ' '+ '**DRAW**' + ' ' + ctx.message.author.mention) #rock
    #Rock paper scissors 
    @commands.command(pass_context=True)
    async def scissors(self, ctx):
        """roles scissors"""
        x = random.randint(1,3)
        if x ==1:
            await self.bot.say("**✂️scissors.**" + ' '+ '**DRAW**' + ' ' + ctx.message.author.mention) #scissors
        elif x ==2:
            await self.bot.say("**📝paper.**" + ' '+ '**YOU WIN**' + ' ' + ctx.message.author.mention) #paper
        elif x ==3:
            await self.bot.say("**🗿rock.**" + ' '+ '**YOU LOSE**' + ' ' + ctx.message.author.mention) #rock



def setup(bot):
    bot.add_cog(rps(bot))

