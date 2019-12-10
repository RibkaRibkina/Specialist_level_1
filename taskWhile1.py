# Дано целое число не меньше 2.
# Напечатайте наименьший целочисленный делитель данного числа больший 1.
# Пример ввода
# 15
# Пример вывода
# 3

number = int(input("Введите число: "))

x = 2
the_list_of_factors = []
while x != number + 1:
    answer = number / x
    if answer == int(answer):
        the_list_of_factors.append(x)
    x += 1

print(min(the_list_of_factors))
