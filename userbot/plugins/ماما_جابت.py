from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("ماما"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("ماما")
        await asyncio.sleep(0.6)
        await event.edit("جابت بيبي")
        await asyncio.sleep(0.7)
        await event.edit("بيبي حلو صغير ")
        await asyncio.sleep(0.6)
        await event.edit("يالله حبيبي")
        await asyncio.sleep(0.7)
        await event.edit("شو زكي و صغير")
        await asyncio.sleep(0.8)
        await event.edit("@Egython تبع")
