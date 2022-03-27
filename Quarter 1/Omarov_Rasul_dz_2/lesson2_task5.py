prices = [57.8, 46.51, 97, 709.5, 14.9, 8.2, 7, 34.1, 2000.35, 11, 15.62, 117.3, 1000]
prices2 = []
for price in prices:
	prices2.append(str(price))
print('Список цен на товары:')
print(prices,'\n')

print('Решение задания под пунктом "А":')
for price in prices2:
	if price.find('.')!=-1 and len(price.split('.')[1]) == 1:
		print(price.split('.')[0], 'руб', price.split('.')[1]+'0', 'коп, ', end='')
	elif price.find('.')!=-1 and len(price.split('.')[1]) == 2:
		print(price.split('.')[0], 'руб', price.split('.')[1], 'коп, ', end='')
	else:
		print(price, 'руб', '00 коп, ', end='')
print('\n')

print('Решение задания под пунктом "B":')
print('id - до сортировки', id(prices))
prices.sort()
print(prices)
print('id - после сортировки', id(prices), '\n')

print('Решение задания под пунктом "C":')
sorted_prices = sorted(prices, reverse = True)
print(sorted_prices,'\n')

print('Решение задания под пунктом "D":')
print(prices[len(prices)-5:])