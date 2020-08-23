import discord
from discord.ext import commands
token = 'NzQ2ODYyODA0Nzc4MDkwNTc4.X0GgMA.nEnuXiGfUUACme-IEWI5oS6VNrY'
bot = commands.Bot(command_prefix = "!")
@bot.event
async def on_ready():
    print('bot is online')

@bot.command()
async def count(ctx,):
    for i in range(10):
        embed = discord.Embed(title = "Counting Bot", description = "Counting Numbers", colour=discord.Color.red())
        #embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        embed.set_footer(text = ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://www.python.org/static/img/python-logo.png')
        embed.add_field(name='Number : ', value=i)
        await ctx.channel.purge(limit=500)
        await ctx.send(embed=embed)
@bot.command()
async def purge(ctx):
    await ctx.channel.purge(limit=100)
bot.run(token)
