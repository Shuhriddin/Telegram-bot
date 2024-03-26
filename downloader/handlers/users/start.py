from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from instadownloader import insta
from loader import dp
from aiogram.dispatcher.filters import Text


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!")


@dp.message_handler(Text(startswith='https://www.instagram.com'))
async def test(message: types.Message):
    url = message.text
    result = insta(url)
    if result['type'] == 'error':
        await message.answer('Bu havola bilan ma`lumot topilmadi')
    if result['type'] == 'video':
        await message.answer_video(video=result['media'], caption=url)
    if result['type'] == 'image':
        await message.answer_photo(photo=result['media'], caption=url)
    if result['type'] == 'carousel':
        for i in result['media']:
            await message.answer_document(document=i, caption=url)