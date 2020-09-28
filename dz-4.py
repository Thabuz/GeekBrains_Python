#  Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
#  speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#  что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
#  WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
#  текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
#  При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Машина {self.name} движется со скоростью {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина {self.name} превысила допустимую скорость!')
        else:
            print(f'Машина {self.name} движется с нормальной скоростью!')



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина {self.name} превысила допустимую скорость!')
        else:
            print(f'Машина {self.name} движется с нормальной скоростью!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police is True:
            print('Это машина полиции!')
        else:
            print('Это не полицейская машина!')


a = Car(50,'red','test_car', False)
a.go()
a.stop()
a.turn('налево')

lada = TownCar(80, 'black', 'Lada', False)
mazda = SportCar(100, 'white', 'Mazda', False)
man = WorkCar(50, 'red', 'Man', False)
toyota = PoliceCar(100, 'white', 'Toyota', True)

lada.show_speed()
mazda.stop()
toyota.go()
