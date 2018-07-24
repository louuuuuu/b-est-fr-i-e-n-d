import discord 
from discord.ext import commands
import asyncio
import random 



class math():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def square(self, ctx, number):
        squared_value = int(number) * int(number)
        await ctx.send(str(number) + " squared is " + str(squared_value))     
    
    @commands.command()
    async def root(self, ctx, left : int):
        await ctx.send(left**(1/2))
        

    @commands.command()
    async def cube(self, ctx, number):
        cubed_value = int(number) * int(number) * int(number)
        await ctx.send(str(number) + " cubed is " + str(cubed_value))            
    
    @commands.command()
    async def add(self, ctx, left : int, right : int):
        await ctx.send(left + right)
    
    @commands.command()
    async def multiply(self, ctx, left : int, right : int):
        await ctx.send(left * right)
    
    @commands.command()
    async def subtract(self, ctx, left : int, right : int):
        await ctx.send(left - right)
    
    @commands.command()
    async def divide(self, ctx, left : int, right : int):
        await ctx.send(left / right)
    
    @commands.command()
    async def double(self, ctx, number):
        double_value = int(number) + int(number) 
        await ctx.send(str(number) + " doubled is " + str(double_value))

    @commands.command()
    async def number(self, ctx, left : int, right : int):
        x =  random.randint(left, right)
        await ctx.send(x)


def setup(bot):
    bot.add_cog(math(bot))
