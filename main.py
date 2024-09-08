import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


api_token = getenv('API_TOKEN')
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message) -> None:
    await message.answer("development in progress")


@dp.message()
async def echo(message: Message) -> None:
   await message.answer(message.text)


async def main() -> None:
    bot = Bot(token=api_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())