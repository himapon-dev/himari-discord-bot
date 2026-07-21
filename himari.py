import discord
import os
import json
import random

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("HIMARI_TOKEN")

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
    print(
        "RECEIVED:",
        repr(message.content),
        "| CHANNEL:",
        getattr(message.channel, "name", None),
        "| AUTHOR:",
        message.author
    )

    if message.author == client.user:
       return
    
    if message.channel.name != "talk-to-himari🐶":
        print("SKIPPED: different channel")
        return
    
    print("SENDING REPLY")
    await message.channel.send(random.choice(REPLIES))

client.run(TOKEN)


