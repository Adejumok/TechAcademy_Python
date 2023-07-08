l = ['Josh', 'Jiel', 'Jessica']
print(l[1][2:6:2])
print(l[2:-1:3])
print(l[2::1][1::4])
print(l[2][1::4])

for i in l:
    print(i)

i = 0
while i < len(l):
    print(l[i])
    i = i + 1

l.insert(-1, 'Joseph')
print(l)
m=['Kike', 'Kemi', 'Kamila', 'Kay']
l.extend(m)
print(l)