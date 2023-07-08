from functools import reduce

for row in range(1, 11):
    for col in range(1, row + 1):
        print('* ', end='')
    print()

s = "Python programming language, Python is easy"
print(s.count("Python"))
print(s.count("Hello"))

print('{} is a {}'.format('Aby', 'girl'))

x = ["abc", "def", "ghi"]
y = ["abc", "def", "ghi"]
z = ["ABC", "DEF", "GHI"]
a = ["abc", "def", "ghi", "jkl"]
print(x == y)
print(x == z)
print(x == a)
