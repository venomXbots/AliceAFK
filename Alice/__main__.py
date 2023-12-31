#
# Copyright (C) 2021-2022 by venomXbots@Github, < https://github.com/TeamInflex >.
#
# This file is part of < https://github.com/venomXbots/AliceAFK > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/venomXbots/AliceAFK/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib

from pyrogram import idle

from Alice.modules import ALL_MODULES

loop = asyncio.get_event_loop()


async def initiate_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Inflex.modules." + all_module)
    print("Started Alice AFK Bot.")
    await idle()
    print("GoodBye! Stopping Bot")


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
