import discord
import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env

client = discord.Client()
token = os.environ.get('TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):

    print(message.content);

client.run(token)