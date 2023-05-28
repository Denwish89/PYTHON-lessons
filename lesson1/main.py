""" Задача №1. Решение в группах
Семинар 1. Ввод-вывод, операторы ветвления
За день машина проезжает n километров. Сколько
дней нужно, чтобы проехать маршрут длиной m
километров? При решении этой задачи нельзя
пользоваться условной инструкцией if и циклами.
Input:
n = 700
m = 750
Output:
2 """

"""Первый вариант решения"""
import math # Подключение библиотетки math (библиотека с математическими операциями), т.е. импортируем библиотеку, чтобы мы могли воспользоваться функциями
print("Задача 1") # выводит текст
n = int(input("Введите количество километров, которое проезжает иашина за день: ")) # выводим запрос для переменной и даем ей параметр int
m = int(input("Введите длину маршрута: ")) ## выводим запрос для переменной и даем ей параметр int

result: float = m / n # объявляем, что результат типа float (значение с плавающей точкой)
result = math/math.ceil(result) # используем подключенную библиотеку, которая нам позволяет округлять до целого (вверх)
print(f"Количество дней = {result}") # выводим результат


"""Второй вариант решения"""
print("Задача 1") # выводит текст
n = int(input("Введите количество километров, которое проезжает иашина за день: ")) # выводим запрос для переменной и даем ей параметр int
if m % n > 0 : # пишем условие, при котором если есть остаток от деления
    result = int (result) # обозначаем что переменная является типом int 
    result += 1
print(f"Количество дней = {result}") # выводим результат

"""Третий вариант решения"""
print("Задача 1") # выводит текст
n = int(input("Введите количество километров, которое проезжает иашина за день: ")) # выводим запрос для переменной и даем ей параметр int

result = m // n + int(m % n > 0) # Делим без остатка и если у нас есть остаток, то прибавляем его
print(f"Количество дней = {result}") # выводим результат