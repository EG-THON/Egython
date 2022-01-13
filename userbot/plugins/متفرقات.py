#Egython

import asyncio
import io
import os
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    
    
@icssbot.on(admin_cmd(pattern="نصائح$"))
@icssbot.on(sudo_cmd(pattern="نصائح$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "pytuneteller pisces --today"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@icssbot.on(admin_cmd(pattern="حكم$"))
@icssbot.on(sudo_cmd(pattern="حكم$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "jotquote"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@icssbot.on(admin_cmd(pattern="مشاهير$"))
@icssbot.on(sudo_cmd(pattern="مشاهير$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "csvfaker -r 10 first_name last_name job"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@icssbot.on(admin_cmd(pattern="اقتباس$"))
@icssbot.on(sudo_cmd(pattern="اقتباس$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "kwot"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "kwot.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)


@icssbot.on(admin_cmd(pattern="برمجيات$"))
@icssbot.on(sudo_cmd(pattern="برمجيات$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "programmingquotes -l EN"
    eply_to_id = event.message.id
    if event.reply_to_msg_id:
        eply_to_id = event.reply_to_msg_id
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    OUTPUT = f"{o}"
    if len(OUTPUT) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "env.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=eply_to_id,
            )
            await event.delete()
    else:
        event = await edit_or_reply(event, OUTPUT)
        
CMD_HELP.update(
    {
        "الاعدادات": "**اسم الاضافـه : **`الاعدادات`\
    \n\n**• الامر **`.نصائح`\
    \n**• الشرح **لــعرض نصائـح انكليزيـه مقتبسـه من علماء ومشـاهير\
    \n\n**• الامر **`.حكم`\
    \n**• الشرح **لعرض حكمـه عشـوائيه بالانكلش\
    \n\n**• الامر **`.مشاهير`\
    \n**• الشرح **لــعرض مشاهير ووظائفهم عشوائي\
    \n\n**• الامر **`.اقتباس`\
    \n**• الشرح **لــعرض اقتباسـات اجنبيـه بالانكلــش.\
    \n\n**• الامر **`.برمجيات`\
    \n**• الشرح **لــعرض اقتباسـات ونصائـح برمجيـه\
    "
    }
)
