# 1.
print(4 + 3 % 5)

# 2.
i = 1
outcome = []
while True:
    if i % 3 == 0:
        break
    outcome.append(i)
    i += 1
print(outcome)

# 3.
result = [2 ** (3 ** 2), (2 ** 3) ** 2, 2 ** 3 ** 2]
print(result)

# 4.
l = [1, 0, 2, 0, 'hello', '', []]
print(list(filter(bool, l)))

# 5.
print(min(max(False, -3, -4), 2, 7))


# 6.
def foo(x):
    x[0] = ['def']
    x[1] = ['abc']

    return id(x)


q = ['abc', 'def']
print(id(q) == foo(q))


# 7.
def goo():
    try:
        return 1
    finally:
        return 2


g = goo()
print(g)

# 8.
lst = "hello world"
print([(k.upper(), len(k)) for k in lst])

# 9.
print([i ** +1 for i in range(3)])

# 10.
j = {1: 2, 3: 4, 4: 6, 6: 4}
print(j.popitem())

# 11.
total = {}


def insert(items):
    if items in total:
        total[items] += 2
    else:
        total[items] = 1


insert('Apple')
insert('Ball')
insert('Apple')
print(len(total))

# 12.
num = {}
lett = {}
comb = {}
num[1] = 56
num[3] = 7
lett[4] = 'B'
comb['Num'] = num
comb['Lett'] = lett
print(comb)

# 13.
a = {}
a[1] = 1
a['1'] = 1
a[1.0] = 4
count = 0
for i in a:
    count += a[i]

print(count)


# 14.
class a:
    def __init__(self, b):
        self.b = b

    def display(self):
        print(self.b)


obj = a("Hi")
del obj


# 15.
class text:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)

    def Change(self, var):
        var = 'New'

o = text()
print(o.variable)

