import asyncio
from collections import deque

@bot.on(admin_cmd(outgoing=True, pattern="واو$"))
@bot.on(sudo_cmd(pattern="واو$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "😲.")
    deq = deque(list("😯😦😧😮😲😦😮😯"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)