from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CallbackQuery
from keyboards.default.buttons import tugmalar, btn
from loader import dp
from aiogram.dispatcher.filters import Text
from keyboards.inline.buttons import tugma


@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    # mevalar = ['Olma', 'Anor', 'Nok', 'Behi', 'Xurmo', 'Gilos', 'Banan', 'Limon']
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!", reply_markup=btn)

#
# @dp.message_handler(content_types=types.ContentType.CONTACT)
# async def test(message: types.Message):
#     await message.answer(message.contact.phone_number)


@dp.message_handler(Text(startswith="Админ 🧑‍🏭"))
async def test(message: types.Message):
    await message.answer("Tanlang!", reply_markup=tugma)


@dp.callback_query_handler(text="say_hello")
async def test(call: CallbackQuery):
    await call.answer(cache_time=60)  # Tugmadagi soatchani yo`qotish uchun
    await call.message.answer('Salomat')
