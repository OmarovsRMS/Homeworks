import os

path_list = ['settings', 'mainapp', 'adminapp', 'authapp']
dir_name = 'data'

if not os.path.exists(dir_name):
	os.mkdir(dir_name)

for dirs in path_list:
	dir_path = os.path.join(dir_name, dirs)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)

