from app.infrastructure.di.bot import BotProvider
from app.infrastructure.di.db import DbProvider
from app.infrastructure.di.config import ConfigProvider
from app.infrastructure.di.fast_stream import FastStreamAppProvider


def get_providers():
    return [
        BotProvider(),
        DbProvider(),
        ConfigProvider(),
        FastStreamAppProvider()
    ]