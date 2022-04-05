import os
import shutil

project_dir = 'lesson7_task_3_templates'
if not os.path.exists(project_dir):
    os.mkdir(project_dir)


folder = r'my_project'
files_list = []

for root, dirs, files in os.walk(folder):
    for file in files:
        if '.html' in file:
            files_list.append(os.path.join(root, file))

for path in files_list:
    folder = os.path.join(project_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)