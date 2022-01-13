#Egython

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@icssbot.on(admin_cmd(pattern="تيكتوك$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="تيكتوك$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    if not reply_message:
        await edit_or_reply(event, "**```يرجي الرد علي الرابط.```**")
        return
    if not reply_message.text:
        await edit_or_reply(event, "**```يرجي الرد علي الرابط.```**")
        return
    chat = "@TIKTOKDOWNLOADROBOT"
    catevent = await edit_or_reply(event, "**جاري التحميل...**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1598492699)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await catevent.edit(
                "`RIP Check Your Blacklist Boss and unblock @TIKTOKDOWNLOADROBOT`"
            )
            return
        if response.text.startswith(""):
            await catevent.edit("Am I Dumb Or Am I Dumb?")
        else:
            await catevent.delete()
            await event.client.send_message(event.chat_id, response.message)


CMD_HELP.update(
    {
        "تيك توك": "**اسم الاضافـه : **`تيك توك`\
    \n\n**• الأمر **`.تيكتوك` بالرد على الرابط\
    \n**• الشرح **تحميل مقاطـع الفيديـو من تيـك تـوك"
    }
)
