import discord
import os
from dotenv import load_dotenv
from commandhandler import CommandHandler, Command

load_dotenv() # take environment variables from .env

# Setup client, command handler, and get auth token
client = discord.Client()
token = os.environ.get('TOKEN')
c_handler = CommandHandler(client)

def help_func():
    print('help_func')

help_command = Command('help', 0, 'Usage: ;sports help', help_func)
c_handler.add_command(help_command)

# Called when the bot first starts up
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


# Called everytime there is a new message
@client.event
async def on_message(message):

    # If the message is from the bot then ignore this message
    if message.author == client.user:
        return

    try:
        if message.content.startswith(';sports'):
            args = message.content.split(' ')   # split into tokens
            args.pop(0)     # get rid of ;sports
            c_handler.execute(message, args)
    
    except Exception as e:
        print(e)


# Start the application
client.run(token)