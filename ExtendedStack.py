class ExtendedStack(list):
    def get_first_element(self):
        return self.pop()

    def get_second_element(self):
        return self.pop()

    def sum(self):
        self.append(self.get_first_element() + self.get_second_element())

    def sub(self):
        self.append(self.get_first_element() - self.get_second_element())

    def mul(self):
        self.append(self.get_first_element() * self.get_second_element())

    def div(self):
        self.append(self.get_first_element() // self.get_second_element())


x = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(x)
x.sum()
print(x)
x.sub()
print(x)
x.mul()
print(x)
x.div()
print(x)
