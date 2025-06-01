from aiogram import Dispatcher

from .handlers.handler import router_user_handler
from .handlers.handler_fsm import router_handler_fsm

routers_list = [
    router_user_handler,
    router_handler_fsm
]

async def include_routers(dp: Dispatcher):
    for i in routers_list:
        dp.include_router(i)