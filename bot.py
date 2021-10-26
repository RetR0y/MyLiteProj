import requests
from config import open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

#1918692872:AAF14XIx1l4wBu4ww_9V6lbpfz9BbfnQEU8 TOKEN_telegram

bot = Bot(token='1918692872:AAF14XIx1l4wBu4ww_9V6lbpfz9BbfnQEU8')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Привет. Введи названия города и я скажу тебе погоду !')

@dp.message_handler()
async def get_weather(message: types.Message):
        try:
            r = requests.get(
                f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric')
            data = r.json()

            city = data["name"]
            weather = data["main"]["temp"]
            wind = data["wind"]["speed"]
            humidity = data["main"]["humidity"]

            await message.reply(f"Погода в городе: {city}\nТемпература: {weather}\nСкорость ветра: {wind}\nВлажность: {humidity}")
        except:
            await message.reply(f"Проверь названия города {city}")



if __name__ == '__main__':
    executor.start_polling(dp)

bot.polling(none_stop=True)