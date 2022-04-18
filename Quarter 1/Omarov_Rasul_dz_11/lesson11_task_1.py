class MyDate():
    def __init__(self, date_value):
        if self.validate(date_value):
            self.date_value = date_value
        else:
            raise ValueError('Не соответствие формата даты')
    @staticmethod
    def validate(param):
        if int(param.split('-')[0]) <= 31 and int(param.split('-')[1]) <= 12:
            return True
        else:
            return False

today = MyDate('21-12-1987')
print(today.date_value)
