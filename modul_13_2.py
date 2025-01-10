from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import asyncio

api = '7917780461:AAF-4gx9eyP12XX5u5rKFFhD5JRYeb712N4'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text = ['?', 'ff', 'hello'])
async def urban_message(message):
    print("Введите команду /start, чтобы начать общение.")

# Хэндлер на команду /start


@dp.message_handler(commands=['start'])
async def cmd_start(message):
    print("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    print("Мы получили сообщение!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
