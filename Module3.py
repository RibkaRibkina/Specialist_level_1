# Модуль 3
# f = open("test.txt", "r", encoding="utf-8")
# f.close()
# open("test.txt", "r+")
# open("test.txt", "w")
# open("test.txt", "w+")
# open("test.txt", "a")
# open("test.txt", "a+")
# with open("test.txt", "r", encoding="utf-8") as f:
#     print(f.read(4))
# with open("test.txt", "r", encoding="utf-8") as f:
#     print(f.readline())
# with open("test.txt", "r", encoding="utf-8") as f:
#     s = f.readline()
#     while s:
#         print(s)
#         s = f.readline()
# with open("test.txt", "r", encoding="utf-8") as f:
#     lines = f.readline()
#     for line in f:
#     print(line)
# with open("test.txt", "a", encoding="utf-8") as f:
#     f.write("\nLine six")
# with open("test.txt", "a", encoding="utf-8") as f:
#     print(f.close())
#     print(f.mode)
#     print(f.name)

# import csv
#
# # with open("test.txt", "r", encoding="utf-8") as f:
# #     reader = csv.reader(f, delimiter=",")
# #     for row in reader:
# #         print(row)
#
# with open("test.txt", "r", encoding="utf-8", newline="\n") as f:
#     writer = csv.writer(f, delimiter="")
#     writer.writerow(["Peter", "Harrison", 21, "369-85-12"])
#

import os

