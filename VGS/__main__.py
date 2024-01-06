import asyncio
import importlib
from pyrogram import Client, idle

from VGS import client

loop = asyncio.get_event_loop()

async def start_bot():
    try:
        print("WTF! L o a d i n g")
        await client.start()
    except Exception as e:
        print(f"{e}")
    

if __name__ == "__main__":
    loop.run_until_complete(start_bot())
print("[INFO]: BOT STARTED 🔥")
