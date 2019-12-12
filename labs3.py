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
print(words)
