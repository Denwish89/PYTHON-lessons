#  Задача 18: Требуется найти в массиве A[1..N] самый близкий по
#  величине элемент к заданному числу X. Пользователь в первой строке
#  вводит натуральное число N – количество элементов в массиве. В
#  последующих строках записаны N целых чисел Ai
#  . Последняя строка
#  содержит число X
#  5
#  1 2 3 4 5
#  6
#  -> 5

N = int(input('Введите количество элементов массива: '))
A = input("Введите через пробел элементы списка: ").split()
A_number = list(map(int, A))
if len(A_number) != N or N == 0:
    print('Введенное количество элементов не соответствует')
else:
    Number = int(input('Введите число X, которому необходимо найти ближайшее по величине из массива: '))
    a = int(Number - A_number[0])
    count = 0
    for i in range(1, N):
        b = abs(Number - A_number[i])
        if b < a:
            a = b
            count = i
    print(f'Число {A_number[count]} ближайшее по величине к заданному числу {Number}')