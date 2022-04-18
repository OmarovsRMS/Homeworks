class Warehouse:
    num_of_printers = 0
    num_of_scaners = 0
    num_of_xeroxes = 0

class Equipment:
    company = 'My_Corporation'
    year = '2022'
    def __init__(self, model, color, inv_number):
        self.model = model
        self.color = color
        self.inv_number = inv_number

class Printers(Equipment):
   type = 'printer'
   def transfer_to_warehouse(self):
       warehouse_dict.update({self.model:self.inv_number})
       Warehouse.num_of_printers += 1


class Scaners(Equipment):
    type = 'scaner'
    def transfer_to_warehouse(self):
        warehouse_dict.update({self.model: self.inv_number})
        Warehouse.num_of_scaners += 1

class Xeroxes(Equipment):
    type = 'xerox'
    def transfer_to_warehouse(self):
        warehouse_dict.update({self.model: self.inv_number})
        Warehouse.num_of_xeroxes += 1

warehouse_dict = {}

hp = Printers('HP', 'Black', 111555)
hp.transfer_to_warehouse()

samsung = Printers('Samsung', 'White', 111666)
samsung.transfer_to_warehouse()

xerox = Xeroxes('XEROX', 'Black', 111777)
xerox.transfer_to_warehouse()

phaser = Scaners('Phaser', 'Red', 111888)
phaser.transfer_to_warehouse()

print(warehouse_dict)
print(f'Количество принтеров на складе: {Warehouse.num_of_printers}')
print(f'Количество ксероксов на складе: {Warehouse.num_of_xeroxes}')
print(f'Количество сканеров на складе: {Warehouse.num_of_scaners}')



