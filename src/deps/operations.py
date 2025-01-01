import aiohttp
from deps.api import openapi as API_KEY

'''
This file contains any operations abstracted into a function that an event will use.
'''

async def ai_generate_response(message):
    '''
    This function is used to generate responses when the name of the bot is mentioned. 

    The function takes in one parameter called "message" (or aka "ctx" in the docs or other code)
    '''

    user_msg = message.content.lower().replace('!', '').replace('?', '').replace(',', '').replace('.', '')

    if 'viktor' in user_msg.split():
        async with aiohttp.ClientSession() as session:
            payload = {
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "Answer or talk as if you are Viktor from Arcane. Keep responses under 200 characters or less. Use expressions when applicable."},
                    {"role": "user", "content": message.content}
                    ],
                "temperature": 0.7
            }
            headers = {"Authorization": f'Bearer {API_KEY}', "Content-Type": "application/json"}

            async with session.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers) as resp:
                response = await resp.json()
                await message.channel.send(response['choices'][0]['message']['content'])
                return
