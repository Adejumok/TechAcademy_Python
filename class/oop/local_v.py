class Demo:
    def __init__(self, a):
        self.a = a

    def m(self):
        print(self.a*2)


d = Demo(10)
d.m()
