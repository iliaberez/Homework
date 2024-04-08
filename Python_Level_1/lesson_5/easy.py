#Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


def make_dir(name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(dir_path)
        print ( 'Директория {} создана' . format (dir_path))
    except:
        print('Директория {} уже существует', dir_path)

for i in range(1,10):
    make_dir('dir_'+ str(i))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

directory = os.getcwd()

with os.scandir(directory) as files:
    subdir = [file.name for file in files if file.is_dir()]

print(subdir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil

shutil.copyfile(__file__, __file__.split('.')[0]+'_copy' + '.py')