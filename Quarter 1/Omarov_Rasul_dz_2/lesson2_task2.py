my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list2 = []

for item in my_list:
	if not item.isalpha():
		my_list2.extend(['"', f'{int(item):02d}', '"'])
	else:
		my_list2.append(item)
print(my_list2)

print(' '.join(my_list2))

