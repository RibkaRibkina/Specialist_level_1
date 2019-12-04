# Модуль 2
#
r = range(10)


# print(r)
# type(r)
# for i in range(1, 11):
#     print(i)
#
# l = [1, 2, 3, 65, 4, 5, 8, ]
# for i in l:
#     print(i)
#
# l.append(6)
# print(l)
# l[2] = 33
# print(l)
# type(l)
# print(list(r))
#
# s1 = "abc"
# s2 = s1
# s1 = s1.upper()

# l1 = ["a", "b", "c"]
# l2 = l1
# l2[0] = "z"
# print(l)
# l.append('d')
# d = l.pop()
# d = l.pop(0)
# l = [3, 6, 5, 2, 8, 4]
# l.sort()
# print(l)
# a = 1;
# b = 2
# a, b = b, a
# a, b, c = 1, 2, 3
# (a, b, c) = (1, 2, 3)
# l = [1,2,3]
# l2 = l
# l2 =l.copy()
#
# s = {1, 4, 3, 6, 5, 3, 5, 3, 2, 1, 4, 5, 6, 4, 4, 3, 2}
# print(s)
# l = [12, 4, 23, 42, 34, 21, 2, 312, 31, 13, 3, 4, 31, 4, 4, 5, 2, 4, 3, 34, 3]
# s = set(l)
# l = list(s)
# print(l)
#
# d = {"a": 100, "b": 200}
# print(d["b"])
# d["b"] = 400
# d["x"] = 500
# print(d)
#
# print("y" in d)
# print(d.get("y",0))
# for key, var in d.items():
#     print(key, var)

# l = [i ** 2 for i in [2, 3, 4] if i > 2]
# print(l)

# def print_second_per_day(days):
#     h = 24 * days
#     m = h * 60
#     s = m * 60
#     print(s)
#
# print_second_per_day(3)

# def print_second_per_day(days=1):
#     h = 24 * days
#     m = h * 60
#     s = m * 60
#     print(s)
#
#
# print_second_per_day()

# def print_second_per_day(days=1):
#     h = 24 * days
#     m = h * 60
#     s = m * 60
#     return s
#
#
# sec = print_second_per_day(3)
# print(sec)


def area_of_disk(radius):
    return 3.14 * radius ** 2

# rad = area_of_disk(2)
# print(rad)

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

