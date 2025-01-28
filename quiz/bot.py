from loguru import logger
from typing import Tuple
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.methods import GetUpdates, SendMessage

from quiz.config import BotConfig
from quiz.transport.telegram.base import base_router


async def init_bot(config: BotConfig) -> Tuple[Bot, Dispatcher]:
    logger.info('Bot initialization...')

    bot = Bot(config.TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.MARKDOWN_V2
    ))

    await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(base_router)

    return bot, dp
