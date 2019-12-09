# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Напечатайте новую строку с заменой первого и второго слов: сначала будет напечатано второе слово,
# потом первое.
# Пример ввода
# Hello world
# Пример вывода
# world Hello



def flip_words_in_places(string):
    the_character_index = string.index(" ")
    a = string[the_character_index + 1:len(string) + 1]
    b = string[0:the_character_index]
    print(a, b)

string = input("Введите 2 слова: ")
flip_words_in_places(string)