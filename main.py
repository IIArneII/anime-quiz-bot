from asyncio import run as async_run

from quiz.app import run
from quiz.config import Config


async def main():
    await run(Config())


if __name__ == '__main__':
    async_run(main())
