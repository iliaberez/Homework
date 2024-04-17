#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


import random


class Card():
    def __init__(self):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line1 = self.generate_line()
        self.line2 = self.generate_line()
        self.line3 = self.generate_line()
        all_line = self.line1 + self.line2 + self.line3
        all_line.sort()
        self.item_all_line = list(filter(lambda x: x != 0, all_line))

    def generate_line(self):
        temp_line = []
        for _ in range(5):
            num = random.randint(1,90)
            while num in self.line1 or num in self.line2 or num in self.line3:
                num = random.randint(1,90)
            temp_line.append(num)
        temp_line.sort()

        for _ in range(0, 3):
            item = random.randint(0, 8)
            temp_line.insert(item, 0)
        return temp_line
    
    def print_line(self, line, list_barrel):
        str = '| '
        for item in line:
            if item == 0:
                str+= '    '
            else:
                if item in list_barrel:
                    str +=' -- '
                else:
                    str += ' {:2.0f} '.format(item)
        str += ' |\n'
        print(str)
    
    def print_card(self, list_barrel):
        self.print_line(self.line1, list_barrel)
        self.print_line(self.line2, list_barrel)
        self.print_line(self.line3, list_barrel)

    def check_barrel_in_card(self, barrel, barrel_list):
        if barrel in self.item_all_line:
            barrel_list.append(barrel)
            

    
card_computer = Card()
card_gamer = Card()

barrel_list = []
barrel_list_computer = []
barrel_list_gamer = []
print('Карточка компьютера:')
card_computer.print_card(barrel_list_computer)
print('------------------------------------')
print('Карточка игрока:')
card_gamer.print_card(barrel_list_gamer)

game = 90

while game:
    barrel = random.randint(1, 90)
    while barrel in barrel_list:
        barrel = random.randint(1, 90)
    barrel_list.append(barrel)
    print('Выпала бочка: ', barrel)
    a = input('Введите y/n если у вас есть или нету ')
    match a:
        case 'y':
            if barrel not in card_gamer.item_all_line:
                print('Вы приограли')
                break
        case 'n':
            if barrel in card_gamer.item_all_line:
                print('Вы приограли')
                break
   
    if barrel in card_computer.item_all_line:
        barrel_list_computer.append(barrel)

    if barrel in card_gamer.item_all_line:
        barrel_list_gamer.append(barrel)  

    if len(barrel_list_computer) == 15:
        print('Вы приограли, компьютер победил')
        break
    if len(barrel_list_gamer) == 15:
        print('Вы победили')
        break

    print('Карточка компьютера:')
    card_computer.print_card(barrel_list)
    print('------------------------------------')
    print('Карточка игрока:')
    card_gamer.print_card(barrel_list)
    game -= 1
