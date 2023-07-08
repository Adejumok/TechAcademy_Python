def init(full_name):
    initials = ''

    mid_name = full_name.split()
    for split in mid_name:
        initials += split[0]

    return initials


names = ['Sowou Ghosh', 'Naomi Willie', 'Salome Odusoro', 'Rose Adeyinka']
result = {init(x): x for x in names}
print(result)
