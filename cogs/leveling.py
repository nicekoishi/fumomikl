import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite
import random
import asyncio

class leveling(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

async def setup(client: commands.Bot) -> None:
    await client.add_cog(leveling(client))