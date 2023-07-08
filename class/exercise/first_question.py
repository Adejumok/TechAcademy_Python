def concat_(l1, l2):
    concat = []
    for i in list1:
        for j in list2:
            if list1.index(i) == list2.index(j):
                concat.append(i+j)
    return concat


list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
print(concat_(list1, list2))