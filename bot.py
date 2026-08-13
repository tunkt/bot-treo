import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot da dang nhap: {bot.user}")

ID phòng voice của bạn
    CHANNEL_ID = 1537535314619404318 

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print(f"Da vao phong thanh cong: {channel.name}")
        except Exception as e:
            print(f"Loi khi vao phong: {e}")
    else:
        print("Khong tim thay phong voice, kiem tra lai ID!")

TOKEN = os.getenv("DISCORD_TOKEN") or "MTUzNzNzOTQwMzK2NzcwOTI1A.GDCGHX.POQusyCxRKF9RCG1SsrFM1HMc4d3sIkPNLu9TM"
bot.run(TOKEN)