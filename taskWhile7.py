# Дано целое положительное число N.
# Напечатайте число Фибоначчи, которое находится в позиции числа N.
# Позиции для чисел Фибоначчи считайте от первого числа 1, то есть 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Пример ввода
# 6
# Пример вывода
# 8

number = int(input("Введите число: "))
fib_one = 1
fib_two = 1
range_fib = [1, 1, ]
while True:
    sum_number = fib_one + fib_two
    fib_one = fib_two
    fib_two = sum_number
    range_fib.append(fib_two)
    if len(range_fib) == number:
        print(range_fib[number - 1])
        break
