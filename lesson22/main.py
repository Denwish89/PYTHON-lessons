# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


number1 = (int(input("Укажите кол-во первого набора чисел: ")))
number1_list = []
for i in range(number1):
    n = int(input("Введите число: "))
    number1_list.append(n)
print(number1_list)


number2 = (int(input("Укажите кол-во второго набора чисел: ")))
number2_list = []
for i in range(number2):
    m = int(input("Введите число: "))
    number2_list.append(m)
print(number2_list)

number3_list = number1_list + number2_list

print(number3_list)
for i in set(number3_list):
    if number3_list.count(i) > 1:
        print(i)
