from discord.ext import commands
import discord
import asyncio





class code():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def py(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```python\n" + msg + "```")
    @commands.command()
    async def css(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```css\n" + msg + "```")
    @commands.command()
    async def asciidoc(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```asciidoc\n" + msg + "```")
    @commands.command()
    async def autohotkey(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```autohotkey\n" + msg + "```")
    @commands.command()
    async def bash(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```bash\n" + msg + "```")
    @commands.command()
    async def coffeescript(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```coffeescript\n" + msg + "```")
    @commands.command()
    async def cpp(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```cpp\n" + msg + "```")
    @commands.command()
    async def cs(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```cs\n" + msg + "```")
    @commands.command()
    async def diff(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```diff\n" + msg + "```")
    @commands.command()
    async def fix(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```fix\n" + msg + "```")
    @commands.command()
    async def glsl(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```glsl\n" + msg + "```")
    @commands.command()
    async def html(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```html\n" + msg + "```")
    @commands.command()
    async def ini(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```ini\n" + msg + "```")     
    @commands.command()
    async def json(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```json\n" + msg + "```")
    @commands.command()
    async def md(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```md\n" + msg + "```")   
    @commands.command()
    async def ml(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```ml\n" + msg + "```")   
    @commands.command()
    async def prolog(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```prolog\n" + msg + "```")
    @commands.command()
    async def tex(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```tex\n" + msg + "```")
    @commands.command()
    async def xl(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```xl\n" + msg + "```")
    @commands.command()
    async def xml(self, ctx, *args):
        msg = " ".join(args)
        await ctx.send("```xml\n" + msg + "```")

    @commands.command()
    async def cog(self, ctx):
        await ctx.send("```python\nclass help():\n  def __init__(self, bot):\n      self.bot = bot\n\n do stuff\n\n def setup(bot):\n   bot.add_cog(help(bot))```"+"To load the cog"+"```Bot.load_extensiond(cog name)```")

    @commands.command()
    async def basic(self, ctx):
        await ctx.send("```python\nimport discord  #Imports discord to the file\n\nBot = commands.Bot(command_prefix=\"prefix\"\ #sets the prefix for the bot\n@Bot.event #when the bot starts up\nasync def on_ready():  #defines the action\n  print(\"blah blah\")  #writes in console\n@Bot.command(pass_contex=True)  #shows its a bot command\nasync def commandtitle():#command title is where you put  your command name needed to activate the command.\n  await Bot.say(\"blahblah\")#blahblah is where you would put what text you want for the bot to say```")

    @commands.command()
    async def random(self, ctx):
        await ctx.send("```python\nimport random\n\nrandom = random.randint(1,2)\nif random ==1:\n   do something\nelif random ==2:\n   do something```")

    @commands.command()
    async def args(self, ctx):
        await ctx.send("```python\n@bot.commands(pass_context=True)\nasync def echo(args):\n   mesg = \"\".join(args)\n   await Bot.say(mesg)```")

    @commands.command()
    async def ctx(self, ctx):
        embed = discord.Embed(title="`CODE HELP`", description="__**CTX LIST**__" , color=0xe5103a)
        embed.set_thumbnail(url="https://gyazo.com/170a0f1c835eaec4283d342671ada158.jpeg")
        embed.add_field(name="*Pass context=True*", value="Needed in @Bot.command(here!)", inline=False)
        embed.add_field(name="*ctx.message.author*", value="Targets the person who did the command", inline=False)
        embed.add_field(name="*ctx.message.author*", value="Targets the person who did the command", inline=False)
        embed.add_field(name="*ctx.message.author.id*", value="In Bot.say says the id of the person who did the command", inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(code(bot))
