#    This file is part of the ChannelAutoForwarder distribution (https://github.com/Captainamarica/NightVissionSenderBot).
#    Copyright (c) 2022 NAVANJANA
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/DARKEMPIRESL/ChannelAutoForwarder/blob/main/License> .

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest
from pyrogram import Client, idle
from vars import var

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apiid = config("API_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    datgbot = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
    plugins=dict(root="plugins")
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@datgbot.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await datgbot(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hi `{ok.user.first_name}`!\n\nI am a channel auto-post bot by @NA_VA_N_JA_NA1!! Read /help to know more!\n\nI can be used in only two channels (one user) at a time. Kindly deploy your own bot.\n\n[More bots](https://t.me/NightVission)..", buttons=[Button.url("Channel", url="https://t.me/NightVission"), Button.url("Dev", url="https://t.me/NightVissionSupport")], link_preview=False)


@datgbot.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\nThis bot will send all new posts in one channel to the other channel. (without forwarded tag)!\n\nAdd me to both the channels and make me an admin in both, and all new messages would be autoposted on the linked channel!!\n\nLiked the bot? Visit Support Group & Comment @NightVissionSupport :)")

@datgbot.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl, event.message)
        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Do visit @NightVissionSupport..")
datgbot.run_until_disconnected()
