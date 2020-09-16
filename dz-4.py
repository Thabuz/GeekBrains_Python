# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    return x ** abs(y)

# Более сложная реализация без оператора **, предусматривающая использование цикла.
def my_func2(x, y):
    out = abs(x)
    if abs(y) == 1:
        return x
    else:
        for i in range(abs(y) - 1):
            out *= abs(x)
    return out



