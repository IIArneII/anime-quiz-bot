from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from loguru import logger


base_router = Router()


@base_router.message(Command("start"))
async def start(msg: Message):
    try:
        await msg.answer("Hello")

    except Exception as e:
        logger.exception(e)
        await msg.answer(str(e))
