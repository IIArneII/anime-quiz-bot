from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )


class LogConfig(BaseConfig):
    model_config = SettingsConfigDict(env_prefix='LOG_', use_enum_values=True)

    class LogLevel(str, Enum):
        debug = 'debug'
        info = 'info'
        error = 'error'

    LEVEL: LogLevel = LogLevel.info
    DIR: str = ''
    RETENTION: int = 5
    ROTATION: int = 10


class BotConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='BOT_')

    TOKEN: str = '0000000000:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'


class Config(BaseSettings):
    log: LogConfig = LogConfig()
    bot: BotConfig = BotConfig()
