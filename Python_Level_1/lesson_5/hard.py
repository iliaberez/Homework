# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import shutil
import sys


print('sys.argv = ', sys.argv)

def write_file(main_dir, cur_dir):
    file = open("temp.txt", "w")
    file.writelines(['main_dir:{}\n'.format(main_dir), 'cur_dir:{}'.format(cur_dir)])


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    

def make_dir():
    if not sys.argv[2]:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), sys.argv[2])
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_path))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_path))

def copy_file():
    try:
        if not sys.argv[2]:
            print("Необходимо указать имя файла вторым параметром")
            return
        shutil.copyfile(sys.argv[2], sys.argv[2]+'copy')
        print('Успешно создана копия {}\n'.format(sys.argv[2]+'copy'))
    except:
        print('Успешно перешёл в {}\n'.format(os.getcwd()))

def go_dir():
    try:
        os.chdir(sys.argv[2])
        print('Успешно перешёл в {}\n'.format(os.getcwd()))
    except:
        print('Директория {} не найдена\n'.format(sys.argv[2]))
    
def rm_file():
    dir_path = os.path.join(os.getcwd(), sys.argv[2])
    if os.path.isfile(dir_path):
        print('Вы уверены что хотите удалить {} yes/no \n'.format(sys.argv[2]))
        res = str(input())
        if res == 'yes':
            try:
                os.remove(dir_path)
                print('Директория {} удалена\n' . format(dir_path))
            except:
                print('Файл {} не обнаружен\n'.format(dir_path))

def show_dir():
    print(os.listdir(os.getcwd()))


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": rm_file,
    "cd": go_dir,
    "ls": show_dir
}

try:
    key = sys.argv[1]
except IndexError:
    key = None

if os.path.isfile("temp.txt"):
    dir = os.getcwd()
    file = open("temp.txt", "r")
    for line in file:
        temp = line.split(':')
        if temp[0] == 'main_dir':
            main_dir = temp[2].split('\\')[-1][:-1]
        if temp[0] == 'cur_dir':
            cur_dir = temp[2].split('\\')[-1]
    if main_dir != cur_dir:
        os.chdir(cur_dir)
    print(os.getcwd)
    file.close()
else:
    main_dir = os.getcwd()
    write_file(main_dir, main_dir)

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")