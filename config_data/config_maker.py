from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


@dataclass
class TestData:
    admin: list[int]
    t_data: list[str]
    db_path: str


def load_config(path: str | None= None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
                 

def load_data(path: str | None= None) -> TestData:
    env = Env()
    env.read_env(path)
    return TestData(admin=list(map(int,env.list('admin'))),
                 t_data=list(map(str, env.list('test_list'))),
                 db_path=env('DB_PATH'))