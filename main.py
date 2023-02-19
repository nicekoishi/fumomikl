import discord, os
from discord.ext import commands
from colorama import Back, Fore, Style
from datetime import datetime
import platform
import json

bot = commands.Bot(command_prefix="01c2baade9b", intents=discord.Intents.all())
plstime = datetime.now()

with open("config.json","r+") as f:
    config = json.load(f)
    TOKEN = config["TOKEN"]

@bot.event
async def on_ready():
    prfx = (Back.BLUE + Fore.GREEN + plstime.strftime("%a %H:%M:%S") + Back.RESET + Fore.WHITE + Style.BRIGHT)

    print(prfx + " Starting bot!"+"\n")
    print(prfx + " Logged in as " + Fore.GREEN + bot.user.name)
    print(prfx + " Bot ID " + Fore.GREEN + str(bot.user.id))
    print(prfx + " OS " + Fore.GREEN + str(platform.platform()))
    print(prfx + " Discord Version " + Fore.GREEN + discord.__version__)
    print(prfx + " Python Version " + Fore.GREEN + str(platform.python_version()))

    synced = await bot.tree.sync()
    print(prfx + " Slash Commands Synced " + Fore.GREEN + str(len(synced)) + " Commands")
   
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('ultrasex'):
        await message.channel.send('https://www.youtube.com/watch?v=6IwcJh43vhI')


bot.run(TOKEN)