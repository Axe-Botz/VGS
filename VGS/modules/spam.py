from pyrogram import Client, filters
from pyrogram.types import Message
import os, sys, asyncio, re
from random import choice


handler = [".", "!"]

async def start_dspam(RiZoeL, message, counts, delay, spam_text):
   for _ in range(counts):
      await RiZoeL.send_message(chat.id, str(spam_text))
      await asyncio.sleep(delay)
     
@Client.on_message(filters.user(Sudos) & filters.command(["delayspam"], prefixes=handler))
@Client.on_message(filters.me & filters.command(["delayspam"], prefixes=handler))
async def delayspam(SpamX: Client, e: Message): 
    usage = spam_usage.delayspam
    Rizoel = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
    Rizoelop = Rizoel[1:]
    if len(Rizoelop) == 2:
       counts = int(Rizoelop[0])
       spam_text = str(Rizoelop[1])
       sleeptime = float(Rizoel[0])
       await start_dspam(SpamX, e, counts, sleeptime, spam_text)
    else:
        await e.reply_text(usage.format(handler))
        return
