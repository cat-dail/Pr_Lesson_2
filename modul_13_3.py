from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['?', 'ff', 'hello'])
async def urban_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")


# Хэндлер на команду /start


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
