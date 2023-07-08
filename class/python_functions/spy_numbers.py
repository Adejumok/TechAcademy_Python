def product(number):
    prod = 1
    for i in str(number):
        prod *= int(i)
    return prod


def sum(number):
    sum_ = 0
    for i in str(number):
        sum_ += int(i)
    return sum_

def process(number):
    for i in range(1, number + 1):
        if sum(i) == product(i):
            print(i)


num = int(input('Enter a number: '))
print(process(num))
