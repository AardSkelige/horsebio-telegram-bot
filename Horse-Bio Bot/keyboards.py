from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from shop import *

from config import URL_HORSEBIO, URL_INSTAGRAM, URL_HONDRO_1200, URL_HONDRO_600

# Этот код создает клавиатуру с тремя кнопками. Клавиатура имеет формат ReplyKeyboardMarkup 
# и установлен параметр resize_keyboard в значение True, что означает, что она будет изменять 
# размеры под экран устройства, на котором отображается чат. Всего клавиатура содержит три ряда 
# с кнопками: первый ряд содержит две кнопки ('Button1' и 'Button2'), а второй ряд содержит одну кнопку ('Button3').

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Button1'),
            KeyboardButton(text='Button2')
        ],
        [
            KeyboardButton(text='Button3')
        ]
    ],
    resize_keyboard=True
)


# Этот код создает Inline-клавиатуры с кнопками.

#CallbackData('buy', 'id', 'name', 'price') создает объект CallbackData с названием 'buy' и 
# параметрами 'id', 'name' и 'price'. CallbackData используется для генерации уникальных callback-данных, 
# которые будут переданы в ответ на нажатие кнопок InlineKeyboardButton.
#InlineKeyboardMarkup создает объект клавиатуры с кнопками. Параметр inline_keyboard принимает список 
# строк кнопок, где каждая строка - это список кнопок.
# Первая Inline-клавиатура keyboard1 имеет две кнопки с названием 'Хондро 600' и 'Хондро 1200', а также одну кнопку 'Cancel'.
# Вторая Inline-клавиатура hondro_600_key имеет одну кнопку 'Купить', которая ссылается на URL-адрес, определенный 
# константой URL_HONDRO_600.
# Третья Inline-клавиатура hondro_1200_key также имеет одну кнопку 'Купить', но ссылается на URL-адрес, определенный 
# константой URL_HONDRO_1200.
cb = CallbackData('buy', 'id', 'name', 'price')


keyboard1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Хондро 600',
                callback_data='buy:0:hondro600:4000'),
            InlineKeyboardButton(
                text='Хондро 1200',
                callback_data='buy:0:hondro1200:6000')
        ], [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

hondro_600_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Купить', url=URL_HONDRO_600)]
    ]
)
hondro_1200_key = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Купить', url=URL_HONDRO_1200)]
    ]
)


# Inline Keyboards Generator
# Этот код определяет функцию keyboard_generator, которая генерирует InlineKeyboardMarkup, содержащий список кнопок, 
# каждая из которых вызывает обратный вызов callback_data, содержащий текст этой кнопки. Функция принимает список 
# элементов, которые будут использоваться в качестве текста кнопок.
# Также код создает animals_kb - экземпляр InlineKeyboardMarkup, который содержит две кнопки "Лошади" и "Собаки", 
# каждая из которых ведет на соответствующую страницу сайта, а также содержит callback_data равный тексту этой кнопки. 
# Он использует функцию InlineKeyboardButton для создания каждой кнопки. row_width=2 указывает, что в каждой строке 
# может быть максимум две кнопки.

def keyboard_generator(items: list) -> InlineKeyboardMarkup:
    kb = []
    for item in items:
        kb.append([InlineKeyboardButton(text=item, callback_data=item)])
        markup = InlineKeyboardMarkup(inline_keyboard=kb)
    return markup


animals_kb = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(
                                              text="Лошади",
                                              url='https://horse-bio.ru/shop/folder/dlya-loshadey',
                                              callback_data="Лошади",
                                          )
                                      ],
                                      [
                                          InlineKeyboardButton(
                                              text="Собаки",
                                              url='https://horse-bio.ru/dlya-sobak',
                                              callback_data="Собаки",
                                          )
                                      ]
                                  ])
