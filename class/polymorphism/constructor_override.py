class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, eno, esal):
        super().__init__(name, age)
        self.eno = eno
        self.esal = esal

    def display(self):
        print(self.name)
        print(self.age)
        print(self.eno)
        print(self.esal)


e = Employee('Jerry', 15, 98, 90300)
e.display()
