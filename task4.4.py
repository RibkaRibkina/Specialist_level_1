# Дано целое число больше 9.
# Напечатайте цифру числа, которая находится в ряду десяток.
# Пример ввода
# 1234
# Пример вывода
# 3

number = int(input("Введите любое число больше 9: "))
print(f"Две последнии цифры числа:  {number % 100 // 10}.")
