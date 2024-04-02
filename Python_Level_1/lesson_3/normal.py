# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    list_fibonacci = [1,1]
    result_list = []
    for i in range(0, m-1):
        temp = list_fibonacci[i] + list_fibonacci[i+1]
        list_fibonacci.append(temp)
        if i >= n-2:
            result_list.append(temp)
    print("Числа Фиббоначе", list_fibonacci)
    return result_list        

print(fibonacci(4,7))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(0,len(origin_list)) :
        for y in range(i, len(origin_list)):
            if origin_list[y] < origin_list[i]:
                temp = origin_list[i]
                origin_list[i] = origin_list[y]
                origin_list[y] = temp
    print(origin_list)                

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def custom_filter(list, func):
    new_list = []
    for i in list:
        if bool(func(i)):
            new_list.append(i)
    print(new_list)

import random
list = []
for i in range(0,20):
    list.append(random.randint(-40, 40))
print(list)
custom_filter(list, lambda x: x> 5)

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

A1 = [2, 1]
A2 = [3, 5]
A3 = [6, 6]
A4 = [5, 2]

B1 = [1, 1]
B2 = [1, 5]
B3 = [5, 5]
B4 = [5, 1]

# не параллелограмм
C1 = [1, 1]
C2 = [5, 5]
C3 = [1, 5]
C4 = [5, 1]

import math

def is_paral(a1, a2, a3, a4):
    # Определим функцию для проверки косинуса угла
    def cos_angle(b1, b2, b3):
        a = (b1[0] - b2[0]) * (b1[0] - b3[0]) + (b1[1] - b2[1]) * (b1[1] - b3[1])
        b = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2)
        c = math.sqrt((b1[0] - b3[0]) ** 2 + (b1[1] - b3[1]) ** 2)
        return a / (b * c)

    cos_a1 = cos_angle(a1, a2, a4)
    cos_a2 = cos_angle(a2, a3, a1)
    cos_a3 = cos_angle(a3, a4, a2)
    cos_a4 = cos_angle(a4, a3, a1)
    # проверяем равенство углов и сумму соседних углов,
    # т.е. проверяем свойства параллелограма
    if cos_a1 == cos_a3 and cos_a2 == cos_a4 and (cos_a1 + cos_a2) == 0.0 and (cos_a3 + cos_a4) == 0.0:
        print('Это паралеллограмм')
    else:
        return ('Это не паралеллограмм')


print(is_paral(A1, A2, A3, A4))
print(is_paral(B1, B2, B3, B4))
print(is_paral(C1, C2, C3, C4))