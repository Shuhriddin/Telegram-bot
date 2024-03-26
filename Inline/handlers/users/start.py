from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CallbackQuery

from keyboards.inline.callback import course_callback, book_callback
from keyboards.inline.keyboard import button, courses, books
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=button)


@dp.callback_query_handler(text_contains='courses')
async def test(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Kurslar", reply_markup=courses)


@dp.callback_query_handler(text_contains='books')
async def test(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer("Kitoblar", reply_markup=books)


@dp.callback_query_handler(course_callback.filter(item='django'))
async def test(call: CallbackQuery):
    # await call.answer(cache_time=60)
    await call.answer("Video tayyorlanmoqda", show_alert=True)


@dp.callback_query_handler(book_callback.filter(item='django'))
async def test(call: CallbackQuery):
    # await call.answer(cache_time=60)
    await call.answer("Kitob tayyorlanmoqda", show_alert=True)