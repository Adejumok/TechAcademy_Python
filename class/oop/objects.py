class Alacada:

    def __init__(self, name):
        self.name=name
        print('**Welcome** ->', self.name)
    def display(self):
        print(f'Holla {self.name}!')


al_ob=Alacada('Jum')
al_ob.display()
print(dir(al_ob))