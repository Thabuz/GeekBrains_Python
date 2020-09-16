# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_div(first,second):
    try:
        return f'{first} / {second} = {int(first) / int(second)}'
    except ZeroDivisionError:
        print("На ноль делить нельзя, введите другое значение!")
    except ValueError:
        print('Неверный ввод, пожалуйста введите числовые значения!')

print(my_div(input('Число №1: '),input('Число №2: ')))

