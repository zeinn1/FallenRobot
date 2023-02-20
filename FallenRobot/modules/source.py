from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as o
from telethon import __version__ as s

from FallenRobot import BOT_NAME, BOT_USERNAME, OWNER_ID, START_IMG, pbot


@pbot.on_message(filters.command(["سورس كرستين", "سورس"]))
async def repo(_, message: Message):
    await message.reply_photo(
        photo=START_IMG,
        caption=f"""**ʜᴇʏ {message.from_user.mention},

اهلين انا بوت اسمي [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

**» آلمـطـور زيـﮯن :**ĐËV ŹËÏŅ
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("آلمـطـور", user_id=OWNER_ID),
                    InlineKeyboardButton(
                        "آلسـورسـ",
                        url="https://t.me/S_EG_P",
                    ),
                ]
            ]
        ),
    )


__mod_name__ = "السورس"
