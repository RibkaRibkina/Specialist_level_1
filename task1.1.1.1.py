# Дано целое положительное число.
# Напечатайте "чёт", если число чётное и "нечет", если число нечётное.
# Пример ввода 1
# 3
# Пример вывода 1
# нечет
# Пример ввода 2
# 4
# Пример вывода 2
# чёт

def even_odd(number):
    """
    int -> str

    checks the number for parity, and prints the answer.
    """
    if number % 2 == 0:
        print("чёт")
    else:
        print("нечет")


number = int(input("Введите число:"))
even_odd(number)
