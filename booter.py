import discord
import os
import subprocess
import sys

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Replace with your actual bot token
BOT_TOKEN = "MTQzNDMzMjA0Njc3NTI5MjA0OQ.GY5I9-.8z4I7sdsQqQlX6LF0ZngYyU-Wndj42xxmaKhfw"

# Replace with your actual Discord user ID
YOUR_USER_ID = 670334804998357013

@client.event
async def on_ready():
    pass  # Do nothing to suppress the ready message

@client.event
async def on_message(message):
    if message.author.id == YOUR_USER_ID and message.content == "/shutdown":
        await message.channel.send("💻 Shutting down...")
        os.system("shutdown /s /t 5")

# Run the bot in a subprocess and redirect output streams
subprocess.Popen([sys.executable, __file__], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Keep the main script running to prevent it from exiting immediately
while True:
    pass
