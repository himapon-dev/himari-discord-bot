import discord
import os
import json
import random

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("HIMARI_TOKEN")

HIMARI_CHANNEL_ID = 1530265522652844262

with open("reply_list_himari.json", encoding="utf-8") as f:
    REPLIES = json.load(f)


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} が起きました🐶")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.channel.id != HIMARI_CHANNEL_ID:
        print(
            "SKIPPED:",
            repr(message.content),
            "| CHANNEL:",
            getattr(message.channel, "name", None),
            "| CHANNEL ID:",
            message.channel.id
        )
        return

    print(
        "RECEIVED:",
        repr(message.content),
        "| CHANNEL:",
        getattr(message.channel, "name", None),
        "| CHANNEL ID:",
        message.channel.id
    )

    await message.channel.send(random.choice(REPLIES))

client.run(TOKEN)


