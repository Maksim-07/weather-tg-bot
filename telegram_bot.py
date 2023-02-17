from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from get_weather import getting_the_weather

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def greet_user(message: types.Message):
    await message.reply('Привет! Напиши название города и я отправлю тебе прогноз погоды на сегодня!')


@dp.message_handler()
async def sending_weather(message: types.Message):
    msg = getting_the_weather(message.text)
    await message.reply(msg)


if __name__ == '__main__':
    executor.start_polling(dp)
