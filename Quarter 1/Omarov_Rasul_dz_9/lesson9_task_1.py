from time import sleep

class TrafficLight:
    __color = 'Красный'
    def running(self):
        print(self.__color)
        sleep(7)
        self.__color = 'Желтый'
        print(self.__color)
        sleep(2)
        self.__color = 'Зеленый'
        print(self.__color)

a = TrafficLight()

a.running()
