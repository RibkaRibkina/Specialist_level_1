import re

# regexp = "a"
# s = "vasyA@mail.ru"
# match = re.match(regexp, s, re.I)
# match = re.search(regexp, s, re.I)
# match = re.findall(regexp, s, re.I)
# print(match.group(0), match.start(), match.end())
# split = re.split("-", "10-20-30-40", maxsplit=2)
# sub = re.subn("a", "b", s)
# print(sub)
#
# pattern = re.compile(regexp, re.I)
# pattern.match(s)
# pattern.findall(s)
# pattern.split(s)
# pattern.subn("b", s)

# s = "Python Programming for the Absolute Beginner"
s = "abc.test.@gmail.com"
s = "abc 12-1234 12-02-2017, asd 56-1235 1-05-2016, xyz 78-1235 25-1-2018"

# r = re.findall(r"\w+", s)
# r = re.findall(r"\w{3} ", s)
r = re.findall(r"\d{1,2}-\d\d?-(\d{4})", s)
print(r)
