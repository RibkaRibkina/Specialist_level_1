# Дано целое число
# Напечатайте "Да", если число состоит из 3 цифр и "Нет", если не состоит.
# Пример ввода
# 179
# Пример вывода
# Да

def numero_constet(number):
    """
    int -> int

    Check the number of digits in the number.
    """
    if number > 0:
        text = str(number)
        if len(text) == 3:
            print("Да")
        else:
            print("Нет")
    else:
        number *= -1
        text = str(number)
        if len(text) == 3:
            print("Да")
        else:
            print("Нет")


number = int(input("Введите число: "))
numero_constet(number)
