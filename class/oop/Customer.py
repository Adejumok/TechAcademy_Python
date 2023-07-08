class Customer:
    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id


c = Customer()
c.set_name('Balayya')
c.set_id('0232')
print(c.get_name(), c.get_id())
