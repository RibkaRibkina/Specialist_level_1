# Дана какая-то строка. Замените в этой строке все числа 1 словом 'one'.
# Напечатайте изменённую строку
# Пример ввода
# 1+1=2
# Пример вывода
# one+one=2


# def replacement(string):
#     string = list(string)
#     list_for_replacement = []
#     for i in string:
#         if i == "1":
#             list_for_replacement.append("one")
#         else:
#             list_for_replacement.append(i)
#     for i in list_for_replacement:
#         string = "".join(list_for_replacement)
#     return string

def replacement(string):
    string_one = string.replace("1", "one")
    return string_one


string = input("Введите строку: ")
print(replacement(string))
