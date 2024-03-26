from aiogram.dispatcher.filters.state import State, StatesGroup


class Ishchi(StatesGroup):
    ism = State()
    yosh = State()
    tel = State()
    kasbi = State()
    manzil = State()
    murojaat_vaqti = State()
    haqida = State()
    maqsad = State()
    check = State()
    back = State()

class Xodim(StatesGroup):
    jobs = State()
    age = State()
    about = State()
    phone = State()
    checking = State()
