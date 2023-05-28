""" Задача 2: Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

number = int(input('Введите трехзначное натуральное число: '))
number1 = 0
if number < 100 and number > 999:
    print('Введенное число некорректно. Введите трехзначное натуральное число')
elif number > 99 and number < 1000:
    number1 = number // 100
    number2 = number // 10 % 10
    number3 = number % 10
    print(number1 + number2 + number3)