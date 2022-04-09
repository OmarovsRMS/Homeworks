class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        return f'Текущая скорость машины - {self.speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость машины {self.name} превышена'
        else:
            return super().show_speed()



class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость машины {self.name} превышена'
        else:
            return super().show_speed()

class PoliceCar(Car):
    pass



town_car = TownCar(70, 'Красная', 'Тойота')
print(town_car.name)
town_car.go()
print(town_car.show_speed())
town_car.turn('налево')
town_car.stop()


work_car = TownCar(29, 'Белая', 'Мазда')
work_car.go()
print(work_car.show_speed())
work_car.turn('направо')
work_car.stop()



