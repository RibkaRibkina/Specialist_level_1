# Даны три целых числа. Определите, как много из чисел равны между собой.
# Напечатайте число 3, если все числа одинаковы, 2 - если только два из них равны и 0, если все числа
# разные.
# Пример ввода
# 10
# 5
# 10
# Пример вывода
# 2

number_one = int(input("Введите число: "))
number_two = int(input("Введите число: "))
number_tree = int(input("Введите число: "))

if number_one == number_two:
    if number_one == number_tree:
        print("3")
    else:
        print("2")
elif number_one == number_tree:
    print("2")
elif number_two == number_tree:
    print("2")
else:
    print("0")
