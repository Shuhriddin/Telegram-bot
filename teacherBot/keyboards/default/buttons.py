from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# btn = ReplyKeyboardMarkup(
#     resize_keyboard=True,
#     keyboard=[
#         [
#             KeyboardButton(text='🔽 First'),
#             KeyboardButton(text='🔽 Second'),
#             KeyboardButton(text='🔽 Three'),
#         ],
#         [
#             KeyboardButton(text='🔽 Four')
#         ]
#     ]
# )

def tugmalar(mevalar):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    for i in mevalar:
        btn.insert(i)
    btn.add('Admin')
    return btn

# btn = ReplyKeyboardMarkup(resize_keyboard=True,
#                           keyboard=[
#                               [
#                                   KeyboardButton(text='Share Contact', request_contact=True),
#                                   KeyboardButton(text='Share location', request_location=True)
#                               ]
#                           ])


btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.insert('Работник 🧑‍🏭')
btn.insert('Работодател 👤')
btn.insert("Админ 🧑‍🏭")
checkbtn = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text='✅ Xa'),
                                       KeyboardButton(text='❌ Yo`q')
                                   ]
                               ])

back_button = ReplyKeyboardMarkup(resize_keyboard=True,
                                  keyboard=[
                                      [
                                          KeyboardButton(text="↩️ Bekor qilish")
                                      ]
                                  ])

btn1 = ReplyKeyboardMarkup(resize_keyboard=True)
btn1.insert(KeyboardButton("📞 Контакты", request_contact=True))
# btn.insert(KeyboardButton("📍 Локация", request_location=True))
