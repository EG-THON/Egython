# edit By: @Egython


import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from userbot import CMD_HELP
from userbot.utils import admin_cmd

# ====================== CONSTANT ===============================
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "** ◄ تم تغير صورة حسابك بنجاح .**"
PP_TOO_SMOL = "** ◄ هذه الصوره صغيره جدا قم بختيار صوره اخرى  .**"
PP_ERROR = "** ◄ حدث خطا اثناء معالجه الصوره  .**"
BIO_SUCCESS = "** ◄ تم تغير بايو حسابك بنجاح .**"
NAME_OK = "** ◄ تم تغير اسم حسابك بنجاح .**"
USERNAME_SUCCESS = "**◄ تم تغير معرف حسابك بنجاح .**"
USERNAME_TAKEN = "** ◄ هذا المعرف مستخدم  .**"
# ===============================================================
@bot.on(admin_cmd(pattern="a2c(?: |$)(.*)"))
async def _(event):
    event.pattern_match.group(1)
    if event.reply_to_msg_id:
        hmm = await event.get_reply_message()
        id_s = hmm.sender_id
    elif event.pattern_match.group(1):
        id_s = event.pattern_match.group(1)
    elif event.is_private:
        id_s = await event.get_input_chat()
    user_s = await event.client.get_entity(id_s)
    if user_s.last_name is None:
        sed_m = " "
    else:
        sed_m = user_s.last_name
    await event.client(
        functions.contacts.AddContactRequest(
            id=id_s,
            first_name=user_s.first_name,
            last_name=sed_m,
            phone="123456",
            add_phone_privacy_exception=True,
        )
    )
    star = await event.edit("**Added To Contacts SucessFully**")
    await asyncio.sleep(3)
    await star.delete()

@bot.on(admin_cmd(pattern="ضع بايو (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(about=bio)  # pylint:disable=E0602
        )
        await event.edit("**◄ تم تغير بايو حسابك بنجاح .**")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="ضع اسم ((.|\n)*)"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "|" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("**◄ تم تغير اسم حسابك بنجاح .**")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@bot.on(admin_cmd(pattern="جلب صوره"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("**◄ جاري تنزيل صورة ملفي الشخصي  .**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await event.client.download_media(  # pylint:disable=E0602
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("**◄ جاري تحميل صورة ملفي الشخصي  .**")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await event.edit("**◄ يجب ان يكون الحجم اقل من 2 ميغا بايت .**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)  # pylint:disable=E0602
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(
                        file=catpic, video=catvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("**◄ تم تغير صورة حسابك بنجاح .**")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:


@bot.on(admin_cmd(outgoing=True, pattern="ضع معرف (.*)"))
async def update_username(username):
    """ امر - ضع معرف - لتغير معرف حسابك """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)


@bot.on(admin_cmd(outgoing=True, pattern="الحساب$"))
async def count(event):
    """ هذا امر الحساب - لعرض معلومات الحساب """
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("**◄ جاري المعـالجه.**")
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)

    result += f"𝐒𝐨𝐮𝐫𝐜𝐞 𝐄𝐠𝐲𝐭𝐡𝐨𝐧 - 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    result += f"**᥀︙المستخدمون :**\t**{u}**\n"
    result += f"**᥀︙المجموعات :**\t**{g}**\n"
    result += f"**᥀︙المجموعات الخارقه :**\t**{c}**\n"
    result += f"**᥀︙القنوات :**\t**{bc}**\n"
    result += f"**᥀︙البوتات :**\t**{b}**\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"

    await event.edit(result)


@bot.on(admin_cmd(outgoing=True, pattern=r"تهيئه"))
async def remove_profilepic(delpfp):
    """ امر حذف الصور - لحذ صوره واحد من حسابك او جميعها """
    group = delpfp.text[8:]
    if group == "الكل":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"**◄ تم حذف ↩︎** {len(input_photos)} **من صور حسابك.**")


@bot.on(admin_cmd(pattern="كروباتي$"))
async def _(event):
    if event.fwd_from:
        return
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"**◄ كروبك ↩︎** {channel_obj.title} @{channel_obj.username} .\n"
    await event.edit(output_str)


name = "Profile Photos"


@bot.on(admin_cmd(pattern="افاتار ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="افاتار ?(.*)", allow_sudo=True))
async def potocmd(event):
    uid = "".join(event.raw_text.split(maxsplit=1)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        photos = await event.client.get_profile_photos(user.sender)
        u = True
    else:
        photos = await event.client.get_profile_photos(chat)
        u = False
    if uid.strip() == "":
        uid = 1
        if int(uid) > (len(photos)):
            return await edit_delete(
                event, "`No photo found of this NIBBA / NIBBI. Now u Die!`"
            )
        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    elif uid.strip() == "الكل":
        if len(photos) > 0:
            await event.client.send_file(event.chat_id, photos)
        else:
            try:
                if u:
                    photo = await event.client.download_profile_photo(user.sender)
                else:
                    photo = await event.client.download_profile_photo(event.input_chat)
                await event.client.send_file(event.chat_id, photo)
            except Exception:
                return await edit_delete(event, "**عذراً .. لا توجد افاتارات لهذا الشخص؟!**")
    else:
        try:
            uid = int(uid)
            if uid <= 0:
                await edit_or_reply(
                    event, "```number Invalid!``` **Are you Comedy Me ?**"
                )
                return
        except BaseException:
            await edit_or_reply(event, "`Are you comedy me ?`")
            return
        if int(uid) > (len(photos)):
            return await edit_delere(
                event, "**عذراً .. لا توجد افاتارات لهذا الشخص؟!**"
            )

        send_photos = await event.client.download_media(photos[uid - 1])
        await event.client.send_file(event.chat_id, send_photos)
    await event.delete()


CMD_HELP.update(
    {
        "الحساب": ".ضع معرف + المعرف الجديد\
\nالشـرح •• لتغيير معرف حسابك.\
\n\n.ضع اسم الاسم الاول / .ضع اسم الاسم الاول + الاسم الثاني\
\nالشـرح •• لتغيير اسم حسابك\
\n\n.جلب صوره\
\nالشـرح •• بالرد ع الصوره لوضعها افاتار حسابك.\
\n\n.افاتار / .افاتار الكل\
\nالشـرح •• بالرد ع شخص لجلب افاتاره /.افاتار الكل لجلب كل افاتارات الشخص.\
\n\n.ضع بايو + البايو الجديد\
\nالشـرح •• لتغير بايو حسابك.\
\n\n.تهيئه / .تهيئه العدد/الكل\
\nالشـرح •• مسـح كل صور حسابك.\
\n\n.كروباتي\
\nالشـرح •• لعــرض كل قنواتك وكروباتك \
\n\n.الحساب\
\nالشـرح •• قائمـه بجميـع كروباتك وقنواتك والبوتات الخ......"
    }
)
@bot.on(admin_cmd(pattern="معرفه (.*)"))  # pylint:disable=E0602
async def _(event):
    ty = event.pattern_match.group(1)
    await event.edit("- يتم التعرف")
    if not ty:
        await event.edit("يجب وضع ايدي المستخدم للحصول على معرفه")
        return
    a = await bot.get_entity(int(ty))
    if not a:
        await event.edit("Your id is invalid")
        return
    b = a.username
    c = f"المعرف هو  :  "
    if not b:
        await event.edit("- ايدي المستخدم غير صالح")
        return
    await event.respond(f"{c}@{b}")
