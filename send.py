import discord
import time
import os
import random
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

pm = ['f', 'r', 'i', 'c', 'k']

@client.event
async def on_ready():
    print(f"Logged on as {client.user.name}")

@client.event
async def on_connect():
    channel = client.get_channel(867676267557552149)

    while True:
        await channel.send("pls beg")
        time.sleep(5)
        await channel.send("pls hunt")
        time.sleep(10)
        await channel.send("pls search")
        time.sleep(10)
        await channel.send("pls fish")
        time.sleep(10)
        await channel.send("pls dig")
        time.sleep(10)
        await channel.send("pls search")
        time.sleep(5)
        await channel.send("pls pm")
        time.sleep(2)
        resp = random.choice(pm)
        await channel.send(resp)
        time.sleep(10)

token = os.getenv("TOKEN")
client.run(token, bot=False)
