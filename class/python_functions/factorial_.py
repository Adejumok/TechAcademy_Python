def factorial(number):
    fact_ = 1
    for i in range(1, number + 1):
        fact_ *= i
    return fact_


def display(first_num, last_num):
    for i in range(first_num, last_num + 1):
        print(factorial(i))


first_number = int(input('Enter the first number: '))
last_number = int(input('Enter the last number: '))

print(display(first_number, last_number))
print(display(last_num=5, first_num=1))
