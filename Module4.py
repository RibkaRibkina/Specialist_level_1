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
# try:
#     txt = input("Введите свой возраст: ")
#     num = int(txt)
# except ValueError as e:
#     print(e)
# except (KeyboardInterrupt, EOFError) as e:
#     if type(e) == EOFError:
#         print("Вы сделали мне EOF")
#     else:
#         print("Отмена операции")
#     print("Вы отменили операцию!")
# except:
#     print("Что то случилось!")
# else:
#     print("Вы ввели: " + txt)
# finally:
#     print("The end")

# try:
#     age = input("Введите свой возраст: ")
#     age = int(age)
#     if age < 18:
#         raise Exception("Не подходите по возрасту")
#     print("Все хорошо!")
# except ValueError as e:
#     print(e)
# except (KeyboardInterrupt, EOFError) as e:
#     if type(e) == EOFError:
#         print("Вы сделали мне EOF")
#     else:
#         print("Отмена операции")
#     print("Вы отменили операцию!")
# except Exception as e:
#     print(e)
# finally:
#     print("The end")

# try:
#     n = 1
#     try:
#         s = "a" > 1
#     except:
#         print("inner")
#         raise Exception("from inner")
#     finally:
#         print("ok")
# except:
#     print("outer")
#     raise Exception("from inner")
# finally:
#     print("The end")

# def one():
#     s = "a" +"b"
#     # raise Exception("")
# def two():
#     n = "a" > 1
# def three():
#     pass
#
# try:
#     one()
#     two()
#     three()
# except:
#     print("Error")


# def a():
#     b()
# def b():
#     x()
# def c():
#     x()
# def x():
#     if True:
#         raise Exception("Error")
#
# try:
#     a()
# except:
#     print("!!!!")

# from typing import List, Dict, Tuple
#
# s: str
# n: int = 1
# s = "a"
#
#
# def is_equal(n1: int, n2: int) -> bool:
#     return n1 == n2
#
#
# x: int = input("")
#
# lst: List[int]
# lst = [1, 2, 3]
# d: Dict[str, int]
# t: List[Tuple[int, int]]
