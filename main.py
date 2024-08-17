import discord
from discord.ext import commands
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="fire_locator")
fire_coords = (34.0522, -118.2437)
location = geolocator.reverse(fire_coords, language='ru')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def firehere(ctx):
    await ctx.send(location.address)

bot.run("TOKEN")
