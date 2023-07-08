from functools import reduce
from recursion import sum_, mult

j = [10, 20, 30, 40]
s = map(lambda x: x ** 2, j)
print(list(s))

t = filter(lambda x: x > 20, j)
print(list(t))

w = filter(lambda x: x % 2 == 0, range(11))
print(list(w))

m = reduce(lambda x, y: x + y, j)
print(m)

special = filter(lambda x: sum_(x) == mult(x), range(101))
print(list(special))
