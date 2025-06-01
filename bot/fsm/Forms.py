from aiogram.fsm.state import State, StatesGroup


class FormOrder(StatesGroup):
    category = State()
    number_v = State()
    phone = State()
    email = State()


class FormDesign(StatesGroup):
    address = State()
    time = State()