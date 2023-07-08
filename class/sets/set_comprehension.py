s = {x * x for x in range(5)}
print(s)

# Removing list's duplicate value
l = [10, 20, 30, 10, 40, 50, 20]
set_ = set(l)
print(list(set_))

# Frozen Set
vowels = 'a', 'e', 'i', 'o', 'u'
k = frozenset(vowels)
l_s = list(k)
l_s.extend(l)
print(l_s)

