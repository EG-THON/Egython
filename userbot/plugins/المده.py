"""
©Java : @Egython
  - Ralls UpTime
  - Commend: .المده
"""

import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "Egythonbot"
ICS_IMG = "https://telegra.ph/file/b1761128b8ca112b77f86.jpg"
ICSS_TEXT = "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 - 𝐄𝐠𝐲𝐭𝐡𝐨𝐧"
ICSEM = "**᥀︙**"


@icssbot.on(admin_cmd(outgoing=True, pattern="المده$"))
@icssbot.on(sudo_cmd(pattern="المده$", allow_sudo=True))
async def uptics(ics):
    if ics.fwd_from:
        return
    icsid = await reply_id(ics)
    icsupt = await get_readable_time((time.time() - StartTime))
    if ICS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"**{ICSEM} المستخدم :** {mention}\n"
        ics_c += f"**{ICSEM} مدة التشغيل :** `{icsupt}`"
        await ics.client.send_file(ics.chat_id, ICS_IMG, caption=ics_c, reply_to=icsid)
        await ics.delete()
    else:
        await edit_or_reply(
            ics,
            f"**{ICSS_TEXT}**\n\n"
            f"**{ICSEM} المستخدم :** {mention}\n"
            f"**{ICSEM} مدة التشغيل :** `{icsupt}`",
        )
