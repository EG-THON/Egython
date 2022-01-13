#Rallsthon

from telethon.tl.types import ChannelParticipantsAdmins


@icssbot.on(admin_cmd(pattern="all$"))
@icssbot.on(sudo_cmd(pattern="all$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    mentions = "تع خد شوكولاته"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await reply_to_id.reply(mentions)
    await event.delete()


@icssbot.on(admin_cmd(pattern="للكل( (.*)|$)"))
@icssbot.on(sudo_cmd(pattern="للكل( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    mentions = input_str or "**هيي اخواتي فالله.**"
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@icssbot.on(admin_cmd(pattern="للادمنيه$"))
@icssbot.on(sudo_cmd(pattern="للادمنيه$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin: **Spam Spotted**"
    chat = await event.get_input_chat()
    reply_to_id = await reply_id(event)
    async for x in event.client.iter_participants(
        chat, filter=ChannelParticipantsAdmins
    ):
        if not x.bot:
            mentions += f"[\u2063](tg://user?id={x.id})"
    await event.client.send_message(event.chat_id, mentions, reply_to=reply_to_id)
    await event.delete()


@icssbot.on(admin_cmd(pattern="صيح (.*)"))
@icssbot.on(sudo_cmd(pattern="صيح (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    if event.reply_to_msg_id:
        reply_msg = await event.get_reply_message()
        u = reply_msg.sender_id
    else:
        user, input_str = input_str.split(" ", 1)
        try:
            u = int(user)
        except ValueError:
            try:
                u = await event.client.get_entity(user)
            except ValueError:
                await event.delete()
                return
            u = int(u.id)
        except Exception:
            await event.delete()
            return
    await event.delete()
    await event.client.send_message(
        event.chat_id,
        f"<a href='tg://user?id={u}'>{input_str}</a>",
        parse_mode="HTML",
        reply_to=reply_to_id,
    )


CMD_HELP.update(
    {
        "التاك": """**اسم الاضافـه : **`التاك`

  •  **◄ الامـر ⦂ **`.تاك`
  •  **الشـرح •• **__تاك للكل ع شكـل ماركـداون فـي المجموعــه__   
  
  •  **◄ الامـر ⦂ **`.all`
  •  **الشـرح •• **__تاك لآخـر 100 شخـص متفاعـل فـي المجموعــه__   

  •  **◄ الامـر ⦂ **`.للكل`
  •  **الشـرح •• **__تاك لآخـر 100 شخـص متفاعـل فـي المجموعــه__ 

  •  **◄ الامـر ⦂ **`.للادمنيه`
  •  **الشـرح •• **__تاك مخفـي للمشـرفيـن فـي المجموعـه__  

  •  **◄ الامـر ⦂ **`.صيح +معرف / ايدي + نص`
  •  **الشـرح •• **__tags that person with the given custom text other way for this is __
  •  **◄ الامـر ⦂ **`Hi username[custom text]`
"""
    }
)
