#Egython ®


from userbot.helpers import *
import base64
import io
import os
from pathlib import Path
from . import *
from telethon import types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url
from youtubesearchpython import Video
import json
import os
import time
import requests
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)

try:

    from youtubesearchpython import *

except:
    os.system("pip install pip install youtube-search-python")
    from youtubesearchpython import SearchVideos

from userbot import bot
from ..helpers.utils import reply_id
from userbot.helpers.functions import deEmojify




@bot.on(admin_cmd(pattern="بحث ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="بحث ?(.*)", allow_sudo=True))
async def FindMusicPleaseBot(Ralls):

    song = Ralls.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await Ralls.edit("**᥀︙قم باضافـة الاغنيـه للامـر .. بحث + اسـم الاغنيـه**")

    await Ralls.edit("**• جاري البحث عن الاغنيه.**")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await Ralls.edit("**- جاري تحميل الاغنيه انتظر..**")

        try:

            await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("عـذراً"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await Ralls.edit(f"**᥀︙عـذراً .. لـم استطـع ايجـاد** {song}")

            await conv.get_response()

            lavde = await conv.get_response()

        except YouBlockedUserError:

            await Ralls.edit(
                "**᥀︙تحـقق من انـك لم تقـم بحظـر البوت @FindMusicPleaseBot .. ثم اعـد استخدام الامـر.️**"
            )

            return

        await Ralls.edit("**جاري ارسال الاغنيه انتظر قليلا.**")

        await bot.send_file(Ralls.chat_id, lavde)

        await bot.send_read_acknowledge(conv.chat_id)

    await Ralls.delete()
