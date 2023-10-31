import asyncio
from aiogram import Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from token1 import bot
dp = Dispatcher()

#основное меню выбора
@dp.message(Command('start'))
async def start_window(msg : types.Message):
    kb = [[types.KeyboardButton(text= "Учеба"),
           types.KeyboardButton(text="Github")],
           [types.KeyboardButton(text="Социальные Сети"),
            types.KeyboardButton(text="ЮФМЛ")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard= True, input_field_placeholder="Выберите интересующий вас раздел!")
    await msg.answer(text='Приветствую вас в моем боте-визитке\nВыберите интересующий вас раздел!', reply_markup=keyboard)

@dp.message(F.text.lower() == 'учеба')
async def ycheba_answ(msg : types.Message):
    await msg.answer("С 2014 - 2023 Обучался в Сургутской Технологической школе\n С 2023 по настоящее время обучаюсь в ЮФМЛ\n Так же являюсь учеником Яндекс Лицея")

@dp.message(F.text.lower() == 'github')
async def my_github(msg : types.Message):
    await msg.answer("Вот мой гитхаб!\nhttps://github.com/semy90")

@dp.message(F.text.lower() == 'социальные сети')
async def my_social_media(msg : types.Message):
    await msg.answer("Тут пока ничего нет :(")

@dp.message(F.text.lower() == "юфмл")
async def upml(msg : types.Message):
    await msg.answer('Однозначно топ!')

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
