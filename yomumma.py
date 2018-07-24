from discord.ext import commands
import random 
class yomumma():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def yomumma(self, ctx, *args):
        mesg = "".join(args) 
        x = random.randint(1,10)
        if x ==1:
            await ctx.send("Yo mumma is so fat when she got on the scale it said, I need your weight not your phone number.  " + mesg)
        elif x ==2:
            await ctx.send("Yo mumma so stupid, when they said it was chilly outside, she grabbed a bowl.  " + mesg)
        elif x ==3:
            await ctx.send("Yo Mumma so fat she uses an air balloon for parachute.  " + mesg)
        elif x ==4:
            await ctx.send("Yo Mumma is so stupid she sold her car for gas money.  " + mesg)
        elif x ==5:
            await ctx.send("Yo mumma so fat, when she went to the beach, all the whales started singing We Are Family.  " + mesg)
        elif x ==6:
            await ctx.send("Yo mumma so fat, she stepped on a scale and it said: To be continued.  " + mesg)
        elif x ==7:
            await ctx.send("yo mumma so stupid, she stared at a cup of orange juice for 12 hours because it said concentrated  " + mesg)
        elif x ==8:
            await ctx.send("Yo mumma so short, she has to slam dunk her bus fare.  " + mesg)
        elif x ==9:
            await ctx.send("Yo mumma so stupid she can’t pass a blood test.  " + mesg)
        elif x ==10:
            await ctx.send("Yo mumma is so poor that she needs coupons for the 99cent store  "  + mesg)    




def setup(bot):
    bot.add_cog(yomumma(bot))


