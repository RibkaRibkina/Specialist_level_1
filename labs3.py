# Работа с файлами и текстом
def read_file(file):
    """
    file -> list

    The function takes the name of a file,
    and returns a list of unique words from
    that file in lowercase.
    """

    with open(file, "r", encoding="utf-8") as file:
        list_file = file.read()
        list_file = list_file.replace(",", "").replace(".", "") \
            .replace(":", "").replace("\n", "").lower().split(" ")
        unique_value = list(set(list_file))
        return unique_value


words = read_file("data.txt")


def save_file(file, wprds):
    """"
    file, list -> file

    The function records the number of
    all unique words in a file and the word
    list itself in alphabetical order.
    """

    total_word = len(words)
    with open(file, "a", encoding="utf-8") as file:
        file.write(f"\nВсего уникальных слов: {total_word}")
        file.write(f"\n=====================")
        words.sort()
        for i in words:
            file.write(f"\n{i}")


save_file("data.txt", words)
