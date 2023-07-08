first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number > (second_number and third_number):
    print(first_number)
elif second_number > (first_number and third_number):
    print(second_number)
else:
    print(third_number)

