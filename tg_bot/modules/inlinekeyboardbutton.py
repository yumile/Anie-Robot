import html
import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from telegram import TelegramObject


class InlineKeyboardButton(TelegramObject):
    """This object represents one button of an inline keyboard.
    Note:
        You must use exactly one of the optional fields. Mind that :attr:`callback_game` is not
        working as expected. Putting a game short name in it might, but is not guaranteed to work.
    Attributes:
        text (:obj:`str`): Label text on the button.
        url (:obj:`str`): Optional. HTTP or tg:// url to be opened when button is pressed.
        login_url (:class:`telegram.LoginUrl`) Optional. An HTTP URL used to automatically
            authorize the user. Can be used as a replacement for the Telegram Login Widget.
        callback_data (:obj:`str`): Optional. Data to be sent in a callback query to the bot when
            button is pressed, UTF-8 1-64 bytes.
        switch_inline_query (:obj:`str`): Optional. Will prompt the user to select one of their
            chats, open that chat and insert the bot's username and the specified inline query in
            the input field. Can be empty, in which case just the bot’s username will be inserted.
        switch_inline_query_current_chat (:obj:`str`): Optional. Will insert the bot's username and
            the specified inline query in the current chat's input field. Can be empty, in which
            case just the bot’s username will be inserted.
        callback_game (:class:`telegram.CallbackGame`): Optional. Description of the game that will
            be launched when the user presses the button.
        pay (:obj:`bool`): Optional. Specify True, to send a Pay button.
    Args:
        text (:obj:`str`): Label text on the button.
        url (:obj:`str`): HTTP or tg:// url to be opened when button is pressed.
        login_url (:class:`telegram.LoginUrl`, optional) An HTTP URL used to automatically
            authorize the user. Can be used as a replacement for the Telegram Login Widget.
        callback_data (:obj:`str`, optional): Data to be sent in a callback query to the bot when
            button is pressed, UTF-8 1-64 bytes.
        switch_inline_query (:obj:`str`, optional): If set, pressing the button will prompt the
            user to select one of their chats, open that chat and insert the bot's username and the
            specified inline query in the input field. Can be empty, in which case just the bot's
            username will be inserted. This offers an easy way for users to start using your bot
            in inline mode when they are currently in a private chat with it. Especially useful
            when combined with switch_pm* actions - in this case the user will be automatically
            returned to the chat they switched from, skipping the chat selection screen.
        switch_inline_query_current_chat (:obj:`str`, optional): If set, pressing the button will
            insert the bot's username and the specified inline query in the current chat's input
            field. Can be empty, in which case only the bot's username will be inserted. This
            offers a quick way for the user to open your bot in inline mode in the same chat - good
            for selecting something from multiple options.
        callback_game (:class:`telegram.CallbackGame`, optional): Description of the game that will
            be launched when the user presses the button. This type of button must always be
            the ``first`` button in the first row.
        pay (:obj:`bool`, optional): Specify True, to send a Pay button. This type of button must
            always be the ``first`` button in the first row.
        **kwargs (:obj:`dict`): Arbitrary keyword arguments.
    """

    def __init__(self,
                 text,
                 url=None,
                 callback_data=None,
                 switch_inline_query=None,
                 switch_inline_query_current_chat=None,
                 callback_game=None,
                 pay=None,
                 login_url=None,
                 **kwargs):
        # Required
        self.text = text

        # Optionals
        self.url = url
        self.login_url = login_url
        self.callback_data = callback_data
        self.switch_inline_query = switch_inline_query
        self.switch_inline_query_current_chat = switch_inline_query_current_chat
        self.callback_game = callback_game
        self.pay = pay

    @classmethod
    def de_json(cls, data, bot):
        if not data:
            return None

        return cls(**data)
    
   __help__ = """
   This is the Special Module Created By @Denzid
- /inlinekeyboardbutton :<URL> Use It To Create A Button URL
"""

__mod_name__ = ""

INLINEKEYBOARDBUTTON_HANDLER = DisableAbleCommandHandler("inlinekeyboardbutton", inlinekeyboardbutton, pass_args=True)

dispatcher.add_handler(INLINEKEYBOARDBUTTON_HANDLER)