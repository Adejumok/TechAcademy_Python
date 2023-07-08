try:
    x = int(input('Enter a number between positive integer: '))
    if x < 0:
        raise ValueError(x)
except ValueError as e:
    print('You provided {}. Please provide integer values only.'.format(e))