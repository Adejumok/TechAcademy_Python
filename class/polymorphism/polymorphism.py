class Book():
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, others):
        return self.pages + others.pages


b1 = Book(100)
b2 = Book(200)
print(b1 + b2)
