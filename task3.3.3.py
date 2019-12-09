# Дана строка, которая может содержать букву f.
# Напечатайте позицию первого и последнего вхождения f. Если буква f встречается только один раз, то
# выведите позицию один раз. Если буква f не встречается, напечатайте -1.
# Позиции букв в слове считайте с 0. Например, в слове hello буква h находится в позиции 0, буква e - в
# позиции 1, буква o - в позиции 4.
# Пример ввода 1
# confort
# Пример вывода 1
# 3
# Пример ввода 2
# office
# Пример вывода 2
# 1 2
# Пример ввода 3
# office
# Пример вывода 3
# -1

def search_letters(string):
    if "f" not in string:
        return "-1"
    else:
        letter = string.index("f")
        last_letter = string.rindex("f")
        if last_letter == letter:
            return f"{letter}"
        else:
            return f"{letter} {last_letter}"

string = input("Введите слово: ")
print(search_letters(string))

