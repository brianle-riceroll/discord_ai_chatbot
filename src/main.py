import discord
from discord.ext import tasks, commands
from discord import app_commands
from deps.api import token as TOKEN, openapi as API_KEY
from deps.games_list import status
import aiohttp


intents = discord.Intents.default()
intents.message_content = True
message = discord.Message
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f'Ready to go!')
    change_status.start()
    await client.tree.sync()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f'{message.author}: {message.content}')

    user_msg = message.content.lower().replace('!', '').replace('?', '').replace(',', '').replace('.', '')

    if 'viktor' in user_msg.split():
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "Answer or talk as if you are Viktor from Arcane. Keep responses under 200 characters or less. Use expressions when applicable."}
                    {"role": "user", "content": message.content}
                    ],
                "temperature": 0.7
            }
            headers = {"Authorization": f'Bearer {API_KEY}', "Content-Type": "application/json"}
            async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers) as resp:
                response = await resp.json()
                await message.channel.send(response['choices'][0]['message']['content'])

        
        
@tasks.loop(hours=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.tree.command(name="viktor", description="Talk with Viktor!")
async def viktor(ctx: commands.Context, *, prompt: str):
    await ctx.response.defer()
    prompt = "Keep it under 250 characters. Answer as if you are Viktor from the show Arcane: " + prompt
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        headers = {"Authorization": f'Bearer {API_KEY}', "Content-Type": "application/json"}
        async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            await ctx.followup.send(response['choices'][0]['message']['content'])




@client.tree.command(name="ping", description="pong")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong")
    

client.run(TOKEN)
