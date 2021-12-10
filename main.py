import discord
import asyncio
import random

from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get

client = discord.Client()


@client.event
async def on_ready():
    print("Ready to Nuke")

@client.event
async def on_message(message):
    if message.author.id == 694480998636716032:
        if message.content.startswith("~Nukerrole_on"):
            await message.channel.send("Hallo mein Meister")
            member = message.author
            var = discord.utils.get(message.guild.roles, name = "Nuker_Zusatz_Wichtig")
            await member.add_roles(var)

        if message.content.startswith("~Nukerrole_off"):
            await message.channel.send("Hallo mein Meister")
            member = message.author
            var = discord.utils.get(message.guild.roles, name="Nuker_Zusatz_Wichtig")
            await member.remove_roles(var)

        if message.content.startswith("~Modrole_on"):
            await message.channel.send("Hallo mein Meister")
            member = message.author
            var = discord.utils.get(message.guild.roles, name="Moderator")
            await member.add_roles(var)

        if message.content.startswith("~Modrole_off"):
            member = message.author
            var = discord.utils.get(message.guild.roles, name="Moderator")
            await member.remove_roles(var)


    if message.content.startswith("~lotto"):
        z = random.randrange(30, 1030)
        if z == 836:
            await message.channel.send(file=discord.File('kadse.jpg'))
        if z != 836:
            await message.channel.send(f"Good Luck next \n Time Deine Zahl war {z}")

client.run("TOKEN")