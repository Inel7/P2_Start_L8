import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True								# Zorgt ervoor dat we berichtinhoud kunnen lezen
bot = commands.Bot(command_prefix="$", intents=intents)    	# Onze commando's zullen met een $ starten

@bot.event
async def on_ready():
    print(f'We zijn ingelogd als {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  	# Bericht door de bot verstuurd
        return  						# Return (doe niets meer hierna)

    if message.content.lower() == 'ping':
        await message.channel.send('pong')
    else:
        await message.channel.send(f"Je zei {message.content}")


discord_token = "VUL HIER JOUW TOKEN IN"
bot.run(discord_token)

@bot.event
async def on_message_delete(message):
    await message.channel.send(f"Bericht van {message.author} werd verwijderd! Bericht: {message.content}")

    @bot.command()
    async def random_kat(context):
        random_nummer = random.randint(1, 10000)
        await context.send(f"https://cataas.com/cat?{random_nummer}")

    @bot.command()
    async def random_hond(context):
        random_nummer = random.randint(1, 10000)
        await context.send(f"https://place.dog/600/600?{random_nummer}")

