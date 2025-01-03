import discord
from discord.ext import tasks, commands
from deps.games_list import status
from deps.operations import ai_generate_response
from deps.characters import *

'''
This file contains all event, tasks, and routines the bot will perform.
'''

intents = discord.Intents.default()
intents.message_content = True
message = discord.Message
client = commands.Bot(command_prefix="!", intents=intents)
bot_character = characters()


@client.event
async def on_ready():
    '''Bot starting'''
    print(f'Ready to go! Bot is {bot_character.usr_select}')
    change_status.start()
    await client.tree.sync()


@client.event
async def on_message(message):
    '''AI Generated responses'''
    if message.author == client.user:
        return

    print(f'{message.author}: {message.content}')
    await ai_generate_response(message, bot_character)

        
@tasks.loop(hours=1)
async def change_status():
    '''Discord status looping'''
    await client.change_presence(activity=discord.Game(next(status)))


@client.tree.command(name="help", description="placeholder")
async def help(ctx: commands.Context, *, prompt: str):
    '''TODO: Help command'''


@client.tree.command(name="ping", description="pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")
    

