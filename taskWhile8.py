# Дана последовательность неотрицательных целых чисел, где каждое число записывается в отдельной
# строке. Последовательность заканчивается на 0.
# Напечатайте длину самого широкого фрагмента последовательности, где все элементы равны друг
# другу.
# Пример ввода
# 1
# 2
# 2
# 2
# 9
# 7
# 7
# 2
# 1
# 0
# Пример вывода
# 3

number = int(input("Введите число: "))
counter = 0
max_counter = []
while number != 0:
    x = number
    number = int(input("Введите число: "))
    if x == number:
        counter += 1
    else:
        counter += 1
        max_counter.append(counter)
        counter = 0
answer = max(max_counter)
print(answer)
print(max_counter)
