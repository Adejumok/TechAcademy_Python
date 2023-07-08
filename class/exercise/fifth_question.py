from functools import reduce


def maxx(l):
    max_ = reduce(lambda i, j: i if i > j else j, l)
    return max_


x = [4, 5, 24, 12, 2]
print(maxx(x))
