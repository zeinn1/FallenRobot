import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext
from telegram.ext.dispatcher import run_async

from FallenRobot import BOT_NAME, BOT_USERNAME, dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler


@run_async
def handwrite(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = update.effective_message.text.split(None, 1)[1]
    m = message.reply_text("Writing the text...")
    req = requests.get(f"https://api.sdbots.tk/write?text={text}").url
    message.reply_photo(
        photo=req,
        caption=f"""
Successfully Written Text 💘

✨ **Written By :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **Requested by :** {update.effective_user.first_name}
❄ **Link :** `{req}`""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=req),
                ],
            ]
        ),
    )
    m.delete()


__help__ = """
 يكتب النص المعطى على صفحة بيضاء بقلم 🖊

❍ /write <text> *:* يكتب النص المعطى.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite)

dispatcher.add_handler(WRITE_HANDLER)

__mod_name__ = "كتابة"
__command_list__ = ["write"]
__handlers__ = [WRITE_HANDLER]
