from aiogram import Dispatcher

from dishka import Provider, Scope, provide, AsyncContainer, make_async_container
from dishka.integrations.aiogram import setup_dishka

from app.tg_bot.handlers import master_router
from app.infrastructure.di import get_providers


def create_dishka() -> AsyncContainer:
    container = make_async_container(*get_bot_providers())
    return container

def get_bot_providers() -> list[Provider]:
    return [
        *get_providers(),
        DpProvider()
    ]

class DpProvider(Provider):

    @provide(scope=Scope.APP)
    def create_dp(
        self,
        dishka: AsyncContainer
    ) -> Dispatcher:
        dp = Dispatcher()
        setup_dishka(container=dishka, router=dp, auto_inject=True)
        dp.include_router(master_router)
        return dp
        

