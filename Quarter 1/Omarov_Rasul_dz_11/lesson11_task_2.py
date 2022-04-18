class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

num1 = input('Введите делимое: ')
num2 = input('Введите делитель: ')

try:
    if int(num2) == 0:
        raise MyError('Деление на ноль невозможно')
    print('Результат равен:', int(num1)/int(num2))
except ValueError:
    print('Вы ввели не число')
except MyError as err:
    print(err)
