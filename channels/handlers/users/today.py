from aiogram import types
from loader import dp


@dp.message_handler(commands='info')
async def test(message: types.Message):
    text = f'<span class="tg-spoiler">spoiler</span>\n' \
           f'<a href="tg://user?id=2038934476">Mendtor</a>\n' \
           f'<code>Python</code>'
    await message.reply(text, parse_mode=types.ParseMode.HTML)

