#Default args
class Demo:
    def sum(self, a=None, b=None, c=None):
        if a != None and b != None and c != None:
            print('The sum of 3: ', a+b+c)
        elif a!=None and b!=None:
            print('The sum of 2: ', a+b)
        else:
            print('Pls provide 2 or 3 args')

d = Demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)


class Demo1:
    def __init__(self):
        print('No Args')

    def __init__(self, a=0):
        print(a)

    def __init__(self, a=0, b=0):
        if a != 0 and b!=0:
            print('The sum of 2: ', a + b)
        else:
            print('Pls provide 2 args')

d1 = Demo1(5, 7)
d1