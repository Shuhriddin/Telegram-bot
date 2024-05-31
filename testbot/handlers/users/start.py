from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from keyboards.default.contact import button
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=button)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def test(message: types.Message):
    await message.answer("Salomat, {}".format(message.from_user.full_name))


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def get_contact(message: types.Message):
    phone = message.contact.phone_number
    await message.answer(f"Telefon raqamingiz: {phone}", reply_markup=ReplyKeyboardRemove())