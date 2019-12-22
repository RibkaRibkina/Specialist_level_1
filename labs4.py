try:
    file_name = input("Введите имя фаила: ")
    file = open(file_name + ".txt", "r", encoding="utf-8")
    list_file = []
    for line in file:
        list_file.append(line.strip())
    print(f"{list_file.pop(0)} цифры в файле")
    print(list_file)
    file.close()
    print("Файл закрыт!")
except FileNotFoundError:
    print("Вы ввели несуществующее имя файла!")
except ValueError:
    print('Это не число. Выходим.')
finally:
    print("Досвидания!")




# file_name = input("Введите имя фаила: ")
# file = open(file_name, "r", encoding="utf-8")
# list_file = []
# for i in file:
#     list_file.append(i.strip())
# list_file.pop(0)
# print(list_file)
# file.close()
# print("Файл закрыт!")