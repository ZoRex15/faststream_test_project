from typing import Any

from dishka import Provider, provide, Scope

from app.config import setup_config, Config


class ConfigProvider(Provider):
    def __init__(self, dev: bool = True):
        super().__init__()
        self.dev = dev

    @provide(scope=Scope.APP)
    def get_config(self) -> Config:
        print('config')
        config = setup_config(self.dev)
        return config
