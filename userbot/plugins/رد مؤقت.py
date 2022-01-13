#Egython

from asyncio import sleep


@icssbot.on(admin_cmd(pattern="رد (\d*) (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="رد (\d*) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    ics = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ics[1]
    ttl = int(ics[0])
    try:
        await event.delete()
    except Exception as e:
        LOGS.info(str(e))
    await sleep(ttl)
    await event.respond(message)


CMD_HELP.update(
    {
        "رد مؤقت": "**اسم الاضافـه : **`رد مؤقت`\
    \n\n**• الامر **`.رد + الوقـت بالثوانـي + الرسالـه`\
    \n**• الشرح **أرسل لك الرسالة المحددة بعد ذلك الوقت المحدد\
    "
    }
)
