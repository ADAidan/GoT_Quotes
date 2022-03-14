import os
import discord
import random
from discord.ext import commands
from quotes import quotes

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='got-quote', help='Gives a random Game of Thrones quote')
async def random_quote(message):
    quote, author = random.choice(list(quotes.items()))
    full_quote = quote + ' ' + author
    await message.send(full_quote)


bot.run(TOKEN)
