import mcwiki
import random
import discord
import os
from discord.ext import commands
from discord.ext.commands.context import Context

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
###
bot = commands.Bot(intents=intents, command_prefix=".")
###


@bot.event
async def on_ready():
    print(f"Got in as {bot.user}")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if message.content.startswith(".search allay"):
        await message.channel.send(
            mcwiki.load("https://minecraft.fandom.com/wiki/Allay")
        )
    if message.content.startswith(".search allay behavior"):
        allay = mcwiki.load("https://minecraft.fandom.com/wiki/Allay#Spawning")
        await message.channel.send(allay.extract(mcwiki.PARAGRAPH, index=5))
    if message.content.startswith(".helpwindow"):
        embedVar = discord.Embed(
            title="**Книга знаний**",
            description="Minecraft — это 3D-«песочница», разработанная компанией *Mojang Studios*, где игрок взаимодействует с игровым миром через размещение и разрушение различных блоков в трёх разных измерениях. Разнообразный игровой процесс позволяет игрокам самим выбирать пути прохождения игры, открывая бесчисленные возможности.",
            color=0x34B4EB,
            url="https://minecraft.wiki/",
        )
        # embedVar.add_field(name="", value="", inline=True)
    embedVar.set_footer(
        text=":exclamation:Вся информация взята с сайта Minecraft Wiki, использование бота некоммерческое. Оригинальный сайт: https://minecraft.wiki/"
    )
    ##.setFooter({ text: 'Вся информаци идет с сайта Minecraft Wiki. Использование этого бота полностью некоммерческое. Оригинальный сайт Minecarft Wiki: https://minecraft.fandom.com/ru/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0', iconURL: 'https://static.wikia.nocookie.net/minecraft_ru_gamepedia/images/c/c0/Make_Stuff_icon_%28MCE%29.png/revision/latest/scale-to-width-down/100?cb=20211005103918' });
    await message.channel.send(embed=embedVar)


@bot.command()
async def mem(ctx):
    with open("images/1.jpeg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem2(ctx):
    with open("images/2.jpg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def meme(ctx: Context):
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


def valid_image(f):
    for extension in [".jpg", ".jpeg"]:
        if f.endswith(extension):
            return True
    return False


###
# @bot.command
# async def mem(ctx):
# with open('images/1.jpeg', 'rb') as f:
# picture = discord.File(f)
# await ctx.send(file=picture)


# RUN source .env first!
bot.run(os.getenv("BOT_TOKEN"))
