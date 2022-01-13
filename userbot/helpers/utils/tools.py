import os
from typing import Optional

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

from ...tosh import ed, eor
from ..tools import media_type
from .utils import runcmd


async def media_to_pic(event, reply):
    mediatype = media_type(reply)
    if mediatype not in ["Photo", "Round Video", "Gif", "Sticker", "Video"]:
        await ed(
            event,
            "**عذرا هذا النوع غير مدعوم.**",
        )
        return None
    catmedia = await reply.download_media(file="./temp")
    catevent = await eor(event, f"**جاري تحويل المتحركه انتظر. **")
    catfile = os.path.join("./temp/", "meme.png")
    if mediatype == "Sticker":
        if catmedia.endswith(".tgs"):
            await runcmd(
                f"lottie_convert.py --frame 0 -if lottie -of png '{catmedia}' '{catfile}'"
            )
        elif catmedia.endswith(".webp"):
            im = Image.open(catmedia)
            im.save(catfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        extractMetadata(createParser(catmedia))
        await runcmd(f"rm -rf '{catfile}'")
        await take_screen_shot(catmedia, 0, catfile)
        if not os.path.exists(catfile):
            await edit_delete(
                catevent, f"**عذرا لم استطع تحويل هذا النوع من الوسائط.**"
            )
            return None
    else:
        im = Image.open(catmedia)
        im.save(catfile)
    await runcmd(f"rm -rf '{catmedia}'")
    return [catevent, catfile, mediatype]


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
