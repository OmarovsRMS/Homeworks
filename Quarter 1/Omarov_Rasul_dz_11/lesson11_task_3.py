class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_list = []
num = None

try:
    while True:
        num = input('Введите число ')
        if num == 'stop':
            print(my_list)
            break
        if num.isdigit():
            my_list.append(num)
        else:
            raise MyError('Вы ввели не число')
except MyError as err:
    print(err)