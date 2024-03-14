from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from wikipeda_search import wiki


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    print(message.from_user)
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")


@dp.message_handler(content_types='text')
async def find(message: types.Message):
    key = message.text
    result = wiki(key)
    await message.answer(result)
