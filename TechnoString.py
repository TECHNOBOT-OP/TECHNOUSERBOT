import os

os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print("•••   TECHNOBOT  SESSION  GENERATOR   •••")
print("\nHello!! Welcome to TechnoBot Session Generator\n")
okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Choose the string session type: \n1. TechnoBot \n2. Music Bot")
    library = input("\nYour Choice: ")
    if library == "1":
        print("\nTelethon Session For TechnoBot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as boy:
            print("\nYour TechnoBot Session Is sent in your Telegram Saved Messages.")
            boy.send_message(
                "me", f"#TECHNOBOT #TECHNO_STRING \n\n`{boy.session.save()}`"
            )
    elif library == "2":
        print("Pyrogram Session for Music Bot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(":memory:", api_id=APP_ID, api_hash=API_HASH) as boy:
            print("\nYour MusicBot Session Is sent in your Telegram Saved Messages.")
            boy.send_message(
                "me",
                f"#TECHNO_MUSIC #MUSICBOT_SESSION\n\n`{boy.export_session_string()}`",
            )
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("Invalid Input")
