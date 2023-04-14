import sqlite3
import re


# Этот код определяет две функции для работы с базой данных SQLite.

# Функция add(item) открывает соединение с базой данных и добавляет новый элемент (item) в 
# таблицу shop, используя метод execute() с SQL-запросом для вставки новой записи в таблицу. 
# Затем она фиксирует изменения с помощью метода commit(), закрывает курсор с помощью close() и завершает работу функции.

async def add(item):
    connect = sqlite3.connect('TG_DB.db')
    cursor = connect.cursor()
    m = []
    m.append(item)
    cursor.execute('INSERT INTO shop VALUES(?)', m)
    connect.commit()
    cursor.close()

# Функция buy() также открывает соединение с базой данных и выполняет запрос на 
# выборку всех данных из таблицы products. Затем она проходит по каждой выбранной 
# записи и создает новый список строк g без кавычек, запятых и скобок с помощью 
# регулярного выражения re.sub(). Затем она создает список c, в котором каждый 
# элемент списка g переносится на новую строку с добавлением символа \n. 
# В конце, с помощью метода join(), все элементы списка c объединяются в одну 
# строку v, которая возвращается функцией buy().

async def buy():
    connect = sqlite3.connect('TG_DB.db')
    cursor = connect.cursor()
    query = 'SELECT * FROM products'
    cursor.execute(query)
    data = cursor.fetchall()
    m = []

    for i in data:
        m.append(i)

    l = len(data)
    g = []

    for i in range(l):
        a = re.sub('|\(|\'|\,|\)', '', str(m[i]))
        g.append(a)
    c = []


    for i in g:
        q = i + '\n'
        c.append(q)

    v = '\n'.join(c)
    return v