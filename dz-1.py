#  Создать список и заполнить его элементами различных типов данных.
#  Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#  Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [11, 23.44, 'hello', [1, 2], (1, 2, 3)]
for i in my_list:
    print(f'Object {i} , type - {type(i)}')