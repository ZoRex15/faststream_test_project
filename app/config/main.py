from typing import Any

from dataclasses import dataclass

from confhub.reader import ReaderConf


@dataclass
class BotConfig:
    token: str
    admin_id: int

@dataclass
class DbConfig:
    scheme: str
    port: int
    user: str
    password: str
    path: str
    host: str
    url: str

@dataclass
class BrokerConfig:
    scheme: str
    login: str
    password: str
    host: str
    
    def __post_init__(self):
        self.url = f'{self.scheme}://{self.login}:{self.password}@{self.host}/'

@dataclass(frozen=True)
class Config:
    bot: BotConfig
    db: DbConfig
    broker: BrokerConfig

def setup_config(dev: bool = True) -> Config:
    reader = ReaderConf('config_dist/settings.yml', 'config_dist/.secrets.yml', dev=dev)
    reader.create_service_urls()
    data = reader.data
    config = Config(
        bot=BotConfig(
            token=data.get('tg_bot')['token'],
            admin_id=data.get('tg_bot')['admin_id']
        ),
        db=DbConfig(
            scheme=data.get('postgresql')['scheme'],
            port=data.get('postgresql')['port'],
            user=data.get('postgresql')['user'],
            password=data.get('postgresql')['password'],
            path=data.get('postgresql')['path'],
            host=data.get('postgresql')['host'],
            url=data.get('postgresql_url')
        ),
        broker=BrokerConfig(
            scheme=data.get('broker')['scheme'],
            login=data.get('broker')['login'],
            password=data.get('broker')['password'],
            host=data.get('broker')['host']
        )
    )
    return config