# Напишите код, который принимает целое число и печатает числа, которые следуют до него и после
# него.
# Пример ввода
# 179
# Пример вывода
# Следующее число для числа 179: 180
# Предыдущее число для числа 179: 178

number = int(input("Введите число: "))
print(f"Следующее число для числа {number}: {number + 1}")
print(f"Предыдущее число для числа {number}: {number - 1}")
