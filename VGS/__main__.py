import asyncio
import importlib
from pyrogram import Client, idle

from VGS import client


async def start_bot():
    try:
        print("WTF! L o a d i n g")
        await client.start()
    except:
        print("Error!")
    

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
print("[INFO]: BOT STARTED 🔥")
