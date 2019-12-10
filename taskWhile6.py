# Дано целое положительное число N.
# Определите, является ли число N числом Фибоначчи. Если это так, напечатайте порядковую позицию
# этого числа, иначе напечатайте -1.
# Позиции для чисел Фибоначчи считайте от первого числа 1, то есть 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Пример ввода
# 8
# Пример вывода
# 6

number = int(input("Введите число: "))
fib_one = 1
fib_two = 1
range_fib = [1, 1, ]
while fib_one <= number:
    sum_number = fib_one + fib_two
    fib_one = fib_two
    fib_two = sum_number
    range_fib.append(fib_two)
if number in range_fib:
    print((range_fib.index(number)) + 1)
else:
    print("-1")
