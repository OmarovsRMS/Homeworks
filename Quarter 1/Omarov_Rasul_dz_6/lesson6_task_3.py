import csv
import pickle
fio_list = []
hobby_list = []
my_dict = {}

with open('lesson6_task_3_users.csv') as file:
	fio = csv.reader(file)
	for row in fio:
		fio_list.append(' '.join(row))

with open('lesson6_task_3_hobby.csv') as f:
	hobby = csv.reader(f)
	for rows in hobby:
		hobby_list.append(', '.join(rows))

while len(hobby_list) < len(fio_list):
	hobby_list.append(None)

def user_hobby():
	if len(hobby_list) > len(fio_list):
		return 1
	else:
		for i in range(len(fio_list)):
			my_dict[fio_list[i]] = hobby_list[i]
		with open('lesson6_task_3_users.pickle', 'wb') as pickfile:
			pickle.dump(my_dict, pickfile)
		return my_dict

print(user_hobby())






