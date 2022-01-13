#Egython

from datetime import datetime

@icssbot.on(
    icss_cmd(pattern="حساب العمر")
)
async def _(e):
    icst = e.txt
    yar = icst[4:5]
    if not yar:
       yar = "2"
    YearNow = datetime.now().year
    MyAge = YearNow - yar
    await eor(e, "عمرك هو {}".format(MyAge))
