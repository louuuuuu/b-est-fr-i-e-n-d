from discord.ext import commands
import discord
import asyncio





class help():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        embed = discord.Embed(title="```🤬Best Friend Bot <3```", description="__**COMMANDS**__", color=0xe5103a)
        embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
        embed.add_field(name="_*FUN*_", value="```md\n<%pat>         [player][]\n<%hug>         [player][]\n<%kiss>        [player][]\n<%slap>        [player][]\n<%punch>       [player][]\n<%yomumma>     [player][]\n<%avatar>      [player][]\n<%coinflip>    [][]\n<%roll>        [][]\n<%ree>         [][]\n<%ball>        [][]```", inline=False)
        embed.add_field(name="_*ROCK  PAPER  SCISSORS*_", value="```md\n<%rock>        [][]\n<%paper>       [][]\n<%scissors>    [][]```", inline=False)
        embed.add_field(name="_*SEARCH*_", value="```md\n<%yt>          [video][]\n<%wiki>        [topic][]\n<%soundcloud>  [song][]\n<%steam>       [steamid][]\n<%urban>       [word][]\n<%cat>         [][]\n<%dog>         [][]```", inline=False)
        embed.add_field(name="_*REDDIT*_", value="```md\n<%wholesome>   [][]\n<%meme>        [][]\n<%bread>       [][]\n<%meirl>       [][]\n<%shitpost>    [][]```", inline=False)
        embed.add_field(name="_*MONEY*_", value="```md\n<%give>        [player][ammount]\n<%dice>        [ammount][]\n<%balance>     [player][]\n<%coin>        [head or tails][ammount]\n<%beg>         [][]```", inline=False)
        embed.add_field(name="_*MATHS*_", value="```md\n<%add>         [number][number]\n<%subtract>    [number][number]\n<%divide>      [number][number]\n<%multiply>    [number][]\n<%root>        [number][]\n<%square>      [number][]\n<%cube>        [number][]\n<%double>      [number][]```", inline=False)
        embed.add_field(name="_*MODERATE*_", value="```md\n<%mute>        [player][]\n<%ban>         [player][]\n<%unmute>      [player][]\n<%kick>        [player][]\n<%clear>       [number][]```", inline=False)
        await ctx.message.author.send(embed=embed)
def setup(bot):
    bot.add_cog(help(bot))
