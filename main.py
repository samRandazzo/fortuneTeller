import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = request.get("https://zenquotes.io/api/random")
  json_data = json.loads(respons.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quit)

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

