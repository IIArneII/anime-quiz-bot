from loguru import logger
from asyncio import sleep, get_running_loop, wait, Event, FIRST_COMPLETED
from signal import SIGINT, SIGTERM, signal
from aiogram import Bot

from quiz.config import Config
from quiz.bot import init_bot
from quiz.logger import init_logger


async def run(config: Config) -> None:
    init_logger(config.log)

    try:
        stop_event = catch_shutdown()

        bot, dp = await init_bot(config.bot)

        logger.info('Running...')

        await wait(
            [dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()), stop_event.wait()],
            return_when=FIRST_COMPLETED,
        )

    except Exception as e:
        logger.exception(e)
    
    finally:
        await shutdown(bot)


async def shutdown(bot: Bot):
    logger.info("Shutting down...")
    await bot.close()


def catch_shutdown() -> Event:
    def handle_signal(signum, frame):
        logger.info(f"Signal {signum} received, shutting down...")
        stop_event.set()
    
    loop = get_running_loop()
    stop_event = Event()

    signal(SIGINT, handle_signal)
    signal(SIGTERM, handle_signal)

    return stop_event
