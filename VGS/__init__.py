from pyrogram import Client
from datetime import datetime
import time
import asyncio

StartTime = time.time()
START_TIME = datetime.now()
SUDO_USER = 6834053539


print("[INFO]: BOOTING UP!!")
API_ID = 20112715
API_HASH = "fe56c4634729f7c557b3298f0bb0cf1e"
STRING = "BQBs4AuaLeg-0qeGfQVSYlvzHM8_GFpGD0WbyJ9TRVMByqtL2ACNWIxatZymGbkSaWHJb3RremDf1UXsNi8l5jUZVmB6I0iiLaxR_AzQ3Me-I3DgaNA9JzbffEKLCnVLpJYq6kBCtae7Ckff-IGcdys_gmXdTYQFlUsbOAowduExCzYpBu6Gk_pDFSVj7fUkmlm5tdYz6StVwLlIaCp-mkQZJcKHTb83I1i-Z6p8pzru-ut6eBnM-SANkuUXtxc73M9vmmeN05ow2FSHWN1YAznX9kWtc4VvherGbLHRPSxijclSnTZHkt61LSToLZDYRl04P-9spIEnS9_uuoWRFEAAAAAYrz8J4A"

userbot = Client(
  ":USERBOT:",
  api_id=API_ID,
  api_hash=API_HASH,
  session_string=STRING,
  plugins=dict(root="VGS/modules")
)

async def startbot():
    await userbot.start()
    getme = await userbot.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop = asyncio.get_event_loop()
loop.run_until_complete(startbot())
