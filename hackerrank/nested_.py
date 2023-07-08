if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        lst.append([name, score])

    lst.sort()
    lst.pop(0)

    l = 0
    lowest_grade = lst[0]
    while l < len(lst):
        l += 1


    print(lst)
