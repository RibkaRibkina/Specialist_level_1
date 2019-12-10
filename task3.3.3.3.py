# Дано целое число
# Напечатайте 1, если число положительное; -1, если число отрицательное; 0, если это число ноль.
# Пример ввода
# 179
# Пример вывода
# 1

def type_of_number(number):
    """
    int -> int

    Checks positive or negative, as well as zero or not.
    """
    if number == 0:
        print("0")
    elif number > 0:
        print("1")
    else:
        print("-1")


number = int(input("Введите число: "))
type_of_number(number)
