import json

from aiogram import Router, F
from aiogram.filters import (
    Command, 
    CommandStart
)
# from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards import keyboard

router_user_handler = Router()


@router_user_handler.message(CommandStart())
async def StartCommand(message: Message):
    text = ("Привет я помощник от сайта\n"
            "https://chebmebel.wordpress.com/?_gl=1*m4phnr*_gcl_au*MTczNTc2NTE2Ny4xNzQ4NTk0MzQ3\n"
            "\nДля полного списка команд\n"
            "/help - список всех команд")
    
    await message.answer(text, reply_markup=keyboard.main_kb())


@router_user_handler.message(Command('help'))
async def cmd_help(message: Message):
    text = (
        "Вот что я умею\n"
        "/help - вы тут\n"
        "/contact - связь с тех.поддержкой\n"
        ""
    )
    await message.answer(text)


@router_user_handler.message(Command('contact'))
async def cmd_contact(message: Message):
    await message.answer('https://t.me/tem_chi')

