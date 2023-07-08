# def spy_rec(num):
#
#     if num == 0:
#         return 1
#     else:
#         int(num[0]) * spy_rec(num[1:])
#
#
# print(spy_rec(2))


def m():
    yield 'Kiki'

k=m()
print(k)
print(type(k))