from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button = ReplyKeyboardMarkup(resize_keyboard=True)

button.add(KeyboardButton('Contact', request_contact=True))