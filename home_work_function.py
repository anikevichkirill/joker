# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('На ноль делить нельзя!')



while True:
    oper = int(input("Выберете действие: 1 - сложение; 2 - вычитание; 3 - умножение; 4 - деление; 0 - выход: "))
    if oper in (0, 1, 2, 3, 4):
        if oper == 1:
            print(addition(float(input('введите первое число: ')), float(input('введите второе число: '))))
        elif oper == 2:
            print(subtraction(float(input('введите первое число: ')), float(input('введите второе число: '))))
        elif oper == 3:
            print(multiplication(float(input('введите первое число: ')), float(input('введите второе число: '))))
        elif oper == 4:
            print(division(float(input('введите первое число: ')), float(input('введите второе число: '))))
        elif oper == 0:
            print("Заходи ежели чё")
            break
    else:
        print("Выбери другое действие!")

# task2

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень). Номер месяца вводить с клавиатуры.

def season(a):
    year = {'Winter': (1, 2, 12),
            'Sping': (3, 4, 5),
            'Summer': (6, 7, 8),
            'Autumn': (9, 10, 11)}

    for key in year.keys():
        if a in year[key]:
            return key


print(season(int(input('Choose number a month: '))))