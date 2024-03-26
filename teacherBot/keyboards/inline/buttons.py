from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

tugma = InlineKeyboardMarkup(inline_keyboard=
                             [
                                 [InlineKeyboardButton(text='Kanal admini', url="https://t.me/shuhriddin_90")],
                                 [
                                     InlineKeyboardButton(text='Salom ber', callback_data='say_hello')
                                 ]
                             ])
