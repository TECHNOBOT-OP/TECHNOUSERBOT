# created by @eve_enryu
# edited & fix by @Technoboy_02

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Technobot import techno

from ..core.managers import eor

menu_category = "extra"


@techno.techno_cmd(
    pattern="firmware ([\s\S]*)",
    command=("firmware", menu_category),
    info={
        "header": "To get lastest Firmware.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}firmware <codename>",
        "examples": "{tr}firmware whyred",
    },
)
async def firmware(event):
    "To get lastest Firmware."
    link = event.pattern_match.group(1)
    firmware = "firmware"
    if link:
        technoevent = await eor(event, "```Processing```")
        async with event.client.conversation("@XiaomiGeeksBot") as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=774181428)
                )
                await conv.send_message(f"/{firmware} {link}")
                respond = await response
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
            else:
                await technoevent.delete()
                await event.client.forward_messages(event.chat_id, respond.message)
    else:
        await eod(event, "check description how to use me")


@techno.techno_cmd(
    pattern="vendor ([\s\S]*)",
    command=("vendor", menu_category),
    info={
        "header": "To get lastest Vendor.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}vendor <codename>",
        "examples": "{tr}vendor whyred",
    },
)
async def vendor(event):
    "To get lastest Vendor."
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    vendor = "vendor"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@techno.techno_cmd(
    pattern="xspecs ([\s\S]*)",
    command=("xspecs", menu_category),
    info={
        "header": "To get quick spec information about device",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}xspecs <codename>",
        "examples": "{tr}xspecs whyred",
    },
)
async def xpexcs(event):
    "To get quick spec information about device"
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    specs = "specs"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@techno.techno_cmd(
    pattern="fastboot ([\s\S]*)",
    command=("fastboot", menu_category),
    info={
        "header": "To get latest fastboot MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}fastboot <codename>",
        "examples": "{tr}fastboot whyred",
    },
)
async def fastboot(event):
    "To get latest fastboot MIUI."
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    fboot = "fastboot"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@techno.techno_cmd(
    pattern="recovery ([\s\S]*)",
    command=("recovery", menu_category),
    info={
        "header": "To get latest recovery MIUI.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}recovery <codename>",
        "examples": "{tr}recovery whyred",
    },
)
async def recovery(event):
    "To get latest recovery MIUI."
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    recovery = "recovery"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@techno.techno_cmd(
    pattern="pb ([\s\S]*)",
    command=("pb", menu_category),
    info={
        "header": "To get latest PBRP.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}pb <codename>",
        "examples": "{tr}pb whyred",
    },
)
async def pb(event):
    "To get latest PBRP."
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    pitch = "pb"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@techno.techno_cmd(
    pattern="of ([\s\S]*)",
    command=("of", menu_category),
    info={
        "header": "To get latest ORangeFox Recover.",
        "description": "Works for Xiaomeme devices only",
        "usage": "{tr}of <codename>",
        "examples": "{tr}of whyred",
    },
)
async def of(event):
    "To get latest ORangeFox Recover."
    link = event.pattern_match.group(1)
    if link:
        pass
    else:
        return await eor(event, "check description how to use me")
    ofox = "of"
    technoevent = await eor(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            return await technoevent.edit("```Unblock @XiaomiGeeksBot plox```")
        else:
            await technoevent.delete()
            await event.client.forward_messages(event.chat_id, respond.message)
