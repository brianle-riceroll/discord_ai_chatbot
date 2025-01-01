import aiohttp
import re
from deps.api import openapi as API_KEY # add openai api keys in api.py

'''
This file contains any operations abstracted into a function that an event will use.
'''

async def ai_generate_response(message, bot_character):
    '''
    This function is used to generate responses when the name of the bot is mentioned. 

    The function takes in one parameter called "message" (or aka "ctx" in the docs or other code)
    '''

    prompt = message.content

    user_msg = re.sub(r'[,.?!;\+\-()><:]', '', prompt.lower())

    name_keywords = bot_character.usr_select.split(" ")
    
    for i in name_keywords: 
        if i.lower() in user_msg.split():
            async with aiohttp.ClientSession() as session:
                payload = {
                    "model": "gpt-4o-mini",
                    "messages": [
                        {"role": "system", "content": f"Answer or talk as if you are {bot_character.usr_select}. Keep responses under 200 characters or less."},
                        {"role": "user", "content": prompt}
                        ],
                    "temperature": 0.7
                }
                headers = {"Authorization": f'Bearer {API_KEY}', "Content-Type": "application/json"}

                async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers) as resp:
                    response = await resp.json()
                    await message.channel.send(response['choices'][0]['message']['content'])
                    return
