def p(n):
    if n == 0:
        return 0
    else:
        return n + p(n - 1)


print(p(5))
