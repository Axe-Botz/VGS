## BY ROMEO BHAI
## FOR ATIT JANEMNN

import asyncio

from threading import Event
from re import sub
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get

from VGS import SUDO_USER

##from cache.data import GROUP, VERIFIED_USERS
NB = [-1001521704453, -1001410362208]
DEVS = 6834053539

## ---------------------------------------------------- ##

def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()

def spam_allowed():
    return SPAM_COUNT[0] < 50


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])


async def extract_args(message, markdown=True):
    if not (message.text or message.caption):
        return ""
    text = message.text or message.caption
    text = text.markdown if markdown else text
    if " " not in text:
        return ""
    text = sub(r"\s+", " ", text)
    text = text[text.find(" ") :].strip()
    return text

## ---------------------------------------------------- ##

@Client.on_message(
    filters.command(["group"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in NB:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.5)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.5)
    await tex.edit_text(
        f"**Successfully Sent Message To** `{done}` **Groups, chat, Failed to Send Message To** `{error}` **Groups**"
    )


@Client.on_message(
    filters.command(["all"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def gucast(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        tex = await message.reply_text("`Started global broadcast...`")
    else:
        return await message.edit_text("**Give A Message or Reply**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.5)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.5)
    await text.edit_text(
        f"**Successfully Sent Message To** `{done}` **chat, Failed to Send Message To** `{error}` **chat**"
)
