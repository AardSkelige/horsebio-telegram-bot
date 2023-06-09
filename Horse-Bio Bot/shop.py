
price1 = 100
price2 = 500

menu_list = ['Магазины', 'Товары', 'Контакты']

county_to_buy = ['Россия', 'Казахстан']

cities_to_buy = {
    'Россия':  [
        'Москва и Московская область',
        'Санкт-Петербург',
        'Екатеринбург',
        'Астрахань',
        'Тюмень',
        'Хабаровск',
        'Иркутск'
    ],
    'Казахстан': [
        'Астана',
        'Караганда']
}

shops_to_buy = {
    'Москва и Московская область': [
        'Центральный склад "Horse-Bio"',
        'Ветеринарная аптека "HORSEVET"',
        'Ветеринарная аптека "IPPOVET"',
        'Магазин "Эквипарк Настасьино"',
        'Магазин "Хорс Аптека"',
        'Магазин "Фураж"',
        'Магазин "Технология Спорта"',
        'Магазин "Умный Ганс"',
        'Магазин "HORSE REHAB"',
    ],
    'Санкт-Петербург': [
        'Конный магазин "EQSTORE"',
        'Конный магазин "OFFHORSE"',

    ],
    'Екатеринбург': [
        'Ветеринарная клиника "VetСфера-9"'
    ],
    'Астрахань': [
        'Магазин конной амуниции "И-го-го"'
    ],
    'Тюмень': [
        'Конный магазин "Лошадок.нет"'
    ],
    'Хабаровск': [
        'Конный магазин "CandyHorse"'
    ],
    'Иркутск': [
        'Центральный склад "Allforhorses38"'
    ],
    'Астана': [
        'Конный магазин "Kula at"'
    ],
    'Караганда': [
        'Конный магазин "КАРАТ"'
    ]
}

shop_info = {
    # Контакты
    'Контакты':
    '<b>Адрес: </b>Россия, Московская область, г. Химки, мкр. Подрезково, ул. Парковая, 11А (ДПК Октябрьский).\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXRu2A">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Будние дни с 9:00 до 19:00, сб, вс - выходные.\n'
    '<b>Телефон:</b> +7 (499) 643-43-14, +7 (916) 101-59-96.\n'
    '<b>Telegram:</b> @horse_bio\n'
    '<b>Сайт:</b> https://horse-bio.ru/\n'
    '<b>E-mail:</b> info@horse-bio.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/horse.bio/">@horse.bio</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/horsebio/">vk.com/horsebio</a>\n'
    '\n'
    'Обращаем Ваше внимание, что по этому адресу находится склад магазина и выдача заказов осуществляется <u>только по предварительному заказу</u>.\n',

    # Россия
    # Москва и Московская область
    # Центральный склад "Horse-Bio"
    'Центральный склад "Horse-Bio"':
    '<b>Адрес: </b>Россия, Московская область, г. Химки, мкр. Подрезково, ул. Парковая, 11А (ДПК Октябрьский).\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXRu2A">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Будние дни с 9:00 до 19:00, сб, вс - выходные.\n'
    '<b>Телефон:</b> +7 (499) 643-43-14, +7 (916) 101-59-96.\n'
    '<b>Telegram:</b> @horse_bio\n'
    '<b>Сайт:</b> https://horse-bio.ru/\n'
    '<b>E-mail:</b> info@horse-bio.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/horse.bio/">@horse.bio</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/horsebio/">vk.com/horsebio</a>\n'
    '\n'
    'Обращаем Ваше внимание, что по этому адресу находится склад магазина и выдача заказов осуществляется <u>только по предварительному заказу</u>.\n',
    # Ветеринарная аптека "HORSEVET"
    'Ветеринарная аптека "HORSEVET"':
    '<b>Филиал 1</b>\n'
    '<b>Адрес: </b>Россия, г. Москва, Ясный проезд, 10. Остановка "Продмаг".\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXVDwB">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 11:00 до 20:00.\n'
    '<b>Телефон:</b> +7 (919) 997-57-00.\n'
    '\n'
    '<b>Филиал 2</b>\n'
    '<b>Адрес: </b>Россия, Московская область, КСК "Пегас" (поселение Краснопахорское, дер. Колотилово).\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXVEhD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 11:00 до 20:00.\n'
    '<b>Телефон:</b> +7 (916) 555-96-62.\n'
    '\n'
    '<b>Филиал 3</b>\n'
    '<b>Адрес: </b>Россия, Московская область, КСК "Максима Парк" (Горки Сухаревские, 67), центральный холл.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqTwi1D">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно, без выходных, с 10:00 до 20:00 (перерыв с 14:30 до 15:00).\n'
    '<b>Телефон:</b> +7 (903) 182-86-27.\n'
    '\n'

    '<b>Телефоны интернет-магазина: </b>+7 (495) 796-80-87, +7 (929) 928-71-12.\n'
    '<b>Сайт: </b>https://horsevet.ru/\n'
    '<b>E-mail:</b> horsevet-apteka@mail.ru и vet-medved@mail.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/horsevet_medvedkovo/">@horsevet_medvedkovo</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/vet_medved">vk.com/vet_medved</a>\n'
    '\n',
    # Ветеринарная аптека "IPPOVET"
    'Ветеринарная аптека "IPPOVET"':
    '<b>Адрес: </b>Россия, Московская область, Ленинский район, д. Богданиха, КСК «Виват, Россия», главное здание манежа 2 этаж.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXh-hD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ср - Пт с 10:00 до 18:00, Сб - Вс с 10:00 до 17:00, Пн, Вт - выходные.\n'
    '<b>График работы интернет-магазина:</b> Пн - Вс с 10:00 до 19:00.\n'
    '<b>Телефон:</b> +7 (925) 852-14-07, +7 (903) 018-79-08.\n'
    '<b>Сайт:</b> https://ippovet.ru/\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/ippovet/">@ippovet</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/club153298675">vk.com/club153298675</a>\n'
    '\n',
    # Магазин "Эквипарк Настасьино"
    'Магазин "Эквипарк Настасьино"':
    '<b>Адрес: </b>Россия, Московская область, Мытищинский район, д. Лысково.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq2qR1B">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно 7:00 - 22:00.\n'
    '<b>Телефон:</b> +7 (985) 725-44-77.\n'
    '<b>Вконтакте:</b> <a href=" https://vk.com/club160034184">vk.com/club160034184</a>\n'
    '\n',
    # Магазин "Хорс Аптека"
    'Магазин "Хорс Аптека"':
    '<b>Филиал 1 - КСК Белая Дача</b>\n'
    '<b>Адрес: </b>Россия, Московская область, г. Котельники, Полевой проезд, дом 3B. На территории КСК Белая Дача.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq2SATA">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Пн - Пт с 10:00 до 19:00, Сб - Вс с 10:00 до 18:00, без выходных.\n'
    '<b>Телефон:</b> +7 (925) 506-03-44\n'
    '\n'
    '<b>Филиал 2 - КСК Отрада</b>\n'
    '<b>Адрес: </b>Россия, Московская область, Красногорский район, Пятницкое шоссе (1,5 км от Митино). На территории КСК Отрада, 11 конюшня​.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq2gsXA">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Вт - Сб с 12:00 до 17:00, Вс, Пн - выходные.\n'
    '<b>Телефон:</b> +7 (903) 170-33-40.\n'
    '\n'
    '<b>Сайт:</b> http://horseapteka.ru/\n'
    '<b>E-mail:</b> horseapteka@yandex.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/horseapteka/">@horseapteka</a>\n'
    '\n',
    # Магазин "Фураж"
    'Магазин "Фураж"':
    '<b>Филиал 1 - КСК Акрон</b>\n'
    '<b>Адрес: </b>Россия, Московская область, Одинцовский район, посёлок Горки-10, Рублёво-Успенское шоссе.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq-eTgB">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ср - Вс с 10:00 до 20:00, Пн с 10:00 до 15:00, Вт - выходной.\n'
    '\n'
    '<b>Филиал 2 - КСК Звёздный</b>\n'
    '<b>Адрес: </b>Россия, Московская область, Щёлковский район, деревня Шевёлкино.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq-uOsB">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Вт - Сб с 10:00 до 20:00, Пн, Вс - выходные.\n'
    '\n'
    '<b>Филиал 3 - КСК Конкорд</b>\n'
    '<b>Адрес: </b>Россия, г. Москва, Балаклавский просп., 33, стр. 1.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq-RoGA">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 10:00 до 20:00.\n'
    '\n'
    '<b>Сайт:</b> https://furazh.com/\n'
    '<b>E-mail:</b> furazhshop@gmail.com\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/furazhstable/">@furazhstable</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/furazh">vk.com/furazh</a>\n'
    '\n',
    # Магазин "Технология Спорта"
    'Магазин "Технология Спорта"':
    '<b>Адрес: </b>Россия, Московская область, Красногорский р-он, пос. Отрадное, Магазин в КСК «Отрада».\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvq-xDXD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> 10:00 - 19:00, Без выходных.\n'
    '<b>Телефон:</b> +7 (495) 139-66-00 / 100, +7 (963) 640-93-75.\n'
    '<b>Сайт:</b> https://racessport.ru/\n'
    '<b>E-mail:</b> otrada@racessport.ru\n'
    '\n',
    # 'Магазин "Умный Ганс"
    'Магазин "Умный Ганс"':
    '<b>Адрес: </b>Россия, г. Москва, Ракетный бульвар, 5 (300 метров от метро ВДНХ, 5 минут пешком, также есть парковка).\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuARakB">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 12:00 до 20:00.\n'
    '<b>Телефон:</b> +7 (977) 537-47-27.\n'
    '<b>Telegram:</b> @klugerhans\n'
    '<b>Сайт:</b> https://klugerhans.ru/\n'
    '<b>E-mail:</b> sales@klugerhans.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/klugerhans.ru/">@klugerhans.ru</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/klugerhans">vk.com/klugerhans</a>\n'
    '\n',
    # Магазин "HORSE REHAB"
    'Магазин "HORSE REHAB"':
    '<b>Адрес: </b>Россия, Московская область, г. Химки, мкр. Подрезково, ул. Парковая, 11А (ДПК Октябрьский).\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvqXRu2A">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 9:00 до 20:00.\n'
    '<b>Телефон:</b> +7 (926) 356-36-33.\n'
    '<b>Telegram:</b> @horse_bio\n'
    '<b>Сайт:</b> https://horse-rehab.ru/shop/\n'
    '<b>E-mail:</b> ksk@horse-rehab.run'
    '<b>Instagram:</b> <a href="https://www.instagram.com/horse_rehab/?hl=ru">@horse_rehab</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/horserehab">vk.com/horserehab</a>\n'
    '\n',
    # Санкт-Петербург
    # Конный магазин "EQSTORE"
    'Конный магазин "EQSTORE"':
    '<b>Адрес: </b>Россия, г. Санкт-Петербург, Парнас, ул. Домостроительная, д. 3Д.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuAtykA">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно 11:00 - 19:30.\n'
    '<b>Телефон:</b> +7 (812) 930-54-00.\n'
    '<b>Сайт:</b> https://eqstore.ru\n'
    '<b>E-mail:</b> info@eqstore.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/eqstore.ru/">@eqstore.ru</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/eqstore_ru">vk.com/eqstore_ru</a>\n'
    '\n',
    # Конный магазин "OFFHORSE"
    'Конный магазин "OFFHORSE"':
    '<b>Адрес: </b>Россия, Санкт-Петербург, проспект Авиаконструкторов, 45, корп. 1.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuEF1oC">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Вт - Вс с 11:00 до 19:00.\n'
    '<b>Телефон:</b> +7 (905) 252-90-09.\n'
    '<b>Сайт:</b> https://ofhorse.shop/\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/ofhorse.shop/">@ofhorse.shop</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/ofhorse">vk.com/ofhorse</a>\n'
    '\n',
    # Екатерингбург
    # Ветеринарная клиника "VetСфера-9"
    'Ветеринарная клиника "VetСфера-9"':
    '<b>Адрес: </b>Россия, г. Екатеринбург, ул. Историческая, 54 и ул. Счастливая, 8.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuESvLD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Пн - Пт с 9:00 до 21:00, Сб - Вс с 10:00 до 15:00.\n'
    '<b>Телефон:</b> +7 (343) 345-66-35, +7 (912) 286-66-33, +7 (982) 702-66-35.\n'
    '<b>Сайт:</b> http://www.vetsfera9.ru/\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/vetsfera9/">vk.com/vetsfera9</a>\n'
    '\n',
    # Астрахань
    # Магазин конной амуниции "И-го-го"
    'Магазин конной амуниции "И-го-го"':
    '<b>Адрес: </b>Россия, г. Астрахань ул. Савушкина, д. 4, корп. 1.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuEhmkD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно 8:00 - 17:00.\n'
    '<b>Телефон:</b> +7 (988) 173-31-39, +7 (8512) 43-31-39.\n'
    '<b>E-mail:</b> info@igogomag.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/igogomag/">@igogomag</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/club24768138">vk.com/club24768138</a>\n'
    '\n',
    # Тюмень
    # Конный магазин "Лошадок.нет"
    'Конный магазин "Лошадок.нет"':
    '<b>Адрес: </b>Россия, г. Тюмень, ул. Калинина 3, отдельный вход, 1-й этаж.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuIqbpA">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Только по предварительной договорённости.\n'
    '<b>Телефон:</b> +7 (906) 873-66-39.\n'
    '<b>Сайт:</b> http://www.loshadok.net/\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/loshadoknet/?hl=ru">@Loshadoknet</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/loshadoknet">vk.com/loshadoknet</a>\n'
    '\n',
    # Хабаровск
    # Конный магазин "CandyHorse"
    'Конный магазин "CandyHorse"':
    '<b>Адрес: </b>Россия, г. Хабаровск, ул Камская 6, офис 2.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuIb3oC">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Пн - Пт с 10:00 до 18:00, Сб - Вс с 11:00 до 17:00.\n'
    '<b>Телефон:</b> +7 (914) 400-74-74.\n'
    '<b>Telegram:</b> @t.me/candyhorse_kh\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/candyhorse_khv/">@candyhorse_khv</a>\n'
    '\n',
    # Иркутск
    # Центральный склад "Allforhorses38"
    'Центральный склад "Allforhorses38"':
    '<b>Адрес: </b>Россия, г. Иркутск, ул Горького 29.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuIshpD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> приём заказов круглосуточно.\n'
    '<b>Телефон:</b> +7 (950) 102-88-47.\n'
    '<b>E-mail:</b> 57431734@rambler.ru\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/allforhorses38/">@allforhorses38</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/allforhorses38">vk.com/allforhorses38</a>\n'
    '\n',
    # Казахстан
    # Астана
    # Конный магазин "Kula at"
    'Конный магазин "Kula at"':
    '<b>Адрес: </b>Казахстан, г. Астана (г. Нур-Султан), ул. Сейфуллина, д. 5, каб. 5.\n'
    '<b>График работы:</b> Пн-Сб 10:00 - 17:00, Вс - выходной.\n'
    '<b>Телефон:</b> +7 (707) 269-73-80.\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/kula.at/">@kula.at</a>\n'
    '\n',
    # Конный магазин "КАРАТ"
    'Конный магазин "КАРАТ"':
    '<b>Адрес: </b>Казахстан, г. Караганда, ул. Воинов Интернационалистов, 31, офис 417.\n'
    '<b>Посмотреть на </b><a href="https://yandex.kz/maps/-/CCUvuMrVlD">Яндекс.Картах</a>\n'
    '<b>График работы:</b> Ежедневно с 10:00 до 19:00.\n'
    '<b>Телефон:</b> +7 (771) 006-01-77, +7 (705) 751-17-17.\n'
    '<b>E-mail:</b> karat@avenda.kz\n'
    '<b>Instagram:</b> <a href="https://www.instagram.com/karat_magazin/">@karat_magazin</a>\n'
    '<b>Вконтакте:</b> <a href="https://vk.com/karatmagazin">vk.com/karatmagazin</a>\n'
    '\n'
}

animals_categories = ['Лошади', 'Собаки']

goods_filter = {
    'Собаки': [
        'Товары для собак по действию',
        'Товары для собак по сериям'
    ],
    'Лошади': [
        'Товары для лошадей по действию',
        'Товары для лошадей по сериям'
    ]
}

# Выводим товары по сериям
goods_by_series = {
    'Товары для лошадей по сериям': [
        'ArtroPro',
        'BronchoPro',
        'EnergyPro',
        'ExterPro',
        'GastroPro',
        'ImmunoPro',
        'LuckyPro',
        'MassPro',
        'QuietPro',
        'VitaPro'
    ],
    'Товары для собак по сериям': [
        'ArtroPro',
        'BronchoPro',
        'EnergyPro',
        'ExterPro',
        'GastroPro',
        'ImmunoPro',
        'LuckyPro',
        'MassPro',
        'QuietPro',
        'VitaPro'
    ]
}

# Выводим товары по действию
goods_by_effect = {
    'Товары для собак по действию': [
        'Для суставов собак',
        'Для ЖКТ собак',
        'Витамины для собак'
    ],
    'Товары для лошадей по действию': [
        'Для суставов',
        'Для лёгких',
        'Для нервной системы',
        'Для жеребят и маток',
        'Для ЖКТ',
        'Для мышц',
        'Для иммунитета',
        'Для копыт',
        'Для спортивных лошадей',
        'Витамины',
        'Гели и крема',
        'Эликсиры',
        'Лакомства'
    ]
}

# Вывод товаров по категории для собак
goods_for_dogs = {
    'Для суставов собак':  [
        '"ХОНДРО" для мелких пород',
        '"ХОНДРО" для крупных пород',
        '"Джуниор" - щенки и молодые собаки',
        '"Хондрофит" для крупных пород',
        '"Хондрофит" для мелких пород',
        '"Хондрофит Плюс" для крупных пород',
        '"Хондрофит Плюс" для мелких пород',
        '"Флексинил" для мелких пород',
        '"Флексинил" для крупных пород,'
    ],
    'Для ЖКТ собак': [
        '"Флоринорм" пробиотик и пребиотик',
    ],
    'Витамины для собак': [
        '"Питательный эликсир"'
    ]
}

dogs_articles = {
    '"Флоринорм" пробиотик и пребиотик':
        '<b>Описание:\n</b>Подкормка предназначена для профилактики и лечения бактериальных заболеваний желудочно-кишечного тракта (ЖКТ), нормализации пищеварения и укрепления иммунитета. Благодаря содержащимся в составе пробиотику и пребиотику добавка оказывает двойное действие на микрофлору ЖКТ: одновременно заселяет кишечник бактериями и выступает в качестве питательной среды для полезных микроорганизмов. Улучшает усвояемость пищи.\n'
        '\n'
        '<b>Рекомендовано:\n</b>собакам и кошкам всех возрастов для нормализации работы ЖКТ и укрепления иммунитета; для улучшения усвояемости пищи и при расстройствах пищеварения, сопровождающихся диареей или запором; при смене вида питания или переходе на новый корм; при восстановление кишечной микрофлоры после приема антибиотиков и дегельминтизации; для профилактики и лечения инфекционных заболеваний; после хирургических вмешательств и пищевых отравлений; при заболеваниях ЖКТ в составе комплексной терапии (гастроэнтерит, панкреатит, колит и т.п.); при аллергии; для предупреждения стрессовых реакций (переезды, выставки и т.п.); а также в период прикорма щенков и котят.\n'
        '\n'
        '<b>Условия хранения:\n</b>при температуре от -30 до +30 ˚С в сухом, защищенном от света месте.\n'
        '\n'
        '<b>Срок годности:\n</b>2 года. После вскрытия упаковки использовать в течение 18 месяцев.\n'
        '\n'
        '<b>Состав:\n</b>спорообразующие бактерии вида Bacillus Subtilis и Bacillus licheniformis в общем количестве не менее 2х109КОЕ/г, лактоза.\n'
        '\n'
        '<b>Противопоказания:\n</b>не установлено, возможна индивидуальная повышенная чувствительность или непереносимость отдельных компонентов.\n'
        '\n'
        '<b>Масса:\n</b>600 грамм.\n'
        '\n'
        '<b>Дозировка и способ применения:</b>\n'
        'Лечение: по 0,3 г на 1 кг веса животного (1,5 мерные ложки на 10 кг) 2 раза в день в течение 15 дней.\n'
        'Профилактика: по 0,2 г на 1 кг веса животного (1 мерная ложка на 10 кг) в день в течение 7 дней. Далее по 0,5 г на 1 кг веса животного (2,5 мерные ложки на 10 кг) в день в течение 4 дней.\n'
        'Для нормализации пищеварения, укрепления иммунитета, улучшения усвояемости пищи в дозе:\n'
        'По 0,2 г на 1 кг веса животного (1 мерная ложка на 10 кг) в день в течение 1-2 месяцев.\n'
        'Важно: дозировку добавки можно корректировать в соответствии с индивидуальными особенностями животных и рекомендациями ветеринарного врача. Добавка не оказывает побочного действия на организм животных в дозах, превышающих рекомендуемые.\n'
         '\n'
        '<b>Масса:\n'
        '</b>600 грамм.\n'
         '\n'
        '<b>Цена:</b>\n' 
        '1600 ₽\n'
}

images_list = {
    '"Флоринорм" пробиотик и пребиотик':
    'https://horse-bio.ru/d/florinorm_dlya_sobak_i_koshek_600_g.jpg'

}

image = 'https://horse-bio.ru/d/florinorm_dlya_sobak_i_koshek_600_g.jpg'