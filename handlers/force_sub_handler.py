# (c) @PredatorHackerzZ

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def handle_force_sub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="𝐘𝐨𝐮 𝐚𝐫𝐞 𝐁𝐚𝐧𝐧𝐞𝐝 𝐭𝐨 𝐮𝐬𝐞 𝐦𝐞. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩](https://t.me/TeleRoid14).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        try:
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except FloodWait as e:
            await asyncio.sleep(e.x)
            invite_link = await bot.create_chat_invite_link(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATES_CHANNEL.startswith("-100") else Config.UPDATES_CHANNEL))
        except Exception as err:
            print(f"Unable to do Force Subscribe to {Config.UPDATES_CHANNEL}\n\nError: {err}")
            return 200
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**𝐏𝐥𝐞𝐚𝐬𝐞 𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐭𝐡𝐢𝐬 𝐁𝐨𝐭!**\n\n"
                 "𝐃𝐮𝐞 𝐭𝐨 𝐎𝐯𝐞𝐫𝐥𝐨𝐚𝐝, 𝐎𝐧𝐥𝐲 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐒𝐮𝐛𝐬𝐜𝐫𝐢𝐛𝐞𝐫𝐬 𝐜𝐚𝐧 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐁𝐨𝐭!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⭕ 𝐉𝐨𝐢𝐧 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ⭕", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 𝐑𝐞𝐟𝐫𝐞𝐬𝐡 🔄", callback_data="refreshForceSub")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="𝐒𝐨𝐦𝐞𝐭𝐡𝐢𝐧𝐠 𝐰𝐞𝐧𝐭 𝐖𝐫𝐨𝐧𝐠. 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐦𝐲 [𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩](https://t.me/TeleRoid14).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
