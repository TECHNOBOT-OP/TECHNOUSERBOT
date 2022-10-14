from . import techno

menu_category = "tools"


@techno.techno_cmd(
    pattern="sdpic(?:\s|$)([\s\S]*)",
    command=("sdpic", menu_category),
    info={
        "header": "This Command Can Capture The Self Destruction Picture",
        "usage": "{tr}sdpic <reply to self distruct pic>",
        "examples": "{tr}sdpic",
    },
)
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await event.client.send_file(
        event.chat_id,
        pic,
        caption=f"""
OwO!! LoL, Secret Pic Mode Pic Destroyed!!
Pic captured By †ê¢hñðßð†
  """,
    )
    await event.delete()
