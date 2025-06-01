import json

from aiogram import Router, F
from aiogram.filters import (
    Command, 
    CommandObject,
    CommandStart
)
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputFileUnion

from bot.keyboards import keyboard
from bot.fsm import Forms


router_handler_fsm = Router()


@router_handler_fsm.message(F.text=="Сделать заказ")
async def place_order(
    message: Message, 
    state: FSMContext
):
    await state.set_state(Forms.FormOrder.category)
    await message.answer(
        "<b>Выберите категорию: </b>",
        reply_markup=keyboard.order_kb())
    

@router_handler_fsm.message(F.text, Forms.FormOrder.category)
async def process_category_order(
    message: Message, 
    state: FSMContext
):
    await state.update_data(category=message.text)
    

    if message.text == "Диваны":
        list_product = (
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/divan-sleepart-biksio-1.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/69.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/sa99ceacde6f34b9681ec5e297d0fe2cdy.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/i-2.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/i-1.webp")

        for index, url in enumerate(list_product):
            await message.answer_photo(
                photo=url, caption=f"Вариант: {index+1}\n 15 890 - 56 890 руб"
            )

    
    elif message.text == "Кровать":
        list_product = (
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/diploma.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/9781_2.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/71whis5gvpl._ac_uf10001000_ql80_.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/900x1200.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/diploma-1.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/orig.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/a76051403fb1cdb69db6353be5c1116d.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/9781_2-1.jpg")
        for index, url in enumerate(list_product):
            await message.answer_photo(
                photo=url, caption=f"Вариант: {index+1}\n12 990 - 67 990 руб"
            )
    
    elif message.text == "Стулья":
        list_product = (
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/19b976562cbfc9591392bca9d30defc9.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/f0677fe6d924ced795db192e53062579.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/9fojcjurtovd4ulw9241m6ldmytvjosx.jpg"
        )
        for index, url in enumerate(list_product):
            await message.answer_photo(
                photo=url, caption=f"Вариант: {index+1}\n1 500 - 10 990 руб"
            )
        
    
    elif message.text == "Кухонные гарнитуры":
        list_product = (
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/49066_0-1200x800-1.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/orig-1.webp",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/7217638214.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/19.jpg",
            "https://chebmebel.wordpress.com/wp-content/uploads/2025/05/orig-2.webp"
        )
        for index, url in enumerate(list_product):
            await message.answer_photo(
                photo=url, caption=f"Вариант: {index+1}\n250 990 - 1 000 000 руб"
            )

    await state.set_state(Forms.FormOrder.number_v)
    await message.answer("<b>Введите номер варианта: </b>")


@router_handler_fsm.message(F.text, Forms.FormOrder.number_v)
async def process_number_v(message: Message, state: FSMContext):
    await state.update_data(number_v=message.text)
    await state.set_state(Forms.FormOrder.phone)
    await message.answer("<b>Введите номер телефона: </b>")


@router_handler_fsm.message(F.text, Forms.FormOrder.phone)
async def process_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Forms.FormOrder.email)
    await message.answer("<b>Введите Email: </b>")


@router_handler_fsm.message(F.text, Forms.FormOrder.email)
async def process_email(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    # data = await state.get_data()
    await state.clear()
    await message.answer(
        "✅ мы свяжемся с вами позже для уточнения заказа"
    )



@router_handler_fsm.message(F.text=='Прайс лист')
async def price_list(message: Message):
    text = (
        "<b>Наш прайс лист:\n"
        "Диваны: 15 890 - 56 890 руб\n"
        "Кровати: 12 990 - 67 990 руб\n"
        "Стулья: 1 500 - 10 990 руб\n"
        "Кухонные гарнитуры: 250 990 - 1 000 000 руб\n"
        "Подробнее вы можете посмотреть:</b>\n"
        "https://chebmebel.wordpress.com/?_gl=1*m4phnr*_gcl_au*MTczNTc2NTE2Ny4xNzQ4NTk0MzQ3"
    )
    await message.answer(text)


@router_handler_fsm.message(F.text=="Свой дизайн")
async def your_design(message: Message, state: FSMContext):
    await state.set_state(Forms.FormDesign.address)
    await message.answer("<b>Введите адрес: </b>")

@router_handler_fsm.message(F.text, Forms.FormDesign.address)
async def process_address(message: Message, state: FSMContext):
    await state.update_data(address=message.text)
    await state.set_state(Forms.FormDesign.time)
    await message.answer("<b>Укажите удобное время: </b>")


@router_handler_fsm.message(F.text, Forms.FormDesign.time)
async def process_time(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.clear()
    await message.answer("✅ Ваша заявка принята!")