# Даны два целых числа - координаты клетки на шахматной доске. Первое число от 1 до 8 обозначает
# вертикаль снизу вверх, второе - горизонталь слева направо.
# Шахматная доска
# Напечатайте слово "Белая", если клетка на данных координатах белая и "Чёрная", если клетка чёрная.
# Пример ввода
# 3
# 2
# Пример вывода
# Белая

number_one = int(input("Введите число от 1 до 8: "))
number_two = int(input("Введите число от 1 до 8: "))
if number_one % 2 == 0 and number_two % 2 == 0:
    print("black")
elif number_one % 2 == 0 and number_two % 2 != 0:
    print("white")
elif number_one % 2 != 0 and number_two % 2 == 0:
    print("white")
else:
    print("black")

