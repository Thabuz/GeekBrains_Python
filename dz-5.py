# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('numbers.txt', 'w') as f:
    a = list(input('Введите набор чисел разделенных пробелами: ').split(' '))
    for i in a:
        f.writelines(i)

with open('numbers.txt', 'r') as f1:
    my_numbers = f1.read()
    my_sum = 0
    for i in my_numbers:
        my_sum += int(i)
    print(f'Сумма введенных чисел - {my_sum}')

