#    Egython - UserBot
#    (c) @Egython

U = "𝐒𝐨𝐮𝐫𝐜𝐞 𝐄𝐠𝐲𝐭𝐡𝐨𝐧 - 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬.\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**᥀︙ قائـمه اوامر الالعاب :** \n◄  `.بلاي` لعرض قائمـة الالعـاب الاحترافيـه\n◄  `.اكس او`\n◄  `.سهم`\n◄  `.نرد`\n◄  `.سلة`\n◄  `.قدم`\n◄  `.حظ` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n• 𝖢𝖧 : @EGYTHON"

@bot.on(admin_cmd(pattern="م22"))
@bot.on(sudo_cmd(pattern="م22", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, U)

@bot.on(admin_cmd(pattern="اكس او$"))
@bot.on(sudo_cmd(pattern="اكس او$", allow_sudo=True))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
