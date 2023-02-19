import discord, os
from discord.ext import commands
from colorama import Back, Fore, Style
from datetime import datetime
import platform
import json

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='01c2baade9b', intents = discord.Intents().all())

    async def on_ready(self):
        prfx = (Back.BLUE + Fore.GREEN + datetime.now().strftime("%a %H:%M:%S") + Back.RESET + Fore.WHITE + Style.BRIGHT)

        print(prfx + " Starting bot!"+"\n")
        print(prfx + " Logged in as " + Fore.GREEN + self.user.name)
        print(prfx + " Bot ID " + Fore.GREEN + str(self.user.id))
        print(prfx + " OS " + Fore.GREEN + str(platform.platform()))
        print(prfx + " Discord Version " + Fore.GREEN + discord.__version__)
        print(prfx + " Python Version " + Fore.GREEN + str(platform.python_version()))

        synced = await self.tree.sync()
        print(prfx + " Slash Commands Synced " + Fore.GREEN + str(len(synced)) + " Commands")

with open("config.json","r+") as f:
    data = json.load(f)
    TOKEN = data["TOKEN"]

client = Client()
client.run(TOKEN)