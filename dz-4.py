# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
my_list = []
with open('home_work.txt', 'r') as f:
    edit_text = f.readlines()
    for i in edit_text:
        i = list(i.rstrip().split(' '))
        i.insert(0, translate[i[0]])
        del i[1]
        my_list += [' '.join(i)]
with open('new_home_work.txt', 'w') as d:
    for i in my_list:
        print(i, file=d)
