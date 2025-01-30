from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


class InlineKeyboard:

    @staticmethod
    def get_message_buttons():
        buttons = [
            [InlineKeyboardButton(text="Anketa to'ldirish", web_app=WebAppInfo(url="https://soff.uz/"))],
        ]
        return InlineKeyboardMarkup(inline_keyboard=buttons)


INLINE_KEYBOARDS = InlineKeyboard()
