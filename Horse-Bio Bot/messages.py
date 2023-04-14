help_message = '''
Отправьте команду /buy_sber, чтобы перейти к покупке.
Узнать правила можно воспользовавшись командой /terms.
'''

start_message = 'Привет! Сейчас ты увидишь работу платежей в Telegram!\n' + help_message

terms = '''\
Правила!
'''

item_title = 'Флексинил'
item_description = '''\
Купить "Флексинил"
'''

AU_error = '''\
В данную страну доставка не оформляется. Сорри
'''

successful_payment = '''
Платеж на сумму `{total_amount} {currency}` совершен успешно!
'''


MESSAGES = {
    'startt': start_message,
    'help': help_message,
    'terms': terms,
    'item_title': item_title,
    'item_description': item_description,
    'AU_error': AU_error,
    'successful_payment': successful_payment,
}