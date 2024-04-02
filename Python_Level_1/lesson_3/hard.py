# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def read_drob(str):
    if str.find('/') > 0:
        str = str.split('/')
        x = int(str[0])
        y = int(str[1])
        return [x,y]
    else:
        return [int(str)]

def read_str(list_str):
    list = []
    operand = 0
    for item in list_str:
        if item == '+' or item == '-':
            operand = list_str.pop(list_str.index(item))
    for item in list_str:
        list.append(read_drob(item))
    return list

str1 = '4 4/5 + 3/4'.split(' ')
#str = input("Введите выражение формата n1 x1/y1 + n2 x2/y2").split(' ')
print(read_str(str))


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import os

path_hours = os.path.join('data', "hours_of.txt")
path_workers = os.path.join('data', 'workers.txt')

file_hours = open(path_hours, 'r', encoding='UTF-8')
file_workers = open(path_workers, 'r', encoding='UTF-8')

list_hours = []
list_workers = []

def read_file(file, list):
    for line in file:
        list.append(line)
    file.close
    list.pop(0)

def count_zarplaty(facts, norma, zarplata):
    zp = 0
    facts = int(facts)
    norma = int(norma)
    zarplata = int(zarplata)
    zp_v_hours = zarplata / norma
    if (facts - norma) > 0:
        zp = zarplata + (facts-norma) * (zp_v_hours * 2)
    elif (facts - norma) < 0 :
        zp = zarplata - (norma - facts) * zp_v_hours
    else:
        zp = zarplata
    return zp

read_file(file_hours, list_hours)
read_file(file_workers, list_workers)

list_surname = []
list_hours_facts = []

for line in list_hours:
    list_surname.append(line[8:16].replace(" ",""))
    if list_hours.index(line) == len(list_hours)-1:
        list_hours_facts.append(line[16:].replace(' ', ''))
    else:
        list_hours_facts.append(line[16:-1].replace(' ', ''))

list_surname_norma = []
list_hours_norma = []
list_zarplata = []

for line in list_workers:
    list_surname_norma.append(line[8:16].replace(" ",""))
    list_zarplata.append(line[16:30].replace(" ",""))
    if list_workers.index(line) == len(list_workers)-1:
        list_hours_norma.append(line[-4:].replace(' ', ''))
    else:
        list_hours_norma.append(line[-4:-1].replace(' ', ''))

print('Фамилия, Фактически отработано, Норма отработки, Зарплата, Выплачено')

for i in range(0,len(list_surname)):
    index = list_surname_norma.index(list_surname[i])
    temp = count_zarplaty(list_hours_facts[i],list_hours_norma[index],list_zarplata[index])
    print("{:10}{:4}{:4}{:6}{:6.2f} ".format(list_surname[i], list_hours_facts[i], list_hours_norma[index], list_zarplata[index], temp))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
    

import os

path_fruits = os.path.join('data', "fruits.txt")

file_fruits = open(path_fruits, 'r', encoding='UTF-8')
list_fruits = []

for line in file_fruits:
    list_fruits.append(line)
file_fruits.close

list = []
list_keys = []

for item in list_fruits:
    list_keys.append(item[0])
list_keys = set(list_keys)
list_keys.remove('\n')
print(list_keys)

for i in list_keys:
    temp_list = []
    for item in list_fruits:
        if i == item[0]:
            temp_list.append(item[:-1])
    list.append(temp_list)

for i in range(0,len(list_keys)):
    index = list_keys.pop()
    name_file = 'data/fruits_' + index + '.txt'
    f = open(name_file, "w")
    for item in list[i]:
        if list[i][0][0] == index:
           f.write('{}\n'.format(item))
    f.close