class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_of_mass(self):
        return self._length*self._width*25*5

road = Road(20, 5000)
print(road.calc_of_mass())
