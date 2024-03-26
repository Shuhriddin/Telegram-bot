from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import btn, checkbtn, btn1, back_button
from aiogram.dispatcher.filters import Text
from states.holatlar import Xodim
from data.config import CHANNEL_ID


@dp.message_handler(Text(startswith='Работодател 👤'))
async def first(message: types.Message):
    await message.answer(text="Bosh menuga qaytasizmi?", reply_markup=back_button)
    text = f"Siz hodim qidiryapsizmi?\nU holda arizani to`ldirib bizga yuboring!"
    await message.answer(text)
    text = 'Kasbini kiriting!\nMasalan: <b>Usta</b>'
    await message.answer(text)
    await Xodim.jobs.set()


@dp.message_handler(state=Xodim.jobs)
async def second(message: types.Message, state: FSMContext):
    if message.text == "↩️ Bekor qilish":
        await message.answer(text="Qaytish", reply_markup=btn)
        await state.finish()
    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
        job = message.text
        await state.update_data(
            {
                'kasb': job
            }
        )
        await message.delete()
        text = f"Yosh chegarasini kiriting!\nMasalan: <b>20-35</b>"
        await message.answer(text)
        await Xodim.next()


@dp.message_handler(state=Xodim.age)
async def second(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    yosh = message.text
    await state.update_data(
        {
            'yosh': yosh
        }
    )
    await message.delete()
    text = f'Tajribasini kiriting!\nMasalan: <b>3 yildan-5 yilgacha</b>'
    await message.answer(text)
    await Xodim.next()


@dp.message_handler(state=Xodim.about)
async def second(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    haqida = message.text
    await state.update_data(
        {
            'haqida': haqida
        }
    )
    await message.delete()
    text = f"Telefon nomeringizni kiriting\nMasalan <b>+998991212121</b>"
    await message.answer(text, reply_markup=btn1)
    await Xodim.next()


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Xodim.phone)
async def second(message: types.Message, state: FSMContext):
    contact = message.contact
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    tel = contact.phone_number
    await state.update_data(
        {
            'tel': tel
        }
    )
    await message.delete()
    data = await state.get_data()
    print(data)
    result = f"👨 Professiya: <b>{data['kasb']}</b>\n" \
             f"⏰ Yosh chegarasi: <b>{data['yosh']}</b>\n" \
             f"👤 Hodim haqida: <b>{data['haqida']}</b>\n" \
             f"📞 Tel nomeringiz: <b>{data['tel']}</b>\n"

    await message.answer(result)
    await message.answer("Ma`lumotlar to`g`rimi?", reply_markup=checkbtn)
    await Xodim.next()


@dp.message_handler(state=Xodim.checking)
async def one(message: types.Message, state: FSMContext):
    if message.text == "✅ Xa":
        data = await state.get_data()
        result = f"👨 Professiya: <b>{data['kasb']}</b>\n" \
                 f"⏰ Yosh chegarasi: <b>{data['yosh']}</b>\n" \
                 f"👤 Hodim haqida: <b>{data['haqida']}</b>\n" \
                 f"📞 Tel nomeringiz: <b>{data['tel']}</b>\n"

        await bot.send_message(chat_id=CHANNEL_ID, text=result)
        await message.answer("Bosh menu!", reply_markup=btn)
        await state.finish()
    else:
        await message.answer("Bosh menu!", reply_markup=btn)
        await state.finish()
























