import os
import random

import discord

from discord.ext import commands
from utils import valid_image


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
###
bot = commands.Bot(intents = intents, command_prefix=".")
###

@bot.event
async def on_ready():
    print(f'Got in as {bot.user}')
    
@bot.command()
async def meme(ctx):
    folder = "images/"
    images = []
    for f in os.listdir(folder):
        if valid_image(f):
            images.append(f)
    # [f for f in os.listdir(folder) if valid_image(f)]
    filename = random.choice(images)
    with open(f"{folder}/{filename}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def test(ctx):
    await ctx.send("Command test complete.")

bot.run(os.getenv("BOT_TOKEN"))
