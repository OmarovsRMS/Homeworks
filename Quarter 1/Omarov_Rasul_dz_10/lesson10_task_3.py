class Cell:
    def __init__(self, num_cells):
        self.num_cells = num_cells
    def __str__(self):
        return f'Клетка содержит {self.num_cells} ячеек'
    def __add__(self, other):
        if self.__class__ != other.__class__:
            raise ValueError('Не соответствуют классы аргуметов')
        else:
            return Cell(self.num_cells + other.num_cells)
    def __sub__(self, other):
        if self.__class__ != other.__class__:
            raise ValueError('Не соответствуют классы аргуметов')
        elif self.num_cells < other.num_cells:
            raise ValueError('Уменьшаемое меньше вычитаемого')
        else:
            return Cell(self.num_cells - other.num_cells)
    def __mul__(self, other):
        if self.__class__ != other.__class__:
            raise ValueError('Не соответствуют классы аргуметов')
        else:
            return Cell(self.num_cells * other.num_cells)
    def __floordiv__(self, other):
        if self.__class__ != other.__class__:
            raise ValueError('Не соответствуют классы аргуметов')
        else:
            return Cell(self.num_cells // other.num_cells)
    def make_order(self, row):
        num_rows = self.num_cells // row
        mod_rows = self.num_cells % row
        for _ in range(num_rows):
            print('*'*row)
        print('*'*mod_rows)
class Car:
    def __init__(self, name):
        self.name = name

cell1 = Cell(15)
cell2 = Cell(5)
car = Car('Мазда')

print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)

cell1.make_order(5)
