from aiogram import types, Dispatcher, Bot, executor
from api import weather

token = '7049372220:AAEvQkY_Pr54Oa3fdn2kzqm6TF78xKTd7vI'
bot = Bot(token)

dp = Dispatcher(bot)

try:
    @dp.message_handler(commands=['start'])
    async def start(message: types.Message):
        await message.answer("Salom Dunyo")

    @dp.message_handler(content_types='text')
    async def first(message: types.Message):
        data = weather(message.text)
        await message.answer(data)
except Exception as e:
    print(e)

if __name__ == '__main__':
    executor.start_polling(dp)