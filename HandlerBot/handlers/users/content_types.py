from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import BoundFilter, Text


class ContainsFilter(BoundFilter):
    key = 'contains'

    def __init__(self, contains):
        self.contains = contains

    async def check(self, message: types.Message):
        return self.contains in message.text


@dp.message_handler(ContainsFilter('ahmoq'), content_types=types.ContentType.TEXT)
async def test2(message: types.Message):
    await message.answer('So`kinma')


@dp.message_handler(Text(startswith='sh'), content_types='text')
async def test(msg: types.Message):
    await msg.answer('So`z sh bilan boshlanadi')


# yana bir usuli
@dp.message_handler(content_types=types.ContentTypes.STICKER)
# @dp.message_handler(content_types='sticker')
async def sticker(msg: types.Message):
    await msg.answer('Siz stikker yubordingiz')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo(message: types.Message):
    await message.answer('Siz Rasm yubordingiz')


@dp.message_handler(content_types='text')
async def letter(msg: types.Message):
    await msg.answer('Text yubordingiz')

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def voice(msg: types.Message):
    await msg.answer('Ovozli habar jo`natildi')