def sum_(num):
    if num == 0:
        return 0
    else:
        return num + sum_(num - 1)


def mult(num):
    if num == 0:
        return 1
    else:
        return num * mult(num - 1)


print(sum_(123))
print(mult(123))
