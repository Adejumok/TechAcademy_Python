# Multilevel

class A:
    def m1(self):
        print("Parent class A: m1 method")


class B(A):
    def m2(self):
        print("Parent class B: ")


print()


# Multiple Inheritance
class J:
    def m2(self):
        print("Parent class J: m1 method")


class K:
    def m2(self):
        print("Parent class K: ")


class L(J, K):
    def m3(self):
        print("Parent class L: m1 method")


l = L()
l.m2()


class Number:
    def __init__(self, num):
        self.num = num

    def display(self):
        print(self.num)


class Power(Number):
    def __init__(self, num, n):
        super().__init__(num)
        self.n = n

    def display(self):
        super().display()
        print(self.n)


p = Power(2, 3)
print(p)
