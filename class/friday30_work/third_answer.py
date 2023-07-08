def first_last_two(letter):
    if len(letter) < 2:
        return ''
    else:
        return letter[0] + letter[1] + letter[-2] + letter[-1]


print(first_last_two('w'))
