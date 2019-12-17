# def work_with_files(file_name):
#     with open(file_name, "r", encoding="utf-8") as file:
#         list_file = file.read()
#         list_file = list_file.replace(",", "").replace(".", "") \
#             .replace(":", "").split("\n")
#         unique_value = list(list_file)
#         return unique_value


# def work_with_files(file_name):
#     file = open(file_name, "r", encoding="utf-8")
#
#
#     file.close()
#     return unique_value





try:
    file_name = input("Введите имя фаила: ")
    file = open(file_name, "r", encoding="utf-8")
    try:
        print(file.readlines())
    except NameError:
        print("Всвязи с неверно веденым форматом фаила\nвывести список значений невозможно! ")
except FileNotFoundError:
    print("Не верный фогрмат файла!!!\nПопробуите еще раз!")
finally:
    file.close()
    print("Файл закрыт!!!")



# print(work_with_files("digit.txt"))


