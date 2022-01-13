import base64

from telethon import events, functions, types
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import EditChatDefaultBannedRightsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import ChatBannedRights

from . import BOTLOG, get_user_from_event
from .sql_helper.locks_sql import get_locks, is_locked, update_lock


@icssbot.on(admin_cmd(pattern=r"قفل (.*)"))
@icssbot.on(sudo_cmd(pattern=r"قفل (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if not event.is_group:
        return await edit_delete(event, "`Idiot! ,This is not a group to lock things `")
    chat_per = (await event.get_chat()).default_banned_rights
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if input_str in (("البوتات", "الاوامر", "الايميل", "التوجيه", "الروابط")):
        update_lock(peer_id, input_str, True)
        await edit_or_reply(event, "`᥀︙تـم قفـل {} بنجـاح .`".format(input_str))
    else:
        msg = chat_per.send_messages
        media = chat_per.send_media
        sticker = chat_per.send_stickers
        gif = chat_per.send_gifs
        gamee = chat_per.send_games
        ainline = chat_per.send_inline
        embed_link = chat_per.embed_links
        gpoll = chat_per.send_polls
        adduser = chat_per.invite_users
        cpin = chat_per.pin_messages
        changeinfo = chat_per.change_info
        if input_str == "الدردشه":
            if msg:
                return await edit_delete(
                    event, "`This group is already locked with messaging permission`"
                )
            msg = True
            locktype = "الرسائل"
        elif input_str == "الوسائط":
            if media:
                return await edit_delete(
                    event, "`This group is already locked with sending media`"
                )
            media = True
            locktype = "الوسائط"
        elif input_str == "الملصقات":
            if sticker:
                return await edit_delete(
                    event, "`This group is already locked with sending stickers`"
                )
            sticker = True
            locktype = "الملصقات"
        elif input_str == "المركادون":
            if embed_link:
                return await edit_delete(
                    event, "`This group is already locked with previewing links`"
                )
            embed_link = True
            locktype = "الماركدون"
        elif input_str == "المتحركه":
            if gif:
                return await edit_delete(
                    event, "`This group is already locked with sending GIFs`"
                )
            gif = True
            locktype = "المتحركات"
        elif input_str == "الالعاب":
            if gamee:
                return await edit_delete(
                    event, "`This group is already locked with sending games`"
                )
            gamee = True
            locktype = "الالعاب"
        elif input_str == "الاونلاين":
            if ainline:
                return await edit_delete(
                    event, "`This group is already locked with using inline bots`"
                )
            ainline = True
            locktype = "اونلاين البوتات"
        elif input_str == "الاستفتاء":
            if gpoll:
                return await edit_delete(
                    event, "`This group is already locked with sending polls`"
                )
            gpoll = True
            locktype = "الاستفتائات"
        elif input_str == "الاضافه":
            if adduser:
                return await edit_delete(
                    event, "`This group is already locked with adding members`"
                )
            adduser = True
            locktype = "اضافة الاعضاء"
        elif input_str == "التثبيت":
            if cpin:
                return await edit_delete(
                    event,
                    "`This group is already locked with pinning messages by users`",
                )
            cpin = True
            locktype = "التثبيت"
        elif input_str == "المعلومات":
            if changeinfo:
                return await edit_delete(
                    event,
                    "`This group is already locked with Changing group info by users`",
                )
            changeinfo = True
            locktype = "تغيير معلومات الكروب"
        elif input_str == "الكل":
            msg = True
            media = True
            sticker = True
            gif = True
            gamee = True
            ainline = True
            embed_link = True
            gpoll = True
            adduser = True
            cpin = True
            changeinfo = True
            locktype = "كل شيئ"
        else:
            if input_str:
                return await edit_delete(
                    event, f"**᥀︙عذراً لايمكن قفل :** `{input_str}`", time=5
                )

            return await edit_or_reply(event, "`᥀︙عذراً لايمكنك قفل اي شي هنا .`")
        try:
            cat = Get(cat)
            await event.client(cat)
        except BaseException:
            pass
        lock_rights = ChatBannedRights(
            until_date=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            embed_links=embed_link,
            send_polls=gpoll,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            await event.client(
                EditChatDefaultBannedRightsRequest(
                    peer=peer_id, banned_rights=lock_rights
                )
            )
            await edit_or_reply(event, f"`᥀︙تـم قفـل {locktype} لهذه الدردشه .`")
        except BaseException as e:
            await edit_delete(
                event,
                f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
                time=5,
            )


@icssbot.on(admin_cmd(pattern="فتح (.*)"))
@icssbot.on(sudo_cmd(pattern="فتح (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    if not event.is_group:
        return await edit_delete(event, "`Idiot! ,This is not a group to lock things `")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    chat_per = (await event.get_chat()).default_banned_rights
    if input_str in (("البوتات", "الاوامر", "الايميل", "التوجيه", "الروابط")):
        update_lock(peer_id, input_str, False)
        await edit_or_reply(event, "`᥀︙تـم فتـح {} بنجـاح .`".format(input_str))
    else:
        msg = chat_per.send_messages
        media = chat_per.send_media
        sticker = chat_per.send_stickers
        gif = chat_per.send_gifs
        gamee = chat_per.send_games
        ainline = chat_per.send_inline
        gpoll = chat_per.send_polls
        embed_link = chat_per.embed_links
        adduser = chat_per.invite_users
        cpin = chat_per.pin_messages
        changeinfo = chat_per.change_info
        if input_str == "الدردشه":
            if not msg:
                return await edit_delete(
                    event, "`This group is already unlocked with messaging permission`"
                )
            msg = False
            locktype = "الرسائل"
        elif input_str == "الوسائط":
            if not media:
                return await edit_delete(
                    event, "`This group is already unlocked with sending media`"
                )
            media = False
            locktype = "الوسائط"
        elif input_str == "الملصقات":
            if not sticker:
                return await edit_delete(
                    event, "`This group is already unlocked with sending stickers`"
                )
            sticker = False
            locktype = "الملصقات"
        elif input_str == "الماركدون":
            if not embed_link:
                return await edit_delete(
                    event, "`This group is already unlocked with preview links`"
                )
            embed_link = False
            locktype = "preview links"
        elif input_str == "المتحركه":
            if not gif:
                return await edit_delete(
                    event, "`This group is already unlocked with sending GIFs`"
                )
            gif = False
            locktype = "المتحركات"
        elif input_str == "الالعاب":
            if not gamee:
                return await edit_delete(
                    event, "`This group is already unlocked with sending games`"
                )
            gamee = False
            locktype = "الالعاب"
        elif input_str == "الاونلاين":
            if not ainline:
                return await edit_delete(
                    event, "`This group is already unlocked with using inline bots`"
                )
            ainline = False
            locktype = "اونلاين البوتات"
        elif input_str == "الاستفتاء":
            if not gpoll:
                return await edit_delete(
                    event, "`This group is already unlocked with sending polls`"
                )
            gpoll = False
            locktype = "الاستفتائات"
        elif input_str == "الاضافه":
            if not adduser:
                return await edit_delete(
                    event, "`This group is already unlocked with adding members`"
                )
            adduser = False
            locktype = "اضافة الاعضاء"
        elif input_str == "التثبيت":
            if not cpin:
                return await edit_delete(
                    event,
                    "`This group is already unlocked with pinning messages by users`",
                )
            cpin = False
            locktype = "التثبيت"
        elif input_str == "المعلومات":
            if not changeinfo:
                return await edit_delete(
                    event,
                    "`This group is already unlocked with Changing grup info by users`",
                )
            changeinfo = False
            locktype = "تغيير معلومات الكروب"
        elif input_str == "الكل":
            msg = False
            media = False
            sticker = False
            gif = False
            gamee = False
            ainline = False
            gpoll = False
            embed_link = False
            adduser = False
            cpin = False
            changeinfo = False
            locktype = "الكل"
        else:
            if input_str:
                return await edit_delete(
                    event, f"**Invalid unlock type :** `{input_str}`", time=5
                )

            return await edit_or_reply(event, "`᥀︙عذراً لايمكنك فتح اي شي هنا .`")
        try:
            cat = Get(cat)
            await event.client(cat)
        except BaseException:
            pass
        unlock_rights = ChatBannedRights(
            until_date=None,
            send_messages=msg,
            send_media=media,
            send_stickers=sticker,
            send_gifs=gif,
            send_games=gamee,
            send_inline=ainline,
            send_polls=gpoll,
            embed_links=embed_link,
            invite_users=adduser,
            pin_messages=cpin,
            change_info=changeinfo,
        )
        try:
            await event.client(
                EditChatDefaultBannedRightsRequest(
                    peer=peer_id, banned_rights=unlock_rights
                )
            )
            await edit_or_reply(event, f"`᥀︙تـم فتـح {locktype} لهذه الدردشه .`")
        except BaseException as e:
            return await edit_delete(
                event,
                f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
                time=5,
            )


@icssbot.on(admin_cmd(pattern="الاعدادات$"))
@icssbot.on(sudo_cmd(pattern="الاعدادات$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    res = ""
    current_db_locks = get_locks(event.chat_id)
    if not current_db_locks:
        res = "**إعدادات الحمايه في هذه الدردشة**"
    else:
        res = "Following are the DataBase permissions in this chat: \n"
        ubots = "❌" if current_db_locks.bots else "✅"
        ucommands = "❌" if current_db_locks.commands else "✅"
        uemail = "❌" if current_db_locks.email else "✅"
        uforward = "❌" if current_db_locks.forward else "✅"
        uurl = "❌" if current_db_locks.url else "✅"
        res += f"👉 `البوتات`: `{ubots}`\n"
        res += f"👉 `الاوامر`: `{ucommands}`\n"
        res += f"👉 `الايميل`: `{uemail}`\n"
        res += f"👉 `التوجيه`: `{uforward}`\n"
        res += f"👉 `الروابط`: `{uurl}`\n"
    current_chat = await event.get_chat()
    try:
        chat_per = current_chat.default_banned_rights
    except AttributeError as e:
        logger.info(str(e))
    else:
        umsg = "❌" if chat_per.send_messages else "✅"
        umedia = "❌" if chat_per.send_media else "✅"
        usticker = "❌" if chat_per.send_stickers else "✅"
        ugif = "❌" if chat_per.send_gifs else "✅"
        ugamee = "❌" if chat_per.send_games else "✅"
        uainline = "❌" if chat_per.send_inline else "✅"
        uembed_link = "❌" if chat_per.embed_links else "✅"
        ugpoll = "❌" if chat_per.send_polls else "✅"
        uadduser = "❌" if chat_per.invite_users else "✅"
        ucpin = "❌" if chat_per.pin_messages else "✅"
        uchangeinfo = "❌" if chat_per.change_info else "✅"
        res += "\n**هذه هي الأذونات الحالية لهذه الدردشة:**\n"
        res += f"👉 `الدردشه`: `{umsg}`\n"
        res += f"👉 `الوسائط`: `{umedia}`\n"
        res += f"👉 `الملصقات`: `{usticker}`\n"
        res += f"👉 `المتحركه`: `{ugif}`\n"
        res += f"👉 `الماركدون`: `{uembed_link}`\n"
        res += f"👉 `الالعاب`: `{ugamee}`\n"
        res += f"👉 `الاونلاين`: `{uainline}`\n"
        res += f"👉 `الاستفتائات`: `{ugpoll}`\n"
        res += f"👉 `الاضافه`: `{uadduser}`\n"
        res += f"👉 `التثبيت`: `{ucpin}`\n"
        res += f"👉 `تغيير معلومات الكروب`: `{uchangeinfo}`\n"
    await edit_or_reply(event, res)


@icssbot.on(admin_cmd(pattern=r"تعطيل (.*)"))
@icssbot.on(sudo_cmd(pattern=r"تعطيل (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    if not event.is_group:
        return await edit_delete(event, "`Idiot! ,This is not a group to lock things `")
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(
        functions.channels.GetParticipantRequest(channel=peer_id, user_id=reply.from_id)
    )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await edit_delete(event, "`᥀︙عذراً لايمكنك تقييد الادمن هنا .`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "الدردشه":
        if msg:
            return await edit_delete(
                event, "`This Group is already locked with messaging permission.`"
            )
        if umsg:
            return await edit_delete(
                event, "`This User is already locked with messaging permission.`"
            )
        umsg = True
        locktype = "الرسائل"
    elif input_str == "الوسائط":
        if media:
            return await edit_delete(
                event, "`This group is already locked with sending media`"
            )
        if umedia:
            return await edit_delete(
                event, "`User is already locked with sending media`"
            )
        umedia = True
        locktype = "الوسائط"
    elif input_str == "الملصقات":
        if sticker:
            return await edit_delete(
                event, "`This group is already locked with sending stickers`"
            )
        if usticker:
            return await edit_delete(
                event, "`This user is already locked with sending stickers`"
            )
        usticker = True
        locktype = "الملصقات"
    elif input_str == "الماركدون":
        if embed_link:
            return await edit_delete(
                event, "`This group is already locked with previewing links`"
            )
        if uembed_link:
            return await edit_delete(
                event, "`This group is already locked with previewing links`"
            )
        uembed_link = True
        locktype = "الماركدون"
    elif input_str == "المتحركه":
        if gif:
            return await edit_delete(
                event, "`This group is already locked with sending GIFs`"
            )
        if ugif:
            return await edit_delete(
                event, "`This user is already locked with sending GIFs`"
            )
        ugif = True
        locktype = "المتحركات"
    elif input_str == "الالعاب":
        if gamee:
            return await edit_delete(
                event, "`This group is already locked with sending games`"
            )
        if ugamee:
            return await edit_delete(
                event, "`This user is already locked with sending games`"
            )
        ugamee = True
        locktype = "الالعاب"
    elif input_str == "الاونلاين":
        if ainline:
            return await edit_delete(
                event, "`This group is already locked with using inline bots`"
            )
        if uainline:
            return await edit_delete(
                event, "`This user is already locked with using inline bots`"
            )
        uainline = True
        locktype = "اونلاين البوتات"
    elif input_str == "الاستفتاء":
        if gpoll:
            return await edit_delete(
                event, "`This group is already locked with sending polls`"
            )
        if ugpoll:
            return await edit_delete(
                event, "`This user is already locked with sending polls`"
            )
        ugpoll = True
        locktype = "الاستفتائات"
    elif input_str == "الاضافه":
        if adduser:
            return await edit_delete(
                event, "`This group is already locked with adding members`"
            )
        if uadduser:
            return await edit_delete(
                event, "`This user is already locked with adding members`"
            )
        uadduser = True
        locktype = "اضافة الاعضاء"
    elif input_str == "التثبيت":
        if cpin:
            return await edit_delete(
                event,
                "`This group is already locked with pinning messages by users`",
            )
        if ucpin:
            return await edit_delete(
                event,
                "`This user is already locked with pinning messages by users`",
            )
        ucpin = True
        locktype = "التثبيت"
    elif input_str == "المعلومات":
        if changeinfo:
            return await edit_delete(
                event,
                "`This group is already locked with Changing group info by users`",
            )
        if uchangeinfo:
            return await edit_delete(
                event,
                "`This user is already locked with Changing group info by users`",
            )
        uchangeinfo = True
        locktype = "تغيير معلومات الكروب"
    elif input_str == "الكل":
        umsg = True
        umedia = True
        usticker = True
        ugif = True
        ugamee = True
        uainline = True
        uembed_link = True
        ugpoll = True
        uadduser = True
        ucpin = True
        uchangeinfo = True
        locktype = "الكل"
    else:
        if input_str:
            return await edit_delete(
                event, f"**Invalid lock type :** `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`᥀︙عذراً لايمكنك قفل اي شي عن هذا الشخص .`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await edit_or_reply(event, f"`᥀︙تـم قفـل {locktype} بنجـاح عن هذا الشخص .`")
    except BaseException as e:
        await edit_delete(
            event,
            f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
            time=5,
        )


@icssbot.on(admin_cmd(pattern=r"تفعيل (.*)"))
@icssbot.on(sudo_cmd(pattern=r"تفعيل (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    peer_id = event.chat_id
    reply = await event.get_reply_message()
    if not event.is_group:
        return await edit_delete(event, "`Idiot! ,This is not a group to lock things `")
    chat_per = (await event.get_chat()).default_banned_rights
    result = await event.client(
        functions.channels.GetParticipantRequest(channel=peer_id, user_id=reply.from_id)
    )
    admincheck = await is_admin(event.client, peer_id, reply.from_id)
    if admincheck:
        return await edit_delete(event, "`᥀︙عذراً لايمكنك تقييد الادمن هنا .`")
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    msg = chat_per.send_messages
    media = chat_per.send_media
    sticker = chat_per.send_stickers
    gif = chat_per.send_gifs
    gamee = chat_per.send_games
    ainline = chat_per.send_inline
    embed_link = chat_per.embed_links
    gpoll = chat_per.send_polls
    adduser = chat_per.invite_users
    cpin = chat_per.pin_messages
    changeinfo = chat_per.change_info
    try:
        umsg = result.participant.banned_rights.send_messages
        umedia = result.participant.banned_rights.send_media
        usticker = result.participant.banned_rights.send_stickers
        ugif = result.participant.banned_rights.send_gifs
        ugamee = result.participant.banned_rights.send_games
        uainline = result.participant.banned_rights.send_inline
        uembed_link = result.participant.banned_rights.embed_links
        ugpoll = result.participant.banned_rights.send_polls
        uadduser = result.participant.banned_rights.invite_users
        ucpin = result.participant.banned_rights.pin_messages
        uchangeinfo = result.participant.banned_rights.change_info
    except AttributeError:
        umsg = msg
        umedia = media
        usticker = sticker
        ugif = gif
        ugamee = gamee
        uainline = ainline
        uembed_link = embed_link
        ugpoll = gpoll
        uadduser = adduser
        ucpin = cpin
        uchangeinfo = changeinfo
    if input_str == "الدردشه":
        if msg:
            return await edit_delete(
                event, "`This Group is locked with messaging permission.`"
            )
        if not umsg:
            return await edit_delete(
                event, "`This User is already unlocked with messaging permission.`"
            )
        umsg = False
        locktype = "الرسائل"
    elif input_str == "الوسائط":
        if media:
            return await edit_delete(event, "`This Group is locked with sending media`")
        if not umedia:
            return await edit_delete(
                event, "`User is already unlocked with sending media`"
            )
        umedia = False
        locktype = "الوسائط"
    elif input_str == "الملصقات":
        if sticker:
            return await edit_delete(
                event, "`This Group is locked with sending stickers`"
            )
        if not usticker:
            return await edit_delete(
                event, "`This user is already unlocked with sending stickers`"
            )
        usticker = False
        locktype = "الملصقات"
    elif input_str == "الماركدون":
        if embed_link:
            return await edit_delete(
                event, "`This Group is locked with previewing links`"
            )
        if not uembed_link:
            return await edit_delete(
                event, "`This user is already unlocked with previewing links`"
            )
        uembed_link = False
        locktype = "الماركدون"
    elif input_str == "المتحركه":
        if gif:
            return await edit_delete(event, "`This Group is locked with sending GIFs`")
        if not ugif:
            return await edit_delete(
                event, "`This user is already unlocked with sending GIFs`"
            )
        ugif = False
        locktype = "المتحركات"
    elif input_str == "الالعاب":
        if gamee:
            return await edit_delete(event, "`This Group is locked with sending games`")
        if not ugamee:
            return await edit_delete(
                event, "`This user is already unlocked with sending games`"
            )
        ugamee = False
        locktype = "الالعاب"
    elif input_str == "الاونلاين":
        if ainline:
            return await edit_delete(
                event, "`This Group is locked with using inline bots`"
            )
        if not uainline:
            return await edit_delete(
                event, "`This user is already unlocked with using inline bots`"
            )
        uainline = False
        locktype = "اونلاين البوتات"
    elif input_str == "الاستفتاء":
        if gpoll:
            return await edit_delete(event, "`This Group is locked with sending polls`")
        if not ugpoll:
            return await edit_delete(
                event, "`This user is already unlocked with sending polls`"
            )
        ugpoll = False
        locktype = "الاستفتائات"
    elif input_str == "الاضافه":
        if adduser:
            return await edit_delete(
                event, "`This Group is locked with adding members`"
            )
        if not uadduser:
            return await edit_delete(
                event, "`This user is already unlocked with adding members`"
            )
        uadduser = False
        locktype = "اضافة الاعضاء"
    elif input_str == "التثبيت":
        if cpin:
            return await edit_delete(
                event,
                "`This Group is locked with pinning messages by users`",
            )
        if not ucpin:
            return await edit_delete(
                event,
                "`This user is already unlocked with pinning messages by users`",
            )
        ucpin = False
        locktype = "التثبيت"
    elif input_str == "المعلومات":
        if changeinfo:
            return await edit_delete(
                event,
                "`This Group is locked with Changing group info by users`",
            )
        if not uchangeinfo:
            return await edit_delete(
                event,
                "`This user is already unlocked with Changing group info by users`",
            )
        uchangeinfo = False
        locktype = "تغيير معلومات الكروب"
    elif input_str == "الكل":
        if not msg:
            umsg = False
        if not media:
            umedia = False
        if not sticker:
            usticker = False
        if not gif:
            ugif = False
        if not gamee:
            ugamee = False
        if not ainline:
            uainline = False
        if not embed_link:
            uembed_link = False
        if not gpoll:
            ugpoll = False
        if not adduser:
            uadduser = False
        if not cpin:
            ucpin = False
        if not changeinfo:
            uchangeinfo = False
        locktype = "الكل"
    else:
        if input_str:
            return await edit_delete(
                event, f"**Invalid lock type :** `{input_str}`", time=5
            )

        return await edit_or_reply(event, "`I can't lock nothing !!`")
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    lock_rights = ChatBannedRights(
        until_date=None,
        send_messages=umsg,
        send_media=umedia,
        send_stickers=usticker,
        send_gifs=ugif,
        send_games=ugamee,
        send_inline=uainline,
        embed_links=uembed_link,
        send_polls=ugpoll,
        invite_users=uadduser,
        pin_messages=ucpin,
        change_info=uchangeinfo,
    )
    try:
        await event.client(EditBannedRequest(peer_id, reply.from_id, lock_rights))
        await edit_or_reply(event, f"`᥀︙تـم فتـح {locktype} بنجـاح عن هذا الشخص .`")
    except BaseException as e:
        await edit_delete(
            event,
            f"`Do I have proper rights for that ??`\n\n**Error:** `{str(e)}`",
            time=5,
        )


@icssbot.on(admin_cmd(pattern="uperm(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="uperm(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    peer_id = event.chat_id
    user, reason = await get_user_from_event(event)
    if not user:
        return
    if not event.is_group:
        return await edit_delete(event, "`Idiot! ,This is not a group to lock things `")
    admincheck = await is_admin(event.client, peer_id, user.id)
    result = await event.client(
        functions.channels.GetParticipantRequest(channel=peer_id, user_id=user.id)
    )
    output = ""
    if admincheck:
        c_info = "✅" if result.participant.admin_rights.change_info else "❌"
        del_me = "✅" if result.participant.admin_rights.delete_messages else "❌"
        ban = "✅" if result.participant.admin_rights.ban_users else "❌"
        invite_u = "✅" if result.participant.admin_rights.invite_users else "❌"
        pin = "✅" if result.participant.admin_rights.pin_messages else "❌"
        add_a = "✅" if result.participant.admin_rights.add_admins else "❌"
        call = "✅" if result.participant.admin_rights.manage_call else "❌"
        output += f"**Admin rights of **{_format.mentionuser(user.first_name ,user.id)} **in {event.chat.title} chat are **\n"
        output += f"__تغيير معلومات الكروب :__ {c_info}\n"
        output += f"__حذف الرسائل :__ {del_me}\n"
        output += f"__حظر الاعضاء :__ {ban}\n"
        output += f"__اضافة الاعضاء :__ {invite_u}\n"
        output += f"__تثبيت الرسائل :__ {pin}\n"
        output += f"__Add admins :__ {add_a}\n"
        output += f"__Manage call :__ {call}\n"
    else:
        chat_per = (await event.get_chat()).default_banned_rights
        try:
            umsg = "❌" if result.participant.banned_rights.send_messages else "✅"
            umedia = "❌" if result.participant.banned_rights.send_media else "✅"
            usticker = "❌" if result.participant.banned_rights.send_stickers else "✅"
            ugif = "❌" if result.participant.banned_rights.send_gifs else "✅"
            ugamee = "❌" if result.participant.banned_rights.send_games else "✅"
            uainline = "❌" if result.participant.banned_rights.send_inline else "✅"
            uembed_link = "❌" if result.participant.banned_rights.embed_links else "✅"
            ugpoll = "❌" if result.participant.banned_rights.send_polls else "✅"
            uadduser = "❌" if result.participant.banned_rights.invite_users else "✅"
            ucpin = "❌" if result.participant.banned_rights.pin_messages else "✅"
            uchangeinfo = "❌" if result.participant.banned_rights.change_info else "✅"
        except AttributeError:
            umsg = "❌" if chat_per.send_messages else "✅"
            umedia = "❌" if chat_per.send_media else "✅"
            usticker = "❌" if chat_per.send_stickers else "✅"
            ugif = "❌" if chat_per.send_gifs else "✅"
            ugamee = "❌" if chat_per.send_games else "✅"
            uainline = "❌" if chat_per.send_inline else "✅"
            uembed_link = "❌" if chat_per.embed_links else "✅"
            ugpoll = "❌" if chat_per.send_polls else "✅"
            uadduser = "❌" if chat_per.invite_users else "✅"
            ucpin = "❌" if chat_per.pin_messages else "✅"
            uchangeinfo = "❌" if chat_per.change_info else "✅"
        output += f"{_format.mentionuser(user.first_name ,user.id)} **permissions in {event.chat.title} chat are **\n"
        output += f"__ارسال الرسائل :__ {umsg}\n"
        output += f"__ارسال الوسائط :__ {umedia}\n"
        output += f"__ارسال الملصقات :__ {usticker}\n"
        output += f"__ارسال المتحركه :__ {ugif}\n"
        output += f"__تضمين الالعاب :__ {ugamee}\n"
        output += f"__تضمين اونلاين البوتات المزعجه :__ {uainline}\n"
        output += f"__ارسال الاستفتائات :__ {ugpoll}\n"
        output += f"__تضمين الروابط :__ {uembed_link}\n"
        output += f"__اضافة الاعضاء :__ {uadduser}\n"
        output += f"__تثبيت الرسائل :__ {ucpin}\n"
        output += f"__تغيير معلومات الكروب :__ {uchangeinfo}\n"
    await edit_or_reply(event, output)


@icssbot.on(events.MessageEdited())
@icssbot.on(events.NewMessage())
async def check_incoming_messages(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    peer_id = event.chat_id
    if is_locked(peer_id, "الاوامر"):
        entities = event.message.entities
        is_command = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityBotCommand):
                    is_command = True
        if is_command:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "᥀︙عذراً لا املك صلاحيات الادمن هنا .\n`{}`".format(str(e))
                )
                update_lock(peer_id, "الاوامر", False)
    if is_locked(peer_id, "التوجيه") and event.fwd_from:
        try:
            await event.delete()
        except Exception as e:
            await event.reply(
                "᥀︙عذراً لا املك صلاحيات الادمن هنا .\n`{}`".format(str(e))
            )
            update_lock(peer_id, "التوجيه", False)
    if is_locked(peer_id, "الايميل"):
        entities = event.message.entities
        is_email = False
        if entities:
            for entity in entities:
                if isinstance(entity, types.MessageEntityEmail):
                    is_email = True
        if is_email:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "᥀︙عذراً لا املك صلاحيات الادمن هنا .\n`{}`".format(str(e))
                )
                update_lock(peer_id, "الايميل", False)
    if is_locked(peer_id, "الروابط"):
        entities = event.message.entities
        is_url = False
        if entities:
            for entity in entities:
                if isinstance(
                    entity, (types.MessageEntityTextUrl, types.MessageEntityUrl)
                ):
                    is_url = True
        if is_url:
            try:
                await event.delete()
            except Exception as e:
                await event.reply(
                    "᥀︙عذراً لا املك صلاحيات الادمن هنا .\n`{}`".format(str(e))
                )
                update_lock(peer_id, "الروابط", False)


@icssbot.on(events.ChatAction())
async def _(event):
    if not event.is_private:
        chat = await event.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            return
    # check for "lock" "bots"
    if not is_locked(event.chat_id, "البوتات"):
        return
    # bots are limited Telegram accounts,
    # and cannot join by themselves
    if event.user_added:
        users_added_by = event.action_message.sender_id
        is_ban_able = False
        rights = types.ChatBannedRights(until_date=None, view_messages=True)
        added_users = event.action_message.action.users
        for user_id in added_users:
            user_obj = await event.client.get_entity(user_id)
            if user_obj.bot:
                is_ban_able = True
                try:
                    await event.client(
                        functions.channels.EditBannedRequest(
                            event.chat_id, user_obj, rights
                        )
                    )
                except Exception as e:
                    await event.reply(
                        "᥀︙عذراً لا املك صلاحيات الادمن هنا .\n`{}`".format(
                            str(e)
                        )
                    )
                    update_lock(event.chat_id, "البوتات", False)
                    break
        if BOTLOG and is_ban_able:
            ban_reason_msg = await event.reply(
                "᥀︙! عذراً [user](tg://user?id={}) لايمكنك اضافة بوتات لهذه الدردشـه .".format(
                    users_added_by
                )
            )


CMD_HELP.update(
    {
        "locks": "**Plugin : **`locks`\
        \n\n**•  Syntax : **`.lock <all/type>`\
        \n•  **Function : **__Allows you to lock the permissions of the chat.__\
        \n\n**•  Syntax : **`.unlock <all/type>`\
        \n•  **Function : **__Allows you to unlock the permissions of the chat.__\
        \n\n•  **Syntax : **`.locks`\
        \n•  **Function : **__To see the active locks__\
        \n\n**•  Syntax : **`.plock <all/type>`\
        \n•  **Function : **__Allows you to lock the permissions of the replied user in that chat.__\
        \n\n**•  Syntax : **`.punlock <all/type>`\
        \n•  **Function : **__Allows you to unlock the permissions of the replied user in that chat.__\
        \n\n**•  Syntax : **`.uperm <reply/username>`\
        \n•  **Function : **__Shows you the admin rights if he is admin else will show his permissions in the chat__\
        \n\n•  **Note :** __Requires proper admin rights in the chat !! and DB Options are available only for lock and unlock commands.__\
        \n•  **Available message types to lock/unlock are: \
        \n•  API Options : **`msg`, `media`, `sticker`, `gif`, `preview` ,`game` ,`inline`, `poll`, `invite`, `pin`, `info`\
        \n**•  DB Options : **`bots`, `commands`, `email`, `forward`, `url`\
        "
    }
)
