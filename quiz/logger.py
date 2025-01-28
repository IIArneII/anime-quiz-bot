from loguru import logger
from sys import stderr

from quiz.config import LogConfig


def init_logger(config: LogConfig) -> None:
    logger.remove()
    logger.add(stderr, level=config.LEVEL.upper())
    
    if config.DIR:
        logger.add(
            f'{config.DIR}/logs.log',
            compression='zip',
            rotation=f'{config.ROTATION} MB',
            retention=config.RETENTION,
            level=config.LEVEL.upper()
        )
