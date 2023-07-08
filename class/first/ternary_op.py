h, i, j, k = 4, 5, 3, 7

max_ = h if h > i and h > j else (i if i > j else j)
print(max_)

min_ = h if h < i and (h < j and h < k) else (i if i < j and i < k else (j if j < k else k))
print(min_)
