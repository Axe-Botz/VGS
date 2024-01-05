import asyncio
import importlib
from pyrogram import Client, idle

from VGS import clients, ids

async def start_bot():
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()            
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())