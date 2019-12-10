# Даны два целых числа. Первое - в диапазоне от 1 до 12 календарный месяц. Второе - в диапазоне от
# 1 до 31 день месяца заданного первым числом.
# Напечатайте дату для следующего дня от заданного в формате день-месяц-год для текущего года.
# Пример ввода 1
# 3
# 30
# Пример вывода 1
# 31-3-2018
# Пример ввода 2
# 3
# 31
# Пример вывода 2
# 1-4-2018

number_one = int(input("Введите число от 1 до 12: "))
number_two = int(input("Введите число от 1 до 31: "))
if number_one == 1 or number_one == 3 or number_one == 5 or number_one == 7 or number_one == 8 or number_one == 10 or number_one == 12:
    if number_two == 31:
        print(f"1-{number_one + 1}-2019")
    else:
        print(f"{number_two + 1}-{number_one}-2019")
elif number_one == 2:
    if number_two == 28:
        print(f"1-{number_one + 1}-2019")
    else:
        print(f"{number_two + 1}-{number_one}-2019")
else:
    if number_two == 30:
        print(f"1-{number_one + 1}-2019")
    else:
        print(f"{number_two + 1}-{number_one}-2019")
