from aiogram import Router

from app.tg_bot.handlers.user_handlers import router


master_router = Router()
master_router.include_router(router)

__all__ = [
    'master_router'
]