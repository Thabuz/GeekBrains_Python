# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = input('Введите элементы списка через пробел: ').split(' ')
new_list = []
counter1 = 0
counter2 = 1
for i in range(len(my_list) - 1):
    if counter2 == len(my_list) - 1 and len(my_list) % 2 == 0:
        new_list += [my_list[counter2]] + [my_list[counter1]]
        break
    elif counter1 == len(my_list) - 1 and len(my_list) % 2 != 0:
        new_list += [my_list[counter1]]
        break
    else:
        new_list += [my_list[counter2]] + [my_list[counter1]]
        counter1 += 2
        counter2 += 2
        continue

print(f'Список после перестановки -> {new_list}')
