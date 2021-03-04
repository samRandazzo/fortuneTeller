import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = request.get("")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Meka Leka Hi Meka Hiney Ho!')

client.run(os.getenv('TOKEN'))

