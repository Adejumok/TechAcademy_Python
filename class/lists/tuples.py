m =(20, 30, 45, 53, 34, 30)
l =(1,)
m = sorted(m, reverse=True)
print(id(m))
print(len(m))
m[1] = 35
print(type(m))
print(m.index(30))
print(id(m))
print(m)


