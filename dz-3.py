# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, positions, wage, bonus):
        self.name = name
        self.surname = surname
        self.positions = positions
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, positions, wage, bonus):
        super().__init__(name, surname, positions, wage, bonus)

    def get_full_name(self):
        print(f'Имя сотрудника {self.name} {self.surname}')

    def get_total_income(self):
        print('Доход с учетом премии - ' + str(self._income['wage'] + self._income['bonus']))

a = Position('Валерий','Гончаров','Стажер',10000, 5000)
a.get_full_name()
a.get_total_income()
