# Обработка файлов регулярными выражениями
import re


def read_file(file_name):
    """
    file -> file

    Reads the file, selects the desired
    information and writes to a new file.
    """

    with open(file_name, "r", encoding="utf-8") as file:
        file = file.read()
        time = re.findall(r"\d{3}.\w+.\w+.\w+.\w+.(\d\d:\d\d:\d\d)", file)
        train_number = re.findall(r"\d{3}", file)
        city = re.findall(r"\d{3}.\w+.(\w+.\w+).\w+.\d\d:\d\d:\d\d", file)


    with open("new_journal.txt", "a", encoding="utf-8") as file:
        for i in range(0, len(time)):
            file.write(f"[{time.pop(0)}] - Поезд № {train_number.pop(0)} {city.pop(0)}\n")



read_file("journal.txt")
