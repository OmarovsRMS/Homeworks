class Warehouse:
    pass

class Equipment:
    company = 'My_Corporation'
    year = '2022'
    def __init__(self, model, color):
        self.model = model
        self.color = color

class Printers(Equipment):
   type = 'printer'

class Scaners(Equipment):
    type = 'scaner'

class Xeroxes(Equipment):
    type = 'xerox'

hp = Printers('HP', 'White')

print(hp.type)
