
import discord
import requests
import random


import os

TOKEN = os.getenv('TOKEN')

TRIGGER_WORDS = ['meme', 'lol', 'haha', 'joke', 'memes', "retard"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_random_meme():
    url = 'https://meme-api.com/gimme'
    try:
        response = requests.get(url)
        data = response.json()
        return data.get('url'), data.get('title')
    except Exception as e:
        return None, None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    content = message.content.lower()
    if any(word in content for word in TRIGGER_WORDS):
        meme_url, meme_title = get_random_meme()
        if meme_url:
            await message.channel.send(f"**{meme_title}**\n{meme_url}")
        else:
            await message.channel.send("Couldn't fetch a meme right now. Try again later!")

client.run(TOKEN)
