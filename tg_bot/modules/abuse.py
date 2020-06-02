import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "Bsdk",
    "Stfu bc",
    "Stfu and Gtfo U nub",
    "Stfu go fuck yourself",
    "you noob",
    "Relax your Rear,ders nothing to fear,The Rape train is finally here",
    "Ur mum gey",
    "Teri maa ki chut",
    "Jaa na lawde",
    "Ur dad gey bc",
    "Bhag madharchod",
    "muh me lega",
    "Fuck off",
    " MUH ME LEGA KYA BSDK",
    "GTFO bsdkCUnt",
    "Lanjakodaka"
  )

@run_async
def dark(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /dark  🤬.
"""

__mod_name__ = "Abuses"

DARK_HANDLER = DisableAbleCommandHandler("dark", dark)

dispatcher.add_handler(DARK_HANDLER)
