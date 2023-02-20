import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite
import random
import asyncio

class level(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        setattr(self.client, "db", await aiosqlite.connect("level.db"))

async def setup(client: commands.Bot) -> None:
    await client.add_cog(level(client))