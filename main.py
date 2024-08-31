import discord
from discord.ext import commands
import OWM

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

kuba = ""

@bot.command()
async def lang(ctx, *, langa):
    OWM.lang = langa
    if OWM.lang == "en":
        await ctx.send(f"Your language :{langa}")
    if OWM.lang == "es":
        await ctx.send(f"Tu idioma :{langa}")
    if OWM.lang == "ru":
        await ctx.send(f"Ваш язык :{langa}")
    if OWM.lang == "lv":
        await ctx.send(f"Tava valoda :{langa}")

@bot.command()
async def city(ctx, *, data):
    global kuba
    kuba = data
    if OWM.lang == "en":
        await ctx.send(f"Your city is {data}")
    if OWM.lang == "es":
        await ctx.send(f"Tu ciudad es {data}")
    if OWM.lang == "ru":
        await ctx.send(f"Ваш город {data}")
    if OWM.lang == "lv":
        await ctx.send(f"Tava pilsēta {data}")

@bot.command()
async def firehere(ctx):
    OWM.setup(kuba)
    await ctx.send(OWM.textfire)

bot.run("Token")
