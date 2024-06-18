from typing import AsyncIterable

from dishka import Scope, Provider, provide, AsyncContainer
from dishka.integrations.faststream import setup_dishka

from faststream import FastStream
from faststream.rabbit import RabbitBroker

from app.config import Config
from app.infrastructure.broker.consumers import master_router


class FastStreamAppProvider(Provider):

    @provide(scope=Scope.APP)
    async def get_app(self, dishka: AsyncContainer, broker: RabbitBroker) -> AsyncIterable[FastStream]:
        app = FastStream(broker)
        setup_dishka(container=dishka, app=app, auto_inject=True)
        yield app
        await app.stop()

    @provide(scope=Scope.APP)
    def get_broker(self, config: Config) -> RabbitBroker:
        broker = RabbitBroker(config.broker.url)
        broker.include_router(master_router)
        return broker

