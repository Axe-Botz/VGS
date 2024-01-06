

async def start_dspam(RiZoeL, message, counts, delay, spam_text):
   for _ in range(counts):
      await RiZoeL.send_message(chat.id, str(spam_text))
      await asyncio.sleep(delay)
     
