def pythagorean():
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print(a*b*c)


pythagorean()