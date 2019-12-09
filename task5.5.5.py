# Дана строка. Удалите все символы '@' из этой строки.
# Напечатайте изменённую строку
# Пример ввода
# john@smith.com
# Пример вывода
# johnsmith.com


def replacement(string):
    """
    str -> str

    returns an email without a character @
    """
    string_repl = string.replace("@", "")
    return string_repl


string = input("Введите email: ")
print(replacement(string))
