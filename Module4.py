# Модуль 4

# print(1)
# input(".........."
# print(.....")
# if 1 == 1:
# print("ok")
# x = "a" * "b"
# foo()
# привет = 1
# # print(abс)
# print(привет)
# abc = 1 / 0
# print(2)
# try:
#     long = 20
#     short = 2
#     total = long*3 + short*2
#     # x = "a" > 1
#     print(total)
# except (NameError, TypeError):
#     print("ой!")
# # except TypeError:
# #     print("Ай!")
# except:
#     print("Ааааай!")
# print("the end")
try:
    txt = input("Введите что-нибудь: ")
    num = int(txt)
except ValueError as e:
    print(e)
except (KeyboardInterrupt, EOFError) as e:
    if type(e) == EOFError:
        print("Вы сделали мне EOF")
    else:
        print("Отмена операции")
    print("Вы отменили операцию!")
else:
    print("Вы ввели: " + txt)
print("The end")