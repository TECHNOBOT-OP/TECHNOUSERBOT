import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from Technobot import StartTime, techno, technoversion

from ..Config import Config
from ..core.managers import eor
from ..helpers.functions import check_data_base_heal_th, get_readable_time, technoalive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

menu_category = "utils"


@techno.techno_cmd(
    pattern="techno$",
    command=("techno", menu_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}techno",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    technoevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    lal = list(EMOJI.split())
    EMOTES = random.choice(lal)
    sweetie_caption = (
        "**⚜ TechnoBot Is Online ⚜**\n\n" + f"{gvarstatus('ALIVE_TEMPLATE')}"
    )
    caption = sweetie_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        technover=technoversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    try:
        results = await event.client.inline_query(Config.BOT_USERNAME, caption)
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        return await eor(
            technoevent,
            f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{TECHNO_IMG}`",
        )
        
@techno.techno_cmd(
    pattern="alive$",
    command=("alive", menu_category),
    info={
        "header": "To check bot's alive status without buttons",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def aamjlive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    technoevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ALI_T = gvarstatus("ALIVE_TEXT")
    if ALI_T is None:
      ALIVE_TEXT = "**__MY BOT IS RUNNING PERFECTLY__**"
    else:
      ALIVE_TEXT = ALI_T
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    lal = list(EMOJI.split())
    EMOTES = random.choice(lal)
    ALIP = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/ac1541810568b41eb57d5.jpg"
    ldl = list(ALIP.split())
    ALIVE_PIC = random.choice(ldl)
    ALT = gvarstatus("ALIVE_TEMPLATE")
    if ALT is None:
      ALIVE_TEMPLATE = "╔───*.·:·.✧✦✧.·:·.*────╗\n"
      ALIVE_TEMPLATE += f"┣━ ⁭⁫{EMOTES} Sƚαƚυʂ : `{check_sgnirts}`\n"
      ALIVE_TEMPLATE += f"┣━ {EMOTES} Tҽʅҽƚԋσɳ : `{version.__version__}`\n"
      ALIVE_TEMPLATE += f"┣━ ⁭⁫{EMOTES} ƚҽƈԋɳσ Bσƚ : `{technoversion}`\n"
      ALIVE_TEMPLATE += f"┣━ ⁭⁫{EMOTES} Uρƚιɱҽ : `{uptime}`\n"
      ALIVE_TEMPLATE += f"┣━ ⁭⁫{EMOTES} Pιɳɠ : `{ms}` ms\n"
      ALIVE_TEMPLATE += f"┣━ ⁭⁫{EMOTES} Pყƚԋσɳ  : `{python_version()}`\n"
      ALIVE_TEMPLATE += "╚───*.·:·.✧✦✧.·:·.*────╝\n"
      ALIVE_TEMPLATE += "  ┏━━━━━━━━━━━━━━┓\n"
      ALIVE_TEMPLATE += f"  ┣ ⁭{EMOTES} Oɯɳҽɾ : {mention}\n"
      ALIVE_TEMPLATE += "  ┗━━━━━━━━━━━━━━┛\n"
    else:
      ALIVE_TEMPLATE = ALT
    sweetie_caption = (
        f"**⚜ TechnoBot is Online ⚜**\n\n" + f"{ALIVE_TEMPLATE}"
    )
    caption = sweetie_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        technover=technoversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    try:
        await borg.send_file(event.chat_id,reply_to=reply_to_id, file=ALIVE_PIC, caption=caption)
        await event.delete()
    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        return await eor(
            technoevent,
            f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{ALIVE_PIC}`",
        )


"""
temp = {ALIVE_TEXT}
**{EMOTES} Master:** {mention}
**{EMOTES} Uptime :** `{uptime}`
**{EMOTES} Telethon Version :** `{telever}`
**{EMOTES} Technouserbot Version :** `{technover}`
**{EMOTES} Python Version :** `{pyver}`
**{EMOTES} Database :** `{dbhealth}`
"""


@techno.techno_cmd(
    pattern="blive$",
    command=("blive", menu_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}blive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    a = gvarstatus("ALIVE_EMOJI") or "✥"
    kiss = list(a.split())
    EMOJI = random.choice(kiss)
    techno_caption = "**TechnoBot Is Online**\n\n"
    techno_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    techno_caption += f"**{EMOJI} Technouserbot Version :** `{technoversion}`\n"
    techno_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    techno_caption += f"**{EMOJI} Uptime :** {uptime}\n"
    techno_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.BOT_USERNAME, techno_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/0dfc14d3f1bab31dccd6b.jpg"
file2 = "https://telegra.ph/file/dae1674ae3780ed6d123f.jpg"
file3 = "https://telegra.ph/file/d01a2163ad90a87a99c8c.jpg"
file4 = "https://telegra.ph/file/a9e2a9fe517e22fd441f6.jpg"
file5 = "https://telegra.ph/file/6827fe35330c99e5a67c0.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"**TechnoBot Is Up**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{mention}』«««\n"
pm_caption += f"┣†ê¢hñðßð† ~ {technoversion}\n"
pm_caption += f"┣𝕋𝔼ℂℍℕ𝕆 ~ [Owner](https://t.me/Technoboy_02)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/TechnoBot_Support)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/TECHNOBOT-OP/TECHNOBOT)\n"
pm_caption += f"**╰────────────**\n"


@techno.techno_cmd(
    pattern="about$",
    command=("about", menu_category),
    info={
        "header": "To check bot's alive status ",
        "options": "Random Media Automatically Get It",
        "usage": [
            "{tr}about",
        ],
    },
)
async def amireallyalive(yes):
    await yes.get_chat()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)
    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await yes.delete()
    await borg.send_file(yes.chat_id, PM_IMG, caption=pm_caption)
    await yes.delete()


@techno.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await technoalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
