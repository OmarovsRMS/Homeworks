class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

worker = Position('Иван', 'Иванов', 'Инженер', 100, 50)

print(worker.name)
print(worker.surname)
print(worker.position)
print(worker.get_full_name())
print(worker.get_total_income())

