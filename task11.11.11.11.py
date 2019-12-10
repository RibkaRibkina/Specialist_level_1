# Даны четыре целых числа - координаты двух клеток на шахматной доске. Первые два числа -
# координаты первой клетки по горизонтали и вертикали от 1 до 8, вторые два числа - координаты
# второй клетки.
# Шахматная доска
# Напечатайте слово "Да", если клетки на данных координатах имеют одинаковый цвет и "Нет", если
# цвет клеток разный.
# Пример ввода
# 1
# 1
# 2
# 6
# Пример вывода
# Да

def color_doard(number_one, number_two):
    """
    (int,int) -> str

    By coordinates returns the color of the Board cell.
    """
    if number_one % 2 == 0 and number_two % 2 == 0:
        return "black"
    elif number_one % 2 == 0 and number_two % 2 != 0:
        return "white"
    elif number_one % 2 != 0 and number_two % 2 == 0:
        return "white"
    else:
        return "black"


number_one = int(input("Введите число от 1 до 8: "))
number_two = int(input("Введите число от 1 до 8: "))
number_tree = int(input("Введите число от 1 до 8: "))
number_four = int(input("Введите число от 1 до 8: "))

if color_doard(number_one, number_two) == color_doard(number_tree, number_four):
    print("Yes")
else:
    print("No")
