# (c) @AbirHasan2005 | @PredatorHackerzZ

import asyncio
from configs import Config
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64


async def ForwardToChannel(bot: Client, message: Message, editable: Message):
    try:
        __SENT = await message.forward(Config.DB_CHANNEL)
        return __SENT
    except FloodWait as sl:
        if sl.x > 45:
            await asyncio.sleep(sl.x)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.x)}s` from `{str(editable.chat.id)}` !!",
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("👤𝐁𝐚𝐧 𝐔𝐬𝐞𝐫", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        return await ForwardToChannel(bot, message, editable)


async def SaveBatchMediaInChannel(bot: Client, editable: Message, message_ids: list):
    try:
        message_ids_str = ""
        for message in (await bot.get_messages(chat_id=editable.chat.id, message_ids=message_ids)):
            sent_message = await ForwardToChannel(bot, message, editable)
            if sent_message is None:
                continue
            message_ids_str += f"{str(sent_message.message_id)} "
            await asyncio.sleep(2)
        SaveMessage = await bot.send_message(
            chat_id=Config.DB_CHANNEL,
            text=message_ids_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("𝐃𝐞𝐥𝐞𝐭𝐞 𝐁𝐚𝐭𝐜𝐡", callback_data="closeMessage")
            ]])
        )
        share_link = f"https://t.me/TeleRoid_FileStore_bot?start=PredatorHackerzZ_{str_to_b64(str(SaveMessage.message_id))}"
        await editable.edit(
            f"**Batch files Added in Database!**\n\nHere is the Permanent Link Of Your Media: {share_link} \n\n"
            f"Just Click On The Given Shareable Link!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open Link", url=share_link)],
                 [InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
                  InlineKeyboardButton("⭕ Support ⭕", url="https://t.me/TeleRoid14")]]
            ),
            disable_web_page_preview=True
        )
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#BATCH_SAVE:\n\n[{editable.reply_to_message.from_user.first_name}](tg://user?id={editable.reply_to_message.from_user.id}) Got Batch Link!",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("𝐎𝐩𝐞𝐧 𝐋𝐢𝐧𝐤", url=share_link)]])
        )
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👤𝐁𝐚𝐧 𝐔𝐬𝐞𝐫", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )


async def SaveMediaInChannel(bot: Client, editable: Message, message: Message):
    try:
        forwarded_msg = await message.forward(Config.DB_CHANNEL)
        file_er_id = str(forwarded_msg.message_id)
        await forwarded_msg.reply_text(
            f"#PRIVATE_FILE:\n\n[{message.from_user.first_name}](tg://user?id={message.from_user.id}) Got File Link!",
            parse_mode="Markdown", disable_web_page_preview=True)
        share_link = f"https://t.me/TeleRoid_FileStore_bot?start=PredatorHackerzZ_{str_to_b64(file_er_id)}"
        await editable.edit(
            f"**Your Media Stored in My Database!**\n\nHere is the Permanent Shareable Link Of Your Files: {share_link} \n\n"
            f"Just Click On the Link to Reterive the Files!",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open Link", url=share_link)],
                 [InlineKeyboardButton("⭕ Channel ⭕", url="https://t.me/TeleRoidGroup"),
                  InlineKeyboardButton("⭕ Support ⭕", url="https://t.me/TeleRoid14")]]
            ),
            disable_web_page_preview=True
        )
    except FloodWait as sl:
        if sl.x > 45:
            await asyncio.sleep(sl.x)
            await bot.send_message(
                chat_id=int(Config.LOG_CHANNEL),
                text=f"#FloodWait:\nGot FloodWait of `{str(sl.x)}s` from `{str(editable.chat.id)}` !!",
                parse_mode="Markdown",
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("👤𝐁𝐚𝐧 𝐔𝐬𝐞𝐫", callback_data=f"ban_user_{str(editable.chat.id)}")]
                    ]
                )
            )
        await SaveMediaInChannel(bot, editable, message)
    except Exception as err:
        await editable.edit(f"Something Went Wrong!\n\n**Error:** `{err}`")
        await bot.send_message(
            chat_id=int(Config.LOG_CHANNEL),
            text=f"#ERROR_TRACEBACK:\nGot Error from `{str(editable.chat.id)}` !!\n\n**Traceback:** `{err}`",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("👤𝐁𝐚𝐧 𝐔𝐬𝐞𝐫", callback_data=f"ban_user_{str(editable.chat.id)}")]
                ]
            )
        )
