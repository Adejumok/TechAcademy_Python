def hello_dec(func):
    def inner():
        print('Hello.. before func execution')
        func()
        print('After func execution')

    return inner


def function_to_be_used():
    print('Inside the function.')
    inp = int(input('Enter grade: '))
    if 75 <= inp <= 100:
        print('A')
    elif 65 <= inp < 75:
        print('B')
    elif 55 <= inp < 65:
        print('C')
    elif inp < 55:
        print('F')



function_to_be_used_final = hello_dec(function_to_be_used)

function_to_be_used_final()
