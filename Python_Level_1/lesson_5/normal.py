# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os


exit = 0

main_directory = os.getcwd()

def go_dir(name_dir):
    try:
        os.chdir(name_dir)
        print('Успешно перешёл в {}\n'.format(os.getcwd()))
    except:
        print('Директория не найдена {}\n'.format(name_dir))

def show_dir():
    print(os.listdir(os.getcwd()))

def make_dir(name_dir):
    dir_path = os.path.join(os.getcwd(), format(name_dir))
    try:
        os.mkdir(dir_path)
        print ( 'Директория {} создана\n'.format(dir_path))
    except:
        print('Директория {} уже существует\n'.format(dir_path))

def rm_dir(name_dir):
    dir_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.removedirs(dir_path)
        print ( 'Директория {} удалена\n' . format(dir_path))
    except:
        print('Директория {} не обнаружена\n'.format(dir_path))

while exit == 0:
    print('1. Перейти в папку\n'
    '2. Просмотреть содержимое текущей папки\n'
    '3. Удалить папку\n'
    '4. Создать папку\n'
    '5. Выход')
    do = str(input())
    if do == '1':
        print('Введите название директории для перехода\n')
        dir = str(input())
        go_dir(dir)
    if do == '2':
        show_dir()
    if do == '3':
        print('Введите название директории которую нужно удалить\n')
        dir = str(input())
        rm_dir(dir)
    if do == '4':
        print('Введите название директории которую нужно создать\n')
        dir = str(input())
        make_dir(dir)
    if do == '5':
        exit = 1