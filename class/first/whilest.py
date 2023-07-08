# value = input('Enter a word: ')
# for i in range(len(value)-1, -1, -1):
#     if i % 2 == 1:
#         print(i)

value = input('Enter a long word: ')
lst = []
c = 0
for i in value:
    if value.count(i) > 1:
        c = value.count(i)
        lst.append([i, c])
print(lst)
