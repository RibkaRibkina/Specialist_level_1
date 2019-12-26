# n = 1
#
#
# def hello(name):
#     return "Hi " + name
#
#
# hi = hello
#
# print(hi("john"))
# print(hello("Mike"))


# def sum_of_inst(start, end):
#     n = 0
#     for i in range(start, end + 1):
#         n += 1
#     return n
#
#
# def sum_of_sqares(start, end):
#     n = 0
#     for i in range(start, end + 1):
#         n += i ** 2
#     return n
#
#
# def sum_of_cubes(start, end):
#     n = 0
#     for i in range(start, end + 1):
#         n += i ** 3
#     return n


def sum_of(start, end, fn):
    n = 0
    for i in range(start, end + 1):
        n += fn(i)
    return n


# def ints(X): return x
#
#
# def squares(x): return x ** 2
#
#
# def cubes(x): return x ** 3
#
#
# def areas(x): return x ** 2 * 3.14


# print(sum_of(1, 10, lambda x: x))
# print(sum_of(1, 10, lambda x: x ** 2))
# print(sum_of(1, 10, lambda x: x ** 3))
# print(sum_of(1, 10, lambda x: x ** 3 * 3.14))

# lst = [1, 2, 3, 4, 5, 6, 7]
# new_lst = []
# for item in lst:
#     new_lst.append(str(item))
#
# new_lst = list(map(lambda i: i * 10, lst))
# print(new_lst)
# lst = [6, 5, 4, 2, 7, 5, 2, 78, 4]
#
# print(set(filter(lambda i: i > 5, lst)))
# from functools import reduce
#
# lst = [1, 2, 3, 4, 5,9,7,8,5,4,3,2,4,45,6,7554]
#
# sum_all = reduce(lambda a, b: a + b, lst, 100)
# print(sum_all)
#
# max_item = reduce(lambda a, b: a if a > b else b, lst)
# print(max_item)

# a = [1, 2, 3]
# b = "xyz"
# c = (None, True, False)
# z = list(zip(a,b,c))
# print(z)

# lst = [1, 2, 3, 4, 5, 9, 7, 8, 5, 4, 3, 2, 4, 45, 6, 7554]
# lst = list(filter(lambda i: i > 5, lst))
# lst = list(map(lambda i: i*10, lst))
# sum_all = (lambda a, b: a + b, lst)
#
# sum_all = (lambda a, b: a + b, list(map(lambda i: i*10, list(filter(lambda i: i > 5, lst)))))
# print(sum_all)

# def compose(f, g):
#     return lambda x: f(g(x))
#
#
# double = lambda x: x * 2
# inc = lambda x: x + 1
#
# inc_and_double = compose(double, inc)
#
# def add(x):
#     return lambda y: x + y
#
# a = add(10)
#
#
# def add(x):
#     def ret(y):
#         return y + x
#     return ret
#
# a = add(10)

# def setup(lst):
#     i = 0
#
#     def ret():
#         nonlocal i
#         v = lst[i]
#         i += 1
#         return v
#
#     return ret
#
#
# next_val = setup([1, 2, 3, 4, 5])
# print(next_val())
# print(next_val())
# print(next_val())


# def hello():
#     return "hello"
#
#
# def add_underscores(fn):
#     return "_" + fn() + "_"
#
#
# hello = add_underscores(hello)
# print(hello)


# def add_underscores(fn):
#     return lambda name: "_" + fn(name) + "_"
#
#
# @add_underscores
# def hello(name):
#     return "hello " + name


# @add_underscores
# def oops():
#     return "oops"


def add_underscores(understroke):
    def decor(fn):
        def wrapper(name):
            s = "_" + fn(name) + "_"
            s += "\n" + understroke
            return s
        return wrapper
    return decor


@add_underscores("===========")
def hello(name):
    return "hello " + name


# hello = add_underscores(hello)
print(hello("John"))
# print(oops)
