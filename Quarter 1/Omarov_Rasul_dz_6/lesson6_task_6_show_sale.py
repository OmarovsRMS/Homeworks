import csv
import sys

price_list = []


with open('lesson6_task_6_bakery.csv', 'r', encoding='utf-8') as file:
	price = csv.reader(file)
	for row in price:
		price_list.append(''.join(row))

if len(sys.argv) == 1:
	for i in range(len(price_list)):
		print(price_list[i])
elif len(sys.argv) == 2:
	for i in range(int(sys.argv[1])-1, len(price_list)):
		print(price_list[i])
elif len(sys.argv) == 3:
	for i in range(int(sys.argv[1])-1, int(sys.argv[2])):
		print(price_list[i])
else:
	print('Введите допустимое количество параметров')
