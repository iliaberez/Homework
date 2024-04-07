# Задание-1:
# Матрицы в питоне реализуются в виде вложенных списков:
# Пример. Дано:

matrix = [[ 1 , 2 , 3 ],
            [ 4 , 5 , 6 ],
            [ 7 , 8 , 9 ]]
print ( "matrix = ")
for line in matrix:
    print (line)
print("matrix_new = ")
matrix_new = list ( map ( list , zip (* matrix )))
for line in matrix_new:
    print (line)

# Выполнить поворот (транспонирование) матрицы
# Пример. Результат:
# matrix_rotate = [[1, 3, 0],
#                  [0, 4, 4],
#                  [8, 1, 2]]

# Суть сложности hard: Решите задачу в одну строку
    
# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:

number = '73167176531330624919225119674426574742355349194934'\
'96983520312774506326239578318016984801869478851843'\
'85861560789112949495459501737958331952853208805511'\
'12540698747158523863050715693290963295227443043557'\
'66896648950445244523161731856403098711121722383113'\
'62229893423380308135336276614282806444486645238749'\
'30358907296290491560440772390713810515859307960866'\
'70172427121883998797908792274921901699720888093776'\
'65727333001053367881220235421809751254540594752243'\
'52584907711670556013604839586446706324415722155397'\
'53697817977846174064955149290862569321978468622482'\
'83972241375657056057490261407972968652414535100474'\
'82166370484403199890008895243450658541227588666881'\
'16427171479924442928230863465674813919123162824586'\
'17866458359124566529476545682848912883142607690042'\
'24219022671055626321111109370544217506941658960408'\
'07198403850962455444362981230987879927244284909188'\
'84580156166097919133875499200524063689912560717606'\
'05886116467109405077541002256983155200055935729725'\
'71636269561882670428252483600823257530420752963450'\

def count_pr(str):
    count = 1
    for item in str:
        count *= int(item)
    return count

max = 1
max_str = ''
current_str = ''
current_count = 1

for item in number:
    if len(current_str) == 5:
        current_count = count_pr(current_str)
        if current_count > max:
            max = current_count
            max_str = current_str
        current_str = current_str[1:]
    current_str += item

index = number.find(max_str)
print(max_str, max, index)

# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random
coord_ferz = []

for i in range(8):
    x = random.randint(0,7)
    y = random.randint(0,7)
    if [x,y] in coord_ferz:
        x = random.randint(0,7)
        y = random.randint(0,7)
    coord_ferz.append([x, y])

doska = []

for x in range(8):
    level = []
    for y in range(8):
        level.append(0)
    doska.append(level)


for item in coord_ferz:
    doska[item[0]][item[1]] = 1
    
for i , line in enumerate ( doska ):
    for j , el in enumerate ( line ):
        print ( "doska[{}][{}] = {}" . format ( i , j , doska [ i ][ j ]))

result = 'No'

def func(item, list):
    x = item[0]
    y = item[1]
    for item in list:
        if x == item[0] or y == item[1]:
            return 'Yes' 
    while x >= 0 and y >= 0:
        x -=1
        y -=1
        if [x,y] in list:
            return 'Yes'
    x = item[0]
    y = item[1]
    while x <= 7 and y <= 7:
        x +=1
        y +=1
        if [x,y] in list:
            return 'Yes'
    x = item[0]
    y = item[1]
    while x >= 0 and y <= 7:
        x -=1
        y +=1
        if [x,y] in list:
            return 'Yes'
    x = item[0]
    y = item[1]
    while x <= 7 and y >= 0:
        x +=1
        y -=1
        if [x,y] in list:
            return 'Yes'
    return 'No'


for item in coord_ferz:
    if func(item, coord_ferz[coord_ferz.index(item)+1:]) == 'Yes':
        result = 'Yes'
        break

for line in doska:
    print (line)

print(coord_ferz)
print(result)