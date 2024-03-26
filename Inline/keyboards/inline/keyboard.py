from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from keyboards.inline.callback import course_callback, book_callback

button = InlineKeyboardMarkup()
btn1 = InlineKeyboardButton(text="Kurslar", callback_data="courses")
button.insert(btn1)
btn2 = InlineKeyboardButton(text="kitoblar", callback_data="books")
button.insert(btn2)
btn3 = InlineKeyboardButton(text="YouTube kanal", url="https://youtube.com/c/Behzod_Asliddinov")
button.insert(btn3)
btn4 = InlineKeyboardButton(text="Ulashish!", switch_inline_query="Shuhriddining boti")
button.insert(btn4)

btn5 = InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat="")
button.add(btn5)

btn6 = InlineKeyboardButton(text="Web App", web_app=WebAppInfo(url='https://google.com'))
button.insert(btn6)


courses = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Django", callback_data=course_callback.new(item='django'))
        ]
    ]
)

books = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Django", callback_data=book_callback.new(item='django'))
        ]
    ]
)