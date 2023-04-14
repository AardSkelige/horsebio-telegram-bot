# В данном коде показаны основы создания Telegram-бота с использованием библиотеки aiogram. 
# Однако, этот код сам по себе не образует полностью функционального бота, 
# так как в нем отсутствует большое количество логики и функциональности, 
# которые могут быть необходимы для создания полноценного бота.

import asyncio

from aiogram import Bot, Dispatcher, types, executor

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import aiogram.utils.markdown as md

bot = Bot(token="")
dp = Dispatcher(bot)

# Кнопки главного меню
menu_button_site = KeyboardButton('Сайт')
menu_button_shops = KeyboardButton('Магазины')
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.row(menu_button_site, menu_button_shops)

# Кнопка возврата в меню
main_menu_button = KeyboardButton('Главное меню')

# Кнопки поиска магазина
country_button_1 = KeyboardButton('Россия')
country_button_2 = KeyboardButton('Казахстан')
country_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
country_buttons.row(country_button_1, country_button_2)

# Кнопки выбора города в Казахстане
kz_city_1 = KeyboardButton('Астана')
kz_city_2 = KeyboardButton('Караганда')
kz_cities = ReplyKeyboardMarkup(resize_keyboard=True)
kz_cities.row(kz_city_1, kz_city_2)

# В функции-обработчике start_handler мы используем декоратор message_handler и команду /start, 
# чтобы приветствовать пользователя и предложить ему выбрать интересующий его пункт меню.



@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_name = message.from_user.full_name
    await message.answer(f'Добро пожаловать, {user_name}! Что тебя интересует?', reply_markup=menu)

# Функция-обработчик all_handler используется для обработки всех входящих сообщений, 
# которые не соответствуют командам /start. В этой функции мы определяем, 
# какую кнопку пользователь нажал, и возвращаем соответствующий ответ. 
# Например, если пользователь нажал кнопку "Магазины", мы выводим другой набор кнопок для выбора страны.

@dp.message_handler()
async def all_handler(message: types.Message):
    if message.text == 'Магазины':
        await message.answer(f'Выбери страну', reply_markup=country_buttons)
    if message.text == 'Казахстан':
        await message.answer(f'Выбери город', reply_markup=kz_cities)
    if message.text == 'Астана':
        await message.answer(text='**unknown**')
    if message.text == 'Сайт':
        await message.answer(f'https://horse-bio.ru/')

# Запускаем polling с помощью функции executor.start_polling(dp), 
# чтобы бот мог получать входящие сообщения от пользователей. 
# Эта функция выполняется бесконечно, пока мы ее не остановим вручную.

if __name__ == "__main__":
    executor.start_polling(dp)
