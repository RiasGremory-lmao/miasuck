from lib2to3.pgen2 import token
from tkinter import BOTH
import discord
import json
import os
import random
from discord.ext import commands
from discord.ext.commands.core import command


with open("./config.json","r") as f:
    config = json.load(f)
client = commands.Bot(command_prefix='moon+')
client.remove_command('help')


@client.event
async def on_ready():
    print('Running')

for filename in os.listdir('./Moderator'):
     if filename.endswith('.py'):
         client.load_extension(f'Moderator.{filename[:-3]}')
for filename in os.listdir('./Music'):
     if filename.endswith('.py'):
         client.load_extension(f'Music.{filename[:-3]}')
@client.event
async def on_ready():
    print('Running')
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.watching, name='Tearmoon Teikoku'))
@client.command()
@commands.has_permissions(manage_messages=True)
async def say(ctx, *, message):
  await ctx.message.delete()
  await ctx.send(message)
@client.command()
async def math(ctx, operation:str):
  await ctx.send(eval(operation))
  import random
import discord
from discord.ext import commands

client.run(config["bottoken"])
import discord
from discord.ext import commands
client = discord.Client