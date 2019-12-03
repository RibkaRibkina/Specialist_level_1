# Дано целое двузначное число.
# Напечатайте число, в котором правая и левая цифры поменяны местами.
# Пример ввода
# 79
# Пример вывода
# 97

number = int(input("Введите двухзначное число: "))
left_number = number // 10
right_number = number % 10
print(f"Число = {str(right_number) + str(left_number)}")
