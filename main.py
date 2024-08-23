import discord
from discord.ext import commands
import OWM

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

tokyo = ""

@bot.command()
async def city(ctx, *, data):
    global tokyo
    tokyo = data
    await ctx.send(f"Your city is {data}")

@bot.command()
async def firehere(ctx):
    OWM.setup(tokyo)
    await ctx.send(OWM.textfire)

bot.run("token")
