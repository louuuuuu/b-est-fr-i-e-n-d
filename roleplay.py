import discord
from discord.ext import commands
import random 
class roleplay():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def hey(self, ctx):
        await ctx.send("Hey best buddie" + " "+ctx.message.author.mention+"!")
    
    @commands.command(pass_context=True)
    async def hug(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,6)
        
        if x==1:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318272367689728/hug2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318272367689728/hug2.gif")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318266370097212/hug1.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318266370097212/hug1.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318265728237568/hug3.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318265728237568/hug3.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318262112616478/hug4.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318262112616478/hug4.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318256056041472/hug5.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318256056041472/hug5.gif")
            await ctx.send(embed=embed)

        if x==6:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466340468146569216/hug2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466340468146569216/hug2.gif")
            await ctx.send(embed=embed)

        if x==6:
            embed=discord.Embed(url="https://media.discordapp.net/attachments/462718094805303307/466339465523101698/tenor.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Hugged" + " "+mesg+"!")
            embed.set_image(url="https://media.discordapp.net/attachments/462718094805303307/466339465523101698/tenor.gif")
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def kiss(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,7)
        
        if x==1:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318277900238848/kiss5.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318277900238848/kiss5.giff")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318286267875338/kiss1.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318286267875338/kiss1.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318289329586206/kiss3.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318289329586206/kiss3.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318289996349440/kiss2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318289996349440/kiss2.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318290214584320/kiss4.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318290214584320/kiss4.gif")
            await ctx.send(embed=embed)
        
        if x==6:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466341610268131328/kiss2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466341610268131328/kiss2.gif")
            await ctx.send(embed=embed)

        if x==7:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466341484333891584/kiss1.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Kissed" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466341484333891584/kiss1.gif")
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def pat(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,8)
        
        if x==1:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318306174042142/pat5.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318306174042142/pat5.gif")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318315070160906/pat1.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318315070160906/pat1.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318316584304640/pat2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318316584304640/pat2.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318319754936330/pat3.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318319754936330/pat3.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466318324859404289/pat.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466318324859404289/pat.gif")
            await ctx.send(embed=embed)

        if x==6:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466341055911165952/pat1.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466341055911165952/pat1.gif")
            await ctx.send(embed=embed)
        if x==7:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466544739358081024/pat2.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466544739358081024/pat2.gif")
            await ctx.send(embed=embed)
        if x==8:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466544731438972968/pat3.gif", color=0xe5103a)
            embed.add_field(name="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗", value=ctx.message.author.mention + " "+"Patted" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466544731438972968/pat3.gif")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def lick(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,5)
        
        if x==1:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466562783996149785/lick3.gif", color=0xe5103a)
            embed.add_field(name="😛👄💋😋👅👄👅💋😋😛👅😛😋👄👅💋", value=ctx.message.author.mention + " "+"Licked" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466562783996149785/lick3.gif")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466562807710875658/lick1.gif", color=0xe5103a)
            embed.add_field(name="😛👄💋😋👅👄👅💋😋😛👅😛😋👄👅💋", value=ctx.message.author.mention + " "+"Licked" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466562807710875658/lick1.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466562823896694787/lick2.gif", color=0xe5103a)
            embed.add_field(name="😛👄💋😋👅👄👅💋😋😛👅😛😋👄👅💋", value=ctx.message.author.mention + " "+"Licked" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466562823896694787/lick2.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466567802845921310/Haruka_dog_lick.gif", color=0xe5103a)
            embed.add_field(name="😛👄💋😋👅👄👅💋😋😛👅😛😋👄👅💋", value=ctx.message.author.mention + " "+"Licked" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466567802845921310/Haruka_dog_lick.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466568675382657025/giphy.gif", color=0xe5103a)
            embed.add_field(name="😛👄💋😋👅👄👅💋😋😛👅😛😋👄👅💋", value=ctx.message.author.mention + " "+"Licked" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466568675382657025/giphy.gif")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def punch(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,7)
        
        if x==1:
            embed=discord.Embed(url="https://images-ext-1.discordapp.net/external/uoi51QBmtSa72fW1SwN3ii3ki2BUY9MD_DFk7yEd0EQ/https/i.kym-cdn.com/photos/images/original/001/100/341/82a.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://images-ext-1.discordapp.net/external/uoi51QBmtSa72fW1SwN3ii3ki2BUY9MD_DFk7yEd0EQ/https/i.kym-cdn.com/photos/images/original/001/100/341/82a.gif")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466330877907959808/Jonathan.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466330877907959808/Jonathan.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466331435717099530/anime-punch-gif-3.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466331435717099530/anime-punch-gif-3.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466331517925326849/rip.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466331517925326849/rip.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466331718568116225/323ecb6c1ce55337a0e3c3a45be7cba0e77d222b_hq.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466331718568116225/323ecb6c1ce55337a0e3c3a45be7cba0e77d222b_hq.gif")
            await ctx.send(embed=embed)

        if x==6:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466552121806946305/3b8.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466552121806946305/3b8.giff")
            await ctx.send(embed=embed)

        if x==7:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/448144848193716224/466552553375531008/heya.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Punched" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/448144848193716224/466552553375531008/heya.gif")
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def slap(self, ctx, *args):
        mesg = ''.join(args)
        x = random.randint(1,8)
        
        if x==1:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466331899069988874/slap.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466331899069988874/slap.gif")
            await ctx.send(embed=embed)
        if x==2:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466332416311689217/slap_2.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466332416311689217/slap_2.gif")
            await ctx.send(embed=embed)
        
        if x==3:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466332594330664963/giphy.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466332594330664963/giphy.gif")
            await ctx.send(embed=embed)

        if x==4:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466332853890711562/The_slap.giff", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466332853890711562/The_slap.gif")
            await ctx.send(embed=embed)
        
        if x==5:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/421016302312882196/466333255650639872/mIg8erJ.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/421016302312882196/466333255650639872/mIg8erJ.gif")
            await ctx.send(embed=embed)
        
        if x==6:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466343746812903445/punch1.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466343746812903445/punch1.gif")
            await ctx.send(embed=embed)

        if x==7:
            embed=discord.Embed(url="https://cdn.discordapp.com/attachments/462718094805303307/466342261526102017/slap2.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://cdn.discordapp.com/attachments/462718094805303307/466342261526102017/slap2.gif")
            await ctx.send(embed=embed)
        if x==8:
            embed=discord.Embed(url="https://media.discordapp.net/attachments/462718094805303307/466545028454678547/slap3.gif", color=0xe5103a)
            embed.add_field(name="🥊🥊😤👊👊🤬❗️❗️❗️😤🥊👊🥊😡😡👊", value=ctx.message.author.mention + " "+"Slapped" + " "+mesg+"!")
            embed.set_image(url="https://media.discordapp.net/attachments/462718094805303307/466545028454678547/slap3.gif")
            await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(roleplay(bot))


