import requests
from telegram import ParseMode, Update
from telegram.ext import CallbackContext, run_async

from FallenRobot import dispatcher
from FallenRobot.modules.disable import DisableAbleCommandHandler


@run_async
def ud(update: Update, context: CallbackContext):
    message = update.effective_message
    text = message.text[len("/ud ") :]
    results = requests.get(
        f"https://api.urbandictionary.com/v0/define?term={text}"
    ).json()
    try:
        reply_text = f'*{text}*\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
    except:
        reply_text = "No results found."
    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN)


UD_HANDLER = DisableAbleCommandHandler(["ud"], ud)

dispatcher.add_handler(UD_HANDLER)

__help__ = """
» - /ud:{word} اكتب الكلمة أو التعبير الذي تريد البحث عنه. مثل / UD Telegram Word: Telegram التعريف: نظام شائع من الاتصالات ذات مرة، حيث سيقوم المرسل بالاتصال بخدمة Telegram والتحدث [رسالة] عبر [الهاتف]. من شأنه أن يرسله الشخص الذي يتخذ الرسالة، عبر جهاز TeleType، إلى مكتب برقية بالقرب من [عنوان]. سيتم بعد ذلك تسليم الرسالة باليد إلى المرسل إليه. من عام 1851 إلى أن أوقفت الخدمة في عام 2006، كانت ويسترن يونيون هي خدمة برقية معروفة في العالم.
"""
"""
__mod_name__ = "Uʀʙᴀɴ D"
__command_list__ = ["ud"]
__handlers__ = [UD_HANDLER]
