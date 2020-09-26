# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('home_work.txt', 'r') as my_file:
    count_string = 0
    for i in my_file.readlines():
        print(i.rstrip(), end='')
        print(f' (Строка содержит - {len(i.rstrip())} символов.)')
        count_string += 1
    print(f'Файл содержит {count_string} строк(и).')
