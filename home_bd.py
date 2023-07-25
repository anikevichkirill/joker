# Создайте новую Базу данных.
# Поля: id, 2 целочисленных поля
# Целочисленные поля заполняются рандомно от 0 до 9
# Посчитайте среднее арифметическое всех элементов без учёта id
# Если среднее арифметическое больше количества записей в БД, то удалите четвёртую запись БД
import sqlite3
import random

a = sqlite3.connect('home.bd')  # создал новую базу данных 'home.bd'
cursor = a.cursor()  # создал курсор для взаимодействия с базой данных
cursor.execute('''CREATE TABLE IF NOT EXISTS жильцы (id INTEGER PRIMARY KEY AUTOINCREMENT, room INT, family INT)''')
# создал таблицу жильцы: с колонками id, кол-во комнат и  количество человек в семье
r = random.randint(0, 9)  # создал рандомно параметр room
f = random.randint(0, 9)  # создал рандомно параметр family
cursor.execute('''INSERT INTO жильцы (room, family) VALUES(?, ?)''', (r, f))  # заполнил таблицу
cursor.execute('''SELECT * FROM жильцы''')  # просмотрел таблицу без id

k = cursor.fetchall()  #
print(k)
a.commit()
sum_line = 0  # сумма строчек оно же id
col = 0  # сумма всех строчек
for i in k:
    col += sum(i)
    sum_line += 1
sa = col/(2 * sum_line)
print(sum_line)
print(col)
print(f'Среднее арифметическое всех элементов без id = {sa}')
if sa > sum_line:
    cursor.execute('''DELETE FROM жильцы WHERE id = 4''')
else:
    print('Goodbay!')


a.commit()
