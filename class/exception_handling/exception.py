try:
    print(10/0)
except ZeroDivisionError as z:
    print("Exception info: ", z)

try:
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    print(x/y)
except (ZeroDivisionError, ValueError) as error:
    print("Can't divide with zero and please provide int values: ", error)
finally:
    print('finally')