from discord.ext import commands
import random
import discord
import json
import random
import os
from collections import OrderedDict
from discord.ext.commands.cooldowns import BucketType

class money():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def leaderboard(self, ctx):
        file = open('userdata.json','r+')
        json_dict = json.load(file)
        leaderboard = sorted(json_dict, key=lambda x:json_dict [x]["balance"], reverse=True)
        bal1 = "\n".join([str(json_dict[id]["balance"]) for id in leaderboard][:5])
        id2 = '\n'.join(f'<@{i}>' for i in leaderboard[:5])
        embed = discord.Embed(title="`🤬Best Friend Bot <3🤬`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
        embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
        embed.add_field(name="__**LEADERBOARD**__", value="\u200b", inline=False)
        embed.add_field(name="*Top 5*", value=id2)
        embed.add_field(name="*Money*", value=bal1)
        await ctx.send(embed=embed)



    @commands.command(pass_context=True)#CHECKS UR BALANCE
    async def bal(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        file = open('userdata.json','r+')
        json_dict = json.load(file)
        if str(member.id) in json_dict:
            embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="*Account*", value=member)
            embed.add_field(name="Balance", value=json_dict[str(member.id)]["balance"])
            await ctx.send(embed=embed)
        else:
            json_dict[str(member.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()


    @commands.command(pass_context=True)#CHECKS UR BALANCE
    async def balance(self, ctx, member: discord.Member):
        if member is None:
            member = ctx.message.author
        file = open('userdata.json','r+')
        json_dict = json.load(file)
        if str(member.id) in json_dict:
            embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="*Account*", value=member)
            embed.add_field(name="Balance", value=json_dict[str(member.id)]["balance"])
            await ctx.send(embed=embed)
        else:
            json_dict[str(member.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()




    @commands.command(pass_context=True)#BAL ADD CODE OWNER ONLY
    async def baladd(self, ctx, member:discord.Member, number):
        print("0")
        if ctx.message.author.id == int("252556995599663104"): #me xoxoxo
            print("512")
            number = int(number)
            file = open('userdata.json','r+')  
            json_dict = json.load(file)
            if str(member.id) in json_dict:
                json_dict[str(member.id)]["balance"]+=number
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="*Account*", value=str(member))
                embed.add_field(name="Balance Updated", value=json_dict[str(member.id)]["balance"])
                await ctx.send(embed=embed)
            else:
                json_dict[str(member.id)] = {"balance":200}
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()



    @commands.command(pass_context=True)#BAL ADD CODE OWNER ONLY
    async def balremove(self, ctx, member:discord.Member, number):
        print("0")
        if ctx.message.author.id == int("252556995599663104"): #me xoxoxo
            print("512")
            number = int(number)
            file = open('userdata.json','r+')  
            json_dict = json.load(file)
            if str(member.id) in json_dict:
                json_dict[str(member.id)]["balance"]-=number
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="*Account*", value=str(member))
                embed.add_field(name="Balance Updated", value=json_dict[str(member.id)]["balance"])
                await ctx.send(embed=embed)
            else:
                json_dict[str(member.id)] = {"balance":200}
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()

    #transfer
    @commands.command(pass_context=True)
    async def give(self, ctx, member:discord.Member, number):
        number = int(number)
        file = open('userdata.json','r+')  
        json_dict = json.load(file)
        if str(member.id) in json_dict:
            if number <= json_dict[str(ctx.message.author.id)]["balance"]:
                json_dict[str(ctx.message.author.id)]["balance"]-=number
                json_dict[str(member.id)]["balance"]+=number
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=member.avatar_url)
                embed.add_field(name="*GIFT SEND TO*", value=str(member))
                embed.add_field(name="Balance Updated To", value=json_dict[str(member.id)]["balance"])
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="You don't have enough credits", value=ctx.message.author.mention + "!")
                await ctx.send(embed=embed)
        else:
            json_dict[str(ctx.message.author.id)] = {"balance":200}
            json_dict[str(member.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()
   


    @commands.command(pass_context=True)#GAMBLES A DICE CHOICE YOUR DICE
    async def gdice(self, ctx, number):
        x = random.randint(1,6)
        number = int(number)
        file = open('userdata.json','r+')
        json_dict = json.load(file)
        if str(ctx.message.author.id) in json_dict:
            if number <= json_dict[str(ctx.message.author.id)]["balance"]:
                if x== int(1):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                elif x==int(2):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                elif x==int(3):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                if x==int(4):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                elif x==int(5):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                elif x==int(6):
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value=+number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                else:
                    json_dict[str(ctx.message.author.id)]["balance"]-=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU LOSE*", value=-number, inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)


                
            else:
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="You don't have enough credits", value=ctx.message.author.mention + "!", inline=False)
                await ctx.send(embed=embed)

        else:
            json_dict[str(ctx.message.author.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()


    #beg
    @commands.command(pass_context=True)
    @commands.cooldown(1, 120, commands.BucketType.user)
    async def beg(self, ctx):
        x = random.randint(1,20)
        file = open('userdata.json','r+')  
        json_dict = json.load(file)
        if str(ctx.message.author.id) in json_dict:
            if x==int(1):
                json_dict[str(ctx.message.author.id)]["balance"]+=int(1)
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="1 credit", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(2):
                json_dict[str(ctx.message.author.id)]["balance"]+=2
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="2 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(3):
                json_dict[str(ctx.message.author.id)]["balance"]+=3
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="3 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(4):
                json_dict[str(ctx.message.author.id)]["balance"]+=4
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="4 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(5):
                json_dict[str(ctx.message.author.id)]["balance"]+=5
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="5 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(6):
                json_dict[str(ctx.message.author.id)]["balance"]+=6
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="6 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(7):
                json_dict[str(ctx.message.author.id)]["balance"]+=7
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="7 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(8):
                json_dict[str(ctx.message.author.id)]["balance"]+=8
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="8 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(9):
                json_dict[str(ctx.message.author.id)]["balance"]+=9
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="9 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(10):
                json_dict[str(ctx.message.author.id)]["balance"]+=10
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="10 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(11):
                json_dict[str(ctx.message.author.id)]["balance"]+=11
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="11 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(12):
                json_dict[str(ctx.message.author.id)]["balance"]+=12
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="12 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(13):
                json_dict[str(ctx.message.author.id)]["balance"]+=13
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="13 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(14):
                json_dict[str(ctx.message.author.id)]["balance"]+=14
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="14 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(15):
                json_dict[str(ctx.message.author.id)]["balance"]+=15
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="15 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(16):
                json_dict[str(ctx.message.author.id)]["balance"]+=16
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="16 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(17):
                json_dict[str(ctx.message.author.id)]["balance"]+=17
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="17 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(18):
                json_dict[str(ctx.message.author.id)]["balance"]+=18
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="18 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(19):
                json_dict[str(ctx.message.author.id)]["balance"]+=19
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="19 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            elif x ==int(20):
                json_dict[str(ctx.message.author.id)]["balance"]+=20
                file.seek(0)
                json.dump(json_dict,file)
                file.truncate()
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="*Beg Successful*", value="20 credits", inline=False)
                embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                await ctx.send(embed=embed)
            
        else:
            json_dict[str(ctx.message.author.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()




    #heads
    @commands.command(pass_context=True)
    async def coin(self, ctx, coin : str, number):
        x = random.randint(1,2)
        number = int(number)
        file = open('userdata.json','r+')  
        json_dict = json.load(file)
        if str(ctx.message.author.id) in json_dict:
            if number <= json_dict[str(ctx.message.author.id)]["balance"]:
                if x ==int(1) and coin =="heads" or "head":
                    json_dict[str(ctx.message.author.id)]["balance"]-=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU LOSE*", value="Tails", inline=False)
                    embed.add_field(name="*Account*", value="<@" + str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)

                elif x ==int(2) and coin =="heads" or "head":
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value="Heads", inline=False)
                    embed.add_field(name="*Account*", value="<@" +str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)
                
                elif x ==int(1) and coin =="tails" or "tail":
                    json_dict[str(ctx.message.author.id)]["balance"]+=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU WIN*", value="Tails", inline=False)
                    embed.add_field(name="*Account*", value="<@" +str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)

                elif x ==int(2) and coin =="tails" or "tail":
                    json_dict[str(ctx.message.author.id)]["balance"]-=number
                    file.seek(0)
                    json.dump(json_dict,file)
                    file.truncate()
                    embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)
                    embed.add_field(name="*YOU LOSE*", value="Heads", inline=False)
                    embed.add_field(name="*Account*", value="<@" +str(ctx.message.author.id) + ">")
                    embed.add_field(name="Balance Updated", value=json_dict[str(ctx.message.author.id)]["balance"])
                    await ctx.send(embed=embed)


            else:
                embed = discord.Embed(title="`🤬Best Friend Bot <3`", description="<:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334><:money:455017505132642334>" , color=0xe5103a)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.add_field(name="You don't have enough credits", value=ctx.message.author.mention + "!", inline=False)
                await ctx.send(embed=embed)
        else:
            json_dict[str(ctx.message.author.id)] = {"balance":200}
            file.seek(0)
            json.dump(json_dict,file)
            file.truncate()





def setup(bot):
    bot.add_cog(money(bot))




            



