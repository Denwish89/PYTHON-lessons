# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

n = int(input("Введите число N: "))
power = 0
while 2 ** power <= n:
    print(2 ** power)
    power += 1