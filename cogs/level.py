import discord
from discord.ext import commands
from discord.ext import app_commands
import aiosqlite
import random
import asyncio

class Level(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    