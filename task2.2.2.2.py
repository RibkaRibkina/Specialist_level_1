# Даны два целых числа.
# Напечатайте меньшее из чисел.
# Пример ввода
# 3
# 7
# Пример вывода
# 3

def comparison(x, y):
    """
    (int, int) -> int

    Compares numbers and returns the smaller.
    """
    if x > y:
        return y
    else:
        y > x
        return x


number_x = int(input("Введите число: "))
number_y = int(input("Введите число: "))
print(comparison(number_x, number_y))
