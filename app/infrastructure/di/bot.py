from typing import AsyncIterable, Any

from aiogram import Bot
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from dishka import Provider, Scope, provide

from app.config import Config


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_bot(self, config: Config) -> Bot:
        print('bot')
        bot = Bot(
            token=config.bot.token,
            default=DefaultBotProperties(
                parse_mode=ParseMode.HTML   
            )
        )
        return bot