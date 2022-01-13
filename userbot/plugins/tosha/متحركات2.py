# TSHEGif for R by: @Egython

from .. import reply_id as rd
from . import *


@icssbot.on(icss_cmd(outgoing=True, pattern="ش1$"))
@icssbot.on(sudo_cmd(pattern="ش1$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    Ti = await rd(icss)
    if fy_gif:
        icss_caption = f"**{TSHE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**⌯ المتحركه الاولى .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif, caption=icss_caption, reply_to=Ti
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ش2$"))
@icssbot.on(sudo_cmd(pattern="ش2$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    th = await rd(icss)
    if fy_gif2:
        icss_caption = f"**{TSHE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**⌯ المتحركه الثانيه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif2, caption=icss_caption, reply_to=th
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ش3$"))
@icssbot.on(sudo_cmd(pattern="ش3$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    kh = await rd(icss)
    if fy_gif3:
        icss_caption = f"**{TSHE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**⌯ المتحركه الثالثه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif3, caption=icss_caption, reply_to=kh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ش4$"))
@icssbot.on(sudo_cmd(pattern="ش4$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    wh = await rd(icss)
    if fy_gif4:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**⌯ المتحركه الرابعه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif4, caption=fyc, reply_to=wh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ش5$"))
@icssbot.on(sudo_cmd(pattern="ش5$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    ih = await rd(icss)
    if fy_gif5:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**⌯ المتحركه الخامسه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif5, caption=fyc, reply_to=ih
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ش6$"))
@icssbot.on(sudo_cmd(pattern="ش6$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    uh = await rd(icss)
    if fy_gif6:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**⌯ المتحركه السادسه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif6, caption=fyc, reply_to=uh
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ش7$"))
@icssbot.on(sudo_cmd(pattern="ش7$", allow_sudo=True))
async def fygif(icss):
    if icss.fwd_from:
        return
    oh = await rd(icss)
    if fy_gif7:
        fyc = f"**{TSHE}**\n"
        fyc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        fyc += f"**⌯ المتحركه السابعه .**"
        await icss.client.send_file(
            icss.chat_id, fy_gif7, caption=fyc, reply_to=oh
        )

