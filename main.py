import os

import discord
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


load_dotenv()

client = discord.Client()
analyzer = SentimentIntensityAnalyzer()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return 

    if msg.content.startswith("hello"):
        await msg.channel.send("Hello!")

client.run(os.getenv('CLIENT_ID'))
    