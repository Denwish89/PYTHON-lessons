# Задача4
# Актеров разделили на списки по трем качествам
# "умные", "красивые", "сильные". На главную роль нужен
# актер обладающий всеми тремя качетсвами.
# Определите, сколько есть претендентов на главную роль

# Красивые:
# Умные:
# Сильные:

beautiful = {"Илья", "Федор", "Скемен", "Олег"}
smart = {"Илья", "Георгий", "Лев"}
strong = {"Илья", "Георгий", "Олег"}

candidates = beautiful.intersection(smart, strong)
print(candidates)

# второй вариант решения
beautiful = {"Илья", "Федор", "Скемен", "Олег"}
smart = {"Илья", "Георгий", "Лев"}
strong = {"Илья", "Георгий", "Олег"}

result = beautiful & smart & strong
print(result)
