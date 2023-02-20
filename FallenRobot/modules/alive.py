from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as telever
from telethon import __version__ as tlhver

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, SUPPORT_CHAT, pbot


@pbot.on_message(filters.command("بوت"))
async def awake(_, message: Message):
    TEXT = f"**هلا {message.from_user.mention},\n\nنعم يقلب البوت اسمي {BOT_NAME}**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **المطور :** [dev zeιn](tg://user?id={OWNER_ID})\n\n"
    BUTTON = [
        [
            InlineKeyboardButton("المساعدة", url=f"https://t.me/{BOT_USERNAME}?start=help"),
            InlineKeyboardButton("السورس", url=f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    await message.reply_photo(
        photo=START_IMG,
        caption=TEXT,
        reply_markup=InlineKeyboardMarkup(BUTTON),
    )


__mod_name__ = "البنك"
