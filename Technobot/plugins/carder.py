from faker import Faker

from . import eor, techno

menu_category = "useless"


@techno.techno_cmd(
    pattern="gencc(?:\s|$)([\s\S]*)",
    command=("gencc", menu_category),
    info={
        "header": "To Make Fake Credit Card in short help u to generate fake cc",
        "usage": [
            "{tr}gencc",
        ],
    },
)
async def _(TECHNOevent):
    if TECHNOevent.fwd_from:
        return
    TECHNOcc = Faker()
    TECHNOname = TECHNOcc.name()
    TECHNOadre = TECHNOcc.address()
    TECHNOcard = TECHNOcc.credit_card_full()

    await eor(
        TECHNOevent,
        f"__**👤 NAME :- **__\n`{TECHNOname}`\n\n__**🏡 ADDRESS :- **__\n`{TECHNOadre}`\n\n__**💸 CARD :- **__\n`{TECHNOcard}`",
    )
