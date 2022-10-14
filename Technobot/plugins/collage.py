# collage plugin for TechnoUserBot by @TECHNO_K_BOY

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from Technobot import techno

from ..core.managers import eod, eor
from ..helpers import reply_id
from ..helpers.utils import _technoutils
from . import make_gif

menu_category = "utils"


@techno.techno_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", menu_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    technoinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    technoid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    technosticker = await reply.download_media(file="./temp/")
    if not technosticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(technosticker)
        await event.edit("`Media format is not supported...`")
        return
    if technoinput:
        if not technoinput.isdigit():
            os.remove(technosticker)
            await event.edit("`You input is invalid, check help`")
            return
        technoinput = int(technoinput)
        if not 0 < technoinput < 10:
            os.remove(technosticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        technoinput = 3
    if technosticker.endswith(".tgs"):
        hmm = await make_gif(event, technosticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(technosticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = technosticker
    endfile = "./temp/collage.png"
    technocmd = f"vcsi -g {technoinput}x{technoinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _technoutils.runcmd(technocmd))[:2]
    if not os.path.exists(endfile):
        for files in (technosticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=technoid,
    )
    await event.delete()
    for files in (technosticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
