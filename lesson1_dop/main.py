# Задача 1
# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменяет элемент в кортеже по заданному
# индексу другим случайным числом

import random
def change_element(numbers, index):
    return  numbers[:index] + (random.randint(1, 100), ) + numbers[index + 1:]

numbers = tuple(random.randint(1, 100) for _ in range(10)) # _ тоже самое что i

index = 4

print(numbers)
numbers = change_element(numbers, index)
print(numbers)
