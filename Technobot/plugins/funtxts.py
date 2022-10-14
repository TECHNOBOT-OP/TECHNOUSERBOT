import nekos

from Technobot import techno

from ..core.managers import eor

menu_category = "fun"


@techno.techno_cmd(
    pattern="why$",
    command=("why", menu_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(techno):
    "Some random Funny questions"
    lol = nekos.why()
    await eor(techno, lol)


@techno.techno_cmd(
    pattern="fact$",
    command=("fact", menu_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(techno):
    "Some random facts"
    tol = nekos.fact()
    await eor(techno, tol)
