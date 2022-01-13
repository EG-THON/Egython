from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("كوم بي"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("كوم بي")
        await asyncio.sleep(0.6)
        await event.edit(" واخذ")
        await asyncio.sleep(0.8)
        await event.edit("البطوله")
        await asyncio.sleep(0.6)
        await event.edit("شوف عرضه ")
        await asyncio.sleep(0.8)
        await event.edit("ولاشوف")
        await asyncio.sleep(0.6)
        await event.edit("طوله ")
