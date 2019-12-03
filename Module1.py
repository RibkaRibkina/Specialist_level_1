# Модуль 1
#
# print(type(1))
# print(2 + 3)
# print(5 - 3)
# print(4 / 2)
# print(5 % 2)
# print(2 ** 3)
# print(type(1.5))
# print(2 + 2 * 2)
# print((2 + 2) * 2)
# print(2 + 1.5)
# print(4 / 2)
# print(int(4 / 2))
# type("hello")
# print("hello")
# print("hello" + "world")
# # print("hello" + 2) ошибка
# # print("abc" + 1) ошибка
# # print(1 + "abc") ошибка
# print("abc" + str(1))
# print(1 + int(2))
# # print(1 + int("abc")) ошибка
# print("abc" * 5)
# print(len("abc"))
# print(len("Вася"))
# # help(len)
# # help(str)
# print("ABC".lower())
# help(str.lower)
# print("Hello world")
# n = 2 + 3
# print(n)
# n1 = 2
# n2 = 4
# n3 = n2 - n1
# print(n3)
# # s = """..................
# # ......................"""
# # s1 = "........ \
# #      ......"
# # print\
# # name = input("Введите Ваше имя: ")
# # age = input("Сколько Вам лет?: ")
# # # greet = "Привет, " + name + "."
# # # greet = greet + " Тебе " + age + " лет."
# # # print(greet)
# # n = 5
# # n = n - 3
# # n = 5
# # n -= 3
# # # greet += " Тебе " + age + " лет."
# # # greet = "Привет, {}. Тебе {} лет.".format(name, age)
# # # greet = "Привет, {0}. Тебе {1} лет.".format(name, age)
# # # print(greet)
# # greet = f"Привет, {name}. Тебе {age} лет."
# #
# # n1 = 2
# # n2 = 3
# # s = str(n1) + " + " + str(n2) + " = " + str(n1) + str(n2)
# # s = "{} + {} = {}".format(n1, n2, n1 + n2)
# # s = f"{n1} + {n2} = {n1 + n2}"
# # print(s)
# # w = int(input("Ведите сторону прямоугольника: "))
# # # h = int(input("Ведите другую сторону: "))
# # # s = f"Площадь прямоугольника {w} x {h} = {w*h}"
# # # print(s)
# # #
# # name = input("Введите Ваше имя: ")
# # age = input("Сколько Вам лет?: ")
# #
# # greet = f"Привет, {name}.\n\tТебе {age} лет."
# # print(greet)
# s1 = "hello"
# s2 = "world"
# print(s1, end="\n")
# print(s2)

# print(2<3)
# print(type(True))
# print(2==2)
# print(bool(0))
# print(bool(0.0))
# print(bool(""))
#
# answer = int(input("Сколько будет 2 + 2"))
# if answer == 4:
#     print("Правильно")
# else:
#     print("Плохо")


# import random
#
# n1 = random.randrange(1, 11)
# n2 = random.randrange(1, 11)
#
# answer = input(f"Сколько будет {n1} + {n2}?: ")
# test = answer.replace('.', '', 1)
#
# if not test.isdigit():
#     print("Надов ввести число!")
# else:
#     if answer == test:
#         answer = int(answer)
#     else:
#         answer = float(answer)
#
#     if answer == n1 + n2:
#         print("Правильно")
#     else:
#         print('Плохо')
#

# import random
#
# num = random.randrange(1,11)
# answer = input("Введите число : ")
#
# if not answer.isdigit():
#     print("Надо ввести число!")
# else:
#     answer = int(answer)
#     if answer > num:
#         print("Меньше!")
#     elif answer < num:
#         print("Больше!")
#     else:
#         print("Правильно!")

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
