import discord
from discord.ext import commands
import random 
import asyncio
import json




class mod():
    def __init__(self, bot):
        self.bot = bot
#CLEAR CHAT
    @commands.command(pass_context=True)
    async def clear(self, ctx, num: int):
        if ctx.message.author.guild_permissions.kick_members or ctx.message.author.id == int("252556995599663104"):
            await ctx.channel.purge(limit=num)

        else:
            embed=discord.Embed(title="__**⚠️Permission denied⚠️**__", description="*Delete messages is needed in you're permssions*" + ctx.message.author.mention, color=0xe5103a)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/448144848193716224/451084781204144128/26a0.png.jpeg")
            await ctx.send(embed=embed)
#KICK
    @commands.command(pass_context=True)

    async def kick(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.kick_members or ctx.message.author.id == int("252556995599663104"):
            await ctx.message.guild.kick(member)
            embed=discord.Embed(title="User Kicked!", description="**{0}** was kicked by **{1}**!".format(member, ctx.message.author), color=0xe5103a)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="__**⚠️Permission denied⚠️**__", description="*Kick members is needed in you're permssions*" + " " + ctx.message.author.mention, color=0xe5103a)
            await ctx.send(embed=embed)
#MUTE
    @commands.command(pass_context=True)
    async def mute(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.mute_members or ctx.message.author.id == int("252556995599663104"):
            role = discord.utils.get(member.guild.roles, name='muted')
            await ctx.add_roles(member, role)
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xe5103a)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="__**⚠️Permission denied⚠️**__", description="*Mute members is needed in you're permssions*" + " " + ctx.message.author.mention, color=0xe5103a)
            await ctx.send(embed=embed)

#UNMUTE
    @commands.command(pass_context=True)
    async def unmute(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.mute_members or ctx.message.author.id == int("252556995599663104"):
            role = discord.utils.get(member.server.roles, name='muted')
            await ctx.remove_roles(member, role)
            embed=discord.Embed(title="User Muted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xe5103a)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="__**⚠️Permission denied⚠️**__", description="*Mute members is needed in you're permssions*" + " " + ctx.message.author.mention, color=0xe5103a)
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def ban(self, ctx, member: discord.Member):
        if ctx.message.author.guild_permissions.ban_members or ctx.message.author.id == int("252556995599663104"):
            await ctx.message.guild.ban(member)
            
            embed=discord.Embed(title="User banned!", description="**{0}** was banned by **{1}**!".format(member, ctx.message.author), color=0xe5103a)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed)     
        else:
            embed=discord.Embed(title="__**⚠️Permission denied⚠️**__", description="*Ban members is needed in you're permssions*" + " " + ctx.message.author.mention, color=0xe5103a)
            await ctx.send(embed=embed)       
            


def setup(bot):
    bot.add_cog(mod(bot))

