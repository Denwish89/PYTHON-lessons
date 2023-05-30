# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# Вариант с массивом
n = int(input("Enter the number if watermelons: "))
numbers = []
for i in range(n):
    num = int(input("Enter weight: "))
    numbers.append(num)
    print(max(numbers), min(numbers))

# Вариант с for без массива
n = int(input("Enter the number if watermelons: "))
num = int(input("Enter weight: "))
mx = num
mn = num
for i in range(n - 1):
    num = int(input("Enter weight: "))
    if num > mx:
        mx = num
    if num < mn:
        mn = num
print(f"max={mx} min={mn}")

# Вариант без массива с циклом for кратко

n = int(input("Enter the number if watermelons: "))
num = int(input("Enter weight: "))
mx = num
mn = num
for i in range(n - 1):
    num = int(input("Enter weight: "))
    mx = max(mx, num)
    mn = min(mn, num)
print(f"max={mx} min={mn}")