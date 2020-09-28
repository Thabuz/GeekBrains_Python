# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
# соответствующее сообщение и завершать скрипт.
from time import sleep
from colorama import Fore, Style

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self, time_work):
        start_time = 0
        while True:
            print(Fore.RED + self.__color[0], end=' ')
            sleep(7)
            start_time += 7
            if time_work <= start_time:
                break
            print(Fore.YELLOW + self.__color[1], end=' ')
            sleep(2)
            start_time += 2
            if time_work <= start_time:
                break
            print(Fore.GREEN + self.__color[2], end=' ')
            sleep(5)
            start_time += 5
            if time_work <= start_time:
                break
        print(Style.RESET_ALL, end='')
        print(f'\nРабота светофора завершена после {time_work} секунд!')

a = TrafficLight()
a.running(35)




