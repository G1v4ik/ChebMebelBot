from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton 
)

from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder,
    InlineKeyboardBuilder)


def main_kb():
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text='Сделать заказ'),
        KeyboardButton(text='Прайс лист'),
        KeyboardButton(text='Свой дизайн')
    )
    

    return kb.as_markup(resize_keyboard=True)


def order_kb():
    kb = ReplyKeyboardBuilder()
    kb.row(
        KeyboardButton(text='Диваны'),
        KeyboardButton(text='Кровать')
    )
    kb.row(
        KeyboardButton(text='Стулья')
    )
    kb.row(
        KeyboardButton(text='Кухонные гарнитуры')
    )
    return kb.as_markup(resize_keyboard=True)