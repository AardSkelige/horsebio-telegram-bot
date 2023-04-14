from main import dp, bot
from config import PAYMENTS_TOKEN
from messages import MESSAGES
from aiogram.types.message import ContentType
from aiogram.types import Message, ShippingOption, ShippingQuery, LabeledPrice,  PreCheckoutQuery, Message, ReplyKeyboardRemove, CallbackQuery, Location
from sql import add, buy
from aiogram.dispatcher.filters import Text, Command

from keyboards import *
from config import chat_id
from shop import *

# Функция запускается при запуске бота


async def send_hello(dp):
    await bot.send_message(chat_id=chat_id, text='<b>Добро пожаловать!</b> Нажми -> /start')


# срабатывает, когда пользователь отправляет команду /shop боту. 
# В ответ на это сообщение бот отправляет текст "Shop" и клавиатуру keyboard, 
# которая определена в keyboards.py


@dp.message_handler(Command('shop'))
async def show_shop(message: Message):
    await message.answer('Shop', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Button1', 'Button2', 'Button3']))
async def get_goods(message: Message):
    await message.answer(message.text, reply_markup=ReplyKeyboardRemove())

# Cрабатывает, когда пользователь нажимает на кнопку с текстом, содержащим строку 'hondro600'. 
# В ответ на это нажатие бот отправляет сообщение с текстом "Купить" и клавиатурой hondro_600_key.


@dp.callback_query_handler(text_contains='hondro600')
async def hondro600(call: CallbackQuery):
    await call.answer(cache_time=60)

    await call.message.answer('Купить', reply_markup=hondro_600_key)

# Функция ниже срабатывает, когда пользователь нажимает на кнопку с именем 'hondro1200', 
# которая определена как фильтр колбэк-данных (callback data) при создании кнопки. 
# В ответ на это нажатие бот отправляет сообщение с текстом "Купить. 
# Он стоит: [цена]", где [цена] - это значение параметра price, которое было передано 
# в колбэк-данных, и клавиатурой hondro_1200_key.

@dp.callback_query_handler(cb.filter(name='hondro1200'))
async def hondro1200(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    p = callback_data.get('price')

    await call.message.answer(f'Купить. Он стоит: {p}', reply_markup=hondro_1200_key)

# Cрабатывает, когда пользователь нажимает на кнопку с текстом, содержащим строку 'cancel'. 
# В ответ на это нажатие бот отправляет сообщение с текстом "Отмена" и удаляет клавиатуру, 
# которая была связана с сообщением, на которое пользователь нажал кнопку.

@dp.callback_query_handler(text_contains='cancel')
async def cancel(call: CallbackQuery):
    await call.answer('Отмена', show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)

# Обработчик команды "/add", которая добавляет запись в базу данных. 
# Для этого извлекается строка из сообщения пользователя, переданного вместе с 
# командой "/add", и вызывается функция add(s), которая добавляет эту строку в базу данных. 
# После успешного добавления записи, бот отправляет пользователю сообщение "Запись успешно добавлена!!!".

@dp.message_handler(Command('add'))
async def add_cmd(message: Message):
    s = ' '.join(message.text.split(' ')[1:])

    await add(s)
    await message.answer('Запись успешно добавлена!!!')

# Обработчик команды "/buy", которая выводит все записи из базы данных. 
# Для этого вызывается функция buy(), которая извлекает все записи из базы данных
# и формирует из них одну строку. Эта строка отправляется пользователю в ответ на команду "/buy".

@dp.message_handler(Command('buy'))
async def buy_cmd(message: Message):
    await message.answer(await buy())


# Этот код обрабатывает команду /start, которую пользователь может отправить боту. 
# При получении этой команды, бот отправляет сообщение пользователю с текстом 
# "Привет! Это главное меню. Выбери интересующую тебя информацию." и клавиатурой, 
# которая генерируется с помощью функции keyboard_generator() из переменной menu_list. 
# Вероятно, menu_list содержит список опций меню, которые пользователь может выбрать. 
# Когда пользователь выбирает один из вариантов меню, бот перенаправляет его на соответствующую 
# функцию обработки сообщений, которая определена в другом месте кода.


@dp.message_handler(Command('start'))
async def main_menu(message: Message):
    await message.answer(text='Привет! Это главное меню. Выбери интересующую тебя информацию.', reply_markup=keyboard_generator(menu_list))

# Это обработчик колбэк-запросов в вашем Telegram-боте. Он отвечает на различные команды, которые пользователь 
# может отправлять в ответ на сообщения от бота.

# Команды, которые обрабатываются в данном обработчике:

# Магазины: показывает список стран, в которых можно купить товары;
# Выбор страны: показывает список городов выбранной страны;
# Выбор города: показывает список магазинов выбранного города;
# Выбор магазина: показывает информацию о выбранном магазине;
# Товары: показывает список категорий товаров (для каких животных);
# Выбор категории товаров: показывает список фильтров товаров (по сериям или по действию);
# Выбор фильтра товаров: показывает список товаров, соответствующих выбранному фильтру (по проблемным зонам или по сериям);
# Выбор товара для собак: показывает информацию о выбранном товаре для собак;
# Показать статью: показывает статью по собакам, соответствующую выбранной команде.
# Если пользователь отправляет некорректную команду, обработчик пишет: {call.data} - 
# Эта функция пока в разработке. Жми сюда: /start

@dp.callback_query_handler()
async def where_to_buy(call: CallbackQuery):
    if call.data == 'Магазины':
        await call.message.answer(text='<b>1. Выберите страну.</b>', reply_markup=keyboard_generator(county_to_buy))
    elif call.data in cities_to_buy:
        await call.message.answer(text='<b>2. Выберите город.</b>', reply_markup=keyboard_generator(cities_to_buy[call.data]))
    elif call.data in shops_to_buy:
        await call.message.answer(text='<b>3. Выберите магазин.</b>', reply_markup=keyboard_generator(shops_to_buy[call.data]))
    elif call.data in shop_info:
        await call.message.answer(text=shop_info[call.data])
        # await call.message.answer_location(latitude=55.943029, longitude=37.332402) карта от телеги
    elif call.data == 'Товары':
        # await call.message.answer(text='<b>1. Для каких животных?</b>', reply_markup=animals_kb) клава со ссылкам на сайт
        await call.message.answer(text='<b>1. Для каких животных?</b>', reply_markup=keyboard_generator(animals_categories))
    elif call.data in goods_filter:
        await call.message.answer(text='<b>2. Показать по сериям или по действию?</b>', reply_markup=keyboard_generator(goods_filter[call.data]))
    elif call.data in goods_by_effect:
        await call.message.answer(text='<b>3. Выберите проблемную зону.</b>', reply_markup=keyboard_generator(goods_by_effect[call.data]))
    elif call.data in goods_by_series:
        await call.message.answer(text='<b>3. Выберите серию товаров.</b>', reply_markup=keyboard_generator(goods_by_series[call.data]))
    elif call.data in goods_for_dogs:
        await call.message.answer(text='<b>4. Выберите товар.</b>', reply_markup=keyboard_generator(goods_for_dogs[call.data]))
    elif call.data in dogs_articles:
        await call.message.answer_photo(photo=images_list[call.data])
        await call.message.answer(text=dogs_articles[call.data])

    else:
        await call.message.answer(text=f'{call.data} - Эта функция пока в разработке. Жми сюда: /start')


# Данный код определяет список цен (объектов типа LabeledPrice) для товаров, которые можно приобрести через сбербанк, 
# а также варианты доставки (объектов типа ShippingOption) с указанием соответствующих цен.
# Сначала мы создаем объекты типа LabeledPrice для каждого товара, указывая наименование и стоимость. 
# Затем мы создаем объекты типа ShippingOption для каждого варианта доставки, указывая идентификатор, название и соответствующие цены, используя метод add() для добавления объектов LabeledPrice.

# Для доставки СДЭК у нас есть только один вариант с указанием цены за доставку в пункт выдачи. 
# Для Почты России мы добавляем две дополнительные цены за дополнительные опции (картонная коробка и срочное отправление). 
# Для самовывоза у нас есть только одна цена за самовывоз в определенном месте.


PRICES = [
    LabeledPrice(label='Флоринорм', amount=1600),
    LabeledPrice(label='Упаковка', amount=200)
]

CDEK_SHIPPING_OPTION = ShippingOption(
    id='cdek',
    title='СДЭК'
).add(LabeledPrice('В пункт выдачи СДЭК', 500))

POST_SHIPPING_OPTION = ShippingOption(
    id='post',
    title='Почта России'
)

POST_SHIPPING_OPTION.add(LabeledPrice('Картонная коробка', 300))
POST_SHIPPING_OPTION.add(LabeledPrice('Срочное отправление', 550))

PICKUP_SHIPPING_OPTION = ShippingOption(
    id='pickup',
    title='Самовывоз'
)

PICKUP_SHIPPING_OPTION.add(LabeledPrice(
    'Самовывоз доступен только в Подрезково', 1000))

# Это обработчики команд бота. Первый обрабатывает команду '/startt', и если её получает, 
# то отправляет пользователю сообщение с текстом 'startt', который берётся из словаря MESSAGES. 
# Второй обрабатывает команду '/help' и отправляет пользователю сообщение с текстом 'help'. 
# Третий обрабатывает команду '/terms' и отправляет пользователю сообщение с текстом 'help'. 
# Однако, команда '/terms' явно должна возвращать текст, связанный с условиями использования сервиса, 
# а не текст, связанный с помощью.

@dp.message_handler(commands=['startt'])
async def start_cmd(message: Message):
    await message.answer(MESSAGES['startt'])


@dp.message_handler(commands=['help'])
async def help_cmd(message: Message):
    await message.answer(MESSAGES['help'])


@dp.message_handler(commands=['terms'])
async def terms_cmd(message: Message):
    await message.answer(MESSAGES['help'])

# Этот код определяет функцию обработчика команды /buy_sber. 
# Когда пользователь отправляет эту команду, бот отправляет ему счет на оплату через Сбербанк.
# Когда пользователь получает счет, он может ввести свою электронную почту и номер телефона для 
# получения уведомлений о платеже. Эти данные можно запрашивать с помощью параметров need_email и need_phone_number.

# В счете указано описание и цена товара, а также его фотография и доступные опции доставки с их стоимостью. 
# Функция также указывает провайдерский токен, который используется для проведения транзакции, а также 
# параметр payload, который может содержать дополнительную информацию, которая будет передана счету.

@dp.message_handler(commands=['buy_sber'])
async def buy_process(message: Message):
    await bot.send_invoice(
        message.chat.id,
        title=MESSAGES['item_title'],
        description=MESSAGES['item_description'],
        provider_token=PAYMENTS_TOKEN,
        currency='RUB',
        photo_url=image,
        photo_height=500,
        photo_width=500,
        need_email=True,
        need_phone_number=True,
        is_flexible=True,
        prices=PRICES,
        start_parameter='example',
        payload='some invoice')

# Этот код отвечает за обработку запросов на доставку. Функция-обработчик shipping_process вызывается, 
# когда пользователь запрашивает опции доставки через команду /buy_sber.

# Первым делом проверяется, является ли страна доставки Великобританией, 
# и если да, то возвращается сообщение об ошибке. Затем, в зависимости от страны и города доставки, 
# формируется список опций доставки, которые будут предоставлены пользователю в качестве выбора.

# Например, если страна Россия, то в список опций будет добавлен вариант отправки почтой России, 
# а если город доставки — Подрезково, то в список опций будет добавлен вариант самовывоза.

# После формирования списка опций доставки вызывается метод bot.answer_shipping_query, 
# который отправляет ответ на запрос с опциями доставки. Если все прошло успешно, то параметр ok устанавливается 
# в значение True, а в качестве ответа передается список опций доставки shipping_options. Если произошла ошибка, 
# то параметр ok устанавливается в значение False, а в качестве ответа передается сообщение об ошибке error_message.

@dp.shipping_query_handler(lambda q: True)
async def shipping_process(shipping_query: ShippingQuery):
    if shipping_query.shipping_address.country_code == 'UK':
        return await bot.answer_shipping_query(
            shipping_query.id, ok=False, error_message=MESSAGES['UK_error']
        )
    shipping_options = [CDEK_SHIPPING_OPTION]
    if shipping_query.shipping_address.country_code == 'RU':
        shipping_options.append(POST_SHIPPING_OPTION)
        if shipping_query.shipping_address.city == 'Подрезково':
            shipping_options.append(PICKUP_SHIPPING_OPTION)

    await bot.answer_shipping_query(
        shipping_query.id,
        ok=True,
        shipping_options=shipping_options
    )


# Этот код является обработчиком запроса на предварительную проверку перед оформлением заказа 
# (pre-checkout query). Функция обработчика принимает запрос на предварительную проверку (pre_checkout_query), 
# проверяет его и отправляет ответ с результатом обработки.

# В данном случае, функция всегда возвращает ответ с положительным результатом (ok=True) 
# и идентификатором запроса на предварительную проверку (pre_checkout_query.id). 
# Это означает, что процесс оформления заказа может быть продолжен.

@dp.pre_checkout_query_handler(lambda q: True)
async def checkout_process(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Этот код определяет обработчик сообщений типа SUCCESSFUL_PAYMENT. 
# Когда пользователь успешно оплатил счет через сервис платежей, 
# бот будет отправлять сообщение с подтверждением успешной оплаты, 
# содержащее общую сумму оплаты и валюту. Сообщение формируется на основе шаблона из словаря MESSAGES.

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def succesful_payment(message: Message):
    await bot.send_message(
        message.chat.id,
        MESSAGES['successful_payment'].format(total_amount=message.successful_payment.total_amount,
                                              currency=message.successful_payment.currency)
    )

# Учитывать, что 500 = 5.00 в стоимости товара
