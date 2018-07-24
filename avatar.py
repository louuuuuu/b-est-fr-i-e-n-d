import discord
from discord.ext import commands

class avatar():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        embed=discord.Embed(url=member.avatar_url, color=0xe5103a)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(avatar(bot))
