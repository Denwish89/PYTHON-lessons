# Задача2
# На вход подаются 2 числа.
# Напишите метод, который вернет сумму, разность, произведение и частное этих чисел.

def calculate(n1, n2):
    return n1 + n2, n1- n2, n1 * n2, n1 / n2

def zadacha2():
    num_f = 9
    num_s = 3
    res = calculate(num_f, num_s)
    print (res)

zadacha2()
