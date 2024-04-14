# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

path_hours = os.path.join('data', "hours_of.txt")
path_workers = os.path.join('data', 'workers.txt')

file_hours = open(path_hours, 'r', encoding='UTF-8')
file_workers = open(path_workers, 'r', encoding='UTF-8')

list_hours = []
list_workers = []

def read_file(file, list):
    for line in file:
        list.append(line.rstrip())
    file.close
    list.pop(0)

read_file(file_hours, list_hours)
read_file(file_workers, list_workers)

class Worker:

    def count_zarplaty(self, facts, norma, zarplata):
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
    
    def __init__(self, str, hours_norma):
        self.surname = str[8:16].replace(" ","")
        self.zarplata = str[16:30].replace(" ","")
        self.hours_facts = str[50:].replace(' ', '')
        self.hours_norma = hours_norma
        self.zarplata_facts = self.count_zarplaty(self.hours_facts, self.hours_norma, self.zarplata)

worker = []

for i in list_workers:
    for y in list_hours:
        if (i[8:16].replace(" ","") == y[8:16].replace(" ","")):
            worker.append(Worker(i, y[-4:].replace(' ', '')))

print('Фамилия, Фактически отработано, Норма отработки, Зарплата, Выплачено')

for item in worker:
     print("{:10}{:4}{:4}{:6}{:6.2f} ".format(item.surname, item.hours_facts, item.hours_norma, item.zarplata, item.zarplata_facts))