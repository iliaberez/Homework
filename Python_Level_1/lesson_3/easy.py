# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    number = number * (10 ** (ndigits+1))
    if number % 10 >= 5:
        number = (number - (number % 10) + 10) / (10 ** (ndigits+1))
    else:
        number = (number - (number % 10)) / (10 ** (ndigits+1))
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if ticket_number // 100000 > 0:
        ticket_number = str(ticket_number)
        left = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
        right = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
        if left == right:
            print("Билет счастливый")
        else:
            print("Повезёт в другой раз")
    else:
        print("У вас не правильный билет")

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))