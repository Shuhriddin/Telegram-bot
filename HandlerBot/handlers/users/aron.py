from aiogram import types
from loader import dp
from aiogram.dispatcher.filters.builtin import Command, CommandStart, CommandSettings


@dp.message_handler(Command('friend'))
# @dp.message_handler(commands='friend')
async def four(message: types.Message):
    await message.answer('RAMAZON KELDI {}'.format(message.from_user.full_name))


@dp.message_handler(CommandSettings())
async def setting(msg: types.Message):
    await msg.answer('SETTINGS')


# https://t.me/shuhahandlerRobot?start=kunuz
@dp.message_handler(CommandStart(deep_link='kunuz'))
async def kunuz(msg: types.Message):
    await msg.answer('Sizni kun uz tavsiya qildi')