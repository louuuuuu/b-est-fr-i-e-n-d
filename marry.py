from discord.ext import commands
import discord
import asyncio
import json


class code():
    def __init__(self, bot):
        self.bot = bot

    


    @commands.command(pass_context=True)
    async def marry(self, ctx, member: discord.Member, message):
        file = open('marry.json','r+')
        json_dict = json.load(file)
        print("32124")
        if str(ctx.message.author.id) in json_dict or str(member.id) in json_dict:
            print("£12312")
            embed = discord.Embed(title="`MARRY`", description="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗" , color=0xe5103a)
            embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
            embed.add_field(name="*You are already married!*", value="Greedy 😡", inline=False)
            await ctx.send(embed=embed)
        
        elif str(ctx.message.author.id) in json_dict or str(member.id) not in json_dict:
            print("1")
            embed = discord.Embed(title="`MARRY`", description="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗" , color=0xe5103a)
            print("2")
            embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
            print("3")
            embed.add_field(name="*Proposal*", value=ctx.message.author.mention +" "+"Proposed to"+" "+"<@"+str(member.id)+">", inline=False)
            print("4")
            embed.add_field(name="*Do you accept?*", value="type yes or no to decline!", inline=False)
            print("5")
            await ctx.send(embed=embed)

            
            if "yes" in message.content.lower(author=member):
                print("6")
                file = open('marry.json','r+')
                json_dict = json.load(file)
                print("32")
                embed = discord.Embed(title="`MARRY`", description="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗" , color=0xe5103a)
                embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
                print("1345124")
                embed.add_field(name="Married", value=ctx.message.author.mention +" " + "Just married" +" " + "<@"+str(member.id)+">", inline=False)
                await ctx.send(embed=embed)
                print("gwqg")
                
                json_dict[str(ctx.message.author.id)] = str(member.id)
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()

            if "no" in message.content.lower(author=member):
                embed = discord.Embed(title="`MARRY`", description="💖💗💗💖💕💗💕❤️💕💗💕❤️💖❤️💗💗" , color=0xe5103a)
                embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
                embed.add_field(name="*Marriage Declined*", value="<@"+str(member.id)+">"+" "+"Declined"+" "+ctx.message.author.mention+" " +"proposal", inline=False)
                await ctx.send(embed=embed)

        
        








    @commands.command(pass_context=True)
    async def divorce(self, ctx, member: discord.Member):
        
        file = open('marry.json','r+')
        json_dict = json.load(file)

        if str(ctx.message.author.id) in json_dict or str(member.id) in json_dict:
            del json_dict[ctx.message.author.id]["member.id"] 
            del json_dict["ctx.message.author.id"]
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()




def setup(bot):
    bot.add_cog(code(bot))
