#
# Copyright (C) 2021-2022 by TeamInflex@Github, < https://github.com/TeamInflex >.
#
# Copyright (C) 2021-2022 by venomXbots@Github, < https://github.com/TeamInflex >.
#
# This file is part of < https://github.com/venomXbots/AliceAFK > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/venomXbots/AliceAFK/blob/master/LICENSE >
#
# All rights reserved.

import asyncio

from typing import Union
from datetime import datetime, timedelta
from Alice import cleanmode, app, botname
from Alice.database import is_cleanmode_on
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


async def put_cleanmode(chat_id, message_id):
    if chat_id not in cleanmode:
        cleanmode[chat_id] = []
    time_now = datetime.now()
    put = {
        "msg_id": message_id,
        "timer_after": time_now + timedelta(minutes=5),
    }
    cleanmode[chat_id].append(put)


async def auto_clean():
    while not await asyncio.sleep(30):
        try:
            for chat_id in cleanmode:
                if not await is_cleanmode_on(chat_id):
                    continue
                for x in cleanmode[chat_id]:
                    if datetime.now() > x["timer_after"]:
                        try:
                            await app.delete_messages(chat_id, x["msg_id"])
                        except FloodWait as e:
                            await asyncio.sleep(e.x)
                        except:
                            continue
                    else:
                        continue
        except:
            continue


asyncio.create_task(auto_clean())


RANDOM = [
    "https://telegra.ph/file/b528d894684d8583b00aa.jpg",
]


HELP_TEXT = f"""ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {botname}'s ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ.

- ᴡʜᴇɴ sᴏᴍᴇᴏɴᴇ ᴍᴇɴᴛɪᴏɴs ʏᴏᴜ ɪɴ ᴀ ᴄʜᴀᴛ, ᴛʜᴇ ᴜsᴇʀ ᴡɪʟʟ ʙᴇ ɴᴏᴛɪғɪᴇᴅ ʏᴏᴜ ᴀʀᴇ ᴀғᴋ. ʏᴏᴜ ᴄᴀɴ ᴇᴠᴇɴ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇᴀsᴏɴ ғᴏʀ ɢᴏɪɴɢ ᴀғᴋ, ᴡʜɪᴄʜ ᴡɪʟʟ ʙᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜsᴇʀ ᴀs ᴡᴇʟʟ.


/afk - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ.

/afk [Reason] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀ ʀᴇᴀsᴏɴ.

/afk [Replied to a Sticker/Photo] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴏғғʟɪɴᴇ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴏʀ sᴛɪᴄᴋᴇʀ.

/afk [Replied to a Sticker/Photo] [Reason] - ᴛʜɪs ᴡɪʟʟ sᴇᴛ ʏᴏᴜ ᴀғᴋ ᴡɪᴛʜ ᴀɴ ɪᴍᴀɢᴇ ᴀɴᴅ ʀᴇᴀsᴏɴ ʙᴏᴛʜ.

/settings - ᴛᴏ ᴄʜᴀɴɢᴇ ᴏʀ ᴇᴅɪᴛ ʙᴀsɪᴄ sᴇᴛᴛɪɴɢs ᴏғ ᴀғᴋ ʙᴏᴛ.
"""

def settings_markup(status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(text="🔄 ᴄʟᴇᴀɴ ᴍᴏᴅᴇ", callback_data="cleanmode_answer"),
            InlineKeyboardButton(
                text="✅ Enabled" if status == True else "❌ Disabled",
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text="🗑 ᴄʟᴏsᴇ ᴍᴇɴᴜ", callback_data="close"),
        ],
    ]
    return buttons
