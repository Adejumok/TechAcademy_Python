def item_removal(l):
    for i in list1:
        if list1.count(i) > 1:
            list1.remove(i)
            if list1.count(i) == 1:
                list1.remove(i)
    return l

list1 = [5, 20, 15, 20, 25, 50, 20]
print(item_removal(list1))