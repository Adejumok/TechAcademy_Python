s = set(range(5))
print(s)

n_s = {1, "1", 1.0, True, "0.0", 0.0}
n_s.add("Lode")
# n_s.update(s)
# n_s.discard('0.0')
nn = n_s | s
print(nn)

a = 10
b = 12
c = a & b
d = a | b
print(c)
print(d)


j={1,2,3,4,5}
k={2,3,6,7,8}
print(j.difference(k))
print(j.symmetric_difference(k))
