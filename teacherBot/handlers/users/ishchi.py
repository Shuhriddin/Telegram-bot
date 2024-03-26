from aiogram import types
from loader import dp, bot
from aiogram.dispatcher import FSMContext
from keyboards.default.buttons import checkbtn, btn, btn1, back_button
from aiogram.dispatcher.filters import Text
from states.holatlar import Ishchi
from data.config import CHANNEL_ID


# @dp.message_handler(commands=['ish', 'work'], state=None)
@dp.message_handler(Text(startswith='Работник'), state=None)
async def bir(message: types.Message):
    await message.answer(text="Bosh menyuga qaytmoqchimisiz?", reply_markup=back_button)
    text = f'<i>Assalomu alaykum.</i> <b>Ish qidiryapsizmi?</b>\n' \
            f'Unda hozir beriladigan savollarga javob bering.\nArizangiz adminga yuboriladi'
    await message.answer(text)
    text = f'Ism va familiyangizni kiriting.\n' \
            f'Masalan: <b>Muhiddinov MuhammadAli</b>'
    await message.answer(text)
    await Ishchi.ism.set()


@dp.message_handler(state=Ishchi.ism)
async def ikki(message: types.Message, state: FSMContext):
    if message.text == "↩️ Bekor qilish":
        await message.answer(text="Bosh menu!", reply_markup=btn)
        await state.finish()
    else:
        message_id = message.message_id
        await bot.delete_message(chat_id=message.chat.id, message_id=message_id-1)
        ism = message.text
        await state.update_data(
            {
                'ism': ism
            }
        )
        await message.delete()
        text = f'Yoshingizni kiriting.\n' \
                f'<b>Masalan:</b> 20.'
        await message.answer(text)
        await Ishchi.next()


@dp.message_handler(state=Ishchi.yosh)
async def uch(message: types.Message, state: FSMContext):
    message_id = message.message_id
    await bot.delete_message(chat_id=message.chat.id, message_id=message_id-1)
    yosh = message.text
    await state.update_data({
        'yosh': yosh
    })
    await message.delete()
    text = f'Telefon raqamingizni kiriting\n' \
            f'Masalan: <b>+998991259009</b>'
    await Ishchi.next()
    await message.answer(text, reply_markup=btn1)


@dp.message_handler(content_types=types.ContentType.CONTACT, state=Ishchi.tel)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    contact = message.contact
    tel = contact.phone_number
    await state.update_data({
        'tel': tel
    })
    await message.delete()
    text = f'Kasbingizni kiriting\n' \
            f'Masalan: <b>Kulol</b>'
    await message.answer(text)
    await Ishchi.next()


@dp.message_handler(state=Ishchi.kasbi)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    kasbi = message.text
    await state.update_data({
        'kasbi': kasbi
    })
    await message.delete()
    text = f'Manzilingizni kiriting\n' \
            f'Masalan: <b>Toshkent shaxar, Yashnobod tumani, 38-140</b>'
    await message.answer(text)
    await Ishchi.next()


@dp.message_handler(state=Ishchi.manzil)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    manzil = message.text
    await state.update_data({
        'manzil': manzil
    })
    await message.delete()
    text = f'Murojaat vaqtini kiriting\n' \
            f'Masalan: <b>10:00-12:00</b>'
    await message.answer(text)
    await Ishchi.next()


@dp.message_handler(state=Ishchi.murojaat_vaqti)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    murojaat_vaqti = message.text
    await state.update_data({
        'murojaat_vaqti': murojaat_vaqti
    })
    await message.delete()
    text = f'O`zingiz haqida kiriting\n' \
            f'Masalan: <b>Men pessimist insonman</b>'
    await message.answer(text)
    await Ishchi.next()


@dp.message_handler(state=Ishchi.haqida)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    haqida = message.text
    await state.update_data({
        'haqida': haqida
    })
    await message.delete()
    text = f'Maqsadingizni kiriting\n' \
            f'Masalan: <b>Meni ota-onam oldida yuzim yorug` bo`ladi InShaAllah</b>'
    await message.answer(text)
    await Ishchi.next()


@dp.message_handler(state=Ishchi.maqsad)
async def uch(message: types.Message, state: FSMContext):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id-1)
    maqsad = message.text
    await state.update_data({
        'maqsad': maqsad
    })
    await message.delete()
    data = await state.get_data()
    print(data)
    result = f"👨 Ism': <b>{data['ism']}</b>\n" \
            f"⏰ Yosh: <b>{data['yosh']}</b>\n" \
            f"📞 Tel: <b>{data['tel']}</b>\n" \
            f"👷‍♀️ Kasbi: <b>{data['kasbi']}</b>\n" \
            f"📍 Manzil: <b>{data['manzil']}</b>\n" \
            f"🕔 Murojaat vaqti: <b>{data['murojaat_vaqti']}</b>\n" \
            f"👤 Ishchi xaqida: <b>{data['haqida']}</b>\n" \
            f"🎯 Maqsad: <b>{data['maqsad']}</b>\n"
    await message.answer(result)
    await message.answer("Ma`lumotlar to`g`rimi?", reply_markup=checkbtn)
    await Ishchi.next()
    # await state.finish()


@dp.message_handler(state=Ishchi.check)
async def uch(message: types.Message, state: FSMContext):
    if message.text == '✅ Xa':
        data = await state.get_data()
        result = f"👨 Ism': <b>{data['ism']}</b>\n" \
                 f"⏰ Yosh: <b>{data['yosh']}</b>\n" \
                 f"📞 Tel: <b>{data['tel']}</b>\n" \
                 f"👷‍♀️ Kasbi: <b>{data['kasbi']}</b>\n" \
                 f"📍 Manzil: <b>{data['manzil']}</b>\n" \
                 f"🕔 Murojaat vaqti: <b>{data['murojaat_vaqti']}</b>\n" \
                 f"👤 Ishchi xaqida: <b>{data['haqida']}</b>\n" \
                 f"🎯 Maqsad: <b>{data['maqsad']}</b>\n"

        await bot.send_message(chat_id=CHANNEL_ID, text=result)
        await message.answer('Bosh menyu!', reply_markup=btn)
        await state.finish()
    else:
        await message.answer('Bosh menyu!', reply_markup=btn)
        await state.finish()
